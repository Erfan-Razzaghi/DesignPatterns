"""
Thread-Safe Singleton Implementation using Metaclass

This example demonstrates a thread-safe Singleton pattern using metaclass.
Suitable for multi-threaded applications.
"""

from utils.logger import setup_logging
import threading

logger = setup_logging()


class SingletonMeta(type):
    """
    Thread-safe Singleton metaclass.
    Any class using this metaclass will have only one instance.
    """
    _instances = {}
    _lock = threading.Lock()
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    logger.info(f"Creating new {cls.__name__} instance")
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class ConfigurationManager(metaclass=SingletonMeta):
    """
    Configuration Manager using thread-safe Singleton.
    Manages application settings.
    """
    
    def __init__(self):
        self.config = {
            "debug_mode": False,
            "max_connections": 100,
            "timeout": 30
        }
        logger.info("ConfigurationManager initialized")
    
    def get(self, key):
        return self.config.get(key)
    
    def set(self, key, value):
        old_value = self.config.get(key)
        self.config[key] = value
        logger.info(f"Config updated - {key}: {old_value} -> {value}")


def demonstrate_threadsafe_singleton():
    """Demonstrate thread-safe singleton behavior."""
    logger.info("=== Thread-Safe Singleton Demonstration ===")
    
    # Create two instances
    config1 = ConfigurationManager()
    config2 = ConfigurationManager()
    
    # Verify they are the same instance
    logger.info(f"config1 is config2: {config1 is config2}")
    logger.info(f"Same ID: {id(config1) == id(config2)}")
    
    # Test shared state
    config1.set("debug_mode", True)
    debug_mode = config2.get("debug_mode")
    logger.info(f"Set via config1, read via config2: {debug_mode}")


def test_thread_safety():
    """Test thread safety with multiple threads."""
    logger.info("\n=== Thread Safety Test ===")
    
    instances = []
    
    def create_instance():
        config = ConfigurationManager()
        instances.append(id(config))
    
    # Create multiple threads
    threads = []
    for i in range(5):
        thread = threading.Thread(target=create_instance)
        threads.append(thread)
        thread.start()
    
    # Wait for completion
    for thread in threads:
        thread.join()
    
    # Check results
    unique_ids = len(set(instances))
    logger.info(f"Threads: {len(instances)}, Unique IDs: {unique_ids}")
    logger.info(f"Thread-safe: {unique_ids == 1}")


if __name__ == "__main__":
    demonstrate_threadsafe_singleton()
    test_thread_safety()