#Supply Chain dataset predictions

# Example code - 
# Use as template / start for your own code. 
# Notice that the code does not run as is.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# 1. Load data
df = pd.read_csv('supply_chain_data.csv')

# --- DATA CLEANING ---

# Drop columns with too many missing values or irrelevant ID columns
cols_to_drop = ['Product_Description', 'Order_Zipcode', 'Customer_Id']
df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])

# Handle missing values: Fill numeric with median and categorical with 'Unknown'
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

categorical_cols = df.select_dtypes(include=['object']).columns
df[categorical_cols] = df[categorical_cols].fillna('Unknown')

# Convert categorical features to numeric (One-Hot Encoding)
# We only select a few relevant features for this example
features = ['Days_for_shipment_scheduled', 'Order_Item_Discount', 'Sales', 'Shipping_Mode']
X = pd.get_dummies(df[features], drop_first=True)
y = df['Late_delivery_risk']

# - Datacleaning

import pandas as pd
import numpy as np

# 1. Load data with specific encoding often required for this dataset
df = pd.read_csv('DataCoSupplyChainDataset.csv', encoding='ISO-8859-1')

# 2. Drop Irrelevant and PII Columns
# These columns don't help predict delivery risk and protect privacy
cols_to_drop = [
    'Customer Email', 'Customer Password', 'Customer Fname', 'Customer Lname', 
    'Product Image', 'Order Zipcode', 'Customer Zipcode', 'Product Description'
]
df_cleaned = df.drop(columns=cols_to_drop)

# 3. Handle Missing Values
# Fill numeric gaps with median and categorical with 'Unknown'
df_cleaned['Order Item Profit Ratio'] = df_cleaned['Order Item Profit Ratio'].fillna(df_cleaned['Order Item Profit Ratio'].median())
df_cleaned['Customer City'] = df_cleaned['Customer City'].fillna('Unknown')

# 4. Date Transformation
# Convert string dates to datetime objects to extract features like 'hour' or 'day'
df_cleaned['order_date'] = pd.to_datetime(df_cleaned['shipping date (DateOrders)'])
df_cleaned['order_hour'] = df_cleaned['order_date'].dt.hour
df_cleaned['order_day'] = df_cleaned['order_date'].dt.dayofweek

# 5. Encoding Categorical Variables
# Convert 'Shipping Mode' and 'Department Name' into numeric format
df_cleaned = pd.get_dummies(df_cleaned, columns=['Shipping Mode', 'Department Name'], drop_first=True)

# 6. Final check for any remaining NaN values
print(df_cleaned.isnull().sum().sum())


# --- VISUALIZATION ---

plt.figure(figsize=(12, 5))

# Plot 1: Target Distribution
plt.subplot(1, 2, 1)
sns.countplot(x='Late_delivery_risk', data=df, palette='viridis')
plt.title('Distribution of Late Delivery Risk (0 = No, 1 = Yes)')

# Plot 2: Correlation Heatmap
plt.subplot(1, 2, 2)
sns.heatmap(df[numeric_cols].corr(), annot=False, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')

plt.tight_layout()
plt.show()

# Explain this. 

# 1. Calculate the correlation matrix for numeric columns
# We use numeric_only=True to avoid errors with text columns
correlation_matrix = df.corr(numeric_only=True)

# 2. Set up the matplotlib figure size
plt.figure(figsize=(12, 8))

# 3. Create a heatmap
# annot=True: Shows the correlation values in each cell
# cmap='coolwarm': Blue for negative, Red for positive correlation
# vmin/vmax: Sets the scale from -1 to 1 for standard correlation
sns.heatmap(correlation_matrix, 
            annot=True, 
            fmt=".2f", 
            cmap='coolwarm', 
            vmin=-1, 
            vmax=1, 
            center=0)

# 4. Add title and display
plt.title('Correlation Heatmap of Supply Chain Features')
plt.show()


# 2. Features (X) and target (y)
target_col = 'Late_delivery_risk'
features = ['Days_for_shipment_scheduled', 'Order_Item_Discount', 'Order_Item_Product_Price']
X = df[features]
y = df[target_col]

# 3. Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# 5. Predict and Evaluate
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")


# --- EVALUATION ---

y_pred = clf.predict(X_test)

print("--- Classification Report ---")
print(classification_report(y_test, y_pred))

# Confusion Matrix Visualization
plt.figure(figsize=(6, 4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
