# Clean code principles

## Goal
Understand the core principles of clean code and why they matter in real-world development.

## Principles 

### Simplcity
Keeping code as straightforward as possible
It's easier to 
* understand 
* debug
* modify
- Devs should avoid unnecessary complexity and only implements what's needed to solve the problem

#### Example
Instead of creating multiple nested conditions to check if a user is an adult, use a simple condition:
```
if age >= 18:
        print("Adult")
```

### Readability
Code written in a way that makes its purpose clear to other devs
Includes
* meaningful variable names
* proper formatting 
* clear logic
It's important since:
* Makes collaboration easier
* Reduces misunderstanding
* Improves code reviews

#### Example
Poor readability:
```
x = 50000 
y = 0.08 
z = x * y
```
Better readability:
```
salary = 50000 
tax_rate = 0.08 
tax_amount = salary * tax_rate
```

### Maintainability
Code can be modified, extended, and fixed without introducing new problems. Good structure and organization help future developers work on the code efficiently.
It's importance since:
* Easier to add new features
* Simplifies bug fixes
* Reduces technical debt

#### Example
Instead of repeating the same calculation in multiple places, create a reusable function:
```
def calculate_discount(price, discount_percentage):
    return price - (price * discount_percentage / 100)
```
If the discount logic changes later, it only needs to be updated in one place

### Consistency
Following the same coding style, naming conventions, and project standards throughout the codebase.
It's importance since:
* Makes code predictable
* Improves teamwork
* Simplifies navigation through large projects

#### Example
Inconsistent naming:
```
userName = "John" 
user_age = 25 
UserEmail = "john@example.com"
```
Consistent naming:
```
user_name = "John" 
user_age = 25
user_email = "john@example.com"
```
Using the same naming convention throughout the project makes the code easier to follow.

### Efficiency
Writing code that performs well and uses resources effectively. However, devs should avoid premature optimization and focus on writing clear code first.
It's importance since:
* Better performance
* Improved user experience
* Efficient use of system resources
#### Example
Inefficient approach:
```
numbers = [1, 2, 3, 4, 5] 
count = 0 
for number in numbers: 
    count += 1
```

Efficient approach:
```
numbers = [1, 2, 3, 4, 5] 
count = len(numbers)
```
Using built-in functions when appropriate can improve performance and make code easier to understand.

## Example

### Messy code
```
def f(a):
    x = 0 
    for i in a: 
        if i > 50: 
            x += i 
    print(x)

```
#### Problems with this code
* The function name `f` is not descriptive.
* Variable names such as `a` and `x` do not explain their purpose.
* There are no comments or documentation.
* The function prints the result instead of returning it, making it harder to reuse.
* The intent of the code is not immediately obvious.

### Cleaner Version

```
def calculate_sum_of_large_numbers(numbers):
    total = 0
    for number in numbers: 
        if number > 50: 
            total += number 
    return total
```

#### Why This Version Is Better
* Uses descriptive function and variable names.
* Clearly communicates its purpose.
* Returns a value instead of printing directly.
* Easier to test and reuse.
* Follows clean code principles of readability and maintainability.

---

# Naming Variables & Functions

## Goal 
Learn how to choose clear and meaningful names for variables and functions.

## Best Practices
* Use descriptive and meaningful names.
* Prefer nouns for variables and classes.
* Prefer verbs for functions and methods.
* Follow the naming conventions of the programming language.
* Avoid single-letter names except for common loop counters such as `i` and `j`.
* Avoid misleading abbreviations.
* Keep names searchable and easy to pronounce.
* Be consistent throughout the project.

## Example

### Poorly Named Code
```
def f(a): 
    t = 0
    for x in a: 
        if x > 50: 
            t += x 
    return t
```

#### Problems
* The function name `f` provides no indication of its purpose.
* The parameter name `a` does not describe the data being passed.
* The variable `t` does not explain what value is being stored.
* Developers must read the entire function to understand what it does.

### Refactored Version
```
def calculate_sum_of_large_numbers(numbers):
    total_sum = 0 
    
    for number in numbers: 
        if number > 50: 
            total_sum += number 
            
    return total_sum
```
#### Improvements
* `calculate_sum_of_large_numbers` clearly describes the function's purpose.
* `numbers` indicates that the input is a collection of numbers.
* `total_sum` explains what value is being accumulated.
* The code becomes self-documenting and easier to maintain.

