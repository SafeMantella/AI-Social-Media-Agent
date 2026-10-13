#!/usr/bin/env python3
"""Baixa um Reel/post de vídeo do Instagram ou TikTok e transcreve o áudio.

Uso:
    python3 instagram_transcript.py <url> [--model medium] [--language en] [--comments]

Requer (já instalados neste projeto, confirmado 24/08/2026):
    - yt-dlp (baixa o vídeo + extrai metadados/perfil/comentários — trata Instagram e TikTok igual)
    - openai-whisper (transcreve; CLI `whisper`)
    - ffmpeg (dependência do whisper pra extrair áudio)

Saída: downloads/<id>.<ext> + transcripts/<id>.{txt,srt,vtt,json,tsv}
       + transcripts/<id>.comments.txt (com --comments)
       + metadados (perfil, legenda) impressos no console.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).parent
DOWNLOADS = BASE / "downloads"
TRANSCRIPTS = BASE / "transcripts"

TOP_COMMENTS = 15


def run(cmd: list[str], check: bool = True) -> str:
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        if check:
            raise SystemExit(f"Comando falhou: {' '.join(cmd)}")
    return result.stdout


def format_comments(comments: list[dict]) -> str:
    """Top comentários por likes (yt-dlp expõe like_count em TikTok e Instagram)."""
    ranked = sorted(comments, key=lambda c: c.get("like_count") or 0, reverse=True)
    lines = []
    for c in ranked[:TOP_COMMENTS]:
        likes = c.get("like_count")
        tag = f" [{likes} likes]" if likes else ""
        lines.append(f"@{c.get('author') or '?'}{tag}: {c.get('text', '').strip()}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="URL do post/reel do Instagram ou do vídeo do TikTok")
    parser.add_argument("--model", default="medium", help="Modelo whisper (tiny/base/small/medium/large)")
    parser.add_argument("--language", default="en",
                        help="Idioma do áudio original; use 'auto' pra deixar o whisper detectar")
    parser.add_argument("--comments", action="store_true", help="Também baixar os comentários (top por likes)")
    parser.add_argument("--cookies-from", metavar="BROWSER",
                        help="Browser logado pra ler cookies (chrome/brave/firefox). "
                             "Instagram e TikTok exigem isso; Safari não é legível sem Full Disk Access. "
                             "No macOS, Chrome/Brave pedem a senha do keychain a cada chamada — pra lote, "
                             "use --cookies-file (exporta uma vez, ver README).")
    parser.add_argument("--cookies-file", metavar="PATH",
                        help="Arquivo cookies.txt (Netscape) já exportado. Não toca no keychain. "
                             "Gerar com: yt-dlp --cookies-from-browser chrome --cookies PATH --skip-download <url>")
    args = parser.parse_args()

    DOWNLOADS.mkdir(exist_ok=True)
    TRANSCRIPTS.mkdir(exist_ok=True)

    if args.cookies_file:
        cookie_args = ["--cookies", args.cookies_file]
    elif args.cookies_from:
        cookie_args = ["--cookies-from-browser", args.cookies_from]
    else:
        cookie_args = []

    print(f"Baixando metadados de {args.url}...")
    meta_cmd = ["yt-dlp", *cookie_args, "-J", "--skip-download", args.url]
    if args.comments:
        meta_cmd.insert(1, "--write-comments")
    meta = json.loads(run(meta_cmd))
    video_id = meta["id"]
    uploader = meta.get("uploader_id") or meta.get("channel") or "?"
    print(f"Perfil: @{uploader} ({meta.get('uploader')})")
    print(f"Legenda: {meta.get('description', '')[:200]}")
    (TRANSCRIPTS / f"{video_id}.caption.txt").write_text(
        f"url: {args.url}\nperfil: @{uploader}\ntitle: {meta.get('title', '')}\n\n{meta.get('description', '')}"
    )

    if args.comments:
        comments = meta.get("comments") or []
        comments_path = TRANSCRIPTS / f"{video_id}.comments.txt"
        comments_path.write_text(format_comments(comments) if comments else "(sem comentários)")
        print(f"Comentários ({len(comments)} baixados, top {TOP_COMMENTS} salvos): {comments_path}")

    print(f"Baixando vídeo ({video_id})...")
    run(["yt-dlp", *cookie_args, "-o", str(DOWNLOADS / "%(id)s.%(ext)s"), args.url])

    video_path = next(DOWNLOADS.glob(f"{video_id}.*"))
    print(f"Transcrevendo com whisper ({args.model}, idioma={args.language})...")
    lang_args = [] if args.language == "auto" else ["--language", args.language]
    run([
        "whisper", str(video_path),
        "--model", args.model,
        *lang_args,
        "--output_dir", str(TRANSCRIPTS),
        "--output_format", "all",
    ])

    txt_path = TRANSCRIPTS / f"{video_id}.txt"
    print(f"\nTranscrição salva em: {txt_path}")
    print(txt_path.read_text())


if __name__ == "__main__":
    main()
