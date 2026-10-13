#!/usr/bin/env python3
"""Pesquisa no Reddit via browser local logado (patchright, venv do Scrapling). SÓ LEITURA.

  reddit-answers login
  reddit-answers research "pergunta em inglês" -d pasta/ [-s LocalLLaMA,LocalLLM] [-t 8] [--show]

Gera em pasta/: reddit-answers.md (resposta da IA + links), reddit-top.tsv (posts mais votados
por busca nos subs), reddit-threads.md (posts + comentários com score), reddit-structure.txt.
"""
import argparse, pathlib, re, sys, time
from patchright.sync_api import sync_playwright

PROFILE = pathlib.Path(__file__).parent / ".profile"  # gitignored
ANSWERS = "https://www.reddit.com/answers/"

DEEP = """() => {
  const out = [], tags = {};
  const BLOCK = /^(P|DIV|LI|UL|OL|H[1-6]|SECTION|ARTICLE|BR)$/;
  const walk = (n) => {
    if (n.nodeType === 3) { const t = n.textContent.trim(); if (t) out.push(t + " "); return; }
    if (n.nodeType !== 1 && n.nodeType !== 11) return;
    const tag = n.tagName || "";
    if (/^(SCRIPT|STYLE|NOSCRIPT|SVG)$/.test(tag)) return;
    if (tag.includes("-")) { const k = tag.toLowerCase() + (n.shadowRoot ? " [shadow]" : ""); tags[k] = (tags[k] || 0) + 1; }
    const blk = BLOCK.test(tag); if (blk) out.push("\\n");
    if (tag === "LI") out.push("- ");
    if (n.shadowRoot) walk(n.shadowRoot);
    n.childNodes.forEach(walk);
    if (tag === "A" && n.href && /\\/comments\\//.test(n.href)) out.push("(" + n.href + ") ");
    if (blk) out.push("\\n");
  };
  walk(document.body);
  return { text: out.join(""), tags };
}"""

THREAD = """() => {
  const t = (e) => e ? e.innerText.trim() : "";
  const post = document.querySelector("#siteTable .thing.link");
  const sc = (e) => { const x = e && e.querySelector(".score.unvoted, .score"); return x ? (x.getAttribute("title") || x.innerText) : ""; };
  const comments = [...document.querySelectorAll(".commentarea .thing.comment")].map(c => {
    let d = 0, p = c.parentElement; while (p) { if (p.matches && p.matches(".thing.comment")) d++; p = p.parentElement; }
    return { depth: d, author: c.getAttribute("data-author"), score: sc(c.querySelector(":scope > .entry")), text: t(c.querySelector(":scope > .entry .md")) };
  });
  return { title: t(document.querySelector("a.title")), sub: post && post.getAttribute("data-subreddit"),
           score: post && post.getAttribute("data-score"), ncomments: post && post.getAttribute("data-comments-count"),
           body: t(document.querySelector("#siteTable .usertext-body .md")),
           ratio: (document.body.innerText.match(/\\d+% upvoted/i) || [])[0] || "", comments };
}"""

SEARCH = """() => [...document.querySelectorAll(".search-result-link")].map(r => ({
  title: r.querySelector(".search-title").innerText.trim(),
  url: r.querySelector(".search-title").href,
  sub: (r.querySelector(".search-subreddit-link") || {}).innerText || "",
  score: parseInt(((r.querySelector(".search-score") || {}).innerText || "0").replace(/[^0-9-]/g, "")) || 0,
  ncomments: parseInt(((r.querySelector(".search-comments") || {}).innerText || "0").replace(/[^0-9]/g, "")) || 0,
  time: (r.querySelector("time") || {}).title || ""
}))"""


class Blocked(Exception):
    pass


