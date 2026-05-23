"""
Risk Management

Calculates position sizing, stop losses, and take profit levels.
"""

import logging
from typing import Dict, Any, Tuple
import pandas as pd

logger = logging.getLogger(__name__)


class RiskManager:
    """
    Manages risk calculations for trades.
    
    Calculates:
    - Position size
    - Stop loss levels
    - Take profit levels
    - Risk-to-reward ratios
    - Risk per trade
    """
    
    def __init__(
        self,
        account_size: float = 10000,
        risk_percent: float = 1.0,
        risk_reward_ratio: float = 1.5
    ):
        """
        Initialize risk manager.
        
        Args:
            account_size: Trading account size
            risk_percent: Risk per trade as % of account
            risk_reward_ratio: Target risk-to-reward ratio
        """
        self.account_size = account_size
        self.risk_percent = risk_percent
        self.risk_reward_ratio = risk_reward_ratio
    
    def calculate_position_size(
        self,
        entry_price: float,
        stop_loss: float
    ) -> float:
        """
        Calculate position size based on risk.
        
        Args:
            entry_price: Entry price
            stop_loss: Stop loss price
        
        Returns:
            float: Position size
        """
        risk_amount = self.account_size * (self.risk_percent / 100)
        price_difference = abs(entry_price - stop_loss)
        
        if price_difference == 0:
            return 0
        
        position_size = risk_amount / price_difference
        
        logger.info(f"Position size: {position_size:.2f} units")
        return position_size
    
    def calculate_stop_loss(
        self,
        entry_price: float,
        atr: float,
        signal_type: str
    ) -> float:
        """
        Calculate stop loss based on ATR.
        
        Args:
            entry_price: Entry price
            atr: Average True Range
            signal_type: Signal type (Buy/Sell)
        
        Returns:
            float: Stop loss price
        """
        if 'BUY' in signal_type:
            stop_loss = entry_price - (atr * 1.5)
        else:
            stop_loss = entry_price + (atr * 1.5)
        
        return round(stop_loss, 2)
    
    def calculate_take_profits(
        self,
        entry_price: float,
        stop_loss: float,
        signal_type: str
    ) -> Tuple[float, float]:
        """
        Calculate take profit levels.
        
        Args:
            entry_price: Entry price
            stop_loss: Stop loss price
            signal_type: Signal type
        
        Returns:
            Tuple: (take_profit_1, take_profit_2)
        """
        risk_amount = abs(entry_price - stop_loss)
        reward_amount = risk_amount * self.risk_reward_ratio
        
        if 'BUY' in signal_type:
            tp1 = entry_price + (reward_amount * 0.5)
            tp2 = entry_price + reward_amount
        else:
            tp1 = entry_price - (reward_amount * 0.5)
            tp2 = entry_price - reward_amount
        
        return round(tp1, 2), round(tp2, 2)
    
    def calculate_risk_reward(
        self,
        entry_price: float,
        stop_loss: float,
        take_profit: float
    ) -> float:
        """
        Calculate risk-to-reward ratio.
        
        Args:
            entry_price: Entry price
            stop_loss: Stop loss price
            take_profit: Take profit price
        
        Returns:
            float: Risk-to-reward ratio
        """
        risk = abs(entry_price - stop_loss)
        reward = abs(take_profit - entry_price)
        
        if risk == 0:
            return 0
        
        ratio = reward / risk
        return round(ratio, 2)
