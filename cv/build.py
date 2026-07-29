#!/usr/bin/env python3
"""Render cv/cv.html and cv/cv.pdf from cv/data.yml + cv/template.html.j2.

First-time setup (macOS Homebrew Python is externally managed, hence the venv):
    python3 -m venv cv/.venv
    cv/.venv/bin/pip install jinja2 pyyaml playwright
    cv/.venv/bin/playwright install chromium

Usage:
    cv/.venv/bin/python cv/build.py                  # writes cv.html and cv.pdf
    cv/.venv/bin/python cv/build.py --html-only      # skip PDF (faster iteration)
    cv/.venv/bin/python cv/build.py --open           # open the PDF when done
"""

from __future__ import annotations

import argparse
import sys
import webbrowser
from pathlib import Path

try:
    import yaml
    from jinja2 import Environment, FileSystemLoader, StrictUndefined
except ImportError as e:
    sys.exit(
        f"Missing dependency: {e.name}.\n"
        "Install with:  pip install jinja2 pyyaml"
    )

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data.yml"
TEMPLATE = "template.html.j2"
HTML_OUT = ROOT / "cv.html"
PDF_OUT = ROOT / "cv.pdf"


def render_pdf(html_path: Path, pdf_path: Path) -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit(
            "Playwright is not installed. Install with:\n"
            "  cv/.venv/bin/pip install playwright\n"
            "  cv/.venv/bin/playwright install chromium\n"
            "Or skip the PDF step with --html-only."
        )

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html_path.as_uri(), wait_until="networkidle")
        page.emulate_media(media="print")
        page.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            prefer_css_page_size=True,
        )
        browser.close()


def main() -> int:
    ap = argparse.ArgumentParser(description="Build the CV.")
    ap.add_argument("--open", action="store_true", help="Open the resulting PDF (or HTML if --html-only).")
    ap.add_argument("--html-only", action="store_true", help="Skip PDF generation.")
    ap.add_argument("--html", type=Path, default=HTML_OUT, help="Output HTML path.")
    ap.add_argument("--pdf", type=Path, default=PDF_OUT, help="Output PDF path.")
    args = ap.parse_args()

    data = yaml.safe_load(DATA.read_text(encoding="utf-8"))

    env = Environment(
        loader=FileSystemLoader(ROOT),
        undefined=StrictUndefined,
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    html = env.get_template(TEMPLATE).render(**data)
    args.html.write_text(html, encoding="utf-8")
    print(f"Wrote {args.html.name}")

    if not args.html_only:
        render_pdf(args.html, args.pdf)
        print(f"Wrote {args.pdf.name}")

    if args.open:
        target = args.html if args.html_only else args.pdf
        webbrowser.open(target.as_uri())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
