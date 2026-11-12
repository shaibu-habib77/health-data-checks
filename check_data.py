
import pandas as pd

# Load the dataset
df = pd.read_csv("data.csv")

print("HEALTH DATA QUALITY CHECK")
print("-------------------------")

# 1. Check dataset dimensions
print("\nDataset shape:", df.shape)

# 2. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 3. Check duplicate records
print("\nDuplicate records:", df.duplicated().sum())

# 4. Check age validity
print("\nInvalid ages:", (~df["age"].between(0, 120)).sum())

# 5. Check BMI validity
print("Invalid BMI:", (~df["bmi"].between(10, 80)).sum())

# 6. Check glucose validity
print("Invalid glucose:", (~df["glucose"].between(20, 600)).sum())

# 7. Check diabetes labels
print("Invalid diabetes labels:",
      (~df["diabetes"].isin([0, 1])).sum())

print("\nData quality check completed.")
