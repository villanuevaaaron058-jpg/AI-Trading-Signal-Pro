"""
Enumeration Types for the Application
"""

from enum import Enum, auto


class SignalType(Enum):
    """Trading signal types"""
    STRONG_BUY = "Strong Buy"
    BUY = "Buy"
    WEAK_BUY = "Weak Buy"
    NEUTRAL = "Neutral"
    WEAK_SELL = "Weak Sell"
    SELL = "Sell"
    STRONG_SELL = "Strong Sell"


class Timeframe(Enum):
    """Market timeframes"""
    M1 = "1m"
    M3 = "3m"
    M5 = "5m"
    M15 = "15m"
    M30 = "30m"
    H1 = "1H"
    H4 = "4H"
    D1 = "1D"
    W1 = "1W"


class TrendDirection(Enum):
    """Market trend directions"""
    STRONG_UP = "Strong Uptrend"
    UP = "Uptrend"
    WEAK_UP = "Weak Uptrend"
    NEUTRAL = "Neutral/Ranging"
    WEAK_DOWN = "Weak Downtrend"
    DOWN = "Downtrend"
    STRONG_DOWN = "Strong Downtrend"


class AlertType(Enum):
    """Alert types"""
    SIGNAL = auto()
    PRICE_ALERT = auto()
    VOLUME_ALERT = auto()
    VOLATILITY_ALERT = auto()
    NEWS_ALERT = auto()
    ERROR = auto()


class MarketRegime(Enum):
    """Market regimes"""
    TRENDING_UP = "Trending Up"
    TRENDING_DOWN = "Trending Down"
    RANGING = "Ranging"
    VOLATILE = "Highly Volatile"
    CONSOLIDATING = "Consolidating"


class IndicatorSignal(Enum):
    """Individual indicator signals"""
    STRONG_BUY = 2
    BUY = 1
    NEUTRAL = 0
    SELL = -1
    STRONG_SELL = -2


class DataProvider(Enum):
    """Market data providers"""
    BINANCE = "binance"
    FINNHUB = "finnhub"
    TWELVEDATA = "twelvedata"
    ALPHAVANTAGE = "alphavantage"
    YAHOO = "yahoo"


class NotificationType(Enum):
    """Notification types"""
    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"
    SIGNAL = "signal"
