# Python Week 2: Demonstration Code
# File: main.py

# --- Part 1: Warm-up & Review (Discussion) ---
# - Briefly review variables and data types from Week 1.
# - (int, float, str, bool)


# --- Part 2: Conditionals (if/elif/else) ---
print("--- Part 2: Conditionals ---")
# Concept: Making decisions in code.

# Example: Check if a number is positive, negative, or zero.
number_to_check = -5

print(f"Checking the number: {number_to_check}")
if number_to_check > 0:
    print("This is a positive number.")
elif number_to_check < 0:
    print("This is a negative number.")
else:
    print("This number is zero.")
print("-" * 20)


# --- Part 3: Lists & for Loops ---
print("--- Part 3: Lists & for Loops ---")
# Concept: A list is an ordered collection of items.
# A 'for' loop is used to do something for each item in the list.

student_names = ["Alice", "Bob", "Charlie", "Diana"]
print(f"Our list of students: {student_names}")

# Let's greet each student
for name in student_names:
    # The variable 'name' will hold one item from the list at a time
    print(f"Hello, {name}!")
print("-" * 20)


# --- Part 4: while Loops ---
print("--- Part 4: while Loops ---")
# Concept: A 'while' loop repeats as long as a certain condition is True.

# Example: A simple counter
count = 1
while count <= 5:
    print(f"Current count is: {count}")
    count = count + 1  # Important: Update the condition variable!
print("The while loop has finished.")
print("-" * 20)


# --- Part 5: Functions (def/return) ---
print("--- Part 5: Functions ---")
# Concept: A way to package up and reuse a block of code.

# Let's take our logic from Part 2.
# Instead of just running it, let's put it in a function.

# A function is defined with 'def', given a name, and can take inputs (parameters).
# It can also 'return' an output value.
def get_number_sign(num: int) -> str:
    """
    This function takes an integer and returns its sign as a string.
    """
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Now, we can CALL the function to use it.
number_to_test = 10
sign = get_number_sign(number_to_test) # The returned value is stored in 'sign'
print(f"The function get_number_sign({number_to_test}) returned: '{sign}'")

number_to_test = -7
sign = get_number_sign(number_to_test)
print(f"The function get_number_sign({number_to_test}) returned: '{sign}'")
print("-" * 20)

print("End of lesson demonstration.")

