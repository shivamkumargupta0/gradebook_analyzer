# -------------------------------------------------------------
# Title: GradeBook Analyzer CLI
# Author: [Your Name]
# Date: 29 Nov 2025
# Purpose: Automates student grade analysis & statistics
# -------------------------------------------------------------

import csv
import statistics

def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    return statistics.median(marks_dict.values())

def find_max_score(marks_dict):
    return max(marks_dict.values())

def find_min_score(marks_dict):
    return min(marks_dict.values())

def assign_grades(marks_dict):
    grades = {}
    for student, score in marks_dict.items():
        if score >= 90:
            grades[student] = "A"
        elif score >= 80:
            grades[student] = "B"
        elif score >= 70:
            grades[student] = "C"
        elif score >= 60:
            grades[student] = "D"
        else:
            grades[student] = "F"
    return grades

def grade_distribution(grades_dict):
    dist = {"A":0, "B":0, "C":0, "D":0, "F":0}
    for g in grades_dict.values():
        dist[g] += 1
    return dist

def manual_input():
    marks = {}
    total = int(input("Enter number of students: "))
    for _ in range(total):
        name = input("Enter student name: ")
        score = int(input(f"Enter marks for {name}: "))
        marks[name] = score
    return marks

def csv_import():
    marks = {}
    filename = input("Enter CSV file name (with extension): ")

    try:
        with open(filename, mode="r") as file:
            reader = csv.reader(file)
            rows = list(reader)
            print("DEBUG rows ->", rows)


            if not rows or len(rows) < 2:
                print("CSV file is empty or missing student rows.")
                return {}

            # detect header
            if rows[0][0].lower() == "name":
                data_rows = rows[1:]
            else:
                data_rows = rows

            for row in data_rows:
                try:
                    name = row[0].strip()
                    score = int(row[1].strip())
                    marks[name] = score
                except:
                    print(f"Invalid row ignored: {row}")

        return marks

    except FileNotFoundError:
        print("File not found. Check the filename and try again.")
        return {}

def print_results_table(marks, grades):
    print("\n---------------------------------------------")
    print("Name\t\tMarks\tGrade")
    print("---------------------------------------------")
    for student in marks:
        print(f"{student}\t\t{marks[student]}\t{grades[student]}")
    print("---------------------------------------------\n")

def main():
    print("=============================================")
    print("       GradeBook Analyzer - Python CLI        ")
    print("=============================================")

    while True:
        print("\nMENU OPTIONS:")
        print("1. Manual Input")
        print("2. Import From CSV")
        print("3. Exit")

        choice = input("Enter option (1/2/3): ")

        if choice == "1":
            marks = manual_input()

        elif choice == "2":
            marks = csv_import()
            if not marks:
                continue

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid option. Try again.")
            continue

        avg = calculate_average(marks)
        med = calculate_median(marks)
        max_score = find_max_score(marks)
        min_score = find_min_score(marks)

        grades = assign_grades(marks)
        dist = grade_distribution(grades)

        passed_students = [name for name, score in marks.items() if score >= 40]
        failed_students = [name for name, score in marks.items() if score < 40]

        print("\nSTATISTICAL SUMMARY:")
        print(f"Average Score: {avg:.2f}")
        print(f"Median Score : {med}")
        print(f"Highest Score: {max_score}")
        print(f"Lowest Score : {min_score}\n")

        print("GRADE DISTRIBUTION:")
        for grade, count in dist.items():
            print(f"{grade}: {count}")

        print("\nPass/Fail Summary:")
        print(f"Passed ({len(passed_students)}): {passed_students}")
        print(f"Failed ({len(failed_students)}): {failed_students}")

        print_results_table(marks, grades)

        repeat = input("Run again? (y/n): ").lower()
        if repeat != "y":
            print("Thank you for using GradeBook Analyzer. Goodbye!")
            break


if __name__ == "__main__":
    main()
