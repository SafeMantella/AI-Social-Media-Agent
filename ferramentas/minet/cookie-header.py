#!/usr/bin/env python3
"""Emite a string de header `Cookie:` de tiktok ou instagram a partir de um
arquivo de cookies em formato Netscape (o que o yt-dlp exporta).

O grabber de cookies embutido do minet (browser_cookie3) NÃO lê o Chrome/Brave
neste Mac (app-bound encryption, 2026). O yt-dlp lê. Então: exporta com yt-dlp
uma vez, e passa o resultado pro minet via `-c "$(cookie-header.py <plataforma>)"`.

Uso:
    python3 cookie-header.py <tiktok|instagram> [caminho_do_arquivo]

Arquivo padrão: ferramentas/minet/cookies.txt

Exportar o arquivo (abre o diálogo de keychain do macOS uma vez):
    yt-dlp --cookies-from-browser chrome --cookies ferramentas/minet/cookies.txt \\
      --skip-download "https://www.tiktok.com/@tiktok" "https://www.instagram.com/instagram/"
"""
import http.cookiejar
import sys
from pathlib import Path

DOMAINS = {"tiktok": "tiktok.com", "instagram": "instagram.com"}


def main() -> None:
    if len(sys.argv) < 2 or sys.argv[1] not in DOMAINS:
        sys.exit("uso: cookie-header.py <tiktok|instagram> [arquivo]")
    domain = DOMAINS[sys.argv[1]]

    path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).parent / "cookies.txt"
    if not path.exists():
        sys.exit(f"arquivo de cookies não encontrado: {path}\n"
                 "exporte primeiro — ver ferramentas/minet/README.md")

    jar = http.cookiejar.MozillaCookieJar(str(path))
    jar.load(ignore_discard=True, ignore_expires=True)
    pairs = [f"{c.name}={c.value}" for c in jar if domain in (c.domain or "")]
    if not pairs:
        sys.exit(f"nenhum cookie de {domain} em {path} — "
                 "você está logado no browser que foi exportado?")
    # sessionid (IG) / sessionid+sid_tt (TikTok) são os que autenticam de fato
    print("; ".join(pairs))


if __name__ == "__main__":
    main()
