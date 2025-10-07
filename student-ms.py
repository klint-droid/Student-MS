import csv
import os

def data_validator(data):
    """Validates input by stripping spaces and checking if not empty."""
    if data and data.strip():
        return data.strip()
    return None


def add_students():
    students_data = []

    while True:
        # ID
        id = input("Enter School ID Number: ")
        validated_id = data_validator(id)

        if validated_id is None or not validated_id.isdigit():
            print("Invalid ID. Must be a number and not empty.")
            continue
        valid_id = int(validated_id)

        # Name
        name = input("Enter student name: ")
        validated_name = data_validator(name)
        if validated_name is None:
            print("Invalid Name! Cannot be empty.")
            continue

        # Age
        age = input("Enter student age: ")
        validated_age = data_validator(age)

        if validated_age is None or not validated_age.isdigit():
            print("Age must be a number.")
            continue

        valid_age = int(validated_age)
        if not (1 <= valid_age <= 120):
            print("Age must be between 1 and 120.")
            continue

        # Room Number
        room_number = input("Enter student room number: ")
        validated_room_number = data_validator(room_number)

        if validated_room_number is None or not validated_room_number.isdigit():
            print("Room number must be a number.")
            continue
        valid_room_number = int(validated_room_number)

        # Add student data
        students_data.append([valid_id, validated_name, valid_age, valid_room_number])

        more = input("Want to add more? (y): ").lower()
        if more != 'y':
            break
    
    return students_data


def view_students():
    if not os.path.exists("ex1.csv"):
        print("No student data found.")
        return
    
    with open("ex1.csv", "r") as file:
        reader = csv.reader(file)
        next(reader, None)
        print("\nCurrent Students Registered\n")
        for row in reader:
            id, name, age, room = row
            print(f"ID: {id}\t Name: {name}\t Age: {age}\t Room No.: {room}")

def count_students():
    if not os.path.exists("ex1.csv"):
        print("No student data found.")
        return 0
    
    with open("ex1.csv", 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        count = sum(1 for _ in reader)

    return count


def main():
    while True:
        print("\n Student Management System\n")
        print("1. Add new students")
        print("2. Display list of students")
        print("3. Exit\n")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            new_students = add_students()
            if new_students:
                file_exists = os.path.exists("ex1.csv")
                with open("ex1.csv", "a", newline='') as file:
                    writer = csv.writer(file)

                    if not file_exists or os.stat("ex1.csv").st_size == 0:
                        writer.writerow(["ID Number", "Name", "Age", "Room Number"])

                    writer.writerows(new_students)
                print(f"Saved {count_students()} student to file.")

        elif choice == '2':
            view_students()

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid Choice. Please try again.")


if __name__ == "__main__":
    main()
