#!/usr/bin/env python3
"""
Simple Abstract Factory Pattern Example

This example demonstrates a pizza restaurant that can make different styles of pizzas.
Each factory creates a family of pizza components that work together.
"""

from abc import ABC, abstractmethod
from utils.logger import setup_logging

# Initialize logger
logger = setup_logging()


# Abstract Products
class Dough(ABC):
    """Abstract dough product."""
    
    @abstractmethod
    def get_type(self) -> str:
        """Get the dough type."""
        pass


class Sauce(ABC):
    """Abstract sauce product."""
    
    @abstractmethod
    def get_type(self) -> str:
        """Get the sauce type."""
        pass


class Cheese(ABC):
    """Abstract cheese product."""
    
    @abstractmethod
    def get_type(self) -> str:
        """Get the cheese type."""
        pass


# Italian Style Products
class ItalianDough(Dough):
    """Italian style thin dough."""
    
    def __init__(self):
        logger.info("Created Italian thin dough")
    
    def get_type(self) -> str:
        return "Thin Italian dough"


class ItalianSauce(Sauce):
    """Italian style tomato sauce."""
    
    def __init__(self):
        logger.info("Created Italian tomato sauce")
    
    def get_type(self) -> str:
        return "Traditional Italian tomato sauce"


class ItalianCheese(Cheese):
    """Italian style mozzarella cheese."""
    
    def __init__(self):
        logger.info("Created Italian mozzarella cheese")
    
    def get_type(self) -> str:
        return "Fresh Italian mozzarella"


# American Style Products
class AmericanDough(Dough):
    """American style thick dough."""
    
    def __init__(self):
        logger.info("Created American thick dough")
    
    def get_type(self) -> str:
        return "Thick American dough"


class AmericanSauce(Sauce):
    """American style sauce."""
    
    def __init__(self):
        logger.info("Created American sauce")
    
    def get_type(self) -> str:
        return "Sweet American pizza sauce"


class AmericanCheese(Cheese):
    """American style cheese blend."""
    
    def __init__(self):
        logger.info("Created American cheese blend")
    
    def get_type(self) -> str:
        return "American cheese blend"


# Abstract Factory
class PizzaIngredientFactory(ABC):
    """Abstract factory for creating pizza ingredients."""
    
    @abstractmethod
    def create_dough(self) -> Dough:
        """Create dough."""
        pass
    
    @abstractmethod
    def create_sauce(self) -> Sauce:
        """Create sauce."""
        pass
    
    @abstractmethod
    def create_cheese(self) -> Cheese:
        """Create cheese."""
        pass


# Concrete Factories
class ItalianPizzaFactory(PizzaIngredientFactory):
    """Factory for Italian pizza ingredients."""
    
    def __init__(self):
        logger.info("Initialized Italian Pizza Factory")
    
    def create_dough(self) -> Dough:
        logger.info("Italian factory creating dough")
        return ItalianDough()
    
    def create_sauce(self) -> Sauce:
        logger.info("Italian factory creating sauce")
        return ItalianSauce()
    
    def create_cheese(self) -> Cheese:
        logger.info("Italian factory creating cheese")
        return ItalianCheese()


class AmericanPizzaFactory(PizzaIngredientFactory):
    """Factory for American pizza ingredients."""
    
    def __init__(self):
        logger.info("Initialized American Pizza Factory")
    
    def create_dough(self) -> Dough:
        logger.info("American factory creating dough")
        return AmericanDough()
    
    def create_sauce(self) -> Sauce:
        logger.info("American factory creating sauce")
        return AmericanSauce()
    
    def create_cheese(self) -> Cheese:
        logger.info("American factory creating cheese")
        return AmericanCheese()


# Client
class Pizza:
    """Pizza that uses ingredients from a factory."""
    
    def __init__(self, name: str, factory: PizzaIngredientFactory):
        self.name = name
        self.factory = factory
        self.dough = None
        self.sauce = None
        self.cheese = None
        logger.info(f"Pizza '{name}' initialized with {factory.__class__.__name__}")
    
    def prepare(self):
        """Prepare the pizza using factory ingredients."""
        logger.info(f"Preparing {self.name} pizza...")
        
        # Create ingredients using the factory
        self.dough = self.factory.create_dough()
        self.sauce = self.factory.create_sauce()
        self.cheese = self.factory.create_cheese()
        
        # Display the ingredients
        logger.info(f"Pizza ingredients:")
        logger.info(f"  - {self.dough.get_type()}")
        logger.info(f"  - {self.sauce.get_type()}")
        logger.info(f"  - {self.cheese.get_type()}")
        
        logger.info(f"{self.name} pizza preparation completed!")


class PizzaRestaurant:
    """Restaurant that can make different styles of pizza."""
    
    def __init__(self, factory: PizzaIngredientFactory):
        self.factory = factory
        logger.info(f"Pizza Restaurant opened with {factory.__class__.__name__}")
    
    def make_pizza(self, pizza_name: str) -> Pizza:
        """Make a pizza using the restaurant's ingredient factory."""
        logger.info(f"Restaurant making {pizza_name} pizza")
        pizza = Pizza(pizza_name, self.factory)
        pizza.prepare()
        return pizza


def demonstrate_abstract_factory():
    """Demonstrate the Abstract Factory pattern."""
    logger.info("=== Abstract Factory Pattern Demo ===")
    
    # Italian restaurant
    logger.info("\n--- Italian Pizza Restaurant ---")
    italian_factory = ItalianPizzaFactory()
    italian_restaurant = PizzaRestaurant(italian_factory)
    italian_pizza = italian_restaurant.make_pizza("Margherita")
    
    print()  # Add spacing
    
    # American restaurant
    logger.info("\n--- American Pizza Restaurant ---")
    american_factory = AmericanPizzaFactory()
    american_restaurant = PizzaRestaurant(american_factory)
    american_pizza = american_restaurant.make_pizza("Pepperoni")
    
    print()  # Add spacing
    
    # Restaurant changing style
    logger.info("\n--- Restaurant Changing Style ---")
    logger.info("Italian restaurant switching to American style...")
    italian_restaurant.factory = american_factory
    fusion_pizza = italian_restaurant.make_pizza("Fusion")


def main():
    """Run the Abstract Factory pattern demonstration."""
    logger.info("🚀 Starting Abstract Factory Pattern Demo")
    
    try:
        demonstrate_abstract_factory()
        logger.info("✅ Demo completed successfully!")
        
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        raise


if __name__ == "__main__":
    main()
