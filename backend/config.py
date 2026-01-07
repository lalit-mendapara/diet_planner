import os 
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
OPENROUTER_MODEL_NAME = os.getenv('OPENROUTER_MODEL_NAME')