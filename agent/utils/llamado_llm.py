from google import genai
import os


def definir_llm():

    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    return client
