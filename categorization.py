from typing import Dict, Any, Union
from openai import OpenAI
import os
from dotenv import load_dotenv
from category_processor import generate_category_prompt, process_category_response
from query_category import QueryCategory
from openai_client import get_openai_client

client = get_openai_client()

def categorize_query(query: str) -> Union[QueryCategory, None]:
    prompt = generate_category_prompt(query)
    
    try:
        response = client.chat.completions.create(
                messages=[{
                    "role": "user",
                    "content": prompt,
                }],
                model="gpt-4o-mini",
            )
        
        llm_response = response.choices[0].message.content
        print(llm_response)
        return process_category_response(llm_response)
    except Exception as e:
        print(f"Error calling LLM API: {str(e)}")
        return None

# def main():
#     # examples taken from the spreadsheet data to test
#     sample_queries = [
#         "I am satisfied with the low minimum balance requirement for my Savings Account.",
#         "I am satisfied with the security features of online banking.",
#         "I am satisfied with the easy online account opening for my Savings Account.",
#         "I am satisfied with the easy fund transfer from my Current Account."
#     ]

#     for query in sample_queries:
#         category = categorize_query(query)
#         # if category:
#         #     print(f"Query: {query}")
#         #     print(f"Category: {category.category}") 
#         #     print(f"Confidence: {category.confidence}")
#         #     print("---")

# if __name__ == "__main__":
#     main()