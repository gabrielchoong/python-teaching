# Python Week 2: Practice Exercises
# File: practice.py

# --- Exercise 1: Conditionals ---
# Objective: Practice using if/elif/else.
#
# Task:
# 1. Create a variable named 'user_age' and set it to an integer value.
# 2. Write a script that checks the age and prints one of the following messages:
#    - "You are old enough to vote." (if age is 18 or older)
#    - "You are not old enough to vote yet." (if age is younger than 18)
#
# Bonus: Can you also handle the case where the age is exactly 18?
print("--- Exercise 1 ---")
# Write your code for Exercise 1 here
user_age = 18
if user_age > 18:
    print("yes vote")
elif user_age < 18:
    print("no")
else: # user_age == 18
    print("yes")


print("-" * 20)


# --- Exercise 2: Lists & for Loops ---
# Objective: Practice creating a list and looping through it.
#
# Task:
# 1. You are given a list of numbers below.
# 2. Write a 'for' loop that goes through each number in the list.
# 3. Inside the loop, print out the number multiplied by 2.
#
# Example Output for the first item:
# 10 * 2 = 20
numbers = [10, 5, 8, 20, 3]
print("--- Exercise 2 ---")
# Write your code for Exercise 2 here
for num in numbers:
    print(f"{num} * 2 = {num*2}")


print("-" * 20)


# --- Exercise 3: Functions & return ---
# Objective: Practice refactoring code into a function.
#
# Task:
# 1. Take your code from Exercise 1 (the voting age checker).
# 2. Create a function named 'is_eligible_to_vote' that takes one parameter, 'age'.
# 3. Instead of printing a message, the function should RETURN a boolean value:
#    - It should return True if the age is 18 or older.
#    - It should return False if the age is less than 18.
# 4. After defining the function, call it with a sample age and print the result.
#
# Example of calling the function:
# can_vote = is_eligible_to_vote(25)
# print(f"Is a 25-year-old eligible to vote? {can_vote}")
print("--- Exercise 3 ---")
# Write your function definition and function call for Exercise 3 here

def is_eligible_to_vote(age):

    return age >= 18
    # 25 >= 18 => True
    # 12 >= 18 => False

    if age >= 18:
        return True
    elif age < 18:
        return False


can_vote = is_eligible_to_vote(25)
print(f"Is a 25-year-old eligible to vote? {can_vote}")

cannot_vote = is_eligible_to_vote(12)
print(f"{cannot_vote}")

print("-" * 20)


# --- Final Challenge Exercise ---
# Objective: Combine all concepts: lists, loops, conditionals, and functions.
#
# Task:
# 1. Write a function named 'filter_positive_numbers'.
# 2. The function should accept one parameter: a list of numbers.
# 3. Inside the function, create a new empty list (e.g., 'positive_numbers = []').
# 4. Loop through the input list of numbers.
# 5. For each number, use an 'if' statement to check if it's positive (> 0).
# 6. If the number is positive, add it to your new list.
# 7. After the loop finishes, the function should RETURN the new list that contains only the positive numbers.
#
# Example of calling the function:
# mixed_numbers = [-5, 10, -3, 8, 0, 1]
# positive_only = filter_positive_numbers(mixed_numbers)
# print(f"The positive numbers are: {positive_only}") # Expected output: [10, 8, 1]
print("--- Final Challenge ---")
# Write your code for the Final Challenge here
def filter_positive_numbers(number: list[int]):
    postiive_numbers = []
    for num in number:
        if num > 0:
            postiive_numbers.append(num)
    return postiive_numbers

mixed_numbers = [-5, 10, -3, 8, 0, 1]
positive_only = filter_positive_numbers(mixed_numbers)
print(f"The positive numbers are: {positive_only}")


print("-" * 20)

