"""
AI Trading Signal Pro - Core Application Module

Core functionality including configuration, logging, and application constants.
"""

__version__ = "1.0.0"
__author__ = "AI Trading Team"
__license__ = "MIT"

from .config import Config
from .logger import setup_logger, get_logger
from .constants import (
    APP_NAME,
    APP_VERSION,
    TIMEFRAMES,
    TRADING_PAIRS,
    SIGNAL_LEVELS,
)

__all__ = [
    'Config',
    'setup_logger',
    'get_logger',
    'APP_NAME',
    'APP_VERSION',
    'TIMEFRAMES',
    'TRADING_PAIRS',
    'SIGNAL_LEVELS',
]
