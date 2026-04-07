# LangChain + DeepAgents Development Guide

This project uses skills that contain up-to-date patterns and working reference scripts.

## CRITICAL: Invoke Skills BEFORE Writing Code

**ALWAYS** invoke the relevant skill first - skills have the correct imports, patterns, and scripts that prevent common mistakes.

### Getting Started
- **framework-selection** - Invoke when choosing between LangChain, LangGraph, and Deep Agents
- **langchain-dependencies** - Invoke before installing packages or when resolving version issues (Python + TypeScript)

### LangChain Skills
- **langchain-fundamentals** - Invoke for create_agent, @tool decorator, middleware patterns
- **langchain-rag** - Invoke for RAG pipelines, vector stores, embeddings
- **langchain-middleware** - Invoke for structured output with Pydantic

### LangGraph Skills
- **langgraph-fundamentals** - Invoke for StateGraph, state schemas, edges, Command, Send, invoke, streaming, error handling
- **langgraph-persistence** - Invoke for checkpointers, thread_id, time travel, memory, subgraph scoping
- **langgraph-human-in-the-loop** - Invoke for interrupts, human review, error handling, approval workflows

### DeepAgents Skills
- **deep-agents-core** - Invoke for DeepAgents harness architecture
- **deep-agents-memory** - Invoke for long-term memory with StoreBackend
- **deep-agents-orchestration** - Invoke for multi-agent coordination

## Environment Setup

Required environment variables (see `example.env`):

```bash
GROQ_API_KEY=<your-key>           # Groq API key (primary LLM)
TAVILY_API_KEY=<your-key>         # Tavily API key (web search)
LANGCHAIN_TRACING_V2=true         # Optional: enable LangSmith tracing
LANGCHAIN_API_KEY=<your-key>      # Optional: LangSmith API key
LANGCHAIN_PROJECT=<project-name>  # Optional: LangSmith project name
PROJECT_ROOT=.                    # Optional: project root directory
```

To use a different LLM provider, update `src/agents/deepagent.py`:
- OpenAI: `from langchain_openai import ChatOpenAI`
- Anthropic: `from langchain_anthropic import ChatAnthropic`