"""
Basic Singleton Implementation using __new__ method

This example demonstrates the simplest form of Singleton pattern in Python.
WARNING: This implementation is NOT thread-safe.
"""

from utils.logger import setup_logging

logger = setup_logging()


class DatabaseConnection:
    """
    Basic Singleton using __new__ method.
    Only one instance will ever be created.
    """
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            logger.info("Creating new DatabaseConnection instance")
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.connection_string = "postgresql://localhost:5432/myapp"
            self.is_connected = False
            self._initialized = True
            logger.info("DatabaseConnection initialized")
    
    def connect(self):
        if not self.is_connected:
            logger.info("Connecting to database")
            self.is_connected = True
        else:
            logger.info("Already connected")
    
    def get_status(self):
        return f"Connected: {self.is_connected}"


def demonstrate_basic_singleton():
    """Demonstrate basic singleton behavior."""
    logger.info("=== Basic Singleton Demonstration ===")
    
    # Create two instances
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    
    # Verify they are the same instance
    logger.info(f"db1 is db2: {db1 is db2}")
    logger.info(f"Same ID: {id(db1) == id(db2)}")
    
    # Test shared state
    db1.connect()
    logger.info(f"db1 status: {db1.get_status()}")
    logger.info(f"db2 status: {db2.get_status()}")  # Same state


if __name__ == "__main__":
    demonstrate_basic_singleton()