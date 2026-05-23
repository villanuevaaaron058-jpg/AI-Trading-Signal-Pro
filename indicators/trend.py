"""
Trend Indicators

EMA, SMA, ADX, and related trend indicators.
"""

import logging
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)


class EMA:
    """
    Exponential Moving Average (EMA)
    
    Weighted moving average that gives more weight to recent prices.
    """
    
    @staticmethod
    def calculate(prices: pd.Series, period: int = 12) -> pd.Series:
        """
        Calculate EMA.
        
        Args:
            prices: Price series
            period: EMA period
        
        Returns:
            pd.Series: EMA values
        """
        return prices.ewm(span=period, adjust=False).mean()


class SMA:
    """
    Simple Moving Average (SMA)
    
    Simple average of prices over a period.
    """
    
    @staticmethod
    def calculate(prices: pd.Series, period: int = 20) -> pd.Series:
        """
        Calculate SMA.
        
        Args:
            prices: Price series
            period: SMA period
        
        Returns:
            pd.Series: SMA values
        """
        return prices.rolling(window=period).mean()


class ADX:
    """
    Average Directional Index (ADX)
    
    Measures trend strength without indicating direction.
    Values above 25 indicate strong trend.
    """
    
    @staticmethod
    def calculate(
        df: pd.DataFrame,
        period: int = 14
    ) -> pd.Series:
        """
        Calculate ADX.
        
        Args:
            df: OHLC data
            period: ADX period
        
        Returns:
            pd.Series: ADX values
        """
        high = df['high']
        low = df['low']
        close = df['close']
        
        plus_dm = high.diff()
        minus_dm = -low.diff()
        
        plus_dm[plus_dm < 0] = 0
        minus_dm[minus_dm < 0] = 0
        
        tr1 = high - low
        tr2 = abs(high - close.shift())
        tr3 = abs(low - close.shift())
        tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        
        atr = tr.rolling(window=period).mean()
        plus_di = 100 * plus_dm.rolling(window=period).mean() / atr
        minus_di = 100 * minus_dm.rolling(window=period).mean() / atr
        
        di_diff = abs(plus_di - minus_di)
        di_sum = plus_di + minus_di
        
        dx = 100 * di_diff / di_sum
        adx = dx.rolling(window=period).mean()
        
        return adx
