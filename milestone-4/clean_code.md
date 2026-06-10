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