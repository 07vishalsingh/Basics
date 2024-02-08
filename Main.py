''' variables is a container that can hold a single value or a group of values  '''
''' variables & data types '''
# Example 1: Tracking Employee Information
employee_name = "John Doe"
employee_age = 30
employee_salary = 50000.00
employee_is_manager = True

# Example 2: Storing Customer Orders
order_id = "ORD12345"
order_items = ["Laptop", "Mouse", "Keyboard"]
order_total_price = 1500.00

# Example 1: Tracking Employee Information
print("Employee Name:", employee_name)
print("Employee Age:", employee_age)
print("Employee Salary:", employee_salary)
print("Is Employee a Manager?:", employee_is_manager)

# Example 2: Storing Customer Orders
print("Order ID:", order_id)
print("Order Items:", order_items)
print("Order Total Price:", order_total_price)


''' loops '''
# Example 3: Printing Even Numbers
for num in range(1, 11):
    if num % 2 == 0:
        print(num)

# Example 4: Iterating Over a List
fruits = ["Apple", "Banana", "Orange"]
for fruit in fruits:
    print("I like", fruit)

# Example 5: Looping Through Dictionary
student_scores = {"John": 85, "Alice": 90, "Bob": 75}
for name, score in student_scores.items():
    print(name, "scored", score)

''' control flow '''
# Example 6: Checking Eligibility for a Discount
age = 25
if age >= 18:
    print("You are eligible for a discount.")
else:
    print("Sorry, you are not eligible for a discount.")

# Example 7: Determining Grade based on Score
score = 75
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print("Your grade is:", grade)
