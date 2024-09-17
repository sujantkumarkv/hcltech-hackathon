import pandas as pd
from customer_context import generate_prompt

# Read the Excel file into a pandas DataFrame
CUSTOMER_CHURN_DATA_XLSX = './given/customer_churn_data.xlsx'
df = pd.read_excel(CUSTOMER_CHURN_DATA_XLSX)


