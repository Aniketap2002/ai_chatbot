from fastapi import FastAPI
from chatbot import get_response

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Chatbot running"}

@app.get("/chat")
def chat(query: str):
    try:
       response = get_response(query)
       print("user asked: ", query)
       print("Gemini: ", response)
       return {"response": response}

    except Exception as e:
       return {"error": str(e)}