students = []


# Add Student
def add_student():
    name = input("Enter student name: ").strip()
    
    if name == "":
        print("Name cannot be empty")
        return
    
    try:
        score = int(input("Enter score (0-100): "))
        
        if 0 <= score <= 100:
            students.append({"name": name, "score": score})
            print("Student added successfully")
        else:
            print("Score must be between 0 and 100")
    
    except:
        print("Invalid input, enter a number")


# View Students
def view_students():
    if len(students) == 0:
        print("No students found")
        return
    
    for student in students:
        grade = get_grade(student["score"])
        print(f'{student["name"]} - {student["score"]} - {grade}')


# Get Grade
def get_grade(score):
    if score >= 70:
        return "Distinction"
    elif score >= 50:
        return "Merit"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"


# Search Student
def search_student():
    name = input("Enter name to search: ").strip().lower()
    
    for student in students:
        if student["name"].lower() == name:
            print(f'{student["name"]} scored {student["score"]}')
            return
    
    print("Student not found")


# Sort Students
def sort_students():
    print("1. Sort by Name (A-Z)")
    print("2. Sort by Score (Highest-Lowest)")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        students.sort(key=lambda x: x["name"])
        print("Sorted by name")
    
    elif choice == "2":
        students.sort(key=lambda x: x["score"], reverse=True)
        print("Sorted by score")
    
    else:
        print("Invalid choice")


# Statistics
def show_statistics():
    if len(students) == 0:
        print("No data available")
        return
    
    scores = [s["score"] for s in students]
    
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)
    
    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")
    print(f"Average score: {average:.2f}")


# Menu System
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Sort Students")
    print("5. Show Statistics")
    print("6. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        sort_students()
    elif choice == "5":
        show_statistics()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice")
