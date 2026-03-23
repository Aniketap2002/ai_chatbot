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
    
    if __name__ == "__main__":
       import uvicorn
       uvicorn.run(app, host="0.0.0.0", port=8000)