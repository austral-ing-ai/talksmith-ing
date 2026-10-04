---
source_file: langchain-mcp-adapters/
source_type: web-capture
ingested_at: 2026-10-04
---

# langchain-mcp-adapters (PyPI) — capture failed: "Client Challenge" bot page

## Provenance
- Original location: research/web/langchain-mcp-adapters/ (page.md; original.html; metadata.yaml)
- Format: html — but the captured document is a bot-protection interstitial, not the PyPI project page. page.md is 294 bytes with a single heading; original.html is 3038 bytes of challenge markup (CSP meta, font preload, script loader). No `original.html` fallback possible: both files hold the same challenge page.
- URL: https://pypi.org/project/langchain-mcp-adapters/
- Fetched at: 2026-08-14T16:57:17Z (HTTP 200, 3038 bytes). Captured title: "Client Challenge".
- Author / source (if known): intended source is the PyPI listing of the `langchain-mcp-adapters` package (LangChain); nothing of it was captured.
- Date of original (if known): unknown

## Key claims
None. The capture contains no content about `langchain-mcp-adapters`. Do not cite this record for any claim about the package.

## Definitions and terminology
None.

## Evidence and examples
None.

## Inconsistencies / open questions
- [verified] The capture is a PyPI "Client Challenge" (JavaScript bot check) page with ~40 words of error text and no package content — checked page.md and the text of original.html. HTTP status 200 masks the failure.
- [open question] Content about the package must come from another source — re-capturing via a browser-based fetch, or capturing the GitHub repo (github.com/langchain-ai/langchain-mcp-adapters) instead, would settle it.

## Images / diagrams
No images captured (metadata.yaml lists `assets: []`; the challenge page references an `errorIcon.svg` that was not downloaded). Companion folder `langchain-mcp-adapters.web/images/` exists and is empty.

## Raw / preserved excerpts

> # Client Challenge
>
> A required part of this site couldn't load. This may be due to a browser extension, network issues, or browser settings. Please check your connection, disable any ad blockers, or try using a different browser.

> JavaScript is disabled in your browser. Please enable JavaScript to proceed.
