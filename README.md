# DeepAgent Template

A production-ready template for building [**LangChain Deep Agents**](https://docs.langchain.com/oss/python/deepagents/overview).

## Prerequisites

| Tool | Version | Install |
|------|---------|---------|
| Python | ≥ 3.12 | [python.org](https://python.org) |
| [uv](https://docs.astral.sh/uv/) | latest | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |

## Quick Start

### 1. Clone and set up environment

```bash
git clone <repo-url>
cd deepagent-template

cp example.env .env
# Fill in your API keys in .env
```

### 2. Install backend dependencies

```bash
uv sync
```

### 3. Start the LangGraph backend

```bash
uv run langgraph dev
# Backend API: http://localhost:2024
# LangGraph Studio: https://smith.langchain.com/studio/?baseUrl=http://localhost:2024
```

### 4. Connect a chat UI

See the [Chat UI](#chat-ui) section below.

## Environment Variables

Copy `example.env` to `.env` and set the following:

| Variable | Required | Description |
|----------|----------|-------------|
| `GROQ_API_KEY` | Yes | [Groq](https://console.groq.com) API key (free tier available) |
| `TAVILY_API_KEY` | Yes | [Tavily](https://tavily.com) API key for web search |
| `LANGCHAIN_TRACING_V2` | No | Set to `true` to enable LangSmith tracing |
| `LANGCHAIN_API_KEY` | No | LangSmith API key |
| `LANGCHAIN_PROJECT` | No | LangSmith project name |
| `PROJECT_ROOT` | No | Root directory for the filesystem backend (default: `.`) |

## Chat UI

This template ships **backend-only**. Connect any LangGraph-compatible chat UI to interact with the agent.

### Option A — Hosted Agent Chat UI (zero setup)

1. Open **[agentchat.vercel.app](https://agentchat.vercel.app)**
2. Enter your connection details:
   - **Deployment URL**: `http://localhost:2024` (local dev) or your deployed URL
   - **Graph ID**: `agent` (the key in `langgraph.json`)
   - **LangSmith API key**: optional, only needed for deployed (non-local) agents
3. Start chatting — the UI auto-detects tool calls and HITL interrupts.

### Option B — Deep Agents UI

A chat UI purpose-built for Deep Agents, with native support for tool calls, HITL interrupts, and agent workflows.

```bash
git clone https://github.com/langchain-ai/deep-agents-ui.git
cd deep-agents-ui
yarn install
yarn dev
```

Then enter the same connection details as above.

### Option C — LangGraph Studio

While `langgraph dev` is running, open LangGraph Studio at:

```
https://smith.langchain.com/studio/?baseUrl=http://localhost:2024
```

Studio lets you visually inspect graph runs, step through nodes, and replay traces.

---

## Project Structure

```
deepagent-template/
├── src/
│   ├── agents/
│   │   ├── deepagent.py      # Main Deep Agent; exports `deepagent`
│   │   └── subagents.py      # Subagent definitions
│   ├── tools/
│   │   ├── tavily.py         # Tavily search/extract/crawl/map/research tools
│   │   └── view_image.py     # Image viewing and content injection tool
│   ├── middleware/
│   │   └── image_content.py  # Middleware to inject images into LLM context
│   ├── prompts/
│   │   ├── __init__.py       # Prompt loader (reads .md files by name)
│   │   └── general.md        # General agent system prompt
│   ├── skills/
│   │   ├── general/
│   │   │   └── web-research/     # Structured web research workflow
│   │   └── tavily/               # Tavily skills (search, extract, map, crawl, research)
│   ├── utils/
│   │   └── workspace.py      # Workspace setup and skill syncing
│   ├── config.py             # Pydantic settings (loads from .env)
│   └── __init__.py
├── tests/                    # Pytest test suite
├── langgraph.json            # LangGraph server config
├── pyproject.toml            # Python dependencies and tooling
└── example.env               # Environment variable template
```

## LLM Configuration

The template defaults to **Groq** (free tier, via `langchain-groq`).

To switch providers, update `src/agents/deepagent.py`:

```python
# OpenAI
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o", api_key=settings.openai_api_key)

# Anthropic
from langchain_anthropic import ChatAnthropic
llm = ChatAnthropic(model="claude-opus-4-6", api_key=settings.anthropic_api_key)
```

## Tools

The agent has access to the following tools:

### Tavily Search Tools (`src/tools/tavily.py`)

- **`tavily_search`** — LLM-optimized web search with snippets, domain filtering, and time ranges
- **`tavily_extract`** — Extract clean markdown from specific URLs, with JavaScript rendering support
- **`tavily_crawl`** — Bulk extract content from multiple pages on a site with depth/breadth control
- **`tavily_map`** — Discover all URLs on a site without extracting content
- **`tavily_research`** — AI-powered deep research with citations and multi-source synthesis

### Image Tools (`src/tools/view_image.py`)

- **`view_image`** — Load images for direct inspection (images are injected into LLM context via middleware)

## Skills

Skills are markdown files that provide the agent with specialized knowledge and workflows.
They live in `src/skills/<skill-name>/SKILL.md`.

Available skills include:

- **Tavily Skills** (`src/skills/tavily/`) — Documentation on using Tavily search, extract, crawl, map, and research tools
- **Web Research** (`src/skills/general/web-research/`) — Structured workflow for comprehensive web research

## Human-in-the-Loop (HITL)

The agent pauses and waits for human approval before:
- Editing existing files (`edit_file`)

This is configured in `interrupt_on` inside `src/agents/deepagent.py`. Set a key to `True`
to enable interrupts for that tool (default options: approve, edit, reject).

## Running Tests

```bash
uv run pytest -v
```

## Development Tips

- **LangSmith Tracing**: set `LANGCHAIN_TRACING_V2=true` and `LANGCHAIN_API_KEY` to send
  traces to LangSmith for debugging.
- **Adding tools**: add LangChain tools to `src/tools/` and pass them to the Deep Agent in
  `src/agents/deepagent.py`.
- **Workspace sync**: the agent automatically syncs skills from `src/skills/` to `.workspace/skills/`
  on startup via `setup_workspace()`.
- **Middleware**: custom middleware can be added to process tool outputs before returning to the LLM.
  See `src/middleware/image_content.py` for an example.
