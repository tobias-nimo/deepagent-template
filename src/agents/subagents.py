# agent/subagents.py

from pathlib import Path

from langchain_groq import ChatGroq

from ..config import settings
from ..prompts import prompts
from ..utils import SKILLS_DEST

from ..tools.tavily import tavily_tools


_ROOT = Path(settings.project_root)

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=settings.groq_api_key,
)

research_subagent = {
    "name": "research-subagent",
    "model": llm,
    "description": "Performs precise, in-depth web research and returns structured, reliable findings.",
    "system_prompt": prompts.get("research"),
    "skills": [str((SKILLS_DEST / "tavily").relative_to(_ROOT))],
    "tools": tavily_tools,
}

subagents = [research_subagent]