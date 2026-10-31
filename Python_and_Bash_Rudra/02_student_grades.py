students = {
    "Raj": "A",
    "Meet": "B",
    "Sujal": "C"
}

while True:
    print("\nChoose an option:")
    print("1. Add Student")
    print("2. Update Student Grade")
    print("3. Display All Students")
    print("4. Exit")

    result = int(input("Enter your choice: "))

    if result == 1:
        s_name = input("Enter Student Name: ")
        s_grade = input("Enter Student Grade: ")

        if s_name in students:
            print("Student already exists")
        else:
            students[s_name] = s_grade
            print("Student added successfully")

    elif result == 2:
        s_name = input("Enter Student Name: ")

        if s_name in students:
            s_grade = input("Enter New Grade: ")
            students[s_name] = s_grade
            print("Grade updated successfully")
        else:
            print("Student does not exist")

    elif result == 3:
        print("\nStudent Grades:")
        for key, value in students.items():
            print(key, ":", value)

    elif result == 4:
        print("Program exited successfully")
        break

    else:
        print("Invalid choice. Please select 1 to 4.")
