from dataclasses import dataclass


def greet(name: str):
    return f"Howdy, {name}!"


@dataclass
class Rectangle:
    length: float
    width: float

    def get_perimeter(self):
        return (self.length + self.width) * 2

    def get_area(self):
        return self.length * self.width
