# Student Data Organizer using Collection Data Types

students = []          # List to store all student records
subjects_set = set()   # Set to store unique subjects

# Function to add student
def add_student():
    print("\nEnter student details:")

    student_id = input("Student ID: ")
    name = input("Name: ")

    # Type casting
    age = int(input("Age: "))

    grade = input("Grade: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")

    subjects_input = input("Subjects (comma-separated): ")

    # Convert subjects into list
    subjects = [sub.strip() for sub in subjects_input.split(",")]

    # Add subjects to set
    subjects_set.update(subjects)

    # Tuple for immutable data
    student_info = (student_id, dob)

    # Dictionary for student details
    student = {
        "id": student_info[0],
        "dob": student_info[1],
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subjects
    }

    # Add dictionary to list
    students.append(student)

    print("\nStudent added successfully!")


# Function to display all students
def display_students():
    if not students:
        print("\nNo student records found.")
        return

    print("\n--- Display All Students ---")

    for student in students:
        subjects = ", ".join(student["subjects"])

        print(
            f"Student ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Grade: {student['grade']} | "
            f"Subjects: {subjects}"
        )


# Function to update student information
def update_student():
    student_id = input("\nEnter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:

            print("\nWhat do you want to update?")
            print("1. Age")
            print("2. Grade")
            print("3. Subjects")

            choice = input("Enter choice: ")

            if choice == "1":
                student["age"] = int(input("Enter new age: "))
                print("Age updated successfully!")

            elif choice == "2":
                student["grade"] = input("Enter new grade: ")
                print("Grade updated successfully!")

            elif choice == "3":
                new_subjects = input("Enter new subjects (comma-separated): ")
                student["subjects"] = [sub.strip() for sub in new_subjects.split(",")]

                # Update set
                subjects_set.update(student["subjects"])

                print("Subjects updated successfully!")

            else:
                print("Invalid choice!")

            return

    print("Student not found!")


# Function to delete student using del keyword
def delete_student():
    student_id = input("\nEnter Student ID to delete: ")

    for i in range(len(students)):
        if students[i]["id"] == student_id:
            del students[i]
            print("Student deleted successfully!")
            return

    print("Student not found!")


# Function to display unique subjects
def display_subjects():
    if not subjects_set:
        print("\nNo subjects available.")
    else:
        print("\nUnique Subjects Offered:")
        for subject in subjects_set:
            print(subject)


# Main program
while True:

    print("\nWelcome to the Student Data Organizer!")
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        display_subjects()

    elif choice == "6":
        print("\nThank you for using the Student Data Organizer!")
        break

    else:
        print("\nInvalid choice! Please try again.")
