#!/usr/bin/env python3
"""
Multithreaded Observer Pattern Example

This demonstrates the Observer pattern working with multiple threads,
including thread-safe operations and concurrent notifications.
"""

import threading
import time
import random
from abc import ABC, abstractmethod
from utils.logger import setup_logging

# Initialize logger
logger = setup_logging()


class Observer(ABC):
    """Observer interface."""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def update(self, subject, message: str):
        """Receive update from subject."""
        pass


class ThreadSafeSubject:
    """Thread-safe subject that can handle concurrent operations."""
    
    def __init__(self, name: str = "ThreadSafeSubject"):
        self._observers = []
        self._lock = threading.Lock()  # Protect observer list
        self.name = name
        logger.info(f"Created thread-safe subject: {self.name}")
    
    def attach(self, observer):
        """Thread-safe attach operation."""
        with self._lock:
            self._observers.append(observer)
            logger.info(f"Thread-safe attached observer: {observer.name}")
    
    def detach(self, observer):
        """Thread-safe detach operation."""
        with self._lock:
            if observer in self._observers:
                self._observers.remove(observer)
                logger.info(f"Thread-safe detached observer: {observer.name}")
    
    def notify(self, message: str):
        """Thread-safe notify operation."""
        with self._lock:
            observers_copy = self._observers.copy()  # Copy to avoid concurrent modification
        
        thread_name = threading.current_thread().name
        logger.info(f"Notifying {len(observers_copy)} observer(s) from thread {thread_name}")
        
        # Notify observers outside the lock to avoid blocking other operations
        for observer in observers_copy:
            observer.update(self, message)


class WorkerObserver(Observer):
    """Observer that simulates work processing."""
    
    def __init__(self, name: str, processing_time: float = 1.0):
        super().__init__(name)
        self.processing_time = processing_time
    
    def update(self, subject, message: str):
        thread_name = threading.current_thread().name
        logger.info(f"🔧 Worker '{self.name}' (thread: {thread_name}) started processing: '{message}'")
        
        # Simulate some work
        time.sleep(self.processing_time)
        
        logger.info(f"✅ Worker '{self.name}' (thread: {thread_name}) finished processing: '{message}'")


class AsyncEmailSubscriber(Observer):
    """Email subscriber that processes notifications asynchronously."""
    
    def __init__(self, name: str, email: str):
        super().__init__(name)
        self.email = email
    
    def update(self, subject, message: str):
        thread_name = threading.current_thread().name
        # Simulate email sending delay
        delay = random.uniform(0.5, 2.0)
        time.sleep(delay)
        logger.info(f"📬 Email sent to {self.name} ({self.email}) from thread {thread_name}: '{message}'")


class DatabaseLogger(Observer):
    """Observer that logs to a simulated database."""
    
    def __init__(self, name: str):
        super().__init__(name)
        self._lock = threading.Lock()  # Protect database writes
    
    def update(self, subject, message: str):
        thread_name = threading.current_thread().name
        
        # Simulate database write with thread safety
        with self._lock:
            logger.info(f"💾 Database '{self.name}' (thread: {thread_name}) logging: '{message}'")
            time.sleep(0.3)  # Simulate database write time
            logger.info(f"✅ Database '{self.name}' write completed")


def demonstrate_concurrent_notifications():
    """Demonstrate concurrent notifications from multiple threads."""
    logger.info("=== Concurrent Notifications Demo ===")
    
    # Create a thread-safe subject
    event_dispatcher = ThreadSafeSubject("Event Dispatcher")
    
    # Create observers
    worker1 = WorkerObserver("FastWorker", 0.5)
    worker2 = WorkerObserver("SlowWorker", 2.0)
    email1 = AsyncEmailSubscriber("Manager", "manager@company.com")
    email2 = AsyncEmailSubscriber("Admin", "admin@company.com")
    db_logger = DatabaseLogger("MainDB")
    
    # Attach observers
    event_dispatcher.attach(worker1)
    event_dispatcher.attach(worker2)
    event_dispatcher.attach(email1)
    event_dispatcher.attach(email2)
    event_dispatcher.attach(db_logger)
    
    # Function to send notifications from different threads
    def send_notifications(thread_id: int, num_messages: int):
        for i in range(num_messages):
            message = f"Event-{thread_id}-{i+1}: Processing request from thread {thread_id}"
            event_dispatcher.notify(message)
            time.sleep(random.uniform(0.3, 0.8))  # Random delay between notifications
    
    # Create multiple threads that will send notifications concurrently
    threads = []
    for thread_id in range(1, 4):  # Create 3 notification threads
        thread = threading.Thread(
            target=send_notifications, 
            args=(thread_id, 2),  # Each thread sends 2 messages
            name=f"NotificationThread-{thread_id}"
        )
        threads.append(thread)
    
    logger.info("Starting concurrent notification threads...")
    
    # Start all threads
    start_time = time.time()
    for thread in threads:
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    logger.info(f"All notification threads completed in {end_time - start_time:.2f} seconds!")


def demonstrate_dynamic_observer_management():
    """Demonstrate adding and removing observers while notifications are happening."""
    logger.info("=== Dynamic Observer Management Demo ===")
    
    system_monitor = ThreadSafeSubject("System Monitor")
    
    # Initial observers
    email_admin = AsyncEmailSubscriber("SysAdmin", "sysadmin@company.com")
    db_logger = DatabaseLogger("AuditDB")
    
    system_monitor.attach(email_admin)
    system_monitor.attach(db_logger)
    
    # Function to continuously send system updates
    def system_updates():
        for i in range(6):
            message = f"System Update {i+1}: CPU usage at {random.randint(20, 90)}%"
            system_monitor.notify(message)
            time.sleep(1)
    
    # Function to dynamically manage observers
    def manage_observers():
        time.sleep(2)  # Let some notifications happen first
        
        # Add new observer
        alert_worker = WorkerObserver("AlertService", 0.3)
        system_monitor.attach(alert_worker)
        logger.info("🔄 Added AlertService observer during runtime")
        
        time.sleep(2)  # Let some more notifications happen
        
        # Remove an observer
        system_monitor.detach(email_admin)
        logger.info("🔄 Removed SysAdmin observer during runtime")
    
    # Start both threads
    update_thread = threading.Thread(target=system_updates, name="SystemUpdates")
    management_thread = threading.Thread(target=manage_observers, name="ObserverManager")
    
    logger.info("Starting system monitoring with dynamic observer management...")
    
    update_thread.start()
    management_thread.start()
    
    # Wait for both to complete
    update_thread.join()
    management_thread.join()
    
    logger.info("Dynamic observer management demo completed!")


def main():
    """Run the multithreaded observer pattern demonstrations."""
    logger.info("🚀 Starting Multithreaded Observer Pattern Demos")
    
    try:
        # Concurrent notifications demo
        demonstrate_concurrent_notifications()
        print()  # Add spacing
        
        # Dynamic observer management demo
        demonstrate_dynamic_observer_management()
        
        logger.info("✅ All multithreaded demos completed successfully!")
        
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        raise


if __name__ == "__main__":
    main()
