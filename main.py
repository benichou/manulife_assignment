from agent.agentic_graph import build_simple_agent_chain


if __name__ == "__main__":
    
    agent_chain = build_simple_agent_chain()
    
    query_list = ["How can AI agents improve observability in DevOps?", 
                "Could you highlight the benefits of AI Agents for me?", 
                "Could you please give me a summary of the previous 2 answers?"]

    # Invoke the graph
    config = {"configurable": {"thread_id": "1"}}
    for query_id, query in enumerate(query_list):
        result = agent_chain.invoke({"query": query, "query_id": query_id}, config)
        
        print("-----------------------QUERY----------------------------")
        print(f"-----------------------{query}----------------------------")
        
        print(f"-----------------------ANSWER----------------------------")
        print(f"-----------------------{result['answer'].content}----------------------------")