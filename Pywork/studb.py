student_db={
    "1001": {"name":"placehlder","age":23,"course":"cs"}
    }

def add_student():
    student_id = input("Enter student ID: ")
    if student_id in student_db:
        print("Student ID already exists! Please choose a unique ID.")
        return
    
    name = input("Enter student name: ").strip()
    age = int(input("Enter student age: "))
    course = input("Enter student course: ")
    
    student_db[student_id] = {"name": name, "age": age, "course": course}
    print(f"Student {name} added successfully!")

def view_students():
    if not student_db:
        print("No students in the database.")
        return
    
    print("\nStudent Database:")
    for student_id, details in student_db.items():
        print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}, Course: {details['course']}")

def search_student():
    student_id = input("Enter student ID to search: ")
    if student_id in student_db:
        details = student_db[student_id]
        print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}, Course: {details['course']}")
    else:
        print("Student not found!")

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting, Goodbye...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()