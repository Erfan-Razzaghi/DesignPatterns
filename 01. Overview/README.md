# Overview - Fundamental OOP Concepts

## Overview

This directory demonstrates three fundamental concepts in object-oriented programming:

1. **Objects are Passed by Reference**
2. **Polymorphism**
3. **Interfaces in Python**

## 1. Objects are Passed by Reference

### What This Means

When you pass an object to a function, you're not passing a copy of the object. Instead, you're passing a reference to the same object in memory. This means that any modifications made to the object inside the function will affect the original object.

### Example Demonstration

The `example_objects_passed_by_ref.py` file shows this concept by:

1. Creating a `Person` object with initial values
2. Passing it to a function that modifies its attributes
3. Showing that the original object is changed after the function call

### Key Takeaway

Objects are **mutable** and when passed to functions, changes made inside the function persist outside the function because both variables point to the same object in memory.

## 2. Polymorphism

### What This Means

Polymorphism allows objects of different classes to be treated as objects of a common base class. The same method call can produce different behavior depending on the actual object type.

### Example Demonstration

The `example_polymorphism.py` file demonstrates:

1. An abstract base class `Animal` with an abstract method `make_sound()`
2. Concrete implementations (`Dog`, `Cat`) that provide specific behaviors
3. How the same method call produces different results based on the object type

### Key Takeaway

Polymorphism enables writing flexible code that works with objects of different types through a common interface.

## 3. Interfaces in Python

### What This Means

An **interface** is a class that contains only abstract methods and defines a contract that implementing classes must follow. In Python, interfaces are implemented using Abstract Base Classes (ABC).

### Example Demonstrations

The `example_interfaces.py` and `example_interface_enforcement.py` files show:

1. How to define pure interfaces with only abstract methods
2. How classes implement interfaces by providing concrete implementations
3. How Python enforces that all abstract methods must be implemented
4. How interface-based programming enables polymorphism
5. Multiple interface implementation

### Key Takeaways

- **Interfaces define contracts** - they specify what methods a class must implement
- **Interfaces contain ONLY abstract methods** - no concrete implementation
- **Classes cannot be instantiated** if they don't implement all abstract methods
- **Interface-based programming** promotes loose coupling and flexibility