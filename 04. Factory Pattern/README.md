# Factory Pattern Example (Python)

This directory contains a simple implementation of the Factory design pattern in Python, using the provided logger from `utils` for proper logging throughout the application.

## Files

- `factory_pattern_example.py` - Factory pattern implementation with animal examples
- `utils/logger.py` - Logging configuration and setup
- `utils/constants.py` - Logging constants and configuration

## Running the Example

```bash
cd "04. Factory Pattern"
python factory_pattern_example.py
```

## Pattern Overview

The Factory pattern provides a way to create objects without specifying the exact class of object that will be created. It encapsulates object creation logic and promotes loose coupling between the client code and the concrete classes.

### Key Components

1. **Product (Animal)** - Abstract interface for objects the factory creates
2. **Concrete Products (Dog, Cat, Bird)** - Specific implementations of the product interface
3. **Factory (AnimalFactory)** - Creates and returns product instances based on input parameters

### Examples Included

1. **Basic Factory Demo** - Shows how to create different animals using the factory
2. **Animal Shelter Scenario** - Real-world example simulating an animal shelter system

### Key Benefits

- **Encapsulation**: Object creation logic is centralized in the factory
- **Flexibility**: Easy to add new animal types without changing client code
- **Polymorphism**: All created objects share the same interface
- **Error Handling**: Factory validates input and provides meaningful error messages

### Features

- Comprehensive logging using the shared logger from `utils`
- Type hints for better code documentation
- Abstract base classes for proper interface definition
- Error handling for invalid animal types
- Registry pattern for managing available types
- Real-world scenario demonstration