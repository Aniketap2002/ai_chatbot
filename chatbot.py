from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# load api key from .env
load_dotenv()
print("API KEY FOUND:", os.getenv("GOOGLE_API_KEY") is not None)

# create AI model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)


# function to get response
def get_response(user_input):
    response = llm.invoke(user_input)
    return response.content