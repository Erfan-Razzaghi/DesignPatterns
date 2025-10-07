from abc import ABC, abstractmethod
from utils.logger import setup_logging

logger = setup_logging()

# Parent class (Abstract Base class)
class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def make_sound(self):
        """Abstract method that must be implemented by subclasses"""
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__}(name='{self.name}')"

# Child class 1
class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

# Child class 2
class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow!"

# Function that demonstrates polymorphism
def demonstrate_polymorphism(animals):
    """
    This function demonstrates polymorphism by calling the same method
    on different objects, each responding according to their specific implementation.
    """
    logger.info("Demonstrating Polymorphism:")
    logger.info("-" * 50)
    
    for animal in animals:
        # Same method call, but different behavior based on the actual object type
        sound = animal.make_sound()
        logger.info(f"{animal} says: '{sound}'")

if __name__ == "__main__":
    logger.info("POLYMORPHISM EXAMPLE WITH ABSTRACT BASE CLASS")
    logger.info("=" * 50)
    
    # Create instances of concrete classes only
    # Note: Cannot create Animal("Generic") directly - it's abstract!
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    
    # Store them in a list as the parent type (Animal)
    animals = [dog, cat]
    
    # Call the polymorphic function
    demonstrate_polymorphism(animals)
    
    logger.info("Key Point: Same method call (make_sound()) produces different behavior")
    logger.info("based on the actual object type - this is polymorphism!")
    logger.info("Note: Animal is now abstract - cannot be instantiated directly!")
    
    # !!!! test_bad_animal = Animal("Bad Boy") # This causes Error Now! !!!! 