def check(pg):
    """Falha com mensagem clara em vez de erro cru de seletor."""
    u, title = pg.url, pg.title().lower()
    if "/login" in u or "/register" in u:
        raise Blocked("sessão expirada: rode `reddit-answers login` de novo")
    if "too many requests" in title or "429" in title:
        raise Blocked("rate limit do Reddit: espere alguns minutos e rode de novo")
    if "blocked" in title or "captcha" in pg.content()[:5000].lower():
        raise Blocked("Reddit bloqueou/pediu captcha: rode com --show, resolva à mão e tente de novo")


def goto(pg, url, sel=None, tries=2):
    for i in range(tries):
        try:
            pg.goto(url, wait_until="domcontentloaded")
            check(pg)
            if sel:
                pg.wait_for_selector(sel, timeout=20000)
            return
        except Blocked:
            raise
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(5)


def ctx(p, show):
    return p.chromium.launch_persistent_context(
        str(PROFILE), headless=False, locale="en-US", viewport={"width": 1280, "height": 900},
        args=[] if show else ["--window-position=-3000,-3000"])  # headless real é bloqueado pelo Reddit; janela fora da tela resolve


def login():
    with sync_playwright() as p:
        c = ctx(p, True)
        (c.pages[0] if c.pages else c.new_page()).goto("https://www.reddit.com/login")
        input("Logue no Reddit na janela aberta e aperte Enter aqui... ")
        c.close()


def post_id(url):
    m = re.search(r"/comments/(\w+)", url)
    return m.group(1) if m else None


def answers(pg, q, d):
    goto(pg, ANSWERS)
    box = pg.locator("textarea, [contenteditable=true], input[type=text]").first
    box.wait_for(timeout=20000)
    box.click()
    pg.keyboard.type(q, delay=40)
    pg.keyboard.press("Enter")
    prev, same, cur = "", 0, {"text": "", "tags": {}}
    for _ in range(30):  # texto estável 3x seguidas = streaming terminou (máx ~60s)
        time.sleep(2)
        cur = pg.evaluate(DEEP)
        same = same + 1 if cur["text"] == prev else 0
        prev = cur["text"]
        if same >= 3:
            break
    text = re.sub(r"\n\s*\n+", "\n\n", cur["text"])
    text = text[text.rfind(q) + len(q):] if q in text else text  # começa depois do eco da pergunta (independe de idioma)
    ph = pg.locator("textarea, input[type=text], [contenteditable=true]").last.get_attribute("placeholder")
    if ph and ph in text:
        text = text.split(ph, 1)[0]  # termina no placeholder do campo de seguimento
    text = text.strip()
    if len(text) < 200:
        pg.screenshot(path=str(d / "reddit-answers-erro.png"))
        raise Blocked(f"Answers não devolveu resposta (veja {d}/reddit-answers-erro.png)")
    links = sorted({h for h in pg.eval_on_selector_all("a[href*='/comments/']", "e=>e.map(a=>a.href)") if "entry_point=games" not in h})
    (d / "reddit-answers.md").write_text(f"# {q}\n\n{text}\n\n## Threads citados\n" + "\n".join(f"- {l}" for l in links) + "\n")
    (d / "reddit-structure.txt").write_text("\n".join(f"{v:4d}  {k}" for k, v in sorted(cur["tags"].items())))
    return links


def top_posts(pg, q, subs):
    rows = []
    for sub in subs:
        try:
            u = f"https://old.reddit.com/r/{sub}/search?q={q.replace(' ', '+')}&restrict_sr=on&sort=relevance&t=year"
            goto(pg, u, ".search-result-link, .search-result-listing, #siteTable")
            for r in pg.evaluate(SEARCH)[:25]:
                rows.append({**r, "sub": r["sub"] or f"r/{sub}"})
        except Blocked:
            raise
        except Exception as e:
            print(f"aviso: busca em r/{sub} falhou ({e})", file=sys.stderr)
        time.sleep(3)
    return rows


