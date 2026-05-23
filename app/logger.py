"""
Logging Configuration and Management

Sets up application-wide logging with file and console handlers.
"""

import logging
import logging.handlers
from pathlib import Path
from typing import Optional
from datetime import datetime

# Logger instance
_logger: Optional[logging.Logger] = None


def setup_logger(
    name: str = "AI-Trading-Signal-Pro",
    log_level: str = "INFO",
    log_dir: Optional[Path] = None,
) -> logging.Logger:
    """
    Setup application logger with file and console handlers.
    
    Args:
        name: Logger name
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_dir: Directory for log files
    
    Returns:
        logging.Logger: Configured logger instance
    """
    global _logger
    
    # Set up log directory
    if log_dir is None:
        log_dir = Path(__file__).parent.parent / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, log_level))
    
    # Remove existing handlers
    logger.handlers.clear()
    
    # Create formatter
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, log_level))
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler with rotation
    log_file = log_dir / f"{datetime.now().strftime('%Y-%m-%d')}.log"
    file_handler = logging.handlers.RotatingFileHandler(
        log_file,
        maxBytes=10485760,  # 10 MB
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)  # Always log everything to file
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    _logger = logger
    logger.info(f"Logger initialized: {name}")
    logger.info(f"Log file: {log_file}")
    logger.info(f"Log level: {log_level}")
    
    return logger


def get_logger(name: str = "AI-Trading-Signal-Pro") -> logging.Logger:
    """
    Get logger instance.
    
    Args:
        name: Logger name
    
    Returns:
        logging.Logger: Logger instance
    """
    return logging.getLogger(name)


def set_log_level(level: str) -> None:
    """
    Change logging level dynamically.
    
    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    if _logger:
        _logger.setLevel(getattr(logging, level))
        _logger.info(f"Log level changed to {level}")
