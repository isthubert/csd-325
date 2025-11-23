# Isaac St Hubert Module 8.2 11/23/2025
# This program displays a class list from a json file and appends a new student

import json

def print_students(student_list):
    for s in student_list:
        print(f"{s['L_Name']}, {s['F_Name']} : ID = {s['Student_ID']} , Email = {s['Email']}")


def main():

    with open("student.json", "r") as f:
        students = json.load(f)

    print("=== Original Student List ===\n")
    print_students(students)

    new_student = {
        "F_Name": "Isaac",
        "L_Name": "St Hubert",
        "Student_ID": 75237,
        "Email": "isthubert@gmail.com"
    }

    students.append(new_student)

    print("\n=== Updated Student List ===")
    print_students(students)

    with open("student.json", "w") as f:
        json.dump(students, f, indent=4)

    print("The student.json file has been updated.")


main()
