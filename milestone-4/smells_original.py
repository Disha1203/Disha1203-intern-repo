# ============================================================
# 1. MAGIC NUMBERS & STRINGS
# ============================================================
def calculate_discount(price, user_type):
    if user_type == "student":
        return price * 0.10
    elif user_type == "teacher":
        return price * 0.20
    elif user_type == "senior":
        return price * 0.15


# ============================================================
# 2. LONG FUNCTION
# ============================================================
def process_order(order):
    # validate
    if order is None:
        print("No order found")
        return
    if "items" not in order or len(order["items"]) == 0:
        print("Order has no items")
        return

    # calculate total
    total = 0
    for item in order["items"]:
        total += item["price"] * item["quantity"]

    # apply discount
    if order["customer_type"] == "vip":
        total = total * 0.90
    elif order["customer_type"] == "member":
        total = total * 0.95

    # apply tax
    tax = total * 0.08
    total = total + tax

    # print receipt
    print(f"Customer: {order['name']}")
    print(f"Items: {len(order['items'])}")
    print(f"Tax: {tax:.2f}")
    print(f"Total: {total:.2f}")


# ============================================================
# 3. DUPLICATE CODE
# ============================================================
def print_math_result(scores):
    total = 0
    for score in scores:
        total += score
    average = total / len(scores)
    if average >= 90:
        grade = "A"
    elif average >= 70:
        grade = "B"
    else:
        grade = "F"
    print(f"Math — Average: {average:.2f}, Grade: {grade}")


def print_science_result(scores):
    total = 0
    for score in scores:
        total += score
    average = total / len(scores)
    if average >= 90:
        grade = "A"
    elif average >= 70:
        grade = "B"
    else:
        grade = "F"
    print(f"Science — Average: {average:.2f}, Grade: {grade}")


def print_english_result(scores):
    total = 0
    for score in scores:
        total += score
    average = total / len(scores)
    if average >= 90:
        grade = "A"
    elif average >= 70:
        grade = "B"
    else:
        grade = "F"
    print(f"English — Average: {average:.2f}, Grade: {grade}")


# ============================================================
# 4. LARGE CLASS (GOD OBJECT)
# ============================================================
class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []
        self.fees = []

    def add_student(self, name):
        self.students.append(name)

    def remove_student(self, name):
        self.students.remove(name)

    def add_teacher(self, name):
        self.teachers.append(name)

    def assign_course(self, course):
        self.courses.append(course)

    def calculate_fee(self, student):
        return 5000 * 0.10

    def send_fee_reminder(self, student):
        print(f"Reminder: {student} has a pending fee.")

    def generate_report_card(self, student, scores):
        average = sum(scores) / len(scores)
        print(f"{student} — Average: {average:.2f}")

    def print_all_students(self):
        for s in self.students:
            print(s)

    def print_all_teachers(self):
        for t in self.teachers:
            print(t)

    def print_all_courses(self):
        for c in self.courses:
            print(c)


# ============================================================
# 5. DEEPLY NESTED CONDITIONALS
# ============================================================
def get_student_status(student):
    if student is not None:
        if isinstance(student, dict):
            if "scores" in student:
                if isinstance(student["scores"], list):
                    if len(student["scores"]) > 0:
                        average = sum(student["scores"]) / len(student["scores"])
                        if average >= 90:
                            return "Excellent"
                        elif average >= 70:
                            return "Passed"
                        else:
                            return "Failed"
                    else:
                        return "No scores found"
                else:
                    return "Scores must be a list"
            else:
                return "Missing scores"
        else:
            return "Invalid student format"
    else:
        return "Student is None"


# ============================================================
# 6. COMMENTED-OUT CODE
# ============================================================
def calculate_final_score(scores):
    # total = 0
    # for s in scores:
    #     total = total + s
    # avg = total / len(scores)
    # return avg

    return sum(scores) / len(scores)

    # TODO: fix this later
    # if avg > 100:
    #     avg = 100


# ============================================================
# 7. INCONSISTENT NAMING
# ============================================================
def Calc(s, tp):
    Res = 0
    for itm in s:
        Res += itm
    AVG = Res / len(s)
    if tp == "student":
        disc = AVG * 0.10
    elif tp == "teacher":
        disc = AVG * 0.20
    else:
        disc = 0
    FinalVal = AVG - disc
    return FinalVal