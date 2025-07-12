import pandas as pd

# Load the exported Tableau CSV file
df = pd.read_csv("bankloan_raw_data.csv")

# Drop duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.fillna(0)  # You can replace with median or mean as needed

# Encode categorical values if needed (example)
if 'Education' in df.columns:
    df['Education'] = df['Education'].replace({1: 'Undergraduate', 2: 'Graduate', 3: 'Professional'})

# Drop ZIP Code if irrelevant
if 'ZIP Code' in df.columns:
    df = df.drop(columns=['ZIP Code'])

# Save cleaned dataset
df.to_csv("bankloan_cleaned.csv", index=False)

print("✅ Data cleaning complete. Cleaned file saved as bankloan_cleaned.csv.")