## Reflections

### What makes a good variable or function name?
A good variable or function name is 
* descriptive
* meaningful
* easy to understand. 

-It should clearly communicate the purpose of the variable or the action performed by the function. 
It reduces the need for comments since the code itself is self explanatory

### What issues can arise from poorly named variables?

Poorly named variables can make code:
* difficult to understand
* maintain
* debug. 
- Developers may misunderstand the purpose of a variable, leading to mistakes and bugs. Unclear names also increase the time required to review and modify code.

### How did refactoring improve code readability?
Refactoring improved readability by replacing vague names with descriptive ones. 
* The updated names clearly explain the purpose of the function and variables, allowing developers to understand the code quickly without analyzing every line.
* This makes the code easier to maintain and reduces confusion during future development.

---

#  Writing Small, Focused Functions

## Goal
Learn how to break down large functions into smaller, more maintainable units.

## Best Practices
* Follow the Single Responsibility Principle (SRP).
* Keep functions short and focused.
* Use descriptive function names.
* Avoid deep nesting when possible.
* Break complex logic into helper functions.
* Make functions reusable.
* Keep parameters to a reasonable number.
* Ensure each function has a clear purpose.

## Example

### Original Code
```
def process_student_scores(scores):
    total = 0
    
    for score in scores:
        total += score

    average = total / len(scores)

    print("Average Score:", average)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    else:
        grade = "F"

    print("Final Grade:", grade)

    if average < 70:
        print("Student needs improvement.")
    else:
        print("Student passed.")

```

#### Problems
The function is handling multiple responsibilities, making it harder to understand and modify.

### Refactored Code
```
def calculate_average(scores):
    return sum(scores) / len(scores)


def determine_grade(average)
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    else:
        return "F"


def evaluate_performance(average):
    if average < 70:
        return "Student needs improvement."
    return "Student passed."


def process_student_scores(scores)
    average = calculate_average(scores)
    grade = determine_grade(average)
    performance = evaluate_performance(average)

    print("Average Score:", average)
    print("Final Grade:", grade)
    print(performance)
```

## Reflections

### Why is breaking down functions beneficial?

* Breaking down functions improves readability, maintainability, and reusability.
* Small functions are easier to understand because each one focuses on a single task. 
* They are also easier to test and debug since problems can be isolated to specific parts of the code.
### How did refactoring improve the structure of the code?

* Refactoring separated the different responsibilities into dedicated functions.
* Instead of one large function handling calculations, grading, and performance evaluation, each task now has its own function. 
* This makes the code more organized, easier to modify, and simpler for other developers to understand.

# Avoiding Code Duplication

## Goal

Understand how to identify and eliminate unnecessary duplication in code.

## DRY Principle
The principle states that every piece of knowledge or logic should exist in only one place within a codebase.

Duplicated code increases maintenance effort because changes must be made in multiple locations. This can lead to inconsistencies and bugs if one copy is updated while others are forgotten.

## Example

### Origin code 
```
def calculate_student_discount(price): 
    return price * 0.10 

def calculate_teacher_discount(price):
     return price * 0.10 
     
def calculate_senior_discount(price): 
    return price * 0.10
```
#### Problems
* The same discount calculation is repeated three times.
* If the discount rate changes, all functions must be updated.
* The duplicated logic increases maintenance effort.

### Refactored version
```
def calculate_discount(price, discount_rate): 
    return price * discount_rate 
    
student_discount = calculate_discount(100, 0.10) 
teacher_discount = calculate_discount(100, 0.10) 
senior_discount = calculate_discount(100, 0.10)

```
## Reflections

### What were the issues with duplicated code?
* Duplicated code increases the amount of code that must be maintained. 
* When business requirements change, developers may need to update multiple locations, which increases the risk of introducing bugs. 
* It also makes the codebase harder to understand because the same logic appears repeatedly.

### How did refactoring improve maintainability?
* Refactoring removed the repeated logic and placed it into a single reusable function. 
* This reduced the amount of code, improved readability, and ensured that future changes only need to be made in one location. 
* The code became easier to maintain and less prone to inconsistencies.