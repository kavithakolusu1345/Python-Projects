import pandas as pd
import matplotlib.pyplot as plt

# Read Excel file
df = pd.read_excel("students.xlsx")
print("=== Student Dataset ===")
print(df)

# Calculate average marks
df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)

print("\n=== Average Marks ===")
print(df[["Name", "Average"]])

# Find top performer
topper = df.loc[df["Average"].idxmax()]

print("\n=== Top Performer ===")
print(topper)

# Create bar chart
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Average"])
plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.grid(True)

plt.show()