from utils.logger import setup_logging
from discounts import (
    DiscountStrategy, 
    NoDiscountStrategy,
    VIPDiscountStrategy,
    SeniorDiscountStrategy,
    StudentDiscountStrategy
)

logger = setup_logging()

# Context Class - uses the strategy
class ShoppingCart:
    """
    Context class that uses discount strategies.
    This class can change its behavior by switching strategies at runtime.
    """
    
    def __init__(self, discount_strategy=None):
        self.items = []
        self.discount_strategy = discount_strategy or NoDiscountStrategy()
    
    def add_item(self, name, price):
        """Add an item to the cart"""
        self.items.append({"name": name, "price": price})
        logger.info(f"Added {name} (${price:.2f}) to cart")
    
    def set_discount_strategy(self, strategy):
        """Change the discount strategy at runtime"""
        self.discount_strategy = strategy
        logger.info(f"Discount strategy changed to: {strategy.get_description()}")
    
    def calculate_total(self):
        """Calculate total with current discount strategy"""
        subtotal = sum(item["price"] for item in self.items)
        discount = self.discount_strategy.calculate_discount(subtotal)
        total = subtotal - discount
        
        logger.info(f"Subtotal: ${subtotal:.2f}")
        logger.info(f"Discount: ${discount:.2f} ({self.discount_strategy.get_description()})")
        logger.info(f"Total: ${total:.2f}")
        logger.info("")
        
        return total

def demonstrate_strategy_pattern():
    """Demonstrate how Strategy Pattern works"""
    
    logger.info("STRATEGY PATTERN EXAMPLE - Shopping Cart Discounts")
    logger.info("=" * 60)
    
    # Create shopping cart
    cart = ShoppingCart()
    
    # Add some items
    cart.add_item("Laptop", 1000.00)
    cart.add_item("Mouse", 25.00)
    cart.add_item("Keyboard", 75.00)
    logger.info("")
    
    # Scenario 1: Regular customer (no discount)
    logger.info("SCENARIO 1: Regular Customer")
    logger.info("-" * 30)
    cart.calculate_total()
    
    # Scenario 2: Student customer
    logger.info("SCENARIO 2: Student Customer")
    logger.info("-" * 30)
    cart.set_discount_strategy(StudentDiscountStrategy())
    cart.calculate_total()
    
    # Scenario 3: VIP customer
    logger.info("SCENARIO 3: VIP Customer")
    logger.info("-" * 30)
    cart.set_discount_strategy(VIPDiscountStrategy())
    cart.calculate_total()
    
    # Scenario 4: Senior customer
    logger.info("SCENARIO 4: Senior Customer")
    logger.info("-" * 30)
    cart.set_discount_strategy(SeniorDiscountStrategy())
    cart.calculate_total()

if __name__ == "__main__":
    demonstrate_strategy_pattern()
    
    
    logger.info("WHY USE STRATEGY PATTERN?")
    logger.info("=" * 40)
    logger.info("✓ FLEXIBILITY: Easy to switch between different algorithms")
    logger.info("✓ EXTENSIBILITY: Add new discount types without changing existing code")
    logger.info("✓ RUNTIME CHANGES: Change behavior during program execution")
    logger.info("✓ CLEAN CODE: Each strategy is isolated and focused")
    logger.info("✓ TESTING: Each strategy can be tested independently")
    logger.info("")
    
    logger.info("WITHOUT STRATEGY PATTERN (Problems):")
    logger.info("-" * 40)
    logger.info("✗ Long if-else chains for different discount types")
    logger.info("✗ Violates Open-Closed Principle (modify existing code)")
    logger.info("✗ Hard to test individual discount logic")
    logger.info("✗ Coupling between discount logic and cart logic")
    logger.info("")
    
    logger.info("WITH STRATEGY PATTERN (Solutions):")
    logger.info("-" * 40)
    logger.info("✓ Each discount type is a separate class")
    logger.info("✓ Easy to add new discount types")
    logger.info("✓ Cart doesn't need to know discount details")
    logger.info("✓ Can change discount strategy at runtime")

    
    logger.info("STRATEGY PATTERN STRUCTURE:")
    logger.info("=" * 35)
    logger.info("1. Strategy Interface: DiscountStrategy (defines contract)")
    logger.info("2. Concrete Strategies: NoDiscount, Student, VIP, Senior")
    logger.info("3. Context: ShoppingCart (uses strategies)")
    logger.info("4. Client: Can switch strategies at runtime")
