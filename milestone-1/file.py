scores = {
    'math': 95,
    'science': 73,
    'english': 61
}

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 70:
        return "B"
    else:
        return "F"

def print_subject_grades(scores):
    for subject, score in scores.items():
        grade = get_letter_grade(score)
        print(f"{subject.capitalize()}: {grade}")

print_subject_grades(scores)