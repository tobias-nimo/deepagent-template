---
name: tavily-search
description: |
  Search the web with LLM-optimized results using Tavily. Use this skill when the user wants to search the web, find articles, look up information, get recent news, discover sources, or says "search for", "find me", "look up", "what's the latest on", "find articles about", or needs current information from the internet. Returns relevant results with content snippets, relevance scores, and metadata — optimized for LLM consumption. Supports domain filtering, time ranges, and multiple search depths.
---

# Tavily Search

Web search returning LLM-optimized results with content snippets and relevance scores.

## When to Use

- You need to find information on any topic
- You don't have a specific URL yet
- First step in the workflow: **search** → extract → map → crawl → research

## Tool: `tavily_search`

Call the `tavily_search` tool with the following parameters:

### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `query` | string | Search query (keep under 400 characters) |

### Optional Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `max_results` | int | 5 | Number of results (0-20) |
| `topic` | string | "general" | `general`, `news`, or `finance` |
| `search_depth` | string | "basic" | `basic` or `advanced` |
| `time_range` | string | None | `day`, `week`, `month`, or `year` |
| `include_domains` | list | None | Focus results to specific domains |
| `exclude_domains` | list | None | Exclude specific domains |
| `country` | string | None | Boost results from specific country |
| `include_answer` | bool | False | Include AI-generated answer in results |
| `include_raw_content` | bool | False | Include full page content (saves separate extract call) |
| `include_images` | bool | False | Include image results |
| `include_image_descriptions` | bool | False | Include AI descriptions of images |
| `include_favicon` | bool | False | Include website favicon URL |

## Search Depth Comparison

| Depth | Speed | Relevance | Best for |
|-------|-------|-----------|----------|
| `basic` | Medium | High | General-purpose (default) |
| `advanced` | Slower | Highest | Precision, specific facts |

## Usage Examples

**Basic search** — Find articles on a topic:
- Query: "climate change impacts 2025"
- Use defaults (5 results, basic depth)

**News search** — Get recent information:
- Query: "AI breakthroughs"
- Set `topic: "news"` and `time_range: "week"`

**Domain-filtered search** — Focus on trusted sources:
- Query: "SEC filings energy sector"
- Set `include_domains: ["sec.gov", "reuters.com"]`

**Comprehensive search** — Get full content with results:
- Query: "React hooks tutorial"
- Set `max_results: 3` and `include_raw_content: true` (saves extract step)

## Tips

- **Keep queries concise** — under 400 characters, think search query not prompt
- **Break complex queries** — multiple searches often yield better results than one long query
- **Use `include_raw_content`** when you need full page text instead of snippets
- **Use `include_domains`** to focus on authoritative sources
- **Use `time_range`** for recent/breaking information
- **Use `advanced` depth** only when you need high precision (slower)

## See Also

- [tavily-extract](../tavily-extract/SKILL.md) — extract content from specific URLs
- [tavily-research](../tavily-research/SKILL.md) — comprehensive multi-source research
