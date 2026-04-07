---
name: tavily-extract
description: |
  Extract clean markdown or text content from specific URLs using Tavily. Use this skill when the user has one or more URLs and wants their content, says "extract", "grab the content from", "pull the text from", "get the page at", "read this webpage", or needs clean text from web pages. Handles JavaScript-rendered pages, returns LLM-optimized markdown, and supports query-focused chunking for targeted extraction.
---

# Tavily Extract

Extract clean markdown or text content from specific URLs.

## When to Use

- You have a specific URL and want its content
- You need text from JavaScript-rendered pages
- Step 2 in the workflow: search → **extract** → map → crawl → research

## Tool: `tavily_extract`

Call the `tavily_extract` tool with the following parameters:

### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `url` or `urls` | string or list | URL(s) to extract content from |

### Optional Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `query` | string | None | Extract content relevant to this query (returns chunks instead of full page) |
| `extract_depth` | string | "basic" | `basic` for simple pages, `advanced` for JavaScript-heavy sites |
| `format` | string | "markdown" | `markdown` or `text` output format |
| `include_images` | bool | False | Include image URLs in extracted content |
| `include_favicon` | bool | False | Include website favicon URL |

## Extract Depth Comparison

| Depth | Speed | Coverage | Best for |
|-------|-------|----------|----------|
| `basic` | Fast | Good | Static pages, articles, documentation |
| `advanced` | Slower | Comprehensive | SPAs, dynamic content, heavily JavaScript-rendered sites |

## Usage Examples

**Extract a single article** — Get full content:
- URL: "https://example.com/article"
- Use defaults (basic depth, markdown format)

**Extract multiple pages** — Batch processing:
- URLs: ["https://example.com/page1", "https://example.com/page2"]
- Process multiple URLs in one call

**JavaScript-heavy site** — Modern app or SPA:
- URL: "https://app.example.com"
- Set `extract_depth: "advanced"`

**Query-focused extraction** — Get only relevant sections:
- URL: "https://docs.example.com/api"
- Set `query: "authentication methods"` to extract only relevant chunks
- More efficient than extracting entire page

## Tips

- **Use `query`** to extract only relevant content instead of full pages
- **Try `basic` first**, only use `advanced` if content is missing
- **Include images** only when visual content matters (adds token usage)
- **Batch multiple URLs** when possible
- If search results already show the content you need, you may skip extract

## See Also

- [tavily-search](../tavily-search/SKILL.md) — find pages when you don't have a URL
- [tavily-crawl](../tavily-crawl/SKILL.md) — extract from many pages on a site