def expand_comments(pg, rounds=6):
    """Clica 'load more comments' (old.reddit) algumas rodadas."""
    for _ in range(rounds):
        more = pg.locator(".commentarea .morecomments a")
        if more.count() == 0:
            break
        try:
            more.first.click(timeout=5000)
            time.sleep(2)
        except Exception:
            break


def thread_md(pg, url, ncom):
    pid = post_id(url)
    goto(pg, f"https://old.reddit.com/comments/{pid}/?sort=top&limit=500", ".thing.link")
    expand_comments(pg)
    d = pg.evaluate(THREAD)
    tops = sorted([c for c in d["comments"] if c["depth"] == 0], key=lambda c: -int(re.sub(r"[^0-9-]", "", c["score"] or "0") or 0))[:ncom]
    md = f"## {d['title']}\nr/{d['sub']} · {d['score']} pts · {d['ratio']} · {d['ncomments']} comentários ({len(d['comments'])} lidos)\nhttps://old.reddit.com/comments/{pid}/\n\n{d['body'][:1500]}\n\n"
    for c in tops:
        md += f"- **{c['score']}** u/{c['author']}: {c['text'][:700]}\n"
    return md


def research(q, d, subs, nthreads, show):
    d = pathlib.Path(d); d.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        c = ctx(p, show)
        pg = c.pages[0] if c.pages else c.new_page()
        try:
            cited = answers(pg, q, d)
        except Blocked:
            c.close(); raise
        except Exception as e:  # Answers falhou mas o resto ainda pode render
            print(f"aviso: Answers falhou ({e}); seguindo só com busca nos subs", file=sys.stderr)
            cited = []
        subs = subs or sorted({m for l in cited for m in re.findall(r"/r/(\w+)/comments", l)})
        found = top_posts(pg, q, subs) if subs else []
        cand = {}
        for r in found:
            pid = post_id(r["url"])
            if pid:
                cand[pid] = {"url": r["url"], "sub": r["sub"], "score": r["score"], "ncomments": r["ncomments"], "time": r["time"], "src": "busca"}
        for l in cited:
            pid = post_id(l)
            if pid:
                if pid in cand:
                    cand[pid]["src"] = "answers+busca"
                else:
                    cand[pid] = {"url": l, "sub": "", "score": -1, "ncomments": 0, "time": "", "src": "answers"}
        ranked = sorted(cand.items(), key=lambda kv: ("answers" not in kv[1]["src"], -kv[1]["score"]))  # citados pelo Answers primeiro (relevância), depois por score
        (d / "reddit-top.tsv").write_text("post_id\tsub\tscore\tcomentarios\tdata\tfonte\turl\n" + "\n".join(
            f"{k}\t{v['sub']}\t{v['score']}\t{v['ncomments']}\t{v['time'][:10]}\t{v['src']}\t{v['url']}" for k, v in ranked) + "\n")
        mds = []
        for pid, v in ranked[:nthreads]:
            try:
                mds.append(thread_md(pg, v["url"], 12))
            except Blocked:
                c.close(); raise
            except Exception as e:
                mds.append(f"## {v['url']}\nerro: {e}\n")
            time.sleep(3)
        (d / "reddit-threads.md").write_text("\n\n".join(mds))
        c.close()
    print(f"ok: {d} — {len(cited)} links do Answers, {len(cand)} candidatos, {len(mds)} threads lidos")


a = argparse.ArgumentParser()
s = a.add_subparsers(dest="cmd", required=True)
s.add_parser("login")
r = s.add_parser("research")
r.add_argument("q"); r.add_argument("-d", "--dir", required=True)
r.add_argument("-s", "--subs", default="", help="subs separados por vírgula (default: os citados pelo Answers)")
r.add_argument("-t", "--threads", type=int, default=12); r.add_argument("--show", action="store_true", help="mostra a janela")
n = a.parse_args()
try:
    login() if n.cmd == "login" else research(n.q, n.dir, [x for x in n.subs.split(",") if x], n.threads, n.show)
except Blocked as e:
    sys.exit(f"ERRO: {e}")
