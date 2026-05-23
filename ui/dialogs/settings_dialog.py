"""
Settings Dialog

Application settings and configuration interface.
"""

import logging
from typing import Optional

from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QTabWidget,
    QGroupBox, QLabel, QLineEdit, QCheckBox,
    QPushButton, QSpinBox, QDoubleSpinBox
)
from PySide6.QtCore import Qt

from app.config import Config

logger = logging.getLogger(__name__)


class SettingsDialog(QDialog):
    """
    Application settings dialog.
    
    Allows user to configure application behavior and API keys.
    """
    
    def __init__(self, config: Config, parent: Optional[QDialog] = None):
        """Initialize settings dialog."""
        super().__init__(parent)
        
        self.config = config
        self.setWindowTitle("Settings")
        self.setMinimumWidth(600)
        self.setMinimumHeight(500)
        
        self._setup_ui()
        logger.info("Settings dialog initialized")
    
    def _setup_ui(self) -> None:
        """Setup dialog UI."""
        layout = QVBoxLayout()
        
        # Tabs
        tabs = QTabWidget()
        
        # General tab
        general_tab = self._create_general_tab()
        tabs.addTab(general_tab, "General")
        
        # API tab
        api_tab = self._create_api_tab()
        tabs.addTab(api_tab, "API Keys")
        
        # Trading tab
        trading_tab = self._create_trading_tab()
        tabs.addTab(trading_tab, "Trading")
        
        layout.addWidget(tabs)
        
        # Buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.accept)
        button_layout.addWidget(save_btn)
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def _create_general_tab(self) -> QWidget:
        """Create general settings tab."""
        from PySide6.QtWidgets import QWidget
        widget = QWidget()
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel("General Settings"))
        layout.addStretch()
        
        widget.setLayout(layout)
        return widget
    
    def _create_api_tab(self) -> QWidget:
        """Create API settings tab."""
        from PySide6.QtWidgets import QWidget
        widget = QWidget()
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel("API Configuration"))
        
        # Binance API
        layout.addWidget(QLabel("Binance API Key:"))
        binance_input = QLineEdit()
        binance_input.setPlaceholderText("Enter Binance API Key")
        layout.addWidget(binance_input)
        
        layout.addWidget(QLabel("Binance Secret Key:"))
        secret_input = QLineEdit()
        secret_input.setPlaceholderText("Enter Binance Secret Key")
        secret_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(secret_input)
        
        layout.addStretch()
        widget.setLayout(layout)
        return widget
    
    def _create_trading_tab(self) -> QWidget:
        """Create trading settings tab."""
        from PySide6.QtWidgets import QWidget
        widget = QWidget()
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel("Trading Configuration"))
        
        # Risk percent
        layout.addWidget(QLabel("Risk Per Trade (%):")
        risk_spin = QDoubleSpinBox()
        risk_spin.setValue(self.config.trading.risk_percent)
        risk_spin.setDecimals(2)
        layout.addWidget(risk_spin)
        
        # Risk/Reward ratio
        layout.addWidget(QLabel("Risk/Reward Ratio:"))
        ratio_spin = QDoubleSpinBox()
        ratio_spin.setValue(self.config.trading.risk_reward_ratio)
        ratio_spin.setDecimals(2)
        layout.addWidget(ratio_spin)
        
        # Alerts
        alerts_check = QCheckBox("Enable Alerts")
        alerts_check.setChecked(self.config.trading.enable_alerts)
        layout.addWidget(alerts_check)
        
        layout.addStretch()
        widget.setLayout(layout)
        return widget
