from abc import ABC, abstractmethod
from utils.logger import setup_logging

logger = setup_logging()

# Simple Interface - defines what a payment processor must do
class PaymentProcessor(ABC):
    """
    Simple interface for payment processing.
    Any payment method must implement these abstract methods.
    """
    
    @abstractmethod
    def process_payment(self, amount):
        """Process a payment of the given amount"""
        pass
    
    @abstractmethod
    def get_provider_name(self):
        """Return the name of the payment provider"""
        pass

# Concrete implementation 1
class CreditCardProcessor(PaymentProcessor):
    """Processes payments via credit card"""
    
    def process_payment(self, amount):
        return f"Processing ${amount:.2f} via Credit Card"
    
    def get_provider_name(self):
        return "Credit Card Payment System"

# Concrete implementation 2
class PayPalProcessor(PaymentProcessor):
    """Processes payments via PayPal"""
    
    def process_payment(self, amount):
        return f"Processing ${amount:.2f} via PayPal"
    
    def get_provider_name(self):
        return "PayPal Payment System"

# Concrete implementation 3
class CryptoProcessor(PaymentProcessor):
    """Processes payments via cryptocurrency"""
    
    def process_payment(self, amount):
        return f"Processing ${amount:.2f} via Cryptocurrency"
    
    def get_provider_name(self):
        return "Crypto Payment System"

# Function that works with ANY payment processor (interface-based programming)
def handle_payment(processor, amount):
    """
    This function can work with any object that implements PaymentProcessor interface.
    It doesn't need to know the specific implementation details.
    """
    logger.info(f"Using: {processor.get_provider_name()}")
    result = processor.process_payment(amount)
    logger.info(f"Result: {result}")
    logger.info("")

if __name__ == "__main__":
    logger.info("SIMPLE INTERFACE EXAMPLE - Payment Processing")
    logger.info("=" * 55)
    
    # Create different payment processors
    credit_card = CreditCardProcessor()
    paypal = PayPalProcessor()
    crypto = CryptoProcessor()
    
    # Process payments using different methods
    # The same function works with all implementations!
    amount = 99.99
    
    logger.info(f"Processing payment of ${amount:.2f} using different methods:")
    logger.info("-" * 55)
    
    handle_payment(credit_card, amount)
    handle_payment(paypal, amount)
    handle_payment(crypto, amount)
    
    logger.info("INTERFACE BENEFITS:")
    logger.info("=" * 25)
    logger.info("✓ Same function (handle_payment) works with all implementations")
    logger.info("✓ Easy to add new payment methods without changing existing code")
    logger.info("✓ Code depends on interface, not specific implementations")
    logger.info("✓ Interface ensures all processors have required methods")
    
    # Demonstrate that interface cannot be instantiated
    logger.info("\nINTERFACE INSTANTIATION TEST:")
    logger.info("=" * 35)
    try:
        # This will fail - cannot instantiate abstract class
        processor = PaymentProcessor()
    except TypeError as e:
        logger.info(f"✓ Cannot create interface directly: {e}")
    
    logger.info("\nSUMMARY:")
    logger.info("• Interface = contract defining required methods")
    logger.info("• Only abstract methods (no implementation)")
    logger.info("• All implementing classes must provide these methods")
    logger.info("• Enables polymorphism and flexible design")