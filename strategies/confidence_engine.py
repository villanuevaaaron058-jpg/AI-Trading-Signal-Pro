"""
Confidence Engine

Calculates signal confidence and reliability metrics.
"""

import logging
from typing import Dict, Any
import pandas as pd

logger = logging.getLogger(__name__)


class ConfidenceEngine:
    """
    Calculates confidence and reliability of trading signals.
    
    Considers:
    - Multi-timeframe alignment
    - Indicator convergence
    - Volume confirmation
    - Historical accuracy
    """
    
    def __init__(self):
        """Initialize confidence engine."""
        self.signal_history: list = []
    
    def calculate_multi_timeframe_confidence(
        self,
        signals: Dict[str, Any]
    ) -> float:
        """
        Calculate confidence based on multi-timeframe alignment.
        
        Args:
            signals: Signals from different timeframes
        
        Returns:
            float: Confidence boost (0-100)
        """
        if not signals:
            return 0
        
        # Count aligned signals
        bullish_count = sum(1 for s in signals.values() if 'BUY' in s.get('signal', ''))
        bearish_count = sum(1 for s in signals.values() if 'SELL' in s.get('signal', ''))
        total = len(signals)
        
        # Calculate alignment percentage
        max_aligned = max(bullish_count, bearish_count)
        alignment = (max_aligned / total) * 100 if total > 0 else 0
        
        # Boost confidence if highly aligned
        if alignment >= 75:
            confidence_boost = 30
        elif alignment >= 50:
            confidence_boost = 15
        else:
            confidence_boost = 0
        
        logger.debug(f"Multi-timeframe alignment: {alignment}%")
        return confidence_boost
    
    def calculate_indicator_convergence(
        self,
        indicators: Dict[str, Any]
    ) -> float:
        """
        Calculate how well indicators align.
        
        Args:
            indicators: Calculated indicators
        
        Returns:
            float: Convergence score (0-100)
        """
        convergence_signals = 0
        total_checks = 0
        
        # RSI
        rsi = indicators.get('RSI', 50)
        if rsi > 70 or rsi < 30:
            convergence_signals += 1
        total_checks += 1
        
        # EMA
        ema_12 = indicators.get('EMA_12', 0)
        ema_26 = indicators.get('EMA_26', 0)
        if ema_12 > ema_26:
            convergence_signals += 1
        total_checks += 1
        
        # ADX
        adx = indicators.get('ADX', 25)
        if adx > 25:
            convergence_signals += 1
        total_checks += 1
        
        # Stochastic
        stoch_k = indicators.get('Stochastic_K', 50)
        if stoch_k > 70 or stoch_k < 30:
            convergence_signals += 1
        total_checks += 1
        
        convergence = (convergence_signals / total_checks) * 100 if total_checks > 0 else 0
        logger.debug(f"Indicator convergence: {convergence}%")
        
        return convergence
