"""
Signal Panel Widget

Displays trading signals and confidence scores.
"""

import logging
from typing import Optional, Dict, Any

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QProgressBar, QFrame
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

from app.config import Config

logger = logging.getLogger(__name__)


class SignalPanel(QWidget):
    """
    Signal display panel.
    
    Shows current trading signals and confidence levels.
    """
    
    def __init__(self, config: Config):
        """Initialize signal panel."""
        super().__init__()
        
        self.config = config
        self.current_signal = None
        self.confidence = 0
        
        self._setup_ui()
        logger.info("Signal panel initialized")
    
    def _setup_ui(self) -> None:
        """Setup widget UI."""
        layout = QVBoxLayout()
        
        # Signal display
        signal_label = QLabel("Current Signal")
        signal_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(signal_label)
        
        self.signal_display = QLabel("NEUTRAL")
        self.signal_display.setStyleSheet(
            "font-size: 24px; font-weight: bold; color: #666666; padding: 10px;"
        )
        self.signal_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.signal_display)
        
        # Confidence bar
        confidence_label = QLabel("Confidence")
        confidence_label.setStyleSheet("font-weight: bold;")
        layout.addWidget(confidence_label)
        
        self.confidence_bar = QProgressBar()
        self.confidence_bar.setValue(0)
        self.confidence_bar.setStyleSheet(
            "QProgressBar { background-color: #2d2d3d; border: 1px solid #3d3d4d; "
            "border-radius: 3px; } "
            "QProgressBar::chunk { background-color: #00d4ff; }"
        )
        layout.addWidget(self.confidence_bar)
        
        # Signal details
        self.details_label = QLabel("No signal data")
        self.details_label.setWordWrap(True)
        self.details_label.setStyleSheet("color: #a0a0a0; font-size: 12px;")
        layout.addWidget(self.details_label)
        
        layout.addStretch()
        self.setLayout(layout)
    
    def set_signal(self, signal_data: Dict[str, Any]) -> None:
        """Update signal display."""
        if signal_data:
            signal_type = signal_data.get('signal', 'NEUTRAL')
            confidence = signal_data.get('confidence', 0)
            
            self.signal_display.setText(signal_type)
            self.confidence_bar.setValue(int(confidence))
            
            # Set color based on signal
            if 'BUY' in signal_type:
                self.signal_display.setStyleSheet(
                    "font-size: 24px; font-weight: bold; color: #00ff41; padding: 10px;"
                )
            elif 'SELL' in signal_type:
                self.signal_display.setStyleSheet(
                    "font-size: 24px; font-weight: bold; color: #ff0033; padding: 10px;"
                )
            else:
                self.signal_display.setStyleSheet(
                    "font-size: 24px; font-weight: bold; color: #666666; padding: 10px;"
                )
            
            logger.info(f"Signal updated: {signal_type} ({confidence}%)")
