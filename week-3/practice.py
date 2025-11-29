# Practice 1
# Try to import the functions that we wrote in week 2 in this file.
# Remember to copy over the function into helper.py

# from helper import filter_positive_numbers

# Practice 2
# Write a function to calculate the average of a list of numbers in helper.py
# Hint: average = sum of all numbers / length of numbers

# from helper import calculate_average

# Practice 3
from dataclasses import dataclass
import math


@dataclass
class Circle:
    radius: float

    def get_radius(self):
        # self.radius
        return 0.0

    def get_area(self):
        return math.pi * (self.radius**2)

    def get_perimeter(self):
        # perimeter of circle = 2 * pi * r
        return 0.0


c1 = Circle(5)

print(
        f"The Area and Perimeter of a Circle with Radius {c1.get_radius()} is {c1.get_area():.2f} and {c1.get_perimeter():.2f}."
)
