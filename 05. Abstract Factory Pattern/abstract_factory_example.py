#!/usr/bin/env python3
"""
Simple Abstract Factory Pattern Example

This example demonstrates a furniture store that creates different styles of furniture.
Each factory creates a family of related furniture pieces.
"""

from abc import ABC, abstractmethod
from utils.logger import setup_logging

# Initialize logger
logger = setup_logging()


# Abstract Products
class Chair(ABC):
    """Abstract chair product."""
    
    @abstractmethod
    def sit_on(self) -> str:
        """Sit on the chair."""
        pass


class Table(ABC):
    """Abstract table product."""
    
    @abstractmethod
    def place_items(self) -> str:
        """Place items on the table."""
        pass


# Concrete Products - Modern Style
class ModernChair(Chair):
    """Modern style chair."""
    
    def __init__(self):
        logger.info("Created Modern Chair")
    
    def sit_on(self) -> str:
        result = "Sitting on a sleek modern chair with clean lines"
        logger.info(f"Modern Chair: {result}")
        return result


class ModernTable(Table):
    """Modern style table."""
    
    def __init__(self):
        logger.info("Created Modern Table")
    
    def place_items(self) -> str:
        result = "Placing items on a minimalist glass table"
        logger.info(f"Modern Table: {result}")
        return result


# Concrete Products - Vintage Style
class VintageChair(Chair):
    """Vintage style chair."""
    
    def __init__(self):
        logger.info("Created Vintage Chair")
    
    def sit_on(self) -> str:
        result = "Sitting on a comfortable vintage armchair with floral patterns"
        logger.info(f"Vintage Chair: {result}")
        return result


class VintageTable(Table):
    """Vintage style table."""
    
    def __init__(self):
        logger.info("Created Vintage Table")
    
    def place_items(self) -> str:
        result = "Placing items on an antique wooden table with carved details"
        logger.info(f"Vintage Table: {result}")
        return result


# Abstract Factory
class FurnitureFactory(ABC):
    """Abstract factory for creating furniture families."""
    
    @abstractmethod
    def create_chair(self) -> Chair:
        """Create a chair."""
        pass
    
    @abstractmethod
    def create_table(self) -> Table:
        """Create a table."""
        pass


# Concrete Factories
class ModernFurnitureFactory(FurnitureFactory):
    """Factory for creating modern furniture."""
    
    def __init__(self):
        logger.info("Initialized Modern Furniture Factory")
    
    def create_chair(self) -> Chair:
        logger.info("Modern Factory creating chair")
        return ModernChair()
    
    def create_table(self) -> Table:
        logger.info("Modern Factory creating table")
        return ModernTable()


class VintageFurnitureFactory(FurnitureFactory):
    """Factory for creating vintage furniture."""
    
    def __init__(self):
        logger.info("Initialized Vintage Furniture Factory")
    
    def create_chair(self) -> Chair:
        logger.info("Vintage Factory creating chair")
        return VintageChair()
    
    def create_table(self) -> Table:
        logger.info("Vintage Factory creating table")
        return VintageTable()


# Client
class FurnitureStore:
    """Furniture store that uses factories to create furniture sets."""
    
    def __init__(self, factory: FurnitureFactory):
        self.factory = factory
        logger.info(f"Furniture Store initialized with {factory.__class__.__name__}")
    
    def create_furniture_set(self):
        """Create a complete furniture set."""
        logger.info("Creating a complete furniture set...")
        
        # Create furniture using the factory
        chair = self.factory.create_chair()
        table = self.factory.create_table()
        
        # Demonstrate using the furniture
        chair.sit_on()
        table.place_items()
        
        logger.info("Furniture set creation completed!")
        return chair, table


