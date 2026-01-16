from typing import Any, Dict

from graph.chains.retrieval_grader import retrieval_grader
from graph.state import GraphState

def grade_documents(state: GraphState) -> Dict[str, Any]:
       



       """
    Determines whether the retrieved documents are relevant to the question
    If any document is not relevant, we will set a flag to run web search

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Filtered out irrelevant documents and updated web_search state
    """
       
       print("----check documents relevance...to question-----")
       question = state["question"]
       documents = state["documents"]
       web_search = False

       filtered_documents = []
       for document in documents:
           result = retrieval_grader.invoke({"question": question, "document": document})
           if result.binary_score.lower() == "yes":
               print("----GRADE - document is relevant")
               filtered_documents.append(document)
           else:
                print("----GRADE - document is NOT relevant")
                web_search = True
                continue
       return { "documents": filtered_documents, "question": question, "web_search": web_search }                


