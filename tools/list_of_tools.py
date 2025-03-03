

def search_wikipedia(state):
    """Fetch information from Wikipedia."""
    from langchain_community.tools import WikipediaQueryRun
    from langchain_community.utilities import WikipediaAPIWrapper
    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    response = wikipedia.run(state['query'])
    return {"retrieved_context": [response]}

def search_duckduckgo(state):
    """Fetch information from DuckDuckGo."""
    from langchain_community.tools import DuckDuckGoSearchRun
    search = DuckDuckGoSearchRun()
    response = search.invoke(state['query'])
    return {"retrieved_context": [response]}





