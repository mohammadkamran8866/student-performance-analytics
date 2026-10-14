import pandas as pd
import numpy as np
from functions import get_grade, get_result

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

subjects = ["Maths", "Science", "English", "Computer"]


df = pd.read_csv("students.csv")

print("========== STUDENT DATA ==========")
print(df)
print()
print("Columns:", list(df.columns))
print("Number of records:", len(df))
print()
df.info()
print()

df["Total"] = df[subjects].sum(axis=1)
df["Average"] = np.round(df["Total"] / len(subjects), 2)

grades = []
for avg in df["Average"]:
    grades.append(get_grade(avg))
df["Grade"] = grades

results = []
for i in range(len(df)):
    marks = df.loc[i, subjects]
    results.append(get_result(marks))
df["Result"] = results

print("========== RESULT TABLE ==========")
print(df[["Student_ID", "Name", "Total", "Average", "Grade", "Result"]])
print()

print("========== OVERALL ANALYSIS ==========")
top = df.loc[df["Average"].idxmax()]
low = df.loc[df["Average"].idxmin()]
print("Highest average:", top["Name"], "-", top["Average"])
print("Lowest average:", low["Name"], "-", low["Average"])
print("Overall class average:", np.round(np.mean(df["Average"]), 2))
print("Average attendance:", np.round(np.mean(df["Attendance"]), 2), "%")
print()

passed = len(df[df["Result"] == "Pass"])
failed = len(df[df["Result"] == "Fail"])
print("Students passed:", passed)
print("Students failed:", failed)
print("Pass percentage:", np.round(passed / len(df) * 100, 2), "%")
print()

print("========== GRADE COUNT ==========")
print(df["Grade"].value_counts())
print()

print("========== SUBJECT-WISE ANALYSIS ==========")
subject_averages = {}
for sub in subjects:
    avg = np.round(np.mean(df[sub]), 2)
    subject_averages[sub] = avg
    print(sub, "-> Highest:", np.max(df[sub]), "| Lowest:", np.min(df[sub]), "| Average:", avg)

best_subject = max(subject_averages, key=subject_averages.get)
weak_subject = min(subject_averages, key=subject_averages.get)
print()
print("Best subject:", best_subject)
print("Weakest subject:", weak_subject)
print()

print("========== DEPARTMENT-WISE AVERAGE ==========")
print(df.groupby("Department")["Average"].mean().round(2))
print()

print("========== TOP 5 STUDENTS ==========")
top5 = df.sort_values("Average", ascending=False).head(5)
print(top5[["Student_ID", "Name", "Department", "Average", "Grade"]])
print()

print("========== LOW ATTENDANCE (below 75%) ==========")
low_att = df[df["Attendance"] < 75]
print(low_att[["Name", "Attendance", "Result"]])

df.to_csv("final_result.csv", index=False)
print()
print("Final results saved in final_result.csv")
