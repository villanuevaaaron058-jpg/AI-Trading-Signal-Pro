"""
Analysis Panel Widget

Displays technical analysis and indicator values.
"""

import logging
from typing import Dict, Any, List

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QTableWidget, QTableWidgetItem, QTabWidget
)
from PySide6.QtCore import Qt

from app.config import Config

logger = logging.getLogger(__name__)


class AnalysisPanel(QWidget):
    """
    Technical analysis panel.
    
    Displays indicator values and analysis details.
    """
    
    def __init__(self, config: Config):
        """Initialize analysis panel."""
        super().__init__()
        
        self.config = config
        self.indicators_data: Dict[str, Any] = {}
        
        self._setup_ui()
        logger.info("Analysis panel initialized")
    
    def _setup_ui(self) -> None:
        """Setup widget UI."""
        layout = QVBoxLayout()
        
        # Tab widget
        tabs = QTabWidget()
        
        # Indicators tab
        indicators_table = QTableWidget()
        indicators_table.setColumnCount(2)
        indicators_table.setHorizontalHeaderLabels(["Indicator", "Value"])
        indicators_table.setMaximumHeight(200)
        tabs.addTab(indicators_table, "Indicators")
        self.indicators_table = indicators_table
        
        # Statistics tab
        stats_table = QTableWidget()
        stats_table.setColumnCount(2)
        stats_table.setHorizontalHeaderLabels(["Metric", "Value"])
        tabs.addTab(stats_table, "Statistics")
        self.stats_table = stats_table
        
        layout.addWidget(tabs)
        layout.addStretch()
        
        self.setLayout(layout)
    
    def update_indicators(self, indicators: Dict[str, Any]) -> None:
        """Update indicator display."""
        self.indicators_data = indicators
        
        self.indicators_table.setRowCount(len(indicators))
        for row, (name, value) in enumerate(indicators.items()):
            self.indicators_table.setItem(row, 0, QTableWidgetItem(name))
            
            if isinstance(value, (int, float)):
                formatted_value = f"{value:.2f}"
            else:
                formatted_value = str(value)
            
            self.indicators_table.setItem(row, 1, QTableWidgetItem(formatted_value))
        
        logger.debug(f"Updated {len(indicators)} indicators")
