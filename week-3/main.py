# Python Week 2: Demonstration Code
# File: main.py

# --- Part 1: Warm-up & Review (Discussion) ---
print("--- Part 1: Cumulative Sum ---")


def cumulative_sum(numbers: list[int | float]) -> int | float:
    total = 0
    for num in numbers:
        # total = total + num
        total += num

    return total


cumsum = cumulative_sum([i for i in range(100)])

print(f"1+2+3+...+99={cumsum}")
print("-" * 30)

# --- Part 2: Importing code ---
print("--- Part 2: Importing Code ---")
from helper import greet, Rectangle

print(f"{greet('Gabriel')}")
print()

rectangle = Rectangle(20, 40)
print(
    f"Perimeter of rectangle of length {rectangle.length} and width {rectangle.width} is {rectangle.get_perimeter()}"
)
print(
    f"Area of rectangle of length {rectangle.length} and width {rectangle.width} is {rectangle.get_area()}"
)
print("-" * 30)
