"""
A tiny demonstration of Object-Oriented Programming in Python.
This example defines a simple class that prints 'Hello, World!'.
"""

class Greeter:
    """A simple Greeter class that encapsulates greeting behavior."""

    def __init__(self, name="World"):
        """
        Constructor that initializes the object with a target name.
        Default is 'World'.
        """
        self.name = name

    def greet(self):
        """Return a greeting message."""
        return f"Hello, {self.name}!"


# Run a simple greeting if this file is executed directly
if __name__ == "__main__":
    greeter = Greeter()
    print(greeter.greet())
