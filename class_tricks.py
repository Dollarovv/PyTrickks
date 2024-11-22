class Person:
    """A simple Person class."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        """Return a formatted string with person's info."""
        return f"{self.name} is {self.age} years old."
