"""
Math Utilities
"""

import math


def round_price(price: float, decimals: int = 2) -> float:
    """
    Round price to specified decimals.
    
    Args:
        price: Price value
        decimals: Decimal places
    
    Returns:
        float: Rounded price
    """
    return round(price, decimals)


def calculate_percentage_change(old_value: float, new_value: float) -> float:
    """
    Calculate percentage change.
    
    Args:
        old_value: Previous value
        new_value: Current value
    
    Returns:
        float: Percentage change
    """
    if old_value == 0:
        return 0
    return ((new_value - old_value) / old_value) * 100


def calculate_pips(price1: float, price2: float, decimal_places: int = 4) -> float:
    """
    Calculate pips between two prices.
    
    Args:
        price1: First price
        price2: Second price
        decimal_places: Decimal places for pip calculation
    
    Returns:
        float: Pips
    """
    pip_value = 10 ** (-decimal_places)
    return abs(price2 - price1) / pip_value
