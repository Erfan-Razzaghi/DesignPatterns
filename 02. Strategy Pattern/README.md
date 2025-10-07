# Strategy Pattern

## Overview

The **Strategy Pattern** is a behavioral design pattern that defines a family of algorithms, encapsulates each one, and makes them interchangeable. This pattern lets the algorithm vary independently from clients that use it.

## What This Pattern Solves

### The Problem
Without the Strategy Pattern, you often end up with:
- Long if-else chains or switch statements for different behaviors
- Violation of the **Open-Closed Principle** (classes should be open for extension but closed for modification)
- Tight coupling between the context and specific algorithms
- Difficulty in testing individual algorithms
- Hard to add new behaviors without modifying existing code

### The Solution
The Strategy Pattern solves these problems by:
- **Encapsulating algorithms** in separate strategy classes
- **Defining a common interface** for all strategies
- **Allowing runtime algorithm selection** without changing the context
- **Following the Open-Closed Principle** - easy to add new strategies without modifying existing code

## Key Components

### 1. Strategy Interface (`DiscountStrategy`)
Defines the contract that all concrete strategies must follow. Contains only abstract methods that represent the algorithm's interface.

### 2. Concrete Strategies
- `NoDiscountStrategy` - No discount for regular customers
- `StudentDiscountStrategy` - 10% discount for students
- `VIPDiscountStrategy` - 20% discount for VIP customers  
- `SeniorDiscountStrategy` - 15% discount for senior customers

### 3. Context Class (`ShoppingCart`)
Uses the strategy objects and can switch between different strategies at runtime. It maintains a reference to a strategy object and delegates the algorithm execution to it.

### 4. Client
The code that creates strategy objects and passes them to the context.

## Open-Closed Principle

The Strategy Pattern is an excellent example of the **Open-Closed Principle** (OCP), one of the SOLID principles:

### Open for Extension
- **Easy to add new discount strategies** by creating new classes that implement `DiscountStrategy`
- **No modification of existing code** required when adding new behaviors
- **New strategies integrate seamlessly** with the existing system

### Closed for Modification  
- **Existing strategy classes remain unchanged** when new strategies are added
- **The context class (`ShoppingCart`) doesn't need modification** for new discount types
- **Client code using existing strategies continues to work** without changes

### Example of OCP in Action
```python
# Adding a new strategy doesn't require changing existing code
class HolidayDiscountStrategy(DiscountStrategy):
    def calculate_discount(self, price):
        return price * 0.25  # 25% holiday discount
    
    def get_description(self):
        return "Holiday special: 25% off"

# The cart can immediately use this new strategy
cart.set_discount_strategy(HolidayDiscountStrategy())
```

## Benefits Demonstrated

### ✅ **Advantages of Strategy Pattern**
- **Runtime algorithm switching**: Change behavior during execution
- **Elimination of conditionals**: No more long if-else chains
- **Easy testing**: Each strategy can be tested independently
- **Code reusability**: Strategies can be reused across different contexts
- **Loose coupling**: Context doesn't depend on concrete strategy implementations

### ❌ **Problems Without Strategy Pattern**
- **Violates Open-Closed Principle**: Must modify existing code for new behaviors
- **Complex conditionals**: Long if-else or switch statements
- **Tight coupling**: Context knows about all possible algorithms
- **Testing difficulties**: Hard to test individual algorithms in isolation
- **Code duplication**: Similar logic scattered across the codebase

## When to Use Strategy Pattern

Use the Strategy Pattern when:
- You have multiple ways to perform a task
- You want to switch algorithms at runtime
- You want to isolate algorithm implementation details
- You have classes that differ only in their behavior
- You want to avoid long conditional statements

## Key Takeaways

- **Strategy Pattern promotes flexibility** by allowing algorithm changes at runtime
- **It follows the Open-Closed Principle** making the code extensible without modification
- **Each strategy is independent** and can be developed, tested, and maintained separately
- **The context remains unaware** of which specific strategy is being used
- **New strategies can be added easily** without affecting existing code
