import os
from dotenv import load_dotenv
import pandas as pd
from openai import OpenAI
# load environment variables
load_dotenv()

OPENAI_ORG = os.getenv("OPENAI_ORG")
OPENAI_ORG_PROJECT_ID = os.getenv("OPENAI_ORG_PROJECT_ID")
client = OpenAI(
  organization=OPENAI_ORG,
  project=OPENAI_ORG_PROJECT_ID,
)

# try:
#     response = client.chat.completions.create(
#             messages=[{
#                 "role": "user",
#                 "content": "say this is a test",
#             }],
#             model="gpt-4o-mini",
#         )
#     llm_response = response.choices[0].message.content
#     print(llm_response)

# except Exception as e:
#     print(f"Error calling LLM API: {str(e)}")

CUSTOMER_CHURN_DATA_XLSX = './given/customer_churn_data.xlsx'
df = pd.read_excel(CUSTOMER_CHURN_DATA_XLSX)

for index, row in df.iterrows():
  print(f"index: {index} | row: {row['Customer_Feedback']}")
