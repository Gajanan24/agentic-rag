from typing import List, TypedList


class GraphState(TypedList):
    """
    Represents the state of a graph.

     Attributes:
        question: question
        generation: LLM generation
        web_search: whether to add search
        documents: list of documents
    """

    question: str
    generation: str
    web_search: bool
    documents: List[str]