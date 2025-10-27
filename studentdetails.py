# Dictionary to store student records
students = {}

def accept_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    students[student_id] = {"Name": name, "Age": age}
    print("Student added successfully.")

def display_students():
    print("Student Records:")
    for student_id, info in students.items():
        print(f"ID: {student_id}, Name: {info['Name']}, Age: {info['Age']}")

def search_student():
    student_id = input("Enter student ID to search: ")
    if student_id in students:
        print(f"Found: ID: {student_id}, Name: {students[student_id]['Name']}, Age: {students[student_id]['Age']}")
    else:
        print("Student not found.")

def delete_student():
    student_id = input("Enter student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully.")
    else:
        print("Student not found.")

# Example usage:
while True:
    print("""
1. Add Student Details 
2. Display All Students
3. Search Student
4. Delete Student
5. Exit """)
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        accept_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
