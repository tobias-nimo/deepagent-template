# agents/deepagent.py

from pathlib import Path
from datetime import date

from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend
from langchain_groq import ChatGroq

from ..config import settings
from ..prompts import prompts
from ..middleware import image_content_middleware
from ..tools.view_image import view_image
from .subagents import subagents
from ..utils import setup_workspace, SKILLS_DEST, AGENT_MD

# Set up .workspace/
_ROOT = Path(settings.project_root)
setup_workspace()

# Chat Model
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=settings.groq_api_key,
)

# Backend
backend = FilesystemBackend(root_dir=settings.project_root, virtual_mode=True)

# Deep Agent
deepagent = create_deep_agent(
    # LLM
    model=llm,
    
    # System prompt
    system_prompt=prompts.get(
        "general",
        project_root=settings.project_root,
        today_date=str(date.today()),
    ),

    # SubAgents
    subagents=subagents,

    # Skills + Memory
    skills=[str((SKILLS_DEST / "general").relative_to(_ROOT))],
    memory=[str(AGENT_MD.relative_to(_ROOT))],

    # Tools
    tools=[view_image], # + built-ins

    # HITL
    interrupt_on={
        "edit_file": True, # If True, default options are: approve, edit, reject
        "read_file": False,
        "write_file": False,
    },

    # Backend
    backend=backend,

    # Middleware
    middleware=[image_content_middleware],

    # Debug mode
    debug=settings.debug

    # Checkpointer is REQUIRED for human-in-the-loop!
    # But LangGraph API platform manages persistence - No checkpointer needed.
    #from langgraph.checkpoint.memory import MemorySaver
    #checkpointer=InMemorySaver(), 
)
