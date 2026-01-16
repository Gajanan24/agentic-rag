from dotenv import load_dotenv

from langgraph.graph import END, StateGraph
from graph.const import RETRIEVE, GRADE_DOCUMENTS, GENERATE, WEB_SEARCH
from graph.nodes import generate, grade_documents, web_search, retrieve

from graph.state import GraphState

load_dotenv()

def decide_to_generate(state):
    print("------assess graded dociuments ----")
    if state["web_search"]:
        print("---DECISION - Not all documents are relevant, need to web search---")
        return WEB_SEARCH
    else:
        print("---DECISION - All documents are relevant, proceed to generate---")
        return GENERATE
    
workflow = StateGraph(GraphState)

workflow.add_node(RETRIEVE, retrieve)
workflow.add_node(GRADE_DOCUMENTS, grade_documents)
workflow.add_node(WEB_SEARCH, web_search)
workflow.add_node(GENERATE, generate)


workflow.set_entry_point(RETRIEVE)
workflow.add_edge(RETRIEVE, GRADE_DOCUMENTS)
workflow.add_conditional_edges(
    GRADE_DOCUMENTS,
    decide_to_generate, 
    {
        WEB_SEARCH: WEB_SEARCH,
        GENERATE: GENERATE
    },
)

workflow.add_edge(WEB_SEARCH, GENERATE)
workflow.add_edge(GENERATE, END)

app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="graph.png")

       