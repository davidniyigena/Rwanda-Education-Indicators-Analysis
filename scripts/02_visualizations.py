# Rwanda Education Indicators Analysis
# Visualization Script
# Author: David Niyigena

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../data/rwanda_education_indicators.csv")

# 1. Enrollment trends over time
enrollment_df = df[df["indicator_name"].str.contains("enrollment", case=False)]

plt.figure(figsize=(10, 6))
sns.lineplot(
    data=enrollment_df,
    x="year",
    y="value",
    hue="education_level",
    marker="o"
)
plt.title("Rwanda School Enrollment Trends")
plt.xlabel("Year")
plt.ylabel("Enrollment Rate (%)")
plt.tight_layout()
plt.savefig("../visuals/enrollment_trends.png")
plt.close()

# 2. Completion rate trends
completion_df = df[df["indicator_name"].str.contains("completion", case=False)]

plt.figure(figsize=(10, 6))
sns.lineplot(
    data=completion_df,
    x="year",
    y="value",
    hue="education_level",
    marker="o"
)
plt.title("Rwanda Completion Rate Trends")
plt.xlabel("Year")
plt.ylabel("Completion Rate (%)")
plt.tight_layout()
plt.savefig("../visuals/completion_rate_trends.png")
plt.close()

# 3. Gender parity index trends
gender_df = df[df["indicator_name"].str.contains("gender parity", case=False)]

plt.figure(figsize=(10, 6))
sns.lineplot(
    data=gender_df,
    x="year",
    y="value",
    hue="education_level",
    marker="o"
)
plt.title("Rwanda Gender Parity Index Trends")
plt.xlabel("Year")
plt.ylabel("Gender Parity Index")
plt.tight_layout()
plt.savefig("../visuals/gender_parity_trends.png")
plt.close()

# 4. Pupil-teacher ratio trend
ptr_df = df[df["indicator_name"].str.contains("pupil-teacher", case=False)]

plt.figure(figsize=(10, 6))
sns.lineplot(
    data=ptr_df,
    x="year",
    y="value",
    marker="o"
)
plt.title("Rwanda Primary Pupil-Teacher Ratio Trend")
plt.xlabel("Year")
plt.ylabel("Students per Teacher")
plt.tight_layout()
plt.savefig("../visuals/pupil_teacher_ratio_trend.png")
plt.close()

# 5. Average indicator value by category
category_summary = (
    df.groupby("category")["value"]
    .mean()
    .reset_index()
    .sort_values(by="value", ascending=False)
)

plt.figure(figsize=(8, 5))
sns.barplot(
    data=category_summary,
    x="category",
    y="value"
)
plt.title("Average Education Indicator Value by Category")
plt.xlabel("Category")
plt.ylabel("Average Value")
plt.tight_layout()
plt.savefig("../visuals/average_indicator_by_category.png")
plt.close()

print("Visualization files created successfully in the visuals folder.")
