# agent/graph.py

from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend
from langchain_groq import ChatGroq

from ..config import settings
from ..prompts import prompts
from .subagents import subagents

# --- Chat Model ---
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=settings.groq_api_key,
)

# --- Backend ---
backend = FilesystemBackend(root_dir=settings.project_root, virtual_mode=True)

# --- Deep Agent ---
agent = create_deep_agent(
    model=llm,
    backend=backend,
    subagents=subagents,
    system_prompt=prompts.get("coordinator-agent"),
    skills=["./src/skills/"],
    # No checkpointer needed — the LangGraph API platform manages persistence.
    interrupt_on={
        "write_file": True,  # Default: approve, edit, reject
        "read_file": False,  # No interrupts needed
        "edit_file": True,   # Default: approve, edit, reject
    },
    name="coordinator-agent",
    debug=False,
)

