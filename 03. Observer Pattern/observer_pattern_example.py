#!/usr/bin/env python3
"""
Simple Observer Pattern Example

The Observer pattern allows objects to be notified when another object changes state.
"""

from abc import ABC, abstractmethod
from utils.logger import setup_logging

# Initialize logger
logger = setup_logging()


class Subject:
    """Maintains observers and notifies them of changes."""
    
    def __init__(self, name: str = "Subject"):
        self._observers = []
        self.name = name
        logger.info(f"Created subject: {self.name}")
    
    def attach(self, observer):
        """Add an observer."""
        self._observers.append(observer)
        logger.info(f"Attached observer: {observer.name}")
    
    def detach(self, observer):
        """Remove an observer."""
        self._observers.remove(observer)
        logger.info(f"Detached observer: {observer.name}")
    
    def notify(self, message: str):
        """Notify all observers."""
        logger.info(f"Notifying {len(self._observers)} observer(s): '{message}'")
        for observer in self._observers:
            observer.update(self, message)


class Observer(ABC):
    """Observer interface."""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def update(self, subject, message: str):
        """Receive update from subject."""
        pass


class ConcreteObserver(Observer):
    """Basic observer that logs received messages."""
    
    def update(self, subject, message: str):
        logger.info(f"Observer '{self.name}' received: '{message}' from '{subject.name}'")


class EmailSubscriber(Observer):
    """Observer for email notifications."""
    
    def __init__(self, name: str, email: str):
        super().__init__(name)
        self.email = email
    
    def update(self, subject, message: str):
        logger.info(f"📧 Email to {self.name} ({self.email}): '{message}'")


def demonstrate_observer_pattern():
    """Simple demonstration of the Observer pattern."""
    logger.info("=== Observer Pattern Demo ===")
    
    # Create a subject
    news_agency = Subject("News Agency")
    
    # Create observers
    observer1 = ConcreteObserver("Alice")
    observer2 = ConcreteObserver("Bob")
    email_sub = EmailSubscriber("Charlie", "charlie@example.com")
    
    # Attach observers
    news_agency.attach(observer1)
    news_agency.attach(observer2)
    news_agency.attach(email_sub)
    
    # Notify observers
    news_agency.notify("Breaking news: Observer pattern works!")
    
    # Detach one observer
    news_agency.detach(observer2)
    
    # Notify remaining observers
    news_agency.notify("Bob has left the building")


def main():
    """Run the observer pattern demonstration."""
    logger.info("🚀 Starting Observer Pattern Demo")
    
    try:
        demonstrate_observer_pattern()
        logger.info("✅ Demo completed successfully!")
        
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        raise


if __name__ == "__main__":
    main()
