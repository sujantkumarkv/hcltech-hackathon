import pandas as pd
from customer_context import generate_prompt
from openai_client import get_openai_client

# Read the Excel file into a pandas DataFrame
CUSTOMER_CHURN_DATA_XLSX = './given/customer_churn_data.xlsx'
df = pd.read_excel(CUSTOMER_CHURN_DATA_XLSX)

client = get_openai_client()

# iterate
for index, row in df.iterrows():
    customer_feedback = str(row['Customer_Feedback'])
    
    # Generate the prompt for the LLM
    final_prompt = generate_prompt(complaint=customer_feedback, row=row)

    try:
        response = client.chat.completions.create(
                messages=[{
                    "role": "user",
                    "content": final_prompt,
                }],
                model="gpt-4o",
            )
        
        final_response = response.choices[0].message.content
    except Exception as e:
        print(f"Error calling LLM API: {str(e)}")
    
    # Store the response in the 'Chatbot Response' column
    df.at[index, 'Chatbot Response'] = final_response
    print(f"{index} done")

df.to_csv("given/new_data.csv")