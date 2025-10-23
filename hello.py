# school_performance_analysis.py

import pandas as pd
import matplotlib.pyplot as plt

# Sample data: replace with your CSV if needed
data = {
    "Student": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Math": [85, 78, 92, 70, 88],
    "Science": [90, 82, 85, 75, 95],
    "English": [88, 79, 90, 72, 86],
    "Attendance": [95, 88, 100, 80, 98]  # percentage
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate average score for each student
df["Average_Score"] = df[["Math", "Science", "English"]].mean(axis=1)

# Calculate pass/fail based on average score >= 75
df["Result"] = df["Average_Score"].apply(lambda x: "Pass" if x >= 75 else "Fail")

# Overall class metrics
average_class_score = df["Average_Score"].mean()
pass_percentage = len(df[df["Result"] == "Pass"]) / len(df) * 100
average_attendance = df["Attendance"].mean()

print("=== School Performance Metrics ===")
print(df)
print(f"\nClass Average Score: {average_class_score:.2f}")
print(f"Class Pass Percentage: {pass_percentage:.2f}%")
print(f"Average Attendance: {average_attendance:.2f}%")

# Visualization
plt.figure(figsize=(10,6))
plt.bar(df["Student"], df["Average_Score"], color='skyblue')
plt.axhline(y=75, color='r', linestyle='--', label='Pass Threshold')
plt.title("Average Scores of Students")
plt.ylabel("Average Score")
plt.xlabel("Student")
plt.legend()
plt.show()

# Save results to CSV
df.to_csv("school_performance_metrics.csv", index=False)
