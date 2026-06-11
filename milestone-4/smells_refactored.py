# ============================================================
# 1. MAGIC NUMBERS & STRINGS — use named constants
# ============================================================
DISCOUNT_RATES = {
    "student": 0.10,
    "teacher": 0.20,
    "senior":  0.15,
}

def calculate_discount(price, user_type):
    discount_rate = DISCOUNT_RATES.get(user_type, 0)
    return price * discount_rate


# ============================================================
# 2. LONG FUNCTION — extract into focused helpers
# ============================================================
VIP_DISCOUNT    = 0.90
MEMBER_DISCOUNT = 0.95
TAX_RATE        = 0.08

def validate_order(order):
    if order is None:
        raise ValueError("No order found")
    if "items" not in order or len(order["items"]) == 0:
        raise ValueError("Order has no items")

def calculate_order_subtotal(items):
    return sum(item["price"] * item["quantity"] for item in items)

def apply_customer_discount(subtotal, customer_type):
    if customer_type == "vip":
        return subtotal * VIP_DISCOUNT
    elif customer_type == "member":
        return subtotal * MEMBER_DISCOUNT
    return subtotal

def apply_tax(amount):
    tax = amount * TAX_RATE
    return amount + tax, tax

def print_receipt(order, tax, total):
    print(f"Customer: {order['name']}")
    print(f"Items: {len(order['items'])}")
    print(f"Tax: {tax:.2f}")
    print(f"Total: {total:.2f}")

def process_order(order):
    validate_order(order)
    subtotal        = calculate_order_subtotal(order["items"])
    discounted      = apply_customer_discount(subtotal, order["customer_type"])
    total, tax      = apply_tax(discounted)
    print_receipt(order, tax, total)


# ============================================================
# 3. DUPLICATE CODE — single reusable function
# ============================================================
def calculate_average(scores):
    return sum(scores) / len(scores)

def determine_grade(average):
    if average >= 90:
        return "A"
    elif average >= 70:
        return "B"
    else:
        return "F"

def print_subject_result(subject, scores):
    average = calculate_average(scores)
    grade   = determine_grade(average)
    print(f"{subject} — Average: {average:.2f}, Grade: {grade}")

# Usage
# print_subject_result("Math",    [92, 88, 95])
# print_subject_result("Science", [70, 65, 80])
# print_subject_result("English", [55, 60, 58])


# ============================================================
# 4. LARGE CLASS — split into focused classes
# ============================================================
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(name)

    def remove_student(self, name):
        self.students.remove(name)

    def print_all_students(self):
        for student in self.students:
            print(student)


class TeacherManager:
    def __init__(self):
        self.teachers = []

    def add_teacher(self, name):
        self.teachers.append(name)

    def print_all_teachers(self):
        for teacher in self.teachers:
            print(teacher)


class FeeManager:
    BASE_FEE      = 5000
    DISCOUNT_RATE = 0.10

    def calculate_fee(self):
        return self.BASE_FEE * self.DISCOUNT_RATE

    def send_fee_reminder(self, student):
        print(f"Reminder: {student} has a pending fee.")


class ReportManager:
    def generate_report_card(self, student, scores):
        average = sum(scores) / len(scores)
        print(f"{student} — Average: {average:.2f}")


# ============================================================
# 5. DEEPLY NESTED CONDITIONALS — use guard clauses
# ============================================================
def get_student_status(student):
    if student is None:
        return "Student is None"

    if not isinstance(student, dict):
        return "Invalid student format"

    if "scores" not in student:
        return "Missing scores"

    if not isinstance(student["scores"], list):
        return "Scores must be a list"

    if len(student["scores"]) == 0:
        return "No scores found"

    average = sum(student["scores"]) / len(student["scores"])

    if average >= 90:
        return "Excellent"
    elif average >= 70:
        return "Passed"
    else:
        return "Failed"


# ============================================================
# 6. COMMENTED-OUT CODE — removed, logic is clean
# ============================================================
def calculate_final_score(scores):
    return sum(scores) / len(scores)


# ============================================================
# 7. INCONSISTENT NAMING — descriptive consistent names
# ============================================================
def calculate_discounted_average(scores, user_type):
    average       = sum(scores) / len(scores)
    discount_rate = DISCOUNT_RATES.get(user_type, 0)
    discounted    = average * discount_rate
    return average - discounted