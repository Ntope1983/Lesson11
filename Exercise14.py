# CRUD with dictionary
students = [{"name": "john",
             "Surname": "Polydoras",
             "FatherName": "Konstantinos",
             "Age": 42,
             "Class": 1,
             "idCard": 1038942,
             "id": 1000},
            {
                "name": "Maria",
                "Surname": "Papadopoulou",
                "FatherName": "Georgios",
                "Age": 21,
                "Class": 1,
                "idCard": 2038451,
                "id": 1001
            },
            {
                "name": "Nikos",
                "Surname": "Dimitriou",
                "FatherName": "Alexandros",
                "Age": 22,
                "Class": 2,
                "idCard": 2038452,
                "id": 1002
            },
            ]


def check_student(x, y, z):
    for stud in students:
        if stud["name"] == x and stud["Surname"] == y and stud["FatherName"] == z:
            print("The student you entered exists with these details")
            print_student_details(stud["id"], False)
            return True
    else:
        return False


def print_student_details(x, all_students):
    if x != 0:
        for student in students:
            if student["id"] == int(x):
                print(
                    f"id: {student["id"]} Name: {student["name"]} Surname: {student["Surname"]},FatherName: {student["FatherName"]}"
                    f"Age: {student["Age"]} Class: {student["Class"]} idCard: {student["idCard"]}")
    elif all_students:
        for student in students:
            print(
                f"id: {student["id"]} Name: {student["name"]} Surname: {student["Surname"]},FatherName: {student["FatherName"]}"
                f"Age: {student["Age"]}, Class: {student["Class"]}, idCard: {student["idCard"]}")
    else:
        for student in students:
            print(f"{student["name"]} {student["FatherName"][0]} {student["Surname"]}")


def get_names():
    while True:
        name = input("Enter your name: ").strip()
        surname = input("Enter your surname: ").strip()
        father_name = input("Enter your father's name: ").strip()

        if not name or not father_name or not surname:
            print("Name, father's name, and surname must not be empty.")
        elif not name.isalpha() or not father_name.isalpha() or not surname.isalpha():
            print("All fields must contain only letters.")
        else:
            return name, surname, father_name


def get_age_class_idcard():
    # Get valid age
    while True:
        age_input = input("Enter your age: ").strip()
        if age_input.isdigit() and int(age_input) > 0:
            age = int(age_input)
            break
        else:
            print("Age must be a positive integer.")

    # Get valid class (1-6)
    while True:
        class_input = input("Enter your class (1-6): ").strip()
        if class_input.isdigit() and 1 <= int(class_input) <= 6:
            class_num = int(class_input)
            break
        else:
            print("Class must be an integer between 1 and 6.")

    # Get valid ID card (letters and numbers only)
    while True:
        id_card = input("Enter your ID card: ").strip()
        if id_card.isalnum():
            break
        else:
            print("ID Card must contain only letters and numbers.")

    return age, class_num, id_card


def insert_student():
    name, surname, fathers_name = get_names()
    if check_student(name, surname, fathers_name):
        option_2 = input("Do u want to Continue with these details? 1:Yes 2:No ")
        if option_2 == "2":
            print("Exit without save:")
            main()
    age, class1, idcard = get_age_class_idcard()
    students.append({
        "name": name,
        "Surname": surname,
        "FatherName": fathers_name,
        "Age": int(age),
        "Class": int(class1),
        "idCard": idcard,
        "id": next_id()
    })


def next_id():
    return max({student["id"] for student in students}) + 1


def get_valid_input(last_number):
    while True:
        try:
            value = int(input(f"\nEnter a number (1 to {last_number}): "))
            if 1 <= value <= last_number:
                return str(value)
            else:
                print(f"Number must be between 1 and {last_number}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    print("--------------------------------")
    menu = {1: "Δημιουργία Εγγραφής",
            2: "Εκτύπωση",
            3: "Ενημέρωση Εγγραφής",
            4: "Διαγραφή Εγγραφής",
            5: "Έξοδος"}
    while True:
        for option in menu:
            print(str(option) + " " + menu[option], end=" ")
        choose_option = get_valid_input(5)
        if choose_option == "1":
            insert_student()

        elif choose_option == "2":
            menu2 = {1: "Εκτύπωση Μαθητή",
                     2: "Εκτύπωση όλων των μαθητών",
                     3: "Εκτύπωση μόνο ονομάτων μαθητών"}
            for option in menu2:
                print(str(option) + " " + menu2[option], end=" ")
            choose_option2 = get_valid_input(3)
            if choose_option2 == "1":
                std_id = int(input("\nGive the student id"))
                print_student_details(std_id, False)
            elif choose_option2 == "2":
                print_student_details(0, True)
            elif choose_option2 == "3":
                print_student_details(0, False)


main()
