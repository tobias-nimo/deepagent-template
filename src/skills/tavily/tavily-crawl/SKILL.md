---
name: tavily-crawl
description: |
  Crawl websites and extract content from multiple pages using Tavily. Use this skill when the user wants to crawl a site, download documentation, extract an entire docs section, bulk-extract pages, or says "crawl", "get all the pages", "download the docs", "extract everything under /docs", "bulk extract", or needs content from many pages on the same domain. Supports depth/breadth control, path filtering, and semantic instructions.
---

# Tavily Crawl

Crawl a website and extract content from multiple pages.

## When to Use

- You need content from many pages on a site (e.g., all `/docs/`)
- You want to bulk-extract pages from a single domain
- Step 4 in the workflow: search → extract → map → **crawl** → research

## Tool: `tavily_crawl`

Call the `tavily_crawl` tool with the following parameters:

### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `url` | string | Website to crawl |

### Optional Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `max_depth` | int | 1 | How deep to crawl (1-5 levels) |
| `max_breadth` | int | 20 | How many links to follow per page |
| `limit` | int | 50 | Maximum total pages to extract |
| `instructions` | string | None | Natural language guidance for semantic focus (extracts relevant chunks instead of full pages) |
| `extract_depth` | string | "basic" | `basic` for simple sites, `advanced` for JavaScript-heavy sites |
| `format` | string | "markdown" | `markdown` or `text` output format |
| `select_paths` | list | None | Regex patterns for URL paths to include |
| `exclude_paths` | list | None | Regex patterns for URL paths to exclude |
| `select_domains` | list | None | Domain regex patterns to include |
| `exclude_domains` | list | None | Domain regex patterns to exclude |
| `allow_external` | bool | True | Follow external domain links or stay on domain |
| `include_images` | bool | False | Include image URLs in results |

## Usage Examples

**Basic crawl** — Get all content from a documentation site:
- URL: "https://docs.example.com"
- Use defaults (depth: 1, limit: 50)

**Deeper crawl with limits** — Explore multiple levels:
- URL: "https://docs.example.com"
- Set `max_depth: 2`, `limit: 100`

**Path-filtered crawl** — Focus on specific sections:
- URL: "https://example.com"
- Set `select_paths: ["/api/.*", "/guides/.*"]`
- Set `exclude_paths: ["/blog/.*"]`

**Semantic focus** — Get only relevant chunks for context:
- URL: "https://docs.example.com"
- Set `instructions: "Find authentication and security documentation"`
- Returns relevant chunks instead of full pages (more efficient)

## Crawl Strategies

**For LLM Context** — Use `instructions` to extract only relevant content:
- Prevents context explosion
- Returns semantic chunks instead of full pages
- More efficient token usage

**For Data Collection** — Crawl everything with path filtering:
- Use `select_paths` and `limit` to control scope
- Don't use `instructions` when you want full pages

## Tips

- **Start conservative** — `max_depth: 1`, `limit: 20` — scale up as needed
- **Use `instructions`** to extract only relevant content for LLM use
- **Use `select_paths`** to focus on specific sections
- **Always set `limit`** to prevent runaway crawls
- **Use map first** to understand site structure before deciding crawl scope
- **Exclude domains** to stay on primary domain

## See Also

- [tavily-map](../tavily-map/SKILL.md) — discover URLs before deciding to crawl
- [tavily-extract](../tavily-extract/SKILL.md) — extract individual pages
- [tavily-search](../tavily-search/SKILL.md) — find pages when you don't have a URL
