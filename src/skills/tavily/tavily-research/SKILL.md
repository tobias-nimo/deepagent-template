---
name: tavily-research
description: |
  Conduct comprehensive AI-powered research with citations using Tavily. Use this skill when the user wants deep research, a detailed report, a comparison, market analysis, literature review, or says "research", "investigate", "analyze in depth", "compare X vs Y", "what does the market look like for", or needs multi-source synthesis with explicit citations. Returns a structured report grounded in web sources. Takes 30-120 seconds. For quick fact-finding, use tavily-search instead.
---

# Tavily Research

Conduct AI-powered deep research that gathers sources, analyzes them, and produces a cited report.

## When to Use

- You need comprehensive, multi-source analysis
- The user wants a comparison, market report, or literature review
- Quick searches aren't enough — you need synthesis with citations
- Step 5 in the workflow: search → extract → map → crawl → **research**

## Tool: `tavily_research`

Call the `tavily_research` tool with the following parameters:

### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `query` | string | Research topic or question |

### Optional Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `model` | string | "mini" | Research model: `mini` for focused, `pro` for comprehensive, `auto` to let API choose |
| `output_schema` | dict | None | JSON schema to structure the research output |
| `citation_format` | string | "numbered" | Format for citations: `numbered`, `mla`, `apa`, or `chicago` |

## Model Selection

| Model | Best For | Duration | Details |
|-------|----------|----------|---------|
| `mini` | Targeted, single-topic research | ~30s | Focused analysis, faster |
| `pro` | Comprehensive multi-angle analysis | ~60-120s | Deeper, more detailed |
| `auto` | Let API choose based on query | Varies | Optimized for complexity |

**Quick reference:**
- "What is X?" or "Tell me about X" → `mini`
- "X vs Y vs Z" or "Best way to..." or "Market trends in X" → `pro`
- Unsure? Use `auto`

## Usage Examples

**Basic research** — Analyze a topic:
- Query: "competitive landscape of AI code assistants"
- Use defaults (mini model)

**Deep comparative analysis** — Complex comparisons:
- Query: "electric vehicle market analysis"
- Set `model: "pro"`

**Targeted research** — Quick single-topic analysis:
- Query: "what is quantum computing"
- Set `model: "mini"`

**Structured research output** — Get research in specific format:
- Query: "fintech trends 2025"
- Set `output_schema` to structure the response
- Set `citation_format: "apa"` for academic citations

## Tips

- **Research takes 30-120 seconds** — it's a blocking operation, so be patient
- **Use `model: "pro"`** for complex comparisons or multi-faceted analysis
- **Use `output_schema`** to get structured output matching your needs
- **For quick facts**, use `tavily_search` instead (returns snippets, not analysis)
- **Choose citation format** based on your use case (numbered for general, apa/mla for academic)

## See Also

- [tavily-search](../tavily-search/SKILL.md) — quick web search for simple lookups
- [tavily-extract](../tavily-extract/SKILL.md) — extract content from specific URLs
- [tavily-crawl](../tavily-crawl/SKILL.md) — bulk extract from a site
