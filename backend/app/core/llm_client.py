from config import OPENROUTER_API_KEY,OPENROUTER_MODEL_NAME
from openai import OpenAI

def get_openrouter_client():
    """
    Initializes and returns the OpenRouter client.
    Centralizing this allows for easy updates to base_urls or headers.
    """
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_API_KEY,
        default_headers={
            "HTTP-Referer": "http://localhost:8000",
            "X-Title": "Diet Planner MVP",
        }
    )
    return client

# Future Gemini Client Placeholder
# def get_gemini_client():
#     import google.generativeai as genai
#     genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
#     return genai.GenerativeModel('gemini-1.5-flash')