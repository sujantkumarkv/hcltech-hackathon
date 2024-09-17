import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load preprocessed data
df = pd.read_csv('preprocessed_bank_data.csv')

# Calculate overall churn rate
churn_rate = (df['Churn'] == 1).mean()
print(f"Overall Churn Rate: {churn_rate:.2%}")

# Analyze churn by tenure
df['tenure_group'] = pd.cut(df['tenure in months'], bins=[0, 12, 24, 36, float('inf')], labels=['0-1 year', '1-2 years', '2-3 years', '3+ years'])
churn_by_tenure = df.groupby('tenure_group')['Churn'].mean()
churn_by_tenure.plot(kind='bar')
plt.title('Churn Rate by Tenure')
plt.show()

# Feature importance using Random Forest
X = df.drop(['customerID', 'Churn', 'Customer_Feedback'], axis=1)
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Print feature importances
for feature, importance in zip(X.columns, rf.feature_importances_):
    print(f"{feature}: {importance:.4f}")

# Model performance (for reference)
y_pred = rf.predict(X_test)
print(classification_report(y_test, y_pred))