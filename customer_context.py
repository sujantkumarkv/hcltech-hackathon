import pandas as pd
from typing import Dict, List
from categorization import categorize_query


def get_relevant_context(complaint: str, customer_data: Dict[str, any]) -> List[str]:
    context = []
    # Add account-related information for LLM context
    if "savings" in complaint.lower():
        context.append(f"Customer has a {'Zero Balance' if customer_data['Zero Balance Account'] == 'Yes' else 'Regular'} Savings Account.")
        context.append(f"Monthly Average Balance: {customer_data['Monthly Average Balance (USD)']} dollars")
        context.append(f"Yearly Average Balance: {customer_data['Yearly Average Balance (USD)']} dollars")
    if "loan" in complaint.lower() and customer_data['Loan Account'] == 'Yes':
        context.append("Customer has an active Loan Account.")
    if "credit" in complaint.lower() and customer_data['Credit Cards'] == 'Yes':
        context.append("Customer has an active Credit Card.")
    # Add service usage information
    services = []
    if customer_data['Netbanking'] == 'Yes': services.append("Netbanking")
    if customer_data['MobileApp'] == 'Yes': services.append("Mobile App")
    if services:
        context.append(f"Customer uses the following services: {', '.join(services)}")
    
    # Add customer tenure
    context.append(f"Customer tenure: {customer_data['tenure in months']} months")
    
    return context

def generate_prompt(complaint: str, row: pd.Series) -> str:

    customer_data = row.to_dict()
    context = get_relevant_context(complaint, customer_data)
    
    prompt = f"""
            Instructions: Respond to the customer's complaint in a polite manner.
            Maintain a friendly tone. Avoid dismissive language.
            Be strictly very concise in your response and respond saying to forward it to the relevant team.
            Customer Complaint: "{complaint}"
            Customer complaint category type: "{categorize_query(complaint)}"

            Relevant Customer Information:
            {chr(10).join(context)}

            {{ If more details are needed, suggest follow-up questions here }}
            """
    
    return prompt.strip()

# NOT USING GENDER, AGE etc due to user privacy
# # Example usage
# customer_data = {
#     'Zero Balance Account': 'Yes',
#     'Monthly Average Balance': 1000,
#     'Loan Account': 'No',
#     'Credit Cards': 'Yes',
#     'Netbanking': 'Yes',
#     'MobileApp': 'Yes',
#     'tenure in months': 24
# }