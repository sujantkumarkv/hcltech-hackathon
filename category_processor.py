import json, re
from typing import Union
from query_category import QueryCategory

def generate_category_prompt(query: str) -> str:
    return f"""
    User:
    Categorize the following customer query into one of these categories: 
    "Current Account", "Customer Support", "Fixed Deposit", "Loans", "Online Banking", "Savings Account", "Credit Card", "Debit Card", "Mobile Banking", "Other"

    Query: "{query}"

    Respond in JSON format matching this structure:
    {{
        "category": <main category>,
        "confidence": <confidence score between 0 and 1>
    }}

    For example, if the query is "I need help with my online banking login".
    {{
        "category": "Online Banking",
        "confidence": 0.9
    }}

    Ensure the confidence score is between 0 and 1, where 1 is highest confidence. 
    IMPORTANT NOTE: the response should be STRICTLY JSON ONLY and SHOULD NOT CONTAIN markdown for JSON like the following:
    ```json
    {{
        "category": "Savings Account",
        "confidence": 0.95
    }}
    ```

    Assistant:
    Understood, here's your categorized json response:
    
    """


def process_category_response(llm_response: str) -> Union[QueryCategory, None]:
    # cleaned_response = re.sub(r'.*?\n?(.*?)\n?', '', llm_response.strip(), flags=re.DOTALL)
    try:
        category_dict = json.loads(llm_response.strip())
        return QueryCategory(**category_dict)
    except json.JSONDecodeError:
        print("Error: LLM response is not valid JSON")
    except ValueError as e:
        print(f"Error: {str(e)}")
    return None