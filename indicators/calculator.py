"""
Indicator Calculator

Unified calculator for all technical indicators.
"""

import logging
from typing import Dict, Any
import pandas as pd
import numpy as np

from .momentum import RSI, Stochastic
from .trend import EMA, SMA, ADX
from .volatility import BollingerBands, ATR
from .volume import VWAP, OBV

logger = logging.getLogger(__name__)


class IndicatorCalculator:
    """
    Calculates all technical indicators for analysis.
    
    Provides a unified interface for indicator calculation.
    """
    
    def __init__(self):
        """Initialize calculator."""
        self.last_indicators: Dict[str, Any] = {}
    
    def calculate_all(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Calculate all indicators.
        
        Args:
            df: OHLCV data
        
        Returns:
            Dict: All indicator values
        """
        indicators = {}
        
        try:
            # Momentum indicators
            indicators['RSI'] = RSI.calculate(df['close']).iloc[-1]
            k_line, d_line = Stochastic.calculate(df)
            indicators['Stochastic_K'] = k_line.iloc[-1]
            indicators['Stochastic_D'] = d_line.iloc[-1]
            
            # Trend indicators
            indicators['EMA_12'] = EMA.calculate(df['close'], 12).iloc[-1]
            indicators['EMA_26'] = EMA.calculate(df['close'], 26).iloc[-1]
            indicators['SMA_20'] = SMA.calculate(df['close'], 20).iloc[-1]
            indicators['SMA_50'] = SMA.calculate(df['close'], 50).iloc[-1]
            indicators['ADX'] = ADX.calculate(df).iloc[-1]
            
            # Volatility indicators
            upper, middle, lower = BollingerBands.calculate(df['close'])
            indicators['BB_Upper'] = upper.iloc[-1]
            indicators['BB_Middle'] = middle.iloc[-1]
            indicators['BB_Lower'] = lower.iloc[-1]
            indicators['ATR'] = ATR.calculate(df).iloc[-1]
            
            # Volume indicators
            indicators['VWAP'] = VWAP.calculate(df).iloc[-1]
            indicators['OBV'] = OBV.calculate(df).iloc[-1]
            
            self.last_indicators = indicators
            logger.debug(f"Calculated {len(indicators)} indicators")
            
        except Exception as e:
            logger.error(f"Error calculating indicators: {e}")
        
        return indicators
    
    def get_last_indicators(self) -> Dict[str, Any]:
        """
        Get last calculated indicators.
        
        Returns:
            Dict: Indicator values
        """
        return self.last_indicators.copy()
