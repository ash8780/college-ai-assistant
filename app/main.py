import os

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from google import genai

load_dotenv()

app = FastAPI(
    title="College AI Assistant",
    description="AI assistant for college students",
    version="1.0.0",
)

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "College AI Assistant is running!",
        "docs": "/docs",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest):
    if client is None:
        return {"error": "GEMINI_API_KEY is missing from .env"}

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=request.message,
        )
        return {"reply": response.text}
    except Exception as e:
        return {"error": str(e)}

from app.tools.calculator import calculate, attendance_percentage
from fastapi import Query


@app.get("/calculate")
def calculate_endpoint(
    expression: str = Query(..., description="Example: 10+20*3")
):
    return calculate(expression)


@app.get("/attendance")
def attendance_endpoint(
    attended: float = Query(..., ge=0),
    total: float = Query(..., gt=0),
):
    return attendance_percentage(attended, total)

from app.tools.calculator import calculate, attendance_percentage
from fastapi import Query


@app.get("/calculate")
def calculate_endpoint(
    expression: str = Query(..., description="Example: 10+20*3")
):
    return calculate(expression)


@app.get("/attendance")
def attendance_endpoint(
    attended: float = Query(..., ge=0),
    total: float = Query(..., gt=0),
):
    return attendance_percentage(attended, total)

from app.tools.timetable import get_timetable


@app.get("/timetable")
def timetable_endpoint(day: str):
    return get_timetable(day)
