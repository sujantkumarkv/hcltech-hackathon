import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import classification_report


# Load preprocessed data
CUSTOMER_CHURN_DATA_XLSX = '../given/customer_churn_data.xlsx'
df = pd.read_excel(CUSTOMER_CHURN_DATA_XLSX)

# Calculate overall churn rate
churn_rate = (df['Churn'] == 1).mean()
print(f"Overall Churn Rate: {churn_rate:.2%}")

# Preprocessing
def preprocess_data(df):
    # Convert 'Churn' and 'Credit Cards' to numerical
    le = LabelEncoder()
    df['Churn'] = le.fit_transform(df['Churn'])
    df['Credit Cards'] = le.fit_transform(df['Credit Cards'])
    
    # Replace empty strings with NaN
    df['Yearly Average Balance (USD)'] = df['Yearly Average Balance (USD)'].replace(' ', np.nan).fillna(df['Monthly Average Balance (USD)'].median(), inplace=True)
    df['Monthly Average Balance (USD)'] = df['Monthly Average Balance (USD)'].replace(' ', np.nan).fillna(df['Monthly Average Balance (USD)'].median(), inplace=True)
    # df['tenure in months'] = df['tenure in months'].replace(' ', np.nan)
    # fill NaN
    # df['Monthly Average Balance (USD)'].fillna(df['Monthly Average Balance (USD)'].median(), inplace=True)
    # df['Yearly Average Balance (USD)'].fillna(df['Yearly Average Balance (USD)'].median(), inplace=True)
    df['tenure in months'].fillna(df['tenure in months'].median(), inplace=True)
    
    return df

df = preprocess_data(df)

# Correlation analysis
correlation_matrix = df[['Churn', 'Monthly Average Balance (USD)', 'Yearly Average Balance (USD)', 'tenure in months', 'Credit Cards']].corr()

# Plotting
plt.figure(figsize=(20, 16))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
plt.title('Correlation Heatmap with Churn')
plt.savefig('correlation_heatmap.png')
plt.close()

# Individual feature analysis
features = ['Monthly Average Balance (USD)', 'Yearly Average Balance (USD)', 'tenure in months', 'Credit Cards']

for feature in features:
    plt.figure(figsize=(10, 6))
    
    if feature != 'Credit Cards':
        # For numerical features
        sns.boxplot(x='Churn', y=feature, data=df)
        plt.title(f'{feature} vs Churn')
    else:
        # For categorical feature (Credit Cards)
        sns.countplot(x='Credit Cards', hue='Churn', data=df)
        plt.title('Credit Cards Ownership vs Churn')
        plt.xlabel('Has Credit Cards')
    
    plt.savefig(f'{feature.lower().replace(" ", "_")}_vs_churn.png')
    plt.close()

print("complete..")