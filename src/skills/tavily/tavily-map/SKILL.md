---
name: tavily-map
description: |
  Discover and list all URLs on a website without extracting content using Tavily. Use this skill when the user wants to find a specific page on a large site, list all URLs, see the site structure, find where something is on a domain, or says "map the site", "find the URL for", "what pages are on", "list all pages", or "site structure". Faster than crawling — returns URLs only. Combine with extract for targeted content retrieval.
---

# Tavily Map

Discover and list URLs on a website without extracting content. Faster than crawling.

## When to Use

- You need to find a specific page on a large site
- You want a list of all URLs before deciding what to extract or crawl
- Step 3 in the workflow: search → extract → **map** → crawl → research

## Tool: `tavily_map`

Call the `tavily_map` tool with the following parameters:

### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `url` | string | Website to discover URLs from |

### Optional Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `max_depth` | int | 1 | How deep to discover (1-5 levels) |
| `max_breadth` | int | 20 | How many links to follow per page |
| `limit` | int | 50 | Maximum URLs to discover |
| `instructions` | string | None | Natural language guidance to filter URLs semantically |
| `select_paths` | list | None | Regex patterns for URL paths to include |
| `exclude_paths` | list | None | Regex patterns for URL paths to exclude |
| `select_domains` | list | None | Domain regex patterns to include |
| `exclude_domains` | list | None | Domain regex patterns to exclude |
| `allow_external` | bool | True | Follow external domain links or stay on domain |

## Usage Examples

**Discover all URLs** — Get full site map:
- URL: "https://docs.example.com"
- Use defaults (depth: 1, limit: 50)

**Semantic URL filtering** — Find pages matching description:
- URL: "https://docs.example.com"
- Set `instructions: "Find API documentation and authentication guides"`

**Path-filtered discovery** — Focus on specific sections:
- URL: "https://example.com"
- Set `select_paths: ["/blog/.*"]`
- Set `limit: 500`

**Deep site mapping** — Explore multiple levels:
- URL: "https://example.com"
- Set `max_depth: 3`, `limit: 200`

## Map + Extract Workflow

More efficient than crawl when you only need specific pages:

**Step 1: Map** — Discover available URLs:
- Call `tavily_map` with site URL
- Review results to find desired pages
- Note specific URL paths

**Step 2: Extract** — Get content from specific URLs:
- Call `tavily_extract` on the URLs you found
- Extract only what you need

## Tips

- **Map returns URLs only** — no content. Use extract or crawl to get content
- **Map + extract beats crawl** for targeted research (when you only need a few pages)
- **Use instructions** for semantic filtering when paths alone aren't enough
- **Always set limit** to prevent discovering thousands of URLs
- **Exclude domains** to stay on primary domain

## See Also

- [tavily-extract](../tavily-extract/SKILL.md) — extract content from URLs you discover
- [tavily-crawl](../tavily-crawl/SKILL.md) — bulk extract when you need many pages
