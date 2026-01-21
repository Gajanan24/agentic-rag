from dotenv import load_dotenv
load_dotenv()  # MUST be first

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from graph.graph import app as langgraph_app
from fastapi.middleware.cors import CORSMiddleware


from fastapi.responses import StreamingResponse


app = FastAPI(
    title="Agentic RAG API",
    description="LangGraph-powered Agentic RAG backend",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# ---------- Request / Response Models ----------

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str
    full_state: dict | None = None


# ---------- API Endpoint ----------

@app.post("/ask", response_model=AnswerResponse)
def ask_question(payload: QuestionRequest):
    try:
        result = langgraph_app.invoke(
            {"question": payload.question}
        )

        return AnswerResponse(
            answer=result.get("generation", ""),
            full_state=result  # optional (remove in prod)
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )