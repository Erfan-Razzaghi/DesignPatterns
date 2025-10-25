import logging
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo  # Python 3.9+, or use pytz for older versions
from .constants import DATE_FORMAT, LOG_COLORS, LOG_FORMAT,LOG_LEVEL
from colorlog import ColoredFormatter

class TimezoneAwareFormatter(ColoredFormatter):
    """Custom formatter that uses timezone-aware local time"""
    
    def __init__(self, *args, timezone: str = 'UTC', **kwargs):
        """
        Initialize the formatter with a specific timezone.
        
        Args:
            timezone: Timezone string (e.g., 'UTC', 'America/New_York', 'Europe/London')
        """
        super().__init__(*args, **kwargs)
        self.timezone = timezone
    
    def formatTime(self, record, datefmt: str = None) -> str:
        """
        Override formatTime to use timezone-aware local time.
        
        Args:
            record: Log record
            datefmt: Date format string
            
        Returns:
            str: Formatted timestamp string
        """
        try:
            # Create datetime from record timestamp
            dt = datetime.fromtimestamp(record.created, tz=ZoneInfo(self.timezone))
            
            # Use provided format or default
            format_str = datefmt if datefmt else DATE_FORMAT
            return dt.strftime(format_str)
            
        except Exception as e:
            # Fallback to UTC if timezone conversion fails
            dt = datetime.fromtimestamp(record.created, tz=ZoneInfo('UTC'))
            format_str = datefmt if datefmt else DATE_FORMAT
            return dt.strftime(format_str)
        
def setup_logging(log_level=None):
    """
    Configure logging for the application
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    
    Returns:
        Logger: Configured logger instance
    """
    # Get log level from environment or use default
    if log_level is None:
        log_level_name = LOG_LEVEL
        log_level = getattr(logging, log_level_name.upper(), logging.INFO)
    
    # Clear any existing handlers from the root logger
    root = logging.getLogger()
    if root.handlers:
        for handler in root.handlers:
            root.removeHandler(handler)
    
    # Create console handler with a specific formatter
    console_handler = logging.StreamHandler(sys.stdout)
    console_formatter = TimezoneAwareFormatter(
        LOG_FORMAT,
        datefmt="%Y-%m-%d %H:%M:%S",
        reset=True,
        timezone="Asia/Tehran",
        log_colors=LOG_COLORS
    )
    console_handler.setFormatter(console_formatter)

    # Configure the root logger with just the console handler
    root.setLevel(log_level)
    root.addHandler(console_handler)
    
    # Get our application logger
    logger = logging.getLogger("Educational")
    logger.setLevel(log_level)
    
    # Add a startup message to verify logging is working
    logger.info(f"Educational logger initialized (Level: {log_level_name})")

    # Silence noisy third-party loggers
    # logging.getLogger("telegram").setLevel(logging.WARNING) #this is an example, uncomment if needed

    return logger
