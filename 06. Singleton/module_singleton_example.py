"""
Module-Level Singleton Implementation (Most Pythonic)

This example demonstrates the most Pythonic way to implement singleton behavior
using module-level instances. Modules are naturally singletons in Python.
"""

from utils.logger import setup_logging
import threading

logger = setup_logging()


class _Settings:
    """
    Private settings class instantiated once at module level.
    The underscore prefix indicates it's private to this module.
    """
    
    def __init__(self):
        self.config = {
            "app_name": "My Application",
            "debug": False,
            "max_connections": 10
        }
        self._lock = threading.RLock()
        logger.info("Settings initialized (Module-level Singleton)")
    
    def get(self, key):
        with self._lock:
            value = self.config.get(key)
            logger.info(f"Settings GET - {key}: {value}")
            return value
    
    def set(self, key, value):
        with self._lock:
            old_value = self.config.get(key)
            self.config[key] = value
            logger.info(f"Settings SET - {key}: {old_value} -> {value}")
    
    def get_all(self):
        with self._lock:
            return self.config.copy()


class _Cache:
    """
    Private cache class instantiated once at module level.
    Simple caching system.
    """
    
    def __init__(self):
        self.data = {}
        self.hits = 0
        self.misses = 0
        self._lock = threading.RLock()
        logger.info("Cache initialized (Module-level Singleton)")
    
    def get(self, key):
        with self._lock:
            if key in self.data:
                self.hits += 1
                logger.info(f"Cache HIT: {key}")
                return self.data[key]
            else:
                self.misses += 1
                logger.info(f"Cache MISS: {key}")
                return None
    
    def set(self, key, value):
        with self._lock:
            self.data[key] = value
            logger.info(f"Cache SET: {key}")
    
    def get_stats(self):
        with self._lock:
            total = self.hits + self.misses
            hit_rate = (self.hits / total * 100) if total > 0 else 0
            return {"hits": self.hits, "misses": self.misses, "hit_rate": f"{hit_rate:.1f}%"}


# Create the singleton instances at module level
# These are the actual singleton objects that will be imported and used
app_settings = _Settings()
app_cache = _Cache()


def demonstrate_module_singletons():
    """Demonstrate module-level singleton behavior."""
    logger.info("=== Module-Level Singleton Demonstration ===")
    
    # Test Settings
    settings1 = app_settings
    settings2 = app_settings
    
    logger.info(f"settings1 is settings2: {settings1 is settings2}")
    logger.info(f"Same ID: {id(settings1) == id(settings2)}")
    
    # Test shared state
    settings1.set("debug", True)
    debug_mode = settings2.get("debug")
    logger.info(f"Set via settings1, read via settings2: {debug_mode}")
    
    # Test Cache
    cache1 = app_cache
    cache2 = app_cache
    
    logger.info(f"cache1 is cache2: {cache1 is cache2}")
    
    # Test cache operations
    cache1.set("user:123", {"name": "Alice"})
    data = cache2.get("user:123")  # Should hit
    missing = cache1.get("user:456")  # Should miss
    
    stats = cache2.get_stats()
    logger.info(f"Cache stats: {stats}")


def test_cross_module_behavior():
    """Test that imports maintain singleton behavior."""
    logger.info("\n=== Cross-Module Import Test ===")
    
    def simulate_module_import():
        # Simulate importing from another module
        from module_singleton_example import app_settings, app_cache
        
        app_settings.set("test_key", "test_value")
        app_cache.set("test_cache", "cached_data")
        
        return id(app_settings), id(app_cache)
    
    # Test cross-module behavior
    ids = simulate_module_import()
    
    # Check values set from "other module"
    test_value = app_settings.get("test_key")
    cached_data = app_cache.get("test_cache")
    
    logger.info(f"Same settings instance: {ids[0] == id(app_settings)}")
    logger.info(f"Same cache instance: {ids[1] == id(app_cache)}")
    logger.info(f"Cross-module data: {test_value}, {cached_data}")


def test_thread_safety():
    """Test thread safety of module-level singletons."""
    logger.info("\n=== Thread Safety Test ===")
    
    results = []
    
    def worker_thread():
        thread_name = threading.current_thread().name
        
        # Import and use singletons
        from module_singleton_example import app_settings, app_cache
        
        app_settings.set(f"thread_{thread_name}", thread_name)
        app_cache.set(f"cache_{thread_name}", f"data_{thread_name}")
        
        results.append({
            "thread": thread_name,
            "settings_id": id(app_settings),
            "cache_id": id(app_cache)
        })
    
    # Create and start threads
    threads = []
    for i in range(3):
        thread = threading.Thread(target=worker_thread, name=f"Worker-{i}")
        threads.append(thread)
        thread.start()
    
    # Wait for completion
    for thread in threads:
        thread.join()
    
    # Check results
    settings_ids = set(result["settings_id"] for result in results)
    cache_ids = set(result["cache_id"] for result in results)
    
    logger.info(f"Unique settings IDs: {len(settings_ids)} (should be 1)")
    logger.info(f"Unique cache IDs: {len(cache_ids)} (should be 1)")
    logger.info(f"Thread-safe: {len(settings_ids) == 1 and len(cache_ids) == 1}")


if __name__ == "__main__":
    demonstrate_module_singletons()
    test_cross_module_behavior()
    test_thread_safety()