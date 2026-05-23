"""
Data Validators
"""

from app.constants import TRADING_PAIRS, TIMEFRAME_LABELS


def validate_pair(pair: str) -> bool:
    """
    Validate trading pair.
    
    Args:
        pair: Trading pair string
    
    Returns:
        bool: True if valid
    """
    all_pairs = []
    for category, pairs in TRADING_PAIRS.items():
        all_pairs.extend(pairs)
    
    return pair.upper() in [p.upper() for p in all_pairs]


def validate_timeframe(timeframe: str) -> bool:
    """
    Validate timeframe.
    
    Args:
        timeframe: Timeframe string
    
    Returns:
        bool: True if valid
    """
    return timeframe in TIMEFRAME_LABELS


def validate_price(price: float) -> bool:
    """
    Validate price value.
    
    Args:
        price: Price value
    
    Returns:
        bool: True if valid
    """
    return isinstance(price, (int, float)) and price > 0
