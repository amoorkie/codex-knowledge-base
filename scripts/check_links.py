from __future__ import annotations

import argparse
import concurrent.futures
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIRS = {
    "ai",
    "backend",
    "community",
    "data",
    "databases",
    "devops",
    "frontend",
    "security",
    "testing",
}
URL_RE = re.compile(r"https?://[^\s>`)]+")
USER_AGENT = "codex-knowledge-base-link-checker/1.0"
SOFT_STATUSES = {401, 403, 405, 429}


def discover_markdown_files() -> list[Path]:
    files: list[Path] = []
    for directory in sorted(CONTENT_DIRS):
        files.extend(sorted((ROOT / directory).glob("*.md")))
    files.extend([ROOT / "README.md", ROOT / "TEMPLATE.md"])
    return files


def discover_urls(paths: list[Path]) -> dict[str, set[str]]:
    url_sources: dict[str, set[str]] = {}
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for url in URL_RE.findall(text):
            normalized = url.rstrip(".,")
            url_sources.setdefault(normalized, set()).add(path.relative_to(ROOT).as_posix())
    return url_sources


def request_url(url: str, timeout: float) -> tuple[str, int | None, str]:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return ("FAIL", None, f"unsupported scheme: {parsed.scheme or 'missing'}")

    headers = {"User-Agent": USER_AGENT}
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                status = getattr(response, "status", 200)
                if 200 <= status < 400:
                    return ("OK", status, method)
                if status in SOFT_STATUSES:
                    return ("WARN", status, method)
                return ("FAIL", status, method)
        except urllib.error.HTTPError as exc:
            if exc.code in SOFT_STATUSES:
                if method == "HEAD":
                    continue
                return ("WARN", exc.code, method)
            if method == "HEAD" and exc.code in SOFT_STATUSES:
                continue
            if method == "HEAD" and exc.code == 405:
                continue
            if method == "HEAD":
                continue
            return ("FAIL", exc.code, method)
        except Exception as exc:
            if method == "HEAD":
                continue
            return ("FAIL", None, str(exc))
    return ("FAIL", None, "request failed")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check URLs referenced in markdown files.")
    parser.add_argument("--timeout", type=float, default=12.0, help="Request timeout in seconds.")
    parser.add_argument(
        "--max-workers",
        type=int,
        default=12,
        help="Maximum concurrent URL checks.",
    )
    args = parser.parse_args()

    url_sources = discover_urls(discover_markdown_files())
    if not url_sources:
        print("No URLs found.")
        return 0

    results: list[tuple[str, str, int | None, str, list[str]]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        future_map = {
            executor.submit(request_url, url, args.timeout): url for url in sorted(url_sources)
        }
        for future in concurrent.futures.as_completed(future_map):
            url = future_map[future]
            status, code, detail = future.result()
            sources = sorted(url_sources[url])
            results.append((status, url, code, detail, sources))

    hard_failures = 0
    warnings = 0
    ok_count = 0
    for status, url, code, detail, sources in sorted(results, key=lambda item: (item[0], item[1])):
        origin = ", ".join(sources)
        if status == "OK":
            ok_count += 1
            print(f"OK   [{code}] {url} ({origin})")
        elif status == "WARN":
            warnings += 1
            print(f"WARN [{code}] {url} ({origin}) :: {detail}")
        else:
            hard_failures += 1
            code_text = code if code is not None else "ERR"
            print(f"FAIL [{code_text}] {url} ({origin}) :: {detail}")

    print(
        f"\nSummary: {ok_count} ok, {warnings} warning, {hard_failures} fail, {len(results)} total unique URLs."
    )
    return 1 if hard_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
