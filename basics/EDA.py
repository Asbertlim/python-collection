# EDA (Exploratory Data Analysis) -> process of investigating, cleaning and visualising data to discover useful information'
# EDA helps us understand the structure, quality, distribution and relationships within a dataset. 
# It allows us to identify missing values, duplicates, outliers and potential patterns before training a machine-learning model.
# df.head() -> first 5 rows
# df.tail() -> last 5 rows
# df.info() -> data types and missing values
# df.describe() -> statistical summary
# df.nunique() -> number of unique values
# df.value_counts() -> freq of categorical values
# df.corr(numeric_only=True) -> correlation btwn numericla variables
# df.isnull.sum() -> identify missing data

# correlation -> measures how strongly two numerical variables are related linearly
# print(df.corr(numeric_only=True)) -> 

# Code

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "study_hours": [2, 5, 3, 8, 6, 1, 7, 4, 9, 3],
    "attendance": [60, 90, 75, 95, 85, 50, 90, 80, 98, 70],
    "previous_score": [45, 75, 60, 90, 80, 30, 85, 65, 95, 55],
    "sleep_hours": [6, 8, 7, 8, 7, 5, 8, 6, 8, 7],
    "result": ["Fail", "Pass", "Fail", "Pass", "Pass",
               "Fail", "Pass", "Pass", "Pass", "Fail"]
}

df = pd.DataFrame(data)

print(df["study_hours"].mean())

duplicates = df.duplicated().sum()
print(duplicates)

pas = 0
fail = 0

print(df["result"].value_counts())

plt.hist(df["previous_score"], bins=5)
plt.xlabel("Previous Score")
plt.ylabel("Frequency")
plt.title("Distribution of Previous Score")
plt.show()

plt.scatter(df["study_hours"], df["previous_score"])
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.title("Study Hours vs Previous Score")
plt.show()