def demonstrate_abstract_factory():
    """Demonstrate the Abstract Factory pattern."""
    logger.info("=== Abstract Factory Pattern Demo ===")
    
    # Create modern furniture store
    logger.info("\n--- Setting up Modern Furniture Store ---")
    modern_factory = ModernFurnitureFactory()
    modern_store = FurnitureStore(modern_factory)
    modern_chair, modern_table = modern_store.create_furniture_set()
    
    print()  # Add spacing
    
    # Create vintage furniture store
    logger.info("\n--- Setting up Vintage Furniture Store ---")
    vintage_factory = VintageFurnitureFactory()
    vintage_store = FurnitureStore(vintage_factory)
    vintage_chair, vintage_table = vintage_store.create_furniture_set()
    
    print()  # Add spacing
    
    # Demonstrate switching factories
    logger.info("\n--- Switching Store Style ---")
    logger.info("Modern store switching to vintage style...")
    modern_store.factory = vintage_factory
    modern_store.create_furniture_set()


def main():
    """Run the Abstract Factory pattern demonstration."""
    logger.info("🚀 Starting Abstract Factory Pattern Demo")
    
    try:
        demonstrate_abstract_factory()
        logger.info("✅ Demo completed successfully!")
        
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        raise


if __name__ == "__main__":
    main()
        """Toggle checkbox state."""
        pass


class Dialog(ABC):
    """Abstract dialog interface."""
    
    def __init__(self, title: str):
        self.title = title
        logger.info(f"Created {self.__class__.__name__} with title: '{title}'")
    
    @abstractmethod
    def show(self) -> str:
        """Show the dialog."""
        pass


# ============= Windows Products =============

class WindowsButton(Button):
    """Windows-style button implementation."""
    
    def render(self) -> str:
        result = f"🪟 [Windows Button: {self.text}]"
        logger.info(f"Rendered Windows button: {result}")
        return result
    
    def click(self) -> str:
        result = f"Windows button '{self.text}' clicked with mouse"
        logger.info(f"Windows button action: {result}")
        return result


class WindowsCheckbox(Checkbox):
    """Windows-style checkbox implementation."""
    
    def render(self) -> str:
        state = "☑️" if self.checked else "☐"
        result = f"🪟 {state} {self.label}"
        logger.info(f"Rendered Windows checkbox: {result}")
        return result
    
    def toggle(self) -> str:
        self.checked = not self.checked
        result = f"Windows checkbox '{self.label}' {'checked' if self.checked else 'unchecked'}"
        logger.info(f"Windows checkbox action: {result}")
        return result


class WindowsDialog(Dialog):
    """Windows-style dialog implementation."""
    
    def show(self) -> str:
        result = f"🪟 Windows Dialog: '{self.title}' [X]"
        logger.info(f"Showed Windows dialog: {result}")
        return result


# ============= macOS Products =============

class MacOSButton(Button):
    """macOS-style button implementation."""
    
    def render(self) -> str:
        result = f"🍎 ⟮ {self.text} ⟯"
        logger.info(f"Rendered macOS button: {result}")
        return result
    
    def click(self) -> str:
        result = f"macOS button '{self.text}' clicked with trackpad"
        logger.info(f"macOS button action: {result}")
        return result


class MacOSCheckbox(Checkbox):
    """macOS-style checkbox implementation."""
    
    def render(self) -> str:
        state = "✅" if self.checked else "⭕"
        result = f"🍎 {state} {self.label}"
        logger.info(f"Rendered macOS checkbox: {result}")
        return result
    
    def toggle(self) -> str:
        self.checked = not self.checked
        result = f"macOS checkbox '{self.label}' {'selected' if self.checked else 'deselected'}"
        logger.info(f"macOS checkbox action: {result}")
        return result


class MacOSDialog(Dialog):
    """macOS-style dialog implementation."""
    
    def show(self) -> str:
        result = f"🍎 ◐ {self.title} ◑"
        logger.info(f"Showed macOS dialog: {result}")
        return result


# ============= Linux Products =============

