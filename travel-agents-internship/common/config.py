import os
from dotenv import load_dotenv

load_dotenv()

PROJECT = os.environ["GOOGLE_CLOUD_PROJECT"]
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1")
MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
