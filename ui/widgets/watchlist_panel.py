"""
Watchlist Panel Widget

Manages trading pair watchlist and favorites.
"""

import logging
from typing import List, Set

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
    QPushButton, QListWidget, QListWidgetItem
)
from PySide6.QtCore import Qt

from app.config import Config
from app.constants import TRADING_PAIRS

logger = logging.getLogger(__name__)


class WatchlistPanel(QWidget):
    """
    Watchlist management panel.
    
    Displays and manages favorite trading pairs.
    """
    
    def __init__(self, config: Config):
        """Initialize watchlist panel."""
        super().__init__()
        
        self.config = config
        self.watchlist: Set[str] = set()
        self.all_pairs: List[str] = []
        
        self._load_all_pairs()
        self._setup_ui()
        logger.info("Watchlist panel initialized")
    
    def _load_all_pairs(self) -> None:
        """Load all available trading pairs."""
        for category, pairs in TRADING_PAIRS.items():
            self.all_pairs.extend(pairs)
        logger.info(f"Loaded {len(self.all_pairs)} trading pairs")
    
    def _setup_ui(self) -> None:
        """Setup widget UI."""
        layout = QVBoxLayout()
        
        # Search box
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search pairs...")
        self.search_input.textChanged.connect(self._filter_pairs)
        search_layout.addWidget(self.search_input)
        layout.addLayout(search_layout)
        
        # Watchlist
        self.watchlist_widget = QListWidget()
        self.watchlist_widget.itemClicked.connect(self._on_pair_selected)
        layout.addWidget(self.watchlist_widget)
        
        # Add default pairs
        for pair in self.all_pairs[:20]:  # Show first 20
            self.watchlist_widget.addItem(pair)
        
        self.setLayout(layout)
    
    def _filter_pairs(self, search_text: str) -> None:
        """Filter pairs by search text."""
        self.watchlist_widget.clear()
        
        filtered = [p for p in self.all_pairs if search_text.lower() in p.lower()]
        for pair in filtered[:20]:  # Limit to 20 results
            self.watchlist_widget.addItem(pair)
        
        logger.debug(f"Filtered pairs: {len(filtered)}")
    
    def _on_pair_selected(self, item: QListWidgetItem) -> None:
        """Handle pair selection."""
        pair = item.text()
        self.watchlist.add(pair)
        logger.info(f"Selected pair: {pair}")
    
    def add_to_watchlist(self, pair: str) -> None:
        """Add pair to watchlist."""
        self.watchlist.add(pair)
        logger.info(f"Added to watchlist: {pair}")
    
    def remove_from_watchlist(self, pair: str) -> None:
        """Remove pair from watchlist."""
        self.watchlist.discard(pair)
        logger.info(f"Removed from watchlist: {pair}")
