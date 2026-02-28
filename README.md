# DeepAgent Template

A production-ready template for building [**LangChain Deep Agents**](https://docs.langchain.com/oss/python/deepagents/overview) with a [**Agent Chat UI**](https://github.com/langchain-ai/agent-chat-ui).

## Architecture

```
┌─────────────────────────────────┐       ┌──────────────────────────────────┐
│        Next.js Frontend         │       │       LangGraph Backend          │
│                                 │       │                                  │
│         Agent Chat UI           │       │  coordinator-agent (graph.py)    │
│                                 │──────▶│  └─ research-agent (subagent)    │
│                                 │ AG-UI │     └─ Tavily MCP (web search)   │
│                                 │       │                                  │
└─────────────────────────────────┘       └──────────────────────────────────┘
```

## Prerequisites

| Tool | Version | Install |
|------|---------|---------|
| Python | ≥ 3.12 | [python.org](https://python.org) |
| [uv](https://docs.astral.sh/uv/) | latest | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Node.js | ≥ 20 | [nodejs.org](https://nodejs.org) |
| npm | ≥ 10 | bundled with Node.js |


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
# LangGraph Studio UI: https://smith.langchain.com/studio/?baseUrl=http://localhost:2024
```

### 4. Install and start the frontend

```bash
cd frontend
npm install
npm run dev
# Open: http://localhost:3000
```

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

---

## Project Structure

```
deepagent-template/
├── src/
│   ├── agent/
│   │   ├── graph.py          # Main LangGraph graph; exports `graph`
│   │   └── subagents.py      # Subagent definitions (research-agent)
│   ├── tools/
│   │   └── web_search_tools.py  # Tavily MCP tool loader
│   ├── prompts/
│   │   ├── __init__.py       # Prompt loader (reads .md files by name)
│   │   ├── coordinator-agent.md
│   │   └── research-subagent.md
│   ├── skills/
│   │   ├── skill-creator/    # Guidance for creating new skills
│   │   └── web-research/     # Structured web research workflow
│   ├── config.py             # Pydantic settings (loads from .env)
│   └── server.py             # FastAPI server (optional, for custom endpoints)
├── tests/                    # Pytest test suite
├── langgraph.json            # LangGraph server config
├── pyproject.toml            # Python dependencies and tooling
└── example.env               # Environment variable template
```

## LLM Configuration

The template defaults to **Groq** (free tier).

To switch providers, update `src/agent/graph.py` and `src/agent/subagents.py`:

```python
# OpenAI
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o", api_key=settings.openai_api_key)

# Anthropic
from langchain_anthropic import ChatAnthropic
llm = ChatAnthropic(model="claude-opus-4-6", api_key=settings.anthropic_api_key)
```

## Skills

Skills are markdown files that provide the agent with specialized knowledge and workflows.
They live in `src/skills/<skill-name>/SKILL.md`.

To add a new skill:

```bash
npx tsx src/skills/skill-creator/scripts/init_skill.ts <skill-name> --path ./src/skills
```

See `src/skills/skill-creator/SKILL.md` for the full guide.

## Human-in-the-Loop (HITL)

The coordinator agent pauses and waits for human approval before:
- Writing new files (`write_file`)
- Editing existing files (`edit_file`)

This is configured in `interrupt_on` inside `src/agent/graph.py`. Set a key to `False`
to disable interrupts for that tool.

## Running Tests

```bash
uv run pytest -v
```

## Development Tips

- **LangGraph Studio**: while `langgraph dev` is running, open LangGraph Studio at
  `https://smith.langchain.com/studio/?baseUrl=http://localhost:2024` to visually inspect
  agent runs, step through nodes, and replay traces.
- **LangSmith Tracing**: set `LANGCHAIN_TRACING_V2=true` and `LANGCHAIN_API_KEY` to send
  traces to LangSmith for debugging.
- **Adding tools**: add LangChain tools to `src/tools/` and pass them to the appropriate
  subagent in `src/agent/subagents.py`.
