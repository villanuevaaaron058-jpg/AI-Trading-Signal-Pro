"""
Signal Engine

Core trading signal generation logic with multi-indicator analysis.
"""

import logging
from typing import Dict, Any
import pandas as pd
import numpy as np

from indicators.calculator import IndicatorCalculator
from app.constants import SIGNAL_LEVELS

logger = logging.getLogger(__name__)


class SignalEngine:
    """
    Generates trading signals based on technical analysis.
    
    Analyzes 15+ indicators and produces:
    - Signal type (Strong Buy to Strong Sell)
    - Confidence score (0-100%)
    - Entry zone
    - Stop loss
    - Take profit levels
    """
    
    def __init__(self):
        """Initialize signal engine."""
        self.indicator_calc = IndicatorCalculator()
        self.last_signal: Dict[str, Any] = {}
    
    def analyze(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Generate trading signal from market data.
        
        Args:
            df: OHLCV data
        
        Returns:
            Dict: Signal analysis with type, confidence, and levels
        """
        if df.empty or len(df) < 30:
            logger.warning("Insufficient data for analysis")
            return self._neutral_signal()
        
        try:
            # Calculate indicators
            indicators = self.indicator_calc.calculate_all(df)
            
            # Generate signal
            signal_score = self._calculate_signal_score(indicators, df)
            signal_type = self._score_to_signal(signal_score)
            confidence = self._calculate_confidence(indicators, signal_score)
            
            # Calculate entry/exit levels
            entry, sl, tp1, tp2 = self._calculate_levels(df, indicators)
            
            signal_data = {
                'signal': signal_type,
                'confidence': confidence,
                'score': signal_score,
                'timestamp': df.index[-1],
                'price': df['close'].iloc[-1],
                'entry': entry,
                'stop_loss': sl,
                'take_profit_1': tp1,
                'take_profit_2': tp2,
                'indicators': indicators,
            }
            
            self.last_signal = signal_data
            logger.info(f"Signal generated: {signal_type} ({confidence}%)")
            
            return signal_data
        
        except Exception as e:
            logger.error(f"Error generating signal: {e}")
            return self._neutral_signal()
    
    def _calculate_signal_score(self, indicators: Dict[str, Any], df: pd.DataFrame) -> float:
        """
        Calculate weighted signal score (-100 to +100).
        
        Positive = Bullish, Negative = Bearish
        
        Args:
            indicators: Calculated indicators
            df: OHLCV data
        
        Returns:
            float: Signal score
        """
        score = 0.0
        weights = 0.0
        
        # RSI analysis (+/- 20 points)
        rsi = indicators.get('RSI', 50)
        if rsi > 70:
            score += 10  # Overbought
            weights += 1
        elif rsi > 60:
            score += 15  # Strong bullish
            weights += 1
        elif rsi > 50:
            score += 8   # Bullish
            weights += 1
        elif rsi < 30:
            score -= 10  # Oversold
            weights += 1
        elif rsi < 40:
            score -= 15  # Strong bearish
            weights += 1
        elif rsi < 50:
            score -= 8   # Bearish
            weights += 1
        
        # EMA Crossover (+/- 25 points)
        ema_12 = indicators.get('EMA_12', 0)
        ema_26 = indicators.get('EMA_26', 0)
        if ema_12 > ema_26:
            score += 20
            weights += 1
        else:
            score -= 20
            weights += 1
        
        # Trend Direction (+/- 20 points)
        sma_20 = indicators.get('SMA_20', 0)
        sma_50 = indicators.get('SMA_50', 0)
        close = df['close'].iloc[-1]
        
        if close > sma_20 > sma_50:
            score += 20
            weights += 1
        elif close < sma_20 < sma_50:
            score -= 20
            weights += 1
        
        # ADX Trend Strength (+/- 15 points)
        adx = indicators.get('ADX', 25)
        if adx > 25:
            score += (adx - 25) * 0.5  # Strengthen existing signal
            weights += 0.5
        
        # Stochastic Analysis (+/- 15 points)
        stoch_k = indicators.get('Stochastic_K', 50)
        if stoch_k > 80:
            score += 10
            weights += 0.5
        elif stoch_k < 20:
            score -= 10
            weights += 0.5
        
        # Volume Confirmation (+/- 10 points)
        avg_volume = df['volume'].rolling(20).mean().iloc[-1]
        current_volume = df['volume'].iloc[-1]
        if current_volume > avg_volume * 1.5:
            if score > 0:
                score += 8  # Volume confirms bullish
            else:
                score -= 8  # Volume confirms bearish
            weights += 0.5
        
        # Normalize score
        if weights > 0:
            normalized_score = (score / weights) * 2  # Scale to -100 to +100
            normalized_score = max(-100, min(100, normalized_score))
        else:
            normalized_score = 0
        
        return normalized_score
    
    def _score_to_signal(self, score: float) -> str:
        """
        Convert score to signal type.
        
        Args:
            score: Signal score (-100 to +100)
        
        Returns:
            str: Signal type
        """
        if score >= 75:
            return "Strong Buy"
        elif score >= 50:
            return "Buy"
        elif score >= 25:
            return "Weak Buy"
        elif score >= -25:
            return "Neutral"
        elif score >= -50:
            return "Weak Sell"
        elif score >= -75:
            return "Sell"
        else:
            return "Strong Sell"
    
    def _calculate_confidence(self, indicators: Dict[str, Any], score: float) -> float:
        """
        Calculate confidence percentage (0-100%).
        
        Args:
            indicators: Calculated indicators
            score: Signal score
        
        Returns:
            float: Confidence percentage
        """
        # Base confidence from signal strength
        base_confidence = 50 + (abs(score) / 2)
        
        # Boost confidence if ADX is high (strong trend)
        adx = indicators.get('ADX', 25)
        if adx > 30:
            base_confidence += 10
        
        # Cap at 100%
        confidence = min(100, base_confidence)
        
        return round(confidence, 1)
    
    def _calculate_levels(self, df: pd.DataFrame, indicators: Dict[str, Any]) -> tuple:
        """
        Calculate entry, stop loss, and take profit levels.
        
        Args:
            df: OHLCV data
            indicators: Calculated indicators
        
        Returns:
            tuple: (entry, stop_loss, take_profit_1, take_profit_2)
        """
        current_price = df['close'].iloc[-1]
        atr = indicators.get('ATR', current_price * 0.01)
        
        # Entry zone is current price
        entry = current_price
        
        # Stop loss is 1.5 x ATR below entry
        stop_loss = entry - (atr * 1.5)
        
        # Risk/reward = 1.5
        risk_amount = entry - stop_loss
        reward_amount = risk_amount * 1.5
        
        # Take profit levels
        take_profit_1 = entry + reward_amount * 0.5
        take_profit_2 = entry + reward_amount
        
        return round(entry, 2), round(stop_loss, 2), round(take_profit_1, 2), round(take_profit_2, 2)
    
    def _neutral_signal(self) -> Dict[str, Any]:
        """
        Return neutral signal.
        
        Returns:
            Dict: Neutral signal data
        """
        return {
            'signal': 'Neutral',
            'confidence': 50.0,
            'score': 0.0,
            'message': 'Insufficient data or no clear signal',
        }
