"""
Comprehensive Singleton Pattern Demonstration

This file demonstrates all four different approaches to implementing the Singleton pattern
in Python by importing and showcasing each implementation from separate files.
"""

from utils.logger import setup_logging
import threading

# Import all singleton implementations
from basic_singleton_example import DatabaseConnection
from threadsafe_singleton_example import ConfigurationManager
from decorator_singleton_example import LoggerManager, CacheManager
from module_singleton_example import app_settings, app_cache

logger = setup_logging()


def demonstrate_all_singleton_patterns():
    """Demonstrate all four singleton patterns."""
    logger.info("=== Comprehensive Singleton Pattern Demonstration ===")
    
    # Method 1: Basic Singleton
    logger.info("\n--- Method 1: Basic Singleton (__new__ method) ---")
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    
    logger.info(f"Same instance: {db1 is db2}")
    db1.connect()
    logger.info(f"Shared state: {db2.get_status()}")
    
    # Method 2: Thread-Safe Singleton
    logger.info("\n--- Method 2: Thread-Safe Singleton (Metaclass) ---")
    config1 = ConfigurationManager()
    config2 = ConfigurationManager()
    
    logger.info(f"Same instance: {config1 is config2}")
    config1.set("debug_mode", True)
    logger.info(f"Shared state: {config2.get('debug_mode')}")
    
    # Method 3: Decorator Singleton
    logger.info("\n--- Method 3: Decorator Singleton ---")
    log1 = LoggerManager()
    log2 = LoggerManager()
    
    logger.info(f"Same instance: {log1 is log2}")
    log1.set_level("DEBUG")
    logger.info(f"Shared config: {log2.get_config()}")
    
    cache1 = CacheManager()
    cache2 = CacheManager()
    cache1.set("test", "data")
    logger.info(f"Cache shared: {cache2.get('test')}")
    
    # Method 4: Module-level Singleton
    logger.info("\n--- Method 4: Module-level Singleton (Most Pythonic) ---")
    settings1 = app_settings
    settings2 = app_settings
    
    logger.info(f"Same instance: {settings1 is settings2}")
    settings1.set("test_mode", True)
    logger.info(f"Shared state: {settings2.get('test_mode')}")
    
    cache1 = app_cache
    cache2 = app_cache
    cache1.set("module_test", "module_data")
    logger.info(f"Module cache shared: {cache2.get('module_test')}")


def compare_implementations():
    """Compare all singleton implementations."""
    logger.info("\n=== Implementation Comparison ===")
    
    implementations = {
        "Basic": DatabaseConnection(),
        "Thread-Safe": ConfigurationManager(),
        "Decorator": LoggerManager(),
        "Module-level": app_settings
    }
    
    for name, instance in implementations.items():
        logger.info(f"{name} Singleton ID: {id(instance)}")
    
    # Verify singleton behavior
    logger.info("\nSingleton Verification:")
    logger.info(f"Basic: {DatabaseConnection() is DatabaseConnection()}")
    logger.info(f"Thread-Safe: {ConfigurationManager() is ConfigurationManager()}")
    logger.info(f"Decorator: {LoggerManager() is LoggerManager()}")
    logger.info(f"Module-level: Always same by import")


def test_thread_safety():
    """Test thread safety across implementations."""
    logger.info("\n=== Thread Safety Test ===")
    
    results = {"basic": [], "threadsafe": [], "decorator": [], "module": []}
    
    def worker():
        results["basic"].append(id(DatabaseConnection()))
        results["threadsafe"].append(id(ConfigurationManager()))
        results["decorator"].append(id(LoggerManager()))
        results["module"].append(id(app_settings))
    
    # Create threads
    threads = [threading.Thread(target=worker) for _ in range(3)]
    
    # Start and wait
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    # Check results
    for name, ids in results.items():
        unique = len(set(ids))
        logger.info(f"{name}: {unique} unique ID(s) (should be 1)")


if __name__ == "__main__":
    demonstrate_all_singleton_patterns()
    compare_implementations()
    test_thread_safety()
    
    logger.info("\n=== All Singleton Patterns Demonstrated! ===")
    logger.info("Choose the right implementation for your use case.")