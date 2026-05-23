"""
Volume Indicators

VWAP, OBV, and related volume indicators.
"""

import logging
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)


class VWAP:
    """
    Volume Weighted Average Price (VWAP)
    
    Average price weighted by volume.
    Used as support/resistance and for confirming trends.
    """
    
    @staticmethod
    def calculate(df: pd.DataFrame) -> pd.Series:
        """
        Calculate VWAP.
        
        Args:
            df: OHLC data with volume
        
        Returns:
            pd.Series: VWAP values
        """
        typical_price = (df['high'] + df['low'] + df['close']) / 3
        vwap = (typical_price * df['volume']).rolling(window=20).sum() / df['volume'].rolling(window=20).sum()
        
        return vwap


class OBV:
    """
    On-Balance Volume (OBV)
    
    Measures buying and selling pressure.
    Rising OBV suggests buying pressure.
    """
    
    @staticmethod
    def calculate(df: pd.DataFrame) -> pd.Series:
        """
        Calculate OBV.
        
        Args:
            df: OHLC data with volume
        
        Returns:
            pd.Series: OBV values
        """
        obv = pd.Series(0.0, index=df.index)
        obv.iloc[0] = df['volume'].iloc[0]
        
        for i in range(1, len(df)):
            if df['close'].iloc[i] > df['close'].iloc[i-1]:
                obv.iloc[i] = obv.iloc[i-1] + df['volume'].iloc[i]
            elif df['close'].iloc[i] < df['close'].iloc[i-1]:
                obv.iloc[i] = obv.iloc[i-1] - df['volume'].iloc[i]
            else:
                obv.iloc[i] = obv.iloc[i-1]
        
        return obv
