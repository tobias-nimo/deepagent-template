# tools/tavily.py

from langchain_tavily import TavilySearch, TavilyExtract, TavilyCrawl, TavilyMap, TavilyResearch

from ..config import settings


tavily_search = TavilySearch(
    max_results=5,
    topic="general",
    # include_answer=False,
    # include_raw_content=False,
    # include_images=False,
    # include_image_descriptions=False,
    # include_favicon=False,
    # search_depth="basic",
    # time_range="day",
    # include_domains=None,
    # exclude_domains=None,
    # country=None
)

tavily_extract = TavilyExtract(
    extract_depth="advanced",
    include_images=False,
    include_favicon=False,
    format="markdown"
)

tavily_crawl = TavilyCrawl(
    max_depth=1,
    max_breadth=20,
    limit=50,
    # instructions=None,
    # select_paths=None,
    # select_domains=None,
    # exclude_paths=None,
    # exclude_domains=None,
    # allow_external=False,
    # include_images=False,
    # categories=None,
    # extract_depth=None,
    # include_favicon=False,
    # format=None
)

tavily_map = TavilyMap(
    max_depth=2,
    max_breadth=20,
    limit=50,
    # instructions=None,
    # select_paths=None,
    # select_domains=None,
    # exclude_paths=None,
    # exclude_domains=None,
    # allow_external=False,
    # categories=None,
)

tavily_research = TavilyResearch(
    model="mini",
    # output_schema=None,
    # stream=False,
    # citation_format="numbered",
)


tavily_tools = [tavily_search, tavily_extract, tavily_crawl, tavily_map, tavily_research]

# Check Langchain pre-built toolkits [here](https://docs.langchain.com/oss/python/integrations/tools)