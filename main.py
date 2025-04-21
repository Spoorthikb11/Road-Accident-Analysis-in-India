# STEP 1: Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files

# STEP 2: Upload the dataset (CSV file)
print("Please upload your 'road_accidents_india.csv' file:")
uploaded = files.upload()  # Upload the file manually when prompted

# STEP 3: Read the uploaded file
df = pd.read_csv("road_accidents_india.csv")
print("\n✅ First 5 rows of the dataset:")
print(df.head())

# STEP 4: Total accidents by state (Top 10)
print("\n📊 Total Accidents by State (Top 10):")
state_data = df.groupby("State/UT")["Total Accidents"].sum().sort_values(ascending=False).head(10)
print(state_data)

# Plotting state-wise data
plt.figure(figsize=(10, 5))
state_data.plot(kind='bar', color='skyblue')
plt.title("Top 10 States by Total Accidents")
plt.ylabel("Total Accidents")
plt.xlabel("State")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# STEP 5: Year-wise trend
print("\n📈 Yearly Total Accidents:")
yearly_data = df.groupby("Year")["Total Accidents"].sum()
print(yearly_data)

# Plotting year-wise trend
plt.figure(figsize=(8, 4))
yearly_data.plot(marker='o', color='green')
plt.title("Yearly Road Accidents in India")
plt.xlabel("Year")
plt.ylabel("Total Accidents")
plt.grid(True)
plt.tight_layout()
plt.show()

# STEP 6: Cause-wise analysis (if 'Cause' column is available)
if 'Cause' in df.columns:
    print("\n🛑 Accidents by Cause (Top 10):")
    cause_data = df.groupby("Cause")["Total Accidents"].sum().sort_values(ascending=False).head(10)
    print(cause_data)

    # Plotting causes
    plt.figure(figsize=(10, 5))
    cause_data.plot(kind='barh', color='coral')
    plt.title("Top Causes of Road Accidents")
    plt.xlabel("Total Accidents")
    plt.tight_layout()
    plt.show()
else:
    print("\n⚠ No 'Cause' column found in your dataset. Skipping cause analysis.")
