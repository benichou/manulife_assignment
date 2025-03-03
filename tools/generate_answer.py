from utilities.models import instantiate_azure_chat_openai
from langchain_core.messages import HumanMessage, AnyMessage, SystemMessage

def generate_answer(state):
    """Generate an answer using the retrieved context."""
    model = instantiate_azure_chat_openai()
    retrieved_context = state['retrieved_context']
    query = state['query']
    query_id = state["query_id"]

    # Prompt Template
    prompt_template = f"""Based on the following context, provide an accurate and concise answer to the query \
                          (disregard any content from the context that does not answer the query):
    Query: {query}
    Context: {retrieved_context}"""

    # Generate the answer
    response = model.invoke([SystemMessage(content=prompt_template)] +
                            [HumanMessage(content="Provide the response.")])
    return {"answer": response, "retrieved_context": [f"Eventually, the final answer for query {query_id} is: {response}"]}