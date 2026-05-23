"""
Momentum Indicators

RSI, Stochastic, and related momentum indicators.
"""

import logging
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)


class RSI:
    """
    Relative Strength Index (RSI)
    
    Measures momentum on a scale of 0-100.
    Values above 70 indicate overbought, below 30 oversold.
    """
    
    @staticmethod
    def calculate(prices: pd.Series, period: int = 14) -> pd.Series:
        """
        Calculate RSI.
        
        Args:
            prices: Close prices
            period: RSI period
        
        Returns:
            pd.Series: RSI values
        """
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        
        return rsi


class Stochastic:
    """
    Stochastic Oscillator
    
    Compares closing price to price range over time.
    Values above 80 indicate overbought, below 20 oversold.
    """
    
    @staticmethod
    def calculate(
        df: pd.DataFrame,
        k_period: int = 14,
        d_period: int = 3
    ) -> tuple:
        """
        Calculate Stochastic Oscillator.
        
        Args:
            df: OHLC data
            k_period: K period
            d_period: D period
        
        Returns:
            tuple: (K line, D line)
        """
        low_min = df['low'].rolling(window=k_period).min()
        high_max = df['high'].rolling(window=k_period).max()
        
        k_line = 100 * (df['close'] - low_min) / (high_max - low_min)
        d_line = k_line.rolling(window=d_period).mean()
        
        return k_line, d_line