class LinuxButton(Button):
    """Linux-style button implementation."""
    
    def render(self) -> str:
        result = f"🐧 [ {self.text} ]"
        logger.info(f"Rendered Linux button: {result}")
        return result
    
    def click(self) -> str:
        result = f"Linux button '{self.text}' clicked with mouse/keyboard"
        logger.info(f"Linux button action: {result}")
        return result


class LinuxCheckbox(Checkbox):
    """Linux-style checkbox implementation."""
    
    def render(self) -> str:
        state = "[X]" if self.checked else "[ ]"
        result = f"🐧 {state} {self.label}"
        logger.info(f"Rendered Linux checkbox: {result}")
        return result
    
    def toggle(self) -> str:
        self.checked = not self.checked
        result = f"Linux checkbox '{self.label}' {'enabled' if self.checked else 'disabled'}"
        logger.info(f"Linux checkbox action: {result}")
        return result


class LinuxDialog(Dialog):
    """Linux-style dialog implementation."""
    
    def show(self) -> str:
        result = f"🐧 +--[ {self.title} ]--+"
        logger.info(f"Showed Linux dialog: {result}")
        return result


# ============= Abstract Factory =============

class UIFactory(ABC):
    """Abstract factory for creating UI component families."""
    
    @abstractmethod
    def create_button(self, text: str) -> Button:
        """Create a button."""
        pass
    
    @abstractmethod
    def create_checkbox(self, label: str) -> Checkbox:
        """Create a checkbox."""
        pass
    
    @abstractmethod
    def create_dialog(self, title: str) -> Dialog:
        """Create a dialog."""
        pass
    
    @abstractmethod
    def get_platform_name(self) -> str:
        """Get the platform name."""
        pass


# ============= Concrete Factories =============

class WindowsUIFactory(UIFactory):
    """Concrete factory for Windows UI components."""
    
    def create_button(self, text: str) -> Button:
        logger.info(f"Windows factory creating button")
        return WindowsButton(text)
    
    def create_checkbox(self, label: str) -> Checkbox:
        logger.info(f"Windows factory creating checkbox")
        return WindowsCheckbox(label)
    
    def create_dialog(self, title: str) -> Dialog:
        logger.info(f"Windows factory creating dialog")
        return WindowsDialog(title)
    
    def get_platform_name(self) -> str:
        return "Windows"


class MacOSUIFactory(UIFactory):
    """Concrete factory for macOS UI components."""
    
    def create_button(self, text: str) -> Button:
        logger.info(f"macOS factory creating button")
        return MacOSButton(text)
    
    def create_checkbox(self, label: str) -> Checkbox:
        logger.info(f"macOS factory creating checkbox")
        return MacOSCheckbox(label)
    
    def create_dialog(self, title: str) -> Dialog:
        logger.info(f"macOS factory creating dialog")
        return MacOSDialog(title)
    
    def get_platform_name(self) -> str:
        return "macOS"


class LinuxUIFactory(UIFactory):
    """Concrete factory for Linux UI components."""
    
    def create_button(self, text: str) -> Button:
        logger.info(f"Linux factory creating button")
        return LinuxButton(text)
    
    def create_checkbox(self, label: str) -> Checkbox:
        logger.info(f"Linux factory creating checkbox")
        return LinuxCheckbox(label)
    
    def create_dialog(self, title: str) -> Dialog:
        logger.info(f"Linux factory creating dialog")
        return LinuxDialog(title)
    
    def get_platform_name(self) -> str:
        return "Linux"


# ============= Factory Provider =============

