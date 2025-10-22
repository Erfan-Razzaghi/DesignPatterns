# Abstract Factory Pattern Example (Python)

This directory contains a simple implementation of the Abstract Factory design pattern in Python, using the provided logger from `utils` for proper logging.

## What is the Abstract Factory Pattern?

The Abstract Factory pattern provides an interface for creating families of related objects without specifying their concrete classes. It's like having different factories that each produce a complete set of related products.

## Pattern Overview

Think of it as having different furniture factories: one makes modern furniture (modern chair, modern table), another makes vintage furniture (vintage chair, vintage table). Each factory produces a complete family of related products.

### Key Components

1. **Abstract Factory** - Interface for creating families of products
2. **Concrete Factory** - Creates specific families (e.g., ModernFactory, VintageFactory)
3. **Abstract Product** - Interface for product types (e.g., Chair, Table)
4. **Concrete Product** - Specific products (e.g., ModernChair, VintageChair)

## When to Use Abstract Factory Pattern

### Use When:
- You need to create families of related objects that work together
- You want to switch between different product families easily
- You need consistency within a product family

### Simple Examples:
- **Furniture Store**: Modern vs Vintage furniture sets
- **Car Factory**: Electric vs Gasoline car components
- **Pizza Restaurant**: Italian vs American style pizza families

## Pros and Cons

### ✅ Advantages
- **Consistency**: Products from same family work well together
- **Easy Switching**: Change entire product family with one line
- **Isolation**: Client doesn't know about concrete classes

### ❌ Disadvantages
- **More Complex**: More classes than simple factory
- **Rigid**: Hard to add new product types
## Files

- `abstract_factory_example.py` - Simple Abstract Factory pattern implementation
- `utils/logger.py` - Logging configuration and setup
- `utils/constants.py` - Logging constants and configuration

## Running the Example

```bash
cd "05. Abstract Factory Pattern"
python abstract_factory_example.py
```

## Example: Furniture Store

The example demonstrates a furniture store that can create different styles of furniture:

- **Modern Factory**: Creates modern-style chairs and tables
- **Vintage Factory**: Creates vintage-style chairs and tables

Each factory creates a complete family of furniture that matches in style.

### Features

- Simple and easy to understand
- Proper logging using the shared logger from `utils`
- Demonstrates switching between product families
- Shows how products from the same family work together