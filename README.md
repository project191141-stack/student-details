## ⚙️ Functions Overview

| Function | Description |
|-----------|--------------|
| `accept_student()` | Prompts user to enter ID, name, and age; stores in dictionary |
| `display_students()` | Displays all student records in a formatted list |
| `search_student()` | Finds a student by ID and prints details |
| `delete_student()` | Deletes a student by ID if found |

***

### 🚀 Getting Started

#### 1. Clone or download the repository
```bash
git clone https://github.com/yourusername/student-record-system.git
cd student-record-system
```

#### 2. Run the application
Make sure Python is installed, then execute:
```bash
python student_records.py
```

#### 3. Use the menu
```
1. Add Student Details
2. Display All Students
3. Search Student
4. Delete Student
5. Exit
```
Select a number to perform the corresponding action.

***

### 🧩 Example Run

```
1. Add Student Details
2. Display All Students
3. Search Student
4. Delete Student
5. Exit
Enter your choice (1-5): 1
Enter student ID: 101
Enter student name: Sarah
Enter student age: 18
Student added successfully.
```

***

### ⚠️ Limitations

- Data is **not persistent** (erased when program exits)  
- No duplicate ID check implemented  
- Minimal input validation  