class UIFactoryProvider:
    """Provider for getting the appropriate UI factory."""
    
    _factories = {
        'windows': WindowsUIFactory,
        'macos': MacOSUIFactory,
        'linux': LinuxUIFactory
    }
    
    @classmethod
    def get_factory(cls, platform: str) -> UIFactory:
        """
        Get the appropriate factory for the platform.
        
        Args:
            platform: Platform name ('windows', 'macos', 'linux')
            
        Returns:
            UIFactory: Appropriate factory instance
            
        Raises:
            ValueError: If platform is not supported
        """
        platform = platform.lower()
        
        if platform not in cls._factories:
            error_msg = f"Unsupported platform: {platform}. Available: {list(cls._factories.keys())}"
            logger.error(error_msg)
            raise ValueError(error_msg)
        
        logger.info(f"Creating factory for platform: {platform}")
        factory_class = cls._factories[platform]
        return factory_class()
    
    @classmethod
    def get_supported_platforms(cls) -> list:
        """Get list of supported platforms."""
        platforms = list(cls._factories.keys())
        logger.info(f"Supported platforms: {platforms}")
        return platforms


# ============= Application Class =============

class Application:
    """Application that uses the UI factory to create components."""
    
    def __init__(self, ui_factory: UIFactory):
        self.ui_factory = ui_factory
        self.components = []
        logger.info(f"Application initialized with {ui_factory.get_platform_name()} UI factory")
    
    def create_settings_dialog(self):
        """Create a settings dialog with various components."""
        logger.info("Creating settings dialog...")
        
        # Create components using the factory
        dialog = self.ui_factory.create_dialog("Settings")
        ok_button = self.ui_factory.create_button("OK")
        cancel_button = self.ui_factory.create_button("Cancel")
        save_checkbox = self.ui_factory.create_checkbox("Save on exit")
        auto_update_checkbox = self.ui_factory.create_checkbox("Auto-update")
        
        self.components = [dialog, ok_button, cancel_button, save_checkbox, auto_update_checkbox]
        
        # Demonstrate rendering
        logger.info("--- Rendering Components ---")
        for component in self.components:
            print(component.render())
        
        # Demonstrate interactions
        logger.info("--- User Interactions ---")
        save_checkbox.toggle()
        ok_button.click()
        
        return self.components


def demonstrate_basic_abstract_factory():
    """Demonstrate basic Abstract Factory pattern."""
    logger.info("=== Basic Abstract Factory Demo ===")
    
    # Get supported platforms
    platforms = UIFactoryProvider.get_supported_platforms()
    logger.info(f"Supported platforms: {platforms}")
    
    # Create factories for different platforms
    for platform in platforms:
        logger.info(f"\n--- Creating UI for {platform.upper()} ---")
        
        # Get the appropriate factory
        factory = UIFactoryProvider.get_factory(platform)
        
        # Create an application with this factory
        app = Application(factory)
        
        # Create and show components
        components = app.create_settings_dialog()
        
        print()  # Add spacing


def demonstrate_runtime_factory_selection():
    """Demonstrate selecting factory at runtime."""
    logger.info("=== Runtime Factory Selection Demo ===")
    
    # Simulate runtime platform detection
    import random
    platforms = UIFactoryProvider.get_supported_platforms()
    selected_platform = random.choice(platforms)
    
    logger.info(f"Simulating runtime platform detection: {selected_platform}")
    
    try:
        # Create factory based on detected platform
        factory = UIFactoryProvider.get_factory(selected_platform)
        app = Application(factory)
        
        # Create a simple login dialog
        logger.info("Creating login dialog...")
        login_dialog = factory.create_dialog("Login")
        login_button = factory.create_button("Login")
        remember_checkbox = factory.create_checkbox("Remember me")
        
        # Show the dialog
        print(login_dialog.render())
        print(login_button.render())
        print(remember_checkbox.render())
        
        # Simulate user interaction
        remember_checkbox.toggle()
        login_button.click()
        
    except ValueError as e:
        logger.error(f"Error: {e}")


def main():
    """Run the Abstract Factory pattern demonstrations."""
    logger.info("🚀 Starting Abstract Factory Pattern Demos")
    
    try:
        # Basic demonstration
        demonstrate_basic_abstract_factory()
        print()
        
        # Runtime selection demonstration
        demonstrate_runtime_factory_selection()
        
        logger.info("✅ All Abstract Factory demos completed successfully!")
        
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        raise


if __name__ == "__main__":
    main()
