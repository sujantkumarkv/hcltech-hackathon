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

try:
    response = client.chat.completions.create(
            messages=[{
                "role": "user",
                "content": "say this is a test",
            }],
            model="gpt-4o-mini",
        )
    llm_response = response.choices[0].message.content
    print(llm_response)

except Exception as e:
    print(f"Error calling LLM API: {str(e)}")