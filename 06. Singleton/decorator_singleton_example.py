"""
Decorator-Based Singleton Implementation

This example demonstrates how to implement the Singleton pattern using a decorator.
Clean, reusable, and can be applied to any class with @singleton.
"""

from utils.logger import setup_logging
import threading

logger = setup_logging()


def singleton(cls):
    """
    Decorator that converts any class into a thread-safe singleton.
    Usage: @singleton
    """
    instances = {}
    lock = threading.Lock()
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            with lock:
                if cls not in instances:
                    logger.info(f"Creating new {cls.__name__} instance")
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance


@singleton
class LoggerManager:
    """
    Logger Manager using decorator-based Singleton.
    Manages logging configuration for the application.
    """
    
    def __init__(self):
        self.log_level = "INFO"
        self.handlers = ["console"]
        logger.info("LoggerManager initialized")
    
    def set_level(self, level):
        old_level = self.log_level
        self.log_level = level.upper()
        logger.info(f"Log level: {old_level} -> {self.log_level}")
    
    def add_handler(self, handler):
        if handler not in self.handlers:
            self.handlers.append(handler)
            logger.info(f"Added handler: {handler}")
    
    def get_config(self):
        return {"level": self.log_level, "handlers": self.handlers}


@singleton
class CacheManager:
    """
    Cache Manager using decorator-based Singleton.
    Simple caching system.
    """
    
    def __init__(self):
        self.cache = {}
        self.hits = 0
        self.misses = 0
        logger.info("CacheManager initialized")
    
    def get(self, key):
        if key in self.cache:
            self.hits += 1
            logger.info(f"Cache HIT: {key}")
            return self.cache[key]
        else:
            self.misses += 1
            logger.info(f"Cache MISS: {key}")
            return None
    
    def set(self, key, value):
        self.cache[key] = value
        logger.info(f"Cache SET: {key}")
    
    def get_stats(self):
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0
        return {"hits": self.hits, "misses": self.misses, "hit_rate": f"{hit_rate:.1f}%"}


def demonstrate_decorator_singleton():
    """Demonstrate decorator-based singleton behavior."""
    logger.info("=== Decorator-Based Singleton Demonstration ===")
    
    # Test LoggerManager
    log1 = LoggerManager()
    log2 = LoggerManager()
    
    logger.info(f"log1 is log2: {log1 is log2}")
    logger.info(f"Same ID: {id(log1) == id(log2)}")
    
    # Test shared state
    log1.set_level("DEBUG")
    log2.add_handler("file")
    config = log1.get_config()
    logger.info(f"Config: {config}")
    
    # Test CacheManager
    cache1 = CacheManager()
    cache2 = CacheManager()
    
    logger.info(f"cache1 is cache2: {cache1 is cache2}")
    
    # Test cache operations
    cache1.set("user:123", {"name": "Alice"})
    data = cache2.get("user:123")  # Should hit
    missing = cache1.get("user:456")  # Should miss
    
    stats = cache2.get_stats()
    logger.info(f"Cache stats: {stats}")


def test_decorator_thread_safety():
    """Test thread safety of decorator singletons."""
    logger.info("\n=== Decorator Thread Safety Test ===")
    
    instances = []
    
    def create_logger():
        log_mgr = LoggerManager()
        instances.append(id(log_mgr))
    
    # Create multiple threads
    threads = []
    for i in range(5):
        thread = threading.Thread(target=create_logger)
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
    demonstrate_decorator_singleton()
    test_decorator_thread_safety()