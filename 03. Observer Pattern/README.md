# Observer Pattern Example (Python)

This directory contains a comprehensive implementation of the Observer design pattern in Python, using the provided logger from `utils` for proper logging throughout the application.

## Files

- `observer_pattern_example.py` - Complete Observer pattern implementation with multiple examples
- `utils/logger.py` - Logging configuration and setup
- `utils/constants.py` - Logging constants and configuration

## Running the Example

```bash
cd "03. Observer Pattern"
python observer_pattern_example.py
```

## Pattern Overview

The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

### Key Components

1. **Subject** - Maintains a list of observers and notifies them of state changes
2. **Observer** - Abstract interface for objects that should be notified of changes  
3. **ConcreteObserver** - Implements the Observer interface to receive notifications

### Examples Included

1. **Basic Observer Pattern** - Simple demonstration with generic observers
2. **Newsletter Subscription** - Real-world example with email subscribers
3. **Stock Price Monitoring** - Financial application with price alerts

### Features

- Comprehensive logging using the shared logger from `utils`
- Type hints for better code documentation
- Abstract base classes for proper interface definition
- Error handling and edge case management
- Multiple real-world examples demonstrating different use cases