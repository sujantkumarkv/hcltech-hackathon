import os
from dotenv import load_dotenv
from openai import OpenAI

# load environment variables
load_dotenv()
OPENAI_ORG = os.getenv("OPENAI_ORG")
OPENAI_ORG_PROJECT_ID = os.getenv("OPENAI_ORG_PROJECT_ID")
client = OpenAI(
  organization=OPENAI_ORG,
  project=OPENAI_ORG_PROJECT_ID,
)
def get_openai_client():
    return client