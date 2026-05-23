"""
Market Data Manager

Manages real-time market data and historical candles.
"""

import logging
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

from app.config import Config

logger = logging.getLogger(__name__)


class MarketDataManager:
    """
    Manages market data from multiple providers.
    
    Handles real-time updates, caching, and data validation.
    """
    
    def __init__(self, config: Config):
        """Initialize market data manager."""
        self.config = config
        self.candles: Dict[str, pd.DataFrame] = {}
        self.current_pair = config.trading.default_pair
        self.current_timeframe = config.trading.default_timeframe
        
        logger.info("Market data manager initialized")
    
    def load_candles(
        self,
        pair: str,
        timeframe: str,
        limit: int = 500
    ) -> pd.DataFrame:
        """
        Load candle data for a trading pair.
        
        Args:
            pair: Trading pair (e.g., 'BTC/USDT')
            timeframe: Timeframe (e.g., '1H')
            limit: Number of candles to load
        
        Returns:
            pd.DataFrame: Candle data with OHLCV columns
        """
        cache_key = f"{pair}_{timeframe}"
        
        # Check cache
        if cache_key in self.candles:
            logger.debug(f"Using cached data for {cache_key}")
            return self.candles[cache_key].copy()
        
        # Generate sample data for demo
        candles = self._generate_sample_candles(pair, timeframe, limit)
        self.candles[cache_key] = candles
        
        logger.info(f"Loaded {len(candles)} candles for {pair} ({timeframe})")
        return candles.copy()
    
    def _generate_sample_candles(
        self,
        pair: str,
        timeframe: str,
        count: int
    ) -> pd.DataFrame:
        """
        Generate sample candle data for demonstration.
        
        In production, this would fetch real data from market data providers.
        
        Args:
            pair: Trading pair
            timeframe: Timeframe
            count: Number of candles
        
        Returns:
            pd.DataFrame: Sample OHLCV data
        """
        # Get timeframe in minutes
        timeframe_minutes = self._timeframe_to_minutes(timeframe)
        
        # Generate timestamps
        now = datetime.utcnow()
        timestamps = [now - timedelta(minutes=i*timeframe_minutes) for i in range(count, 0, -1)]
        
        # Generate realistic OHLCV data
        np.random.seed(42)
        close_prices = 100 + np.cumsum(np.random.randn(count) * 0.5)
        
        data = {
            'timestamp': timestamps,
            'open': close_prices + np.random.randn(count) * 0.3,
            'high': close_prices + np.abs(np.random.randn(count) * 0.5),
            'low': close_prices - np.abs(np.random.randn(count) * 0.5),
            'close': close_prices,
            'volume': np.random.uniform(1000000, 5000000, count),
        }
        
        df = pd.DataFrame(data)
        df.set_index('timestamp', inplace=True)
        
        return df
    
    def _timeframe_to_minutes(self, timeframe: str) -> int:
        """
        Convert timeframe string to minutes.
        
        Args:
            timeframe: Timeframe (e.g., '1H', '5m')
        
        Returns:
            int: Minutes
        """
        timeframe_map = {
            '1m': 1, '3m': 3, '5m': 5, '15m': 15,
            '30m': 30, '1H': 60, '4H': 240, '1D': 1440, '1W': 10080
        }
        return timeframe_map.get(timeframe, 60)
    
    def get_latest_candle(self, pair: str, timeframe: str) -> Optional[pd.Series]:
        """
        Get the latest candle for a pair.
        
        Args:
            pair: Trading pair
            timeframe: Timeframe
        
        Returns:
            pd.Series: Latest candle data
        """
        cache_key = f"{pair}_{timeframe}"
        if cache_key in self.candles:
            return self.candles[cache_key].iloc[-1]
        return None
    
    def clear_cache(self) -> None:
        """Clear data cache."""
        self.candles.clear()
        logger.info("Market data cache cleared")
