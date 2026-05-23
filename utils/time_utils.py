"""
Time Utilities
"""

from datetime import datetime, timedelta
import pytz


def format_timestamp(timestamp: datetime, format_str: str = '%Y-%m-%d %H:%M:%S') -> str:
    """
    Format datetime to string.
    
    Args:
        timestamp: Datetime object
        format_str: Format string
    
    Returns:
        str: Formatted timestamp
    """
    if isinstance(timestamp, str):
        return timestamp
    return timestamp.strftime(format_str)


def parse_timeframe(timeframe: str) -> int:
    """
    Convert timeframe string to minutes.
    
    Args:
        timeframe: Timeframe string (e.g., '1H', '5m')
    
    Returns:
        int: Minutes
    """
    timeframe_map = {
        '1m': 1, '3m': 3, '5m': 5, '15m': 15,
        '30m': 30, '1H': 60, '4H': 240,
        '1D': 1440, '1W': 10080
    }
    return timeframe_map.get(timeframe, 60)


def get_candle_timestamp(timeframe: str) -> datetime:
    """
    Get current candle open time.
    
    Args:
        timeframe: Timeframe string
    
    Returns:
        datetime: Candle open time
    """
    minutes = parse_timeframe(timeframe)
    now = datetime.utcnow()
    
    # Round down to nearest timeframe
    candle_time = now.replace(minute=(now.minute // minutes) * minutes, second=0, microsecond=0)
    return candle_time
