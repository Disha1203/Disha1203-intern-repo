students = [
    {"name": "Alice", "scores": [92, 88, 95]},
    {"name": "Bob", "scores": [60, 55, 58]},
    {"name": "Carol", "scores": [78, 82, 74]},
    {"name": "David", "scores": [95, 98, 100]},
    {"name": "Eve", "scores": [40, 45, 38]},
]


def calculate_average(scores):
    return sum(scores) / len(scores)


def determine_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def determine_status(grade):
    if grade == "F":
        return "Fail"
    return "Pass"


def build_student_result(student):
    average = calculate_average(student["scores"])
    grade = determine_grade(average)
    status = determine_status(grade)

    return {
        "name": student["name"],
        "average": average,
        "grade": grade,
        "status": status
    }


def print_result(result):
    print(
        f"{result['name']} | "
        f"Avg: {result['average']:.2f} | "
        f"Grade: {result['grade']} | "
        f"{result['status']}"
    )


def process_students(students):
    for student in students:
        result = build_student_result(student)
        print_result(result)


process_students(students)