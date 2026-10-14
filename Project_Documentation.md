# Student Performance Analytics System

## 1. Project Title
Student Performance Analytics System

Student Name: MOHD KAMRAN

Course: Python with AI - EWB Courses

## 2. Objective
Teachers have to calculate totals, averages, grades and results for many students. Doing this by hand takes time and mistakes can happen. This project does all of it automatically using Python, NumPy and Pandas.

## 3. Technologies Used
- Python 3
- NumPy
- Pandas
- VS Code

## 4. Dataset Description
File: students.csv (20 student records)

| Column | Meaning |
|---|---|
| Student_ID | Unique ID of the student |
| Name | Student name |
| Department | CSE, IT, ECE or MECH |
| Maths, Science, English, Computer | Marks out of 100 |
| Attendance | Attendance percentage |

## 5. Implementation
1. Imported pandas and numpy.
2. Loaded students.csv into a Pandas DataFrame using read_csv.
3. Displayed the data, columns and number of records.
4. Calculated Total with sum() and Average using NumPy round().
5. Used the function get_grade() with a loop to give each student a grade.
6. Used the function get_result() with a loop to find Pass or Fail.
7. Found highest, lowest and class average using idxmax(), idxmin() and np.mean().
8. Did subject-wise analysis using a for loop with np.max(), np.min() and np.mean().
9. Found the top 5 students using sort_values().
10. Saved the final table to final_result.csv.

### Grading Rule
| Average | Grade |
|---|---|
| 90 and above | A+ |
| 80 to 89 | A |
| 70 to 79 | B |
| 60 to 69 | C |
| 40 to 59 | D |
| Below 40 | F |

### Pass / Fail Rule
A student passes only if marks are 35 or more in every subject. If any subject is below 35, the student fails.

## 6. Key Features
- get_grade() function (in functions.py)
- get_result() function (in functions.py)
- Total and average marks of each student
- Pass / fail count and pass percentage
- Highest, lowest and class average
- Subject-wise highest, lowest and average
- Best and weakest subject
- Department-wise average
- Top 5 students
- Low attendance list

## 7. Output / Screenshots
Add your screenshots here, for example:

![Output 1](screenshots/output1.png)
![Output 2](screenshots/output2.png)

## 8. Final Outcome
The program runs without errors and shows all the results clearly. Isha Malhotra is the top student with an average of 94.5. Computer is the best subject and Maths is the weakest. 18 out of 20 students passed (90%) and the class average is 70.0.

## 9. Challenges & Learning
- Challenge: Showing all columns in the terminal. Solution: used pd.set_option to widen the display.
- Challenge: Writing the pass/fail rule. Solution: used a for loop to check every subject.
- Learning: How to use Pandas DataFrames, NumPy functions, loops and functions together in one project.

## 10. GitHub Repository
Link: PASTE YOUR GITHUB LINK HERE

## How to Run
1. Install the libraries: `pip install pandas numpy`
2. Keep main.py and students.csv in the same folder.
3. Run: `python main.py`
