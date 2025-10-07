import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.logger import setup_logging

logger = setup_logging()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"

# Function to modify object attributes
def modify_person(person):
    logger.info(f"Inside function - Before: {person}")
    person.name = "Modified Name"
    person.age = 999
    logger.info(f"Inside function - After: {person}")

if __name__ == "__main__":
    
    # Test 1: Modifying object attributes
    logger.info("\n1. MODIFYING OBJECT ATTRIBUTES:")
    logger.info("-" * 40)
    person1 = Person("Alice", 25)
    logger.info(f"Original: {person1}")
    modify_person(person1)
    logger.info(f"After function call: {person1}")
    logger.info("(Objects are passed by reference)")
    