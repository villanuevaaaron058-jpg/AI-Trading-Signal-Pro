"""
Application Constants and Configuration Values
"""

from enum import Enum
from typing import Dict, List

# Application Info
APP_NAME = "AI Trading Signal Pro"
APP_VERSION = "1.0.0"
APP_AUTHOR = "AI Trading Team"
APP_LICENSE = "MIT"

# Timeframes
TIMEFRAMES = {
    "1m": 1,
    "3m": 3,
    "5m": 5,
    "15m": 15,
    "30m": 30,
    "1H": 60,
    "4H": 240,
    "1D": 1440,
    "1W": 10080,
}

TIMEFRAME_LABELS = list(TIMEFRAMES.keys())

# Trading Pairs - Forex
FOREX_PAIRS = [
    "EUR/USD",
    "GBP/USD",
    "USD/JPY",
    "USD/CAD",
    "USD/CHF",
    "AUD/USD",
    "NZD/USD",
    "EUR/GBP",
    "EUR/JPY",
    "GBP/JPY",
]

# Trading Pairs - Crypto
CRYPTO_PAIRS = [
    "BTC/USDT",
    "ETH/USDT",
    "BNB/USDT",
    "XRP/USDT",
    "ADA/USDT",
    "SOL/USDT",
    "DOGE/USDT",
    "AVAX/USDT",
    "MATIC/USDT",
    "LINK/USDT",
]

# Trading Pairs - Commodities
COMMODITY_PAIRS = [
    "XAU/USD",  # Gold
    "XAG/USD",  # Silver
    "CL=F",     # Crude Oil
    "NG=F",     # Natural Gas
    "ZC=F",     # Corn
]

# Trading Pairs - Indices
INDICES_PAIRS = [
    "NASDAQ",
    "SPX500",
    "DAX",
    "FTSE",
    "CAC40",
    "NIKKEI",
    "ASX200",
]

TRADING_PAIRS = {
    "Forex": FOREX_PAIRS,
    "Crypto": CRYPTO_PAIRS,
    "Commodities": COMMODITY_PAIRS,
    "Indices": INDICES_PAIRS,
}

# Signal Levels
class SignalLevel(Enum):
    """Trading signal levels"""
    STRONG_BUY = 1
    BUY = 2
    WEAK_BUY = 3
    NEUTRAL = 4
    WEAK_SELL = 5
    SELL = 6
    STRONG_SELL = 7

SIGNAL_LEVELS = {
    "Strong Buy": (90, 100),
    "Buy": (75, 89),
    "Weak Buy": (60, 74),
    "Neutral": (40, 59),
    "Weak Sell": (26, 39),
    "Sell": (11, 25),
    "Strong Sell": (0, 10),
}

# Indicator Settings
INDICATOR_PERIODS = {
    "RSI": 14,
    "MACD_FAST": 12,
    "MACD_SLOW": 26,
    "MACD_SIGNAL": 9,
    "SMA_FAST": 20,
    "SMA_SLOW": 50,
    "EMA_FAST": 12,
    "EMA_SLOW": 26,
    "BB_PERIOD": 20,
    "BB_STDDEV": 2,
    "STOCH_K": 14,
    "STOCH_D": 3,
    "ADX_PERIOD": 14,
    "ATR_PERIOD": 14,
}

# UI Colors (Dark Theme)
COLORS = {
    "bg_primary": "#1e1e2e",
    "bg_secondary": "#2d2d3d",
    "text_primary": "#ffffff",
    "text_secondary": "#a0a0a0",
    "accent": "#00d4ff",
    "success": "#00ff41",
    "danger": "#ff0033",
    "warning": "#ffaa00",
    "neutral": "#666666",
    "chart_bg": "#161622",
    "grid": "#2d2d3d",
}

# Confidence Thresholds
CONFIDENCE_THRESHOLDS = {
    "strong_buy": 90,
    "buy": 75,
    "weak_buy": 60,
    "neutral_high": 55,
    "neutral_low": 45,
    "weak_sell": 40,
    "sell": 25,
    "strong_sell": 10,
}

# Risk Management
RISK_REWARD_RATIO = 1.5
DEFAULT_RISK_PERCENT = 1.0  # Risk 1% per trade

# API Configuration
API_TIMEOUTS = {
    "default": 10,
    "market_data": 15,
    "websocket": 30,
}

# Cache Settings
CACHE_DURATION = {
    "market_data": 60,      # 1 minute
    "indicators": 120,      # 2 minutes
    "signals": 300,         # 5 minutes
}

# Application Settings
APP_CONFIG = {
    "window_width": 1600,
    "window_height": 900,
    "default_theme": "dark",
    "default_timeframe": "1H",
    "update_interval": 1000,  # 1 second
    "max_candles_display": 500,
    "enable_sounds": True,
    "enable_notifications": True,
}

# Log Settings
LOG_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "max_bytes": 10485760,  # 10 MB
    "backup_count": 5,
}
