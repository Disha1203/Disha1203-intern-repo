# Clean Code Principles

**Issue Number:** #64
**Milestone:** 4
**Date Completed:** 11/6/26



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
