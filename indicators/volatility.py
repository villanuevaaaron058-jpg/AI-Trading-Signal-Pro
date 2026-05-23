"""
Volatility Indicators

Bollinger Bands, ATR, and related volatility indicators.
"""

import logging
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)


class BollingerBands:
    """
    Bollinger Bands
    
    Shows volatility and potential overbought/oversold levels.
    Consists of a middle band (SMA) and upper/lower bands (2 std deviations).
    """
    
    @staticmethod
    def calculate(
        prices: pd.Series,
        period: int = 20,
        std_dev: float = 2.0
    ) -> tuple:
        """
        Calculate Bollinger Bands.
        
        Args:
            prices: Price series
            period: Period
            std_dev: Standard deviations
        
        Returns:
            tuple: (upper_band, middle_band, lower_band)
        """
        middle = prices.rolling(window=period).mean()
        std = prices.rolling(window=period).std()
        
        upper = middle + (std * std_dev)
        lower = middle - (std * std_dev)
        
        return upper, middle, lower


class ATR:
    """
    Average True Range (ATR)
    
    Measures market volatility.
    Used for setting stop losses and profit targets.
    """
    
    @staticmethod
    def calculate(df: pd.DataFrame, period: int = 14) -> pd.Series:
        """
        Calculate ATR.
        
        Args:
            df: OHLC data
            period: ATR period
        
        Returns:
            pd.Series: ATR values
        """
        high = df['high']
        low = df['low']
        close = df['close']
        
        tr1 = high - low
        tr2 = abs(high - close.shift())
        tr3 = abs(low - close.shift())
        
        tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        atr = tr.rolling(window=period).mean()
        
        return atr
