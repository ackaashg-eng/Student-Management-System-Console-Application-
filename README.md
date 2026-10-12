# Student Management System

A console-based Student Management System written in Python. It was built as a Day 1 practical project to apply Python fundamentals: variables, data types, input and output, conditional statements, loops, functions, and local vs. global scope.

## Features

- Add a student (ID, name, marks)
- View all students
- Search for a student by ID
- Update a student's marks
- Delete a student (with confirmation)
- Display a grade report
- Exit the application

### Extras

- Student ID validation (numeric and unique)
- Marks validation (0-100)
- Automatic grade calculation
- Class average marks
- Top performer display

## Grading Scale

| Marks | Grade |
|-------|-------|
| 75 and above | A |
| 65 - 74 | B |
| 50 - 64 | C |
| 35 - 49 | D |
| Below 35 | F |

## Concepts Used

- Variables and data types (`int`, `float`, `str`, `bool`, `list`, `dict`)
- `input()` and `print()` with f-string formatting
- Conditional statements (`if`, `elif`, `else`)
- Loops (`while`, `for`) with `continue`
- Functions with parameters and return values
- A global list of dictionaries for storing records, and local variables inside functions

## How to Run

1. Install Python 3.
2. Download `student_management.py`.
3. Run it in a terminal:

```bash
python student_management.py
```

## Sample Menu

```
===== STUDENT MANAGEMENT SYSTEM =====
1. Add Student
2. View All Students
3. Search Student by ID
4. Update Student Marks
5. Delete Student
6. Display Grade Report
7. Exit
Enter your choice (1-7):
```

## Note

Student data is stored in memory only, so all records are cleared when the program exits.