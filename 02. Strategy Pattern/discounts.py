from abc import ABC, abstractmethod

# Strategy Interface - defines the contract for all strategies
class DiscountStrategy(ABC):
    """
    Strategy interface for different discount calculation methods.
    This is the contract that all discount strategies must follow.
    """
    
    @abstractmethod
    def calculate_discount(self, price):
        """Calculate discount amount for given price"""
        pass
    
    @abstractmethod
    def get_description(self):
        """Get description of the discount strategy"""
        pass

# Concrete Strategy 1: No Discount
class NoDiscountStrategy(DiscountStrategy):
    """Strategy for regular customers with no discount"""
    
    def calculate_discount(self, price):
        return 0
    
    def get_description(self):
        return "No discount applied"

# Concrete Strategy 2: Student Discount
class StudentDiscountStrategy(DiscountStrategy):
    """Strategy for student customers with 10% discount"""
    
    def calculate_discount(self, price):
        return price * 0.10  # 10% discount
    
    def get_description(self):
        return "Student discount: 10% off"

# Concrete Strategy 3: VIP Discount
class VIPDiscountStrategy(DiscountStrategy):
    """Strategy for VIP customers with 20% discount"""
    
    def calculate_discount(self, price):
        return price * 0.20  # 20% discount
    
    def get_description(self):
        return "VIP discount: 20% off"

# Concrete Strategy 4: Senior Discount
class SeniorDiscountStrategy(DiscountStrategy):
    """Strategy for senior customers with 15% discount"""
    
    def calculate_discount(self, price):
        return price * 0.15  # 15% discount
    
    def get_description(self):
        return "Senior discount: 15% off"