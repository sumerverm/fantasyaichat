import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is required and was not found in the environment or .env file.")

SLEEPER_USERNAME = os.getenv("SLEEPER_USERNAME")
MSF_API_KEY = os.getenv("MSF_API_KEY")
MSF_API_PASSWORD = os.getenv("MSF_API_PASSWORD")
