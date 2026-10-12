"""
Student Management System (Console Application)
Day 1 Practical Project - Python Fundamentals

"""


students = []

def find_student(student_id):
    """Return the student dictionary with the given ID, or None if not found."""
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def calculate_grade(marks):
    """Return the grade letter for the given marks."""
    if marks >= 75:
        return "A"
    elif marks >= 65:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 35:
        return "D"
    else:
        return "F"


def get_valid_id(id_new=False):
    """
    Keep asking until the user enters a valid numeric ID.
    If id_new is True, the ID must not already exist.
    Returns the ID as an int.
    """
    while True:
        text = input("Enter Student ID: ").strip()

        if not text.isdigit():
            print("  Invalid ID. Please enter numbers only.")
            continue

        id = int(text)

        if id_new and find_student(id) is not None:
            print("  That ID already exists. Please use a different ID.")
            continue

        return id


def get_valid_marks():
    """Keep asking until the user enters marks between 0 and 100. Returns a float."""
    while True:
        text = input("Enter Marks (0-100): ").strip()

        try:
            marks = float(text)
        except ValueError:
            print("  Invalid marks. Please enter a number.")
            continue

        if 0 <= marks <= 100:
            return marks
        print("  Marks must be between 0 and 100.")


def get_valid_name():
    """Keep asking until the user enters a non-empty name. Returns a string."""
    while True:
        name = input("Enter Student Name: ").strip()
        if name:
            return name
        print("  Name cannot be empty.")


def print_student(student):
    """Print one student's details in a readable format."""
    print(f"  ID: {student['id']} | Name: {student['name']} | Marks: {student['marks']:.1f}")


def add_student():
    """Add a new student to the global list."""
    print("\n--- Add Student ---")
    student_id = get_valid_id(id_new =True)
    name = get_valid_name()
    marks = get_valid_marks()

    # Build the record as a dictionary and append it to the global list.
    new_student = {"id": student_id, "name": name, "marks": marks}
    students.append(new_student)
    print(f"Student '{name}' added successfully.")


def view_all_students():
    """Display every student, or a message if there are none."""
    print("\n--- All Students ---")
    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        print_student(student)
    print(f"Total students: {len(students)}")


def search_student():
    """Search for a student by ID and display the result."""
    print("\n--- Search Student ---")
    student_id = get_valid_id()
    student = find_student(student_id)

    if student is None:
        print("Student not found.")
    else:
        print("Student found:")
        print_student(student)


def update_marks():
    """Update the marks of an existing student."""
    print("\n--- Update Student Marks ---")
    student_id = get_valid_id()
    student = find_student(student_id)

    if student is None:
        print("Student not found.")
        return

    print(f"Current marks for {student['name']}: {student['marks']:.1f}")
    student["marks"] = get_valid_marks()
    print("Marks updated successfully.")


def delete_student():
    """Delete a student after asking for confirmation."""
    print("\n--- Delete Student ---")
    student_id = get_valid_id()
    student = find_student(student_id)

    if student is None:
        print("Student not found.")
        return

    confirm = input(f"Delete '{student['name']}'? (y/n): ").strip().lower()
    if confirm == "y":
        students.remove(student)
        print("Student deleted successfully.")
    else:
        print("Deletion cancelled.")


def calculate_average():
    """Return the average marks of all students (0 if there are none)."""
    if len(students) == 0:
        return 0
    total = 0
    for student in students:
        total += student["marks"]
    return total / len(students)


def find_top_performer():
    """Return the student with the highest marks, or None if there are none."""
    if len(students) == 0:
        return None
    top = students[0]
    for student in students:
        if student["marks"] > top["marks"]:
            top = student
    return top


def display_grade_report():
    """Show each student's grade, plus the class average and top performer."""
    print("\n--- Grade Report ---")
    if len(students) == 0:
        print("No student records found.")
        return

    print(f"{'ID':<8}{'Name':<20}{'Marks':<10}{'Grade':<6}")
    print("-" * 44)
    for student in students:
        grade = calculate_grade(student["marks"])
        print(f"{student['id']:<8}{student['name']:<20}{student['marks']:<10.1f}{grade:<6}")
    print("-" * 44)

    print(f"Class average: {calculate_average():.2f}")

    top = find_top_performer()
    print(f"Top performer: {top['name']} (ID {top['id']}) with {top['marks']:.1f} marks")


# Menu and main loop

def show_menu():
    """Print the main menu."""
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Display Grade Report")
    print("7. Exit")


def main():
    """Run the menu loop until the user chooses Exit."""
    running = True  # boolean flag controlling the loop

    while running:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            display_grade_report()
        elif choice == "7":
            print("\nThank you for using the Student Management System. Goodbye!")
            running = False
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()