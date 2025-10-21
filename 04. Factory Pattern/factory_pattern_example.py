#!/usr/bin/env python3
"""
Simple Factory Pattern Example

The Factory pattern provides a way to create objects without specifying
the exact class of object that will be created.
"""

from abc import ABC, abstractmethod
from utils.logger import setup_logging

# Initialize logger
logger = setup_logging()


class Animal(ABC):
    """Abstract animal class."""
    
    def __init__(self, name: str):
        self.name = name
        logger.info(f"Created {self.__class__.__name__}: {self.name}")
    
    @abstractmethod
    def make_sound(self) -> str:
        """Make the animal's characteristic sound."""
        pass
    
    @abstractmethod
    def get_info(self) -> str:
        """Get information about the animal."""
        pass


class Dog(Animal):
    """Dog implementation."""
    
    def make_sound(self) -> str:
        sound = "Woof!"
        logger.info(f"Dog {self.name} says: {sound}")
        return sound
    
    def get_info(self) -> str:
        info = f"Dog named {self.name} - loyal and friendly"
        logger.info(f"Dog info: {info}")
        return info


class Cat(Animal):
    """Cat implementation."""
    
    def make_sound(self) -> str:
        sound = "Meow!"
        logger.info(f"Cat {self.name} says: {sound}")
        return sound
    
    def get_info(self) -> str:
        info = f"Cat named {self.name} - independent and curious"
        logger.info(f"Cat info: {info}")
        return info


class Bird(Animal):
    """Bird implementation."""
    
    def make_sound(self) -> str:
        sound = "Tweet!"
        logger.info(f"Bird {self.name} says: {sound}")
        return sound
    
    def get_info(self) -> str:
        info = f"Bird named {self.name} - can fly and sing"
        logger.info(f"Bird info: {info}")
        return info


class AnimalFactory:
    """Factory class to create animals."""
    
    # Registry of available animal types
    _animal_types = {
        'dog': Dog,
        'cat': Cat,
        'bird': Bird
    }
    
    @classmethod
    def create_animal(cls, animal_type: str, name: str) -> Animal:
        """
        Create an animal of the specified type.
        
        Args:
            animal_type: Type of animal to create ('dog', 'cat', 'bird')
            name: Name for the animal
            
        Returns:
            Animal: Created animal instance
            
        Raises:
            ValueError: If animal_type is not supported
        """
        animal_type = animal_type.lower()
        
        if animal_type not in cls._animal_types:
            error_msg = f"Unknown animal type: {animal_type}. Available types: {list(cls._animal_types.keys())}"
            logger.error(error_msg)
            raise ValueError(error_msg)
        
        logger.info(f"Factory creating {animal_type} named {name}")
        animal_class = cls._animal_types[animal_type]
        return animal_class(name)
    
    @classmethod
    def get_available_types(cls) -> list:
        """Get list of available animal types."""
        types = list(cls._animal_types.keys())
        logger.info(f"Available animal types: {types}")
        return types


def demonstrate_factory_pattern():
    """Demonstrate the Factory pattern."""
    logger.info("=== Factory Pattern Demo ===")
    
    # Show available types
    available_types = AnimalFactory.get_available_types()
    logger.info(f"We can create these animals: {available_types}")
    
    # Create different animals using the factory
    animals = []
    
    try:
        # Create various animals
        dog = AnimalFactory.create_animal("dog", "Buddy")
        cat = AnimalFactory.create_animal("cat", "Whiskers")
        bird = AnimalFactory.create_animal("bird", "Tweety")
        
        animals = [dog, cat, bird]
        
        # Demonstrate polymorphism - all animals can make sounds and provide info
        logger.info("--- Demonstrating polymorphism ---")
        for animal in animals:
            animal.make_sound()
            animal.get_info()
        
        # Try to create an unknown animal type
        logger.info("--- Testing error handling ---")
        try:
            unknown = AnimalFactory.create_animal("dragon", "Smaug")
        except ValueError as e:
            logger.info(f"Expected error caught: {e}")
        
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise


def demonstrate_animal_shelter():
    """Demonstrate a real-world scenario - animal shelter."""
    logger.info("=== Animal Shelter Scenario ===")
    
    # Simulate animals arriving at shelter
    arrivals = [
        ("dog", "Max"),
        ("cat", "Luna"),
        ("bird", "Charlie"),
        ("dog", "Bella"),
        ("cat", "Oliver")
    ]
    
    shelter_animals = []
    
    logger.info("Animals arriving at the shelter:")
    for animal_type, name in arrivals:
        try:
            animal = AnimalFactory.create_animal(animal_type, name)
            shelter_animals.append(animal)
            logger.info(f"✅ {name} the {animal_type} has been admitted to the shelter")
        except ValueError as e:
            logger.error(f"❌ Could not admit animal: {e}")
    
    # Daily roll call
    logger.info(f"--- Daily roll call ({len(shelter_animals)} animals) ---")
    for animal in shelter_animals:
        animal.make_sound()


def main():
    """Run the factory pattern demonstrations."""
    logger.info("🚀 Starting Factory Pattern Demo")
    
    try:
        # Basic factory demo
        demonstrate_factory_pattern()
        print()  # Add spacing
        
        # Real-world scenario
        demonstrate_animal_shelter()
        
        logger.info("✅ Factory Pattern demo completed successfully!")
        
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        raise


if __name__ == "__main__":
    main()
