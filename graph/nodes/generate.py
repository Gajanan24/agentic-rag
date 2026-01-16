from typing import Any, Dict

from graph.state import GraphState
from graph.chains.generation import generation_chain

def generate(state : GraphState) -> Dict[str, Any]:
    print(" GENERTE -----")
    question = state["question"]
    documents = state["documents"]

    generation = generation_chain.invoke({ "context": documents, "question": question })
    return { "generation": generation, "question": question, "documents": documents }