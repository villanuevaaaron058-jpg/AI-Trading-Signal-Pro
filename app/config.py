"""
Application Configuration Management

Handles loading, saving, and managing application settings.
"""

import json
from pathlib import Path
from typing import Any, Dict, Optional
from dataclasses import dataclass, asdict, field
import logging

logger = logging.getLogger(__name__)


@dataclass
class APIConfig:
    """API Configuration"""
    binance_api_key: str = ""
    binance_secret_key: str = ""
    finnhub_api_key: str = ""
    twelvedata_api_key: str = ""
    alphavantage_api_key: str = ""


@dataclass
class UIConfig:
    """UI Configuration"""
    theme: str = "dark"
    window_width: int = 1600
    window_height: int = 900
    window_x: int = 100
    window_y: int = 100
    fullscreen: bool = False
    show_grid: bool = True
    show_volume: bool = True
    dark_mode: bool = True


@dataclass
class TradingConfig:
    """Trading Configuration"""
    default_timeframe: str = "1H"
    default_pair: str = "BTC/USDT"
    risk_percent: float = 1.0
    risk_reward_ratio: float = 1.5
    enable_alerts: bool = True
    enable_notifications: bool = True
    enable_sounds: bool = True


@dataclass
class DataConfig:
    """Data Configuration"""
    primary_provider: str = "binance"
    secondary_provider: str = "finnhub"
    cache_enabled: bool = True
    cache_duration: int = 60
    max_candles: int = 500
    auto_refresh: bool = True
    refresh_interval: int = 5000  # milliseconds


class Config:
    """
    Application configuration manager.
    
    Handles loading, saving, and managing all application settings.
    Supports multiple configuration profiles.
    """
    
    def __init__(self, config_dir: Optional[Path] = None):
        """Initialize configuration manager."""
        self.config_dir = config_dir or Path(__file__).parent.parent / "config"
        self.config_dir.mkdir(parents=True, exist_ok=True)
        
        # Configuration paths
        self.main_config_path = self.config_dir / "app_config.json"
        self.api_config_path = self.config_dir / "api_config.json"
        self.user_settings_path = self.config_dir / "user_settings.json"
        
        # Initialize sections
        self.api = APIConfig()
        self.ui = UIConfig()
        self.trading = TradingConfig()
        self.data = DataConfig()
        self.custom: Dict[str, Any] = {}
    
    def load(self) -> None:
        """Load configuration from files."""
        logger.info("Loading application configuration...")
        
        try:
            if self.main_config_path.exists():
                with open(self.main_config_path, 'r') as f:
                    config_data = json.load(f)
                    self._load_section(config_data, "ui", self.ui)
                    self._load_section(config_data, "trading", self.trading)
                    self._load_section(config_data, "data", self.data)
                logger.info(f"Loaded main config from {self.main_config_path}")
            
            if self.api_config_path.exists():
                with open(self.api_config_path, 'r') as f:
                    api_data = json.load(f)
                    self._load_section(api_data, "api", self.api)
                logger.info(f"Loaded API config from {self.api_config_path}")
            
            if self.user_settings_path.exists():
                with open(self.user_settings_path, 'r') as f:
                    self.custom = json.load(f)
                logger.info(f"Loaded user settings from {self.user_settings_path}")
            
            logger.info("Configuration loaded successfully")
        
        except Exception as e:
            logger.warning(f"Error loading config: {e}. Using defaults.")
            self._create_default_configs()
    
    def save(self) -> None:
        """Save configuration to files."""
        logger.info("Saving application configuration...")
        
        try:
            # Save main config
            main_config = {
                "ui": asdict(self.ui),
                "trading": asdict(self.trading),
                "data": asdict(self.data),
            }
            with open(self.main_config_path, 'w') as f:
                json.dump(main_config, f, indent=2)
            
            # Save API config (careful with sensitive data)
            api_config = {"api": asdict(self.api)}
            with open(self.api_config_path, 'w') as f:
                json.dump(api_config, f, indent=2)
            
            # Save user settings
            with open(self.user_settings_path, 'w') as f:
                json.dump(self.custom, f, indent=2)
            
            logger.info("Configuration saved successfully")
        
        except Exception as e:
            logger.error(f"Error saving config: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value by key."""
        keys = key.split('.')
        value = self.custom
        
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any) -> None:
        """Set configuration value by key."""
        keys = key.split('.')
        config = self.custom
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
    
    def _load_section(self, data: Dict[str, Any], section: str, obj: Any) -> None:
        """Load configuration section into object."""
        if section in data:
            for key, value in data[section].items():
                if hasattr(obj, key):
                    setattr(obj, key, value)
    
    def _create_default_configs(self) -> None:
        """Create default configuration files."""
        logger.info("Creating default configuration files...")
        self.save()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary."""
        return {
            "api": asdict(self.api),
            "ui": asdict(self.ui),
            "trading": asdict(self.trading),
            "data": asdict(self.data),
            "custom": self.custom,
        }
    
    def __repr__(self) -> str:
        """String representation."""
        return f"Config(api={bool(self.api.binance_api_key)}, ui={self.ui.theme})"
