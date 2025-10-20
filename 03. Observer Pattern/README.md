# Observer Pattern Example (Python)

This directory contains a comprehensive implementation of the Observer design pattern in Python, using the provided logger from `utils` for proper logging throughout the application.

## Files

- `observer_pattern_example.py` - Basic Observer pattern implementation
- `multithreaded_observer_example.py` - Advanced multithreaded Observer pattern example
- `utils/logger.py` - Logging configuration and setup
- `utils/constants.py` - Logging constants and configuration

## Overview

The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

### Key Components

1. **Subject** - Maintains a list of observers and notifies them of state changes
2. **Observer** - Abstract interface for objects that should be notified of changes  
3. **ConcreteObserver** - Implements the Observer interface to receive notifications

### Examples Included

**Basic Observer Pattern (`observer_pattern_example.py`):**
- Simple demonstration with generic observers
- Email subscription example

**Multithreaded Observer Pattern (`multithreaded_observer_example.py`):**
- Thread-safe subject implementation
- Concurrent notifications from multiple threads
- Dynamic observer management during runtime
- Various observer types (workers, email subscribers, database loggers)

### Features

- Comprehensive logging using the shared logger from `utils`
- Type hints for better code documentation
- Abstract base classes for proper interface definition
- Error handling and edge case management
- Multiple real-world examples demonstrating different use cases