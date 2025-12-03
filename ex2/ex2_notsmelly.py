# ex2_smelly.py

class Shape:
    """Base class for all shapes."""

    def calculate_area(self):
        """Subclasses must implement this."""
        raise NotImplementedError("Subclasses must implement calculate_area().")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        # Keep 3.14 to preserve original behaviour / test expectations
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height
