"""
Main Application Window

Primary UI container with menu bar, toolbars, and dock widgets.
"""

import logging
from pathlib import Path
from typing import Optional

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QDockWidget, QStatusBar, QLabel, QComboBox,
    QLineEdit, QPushButton, QSplitter
)
from PySide6.QtCore import Qt, QSize, QTimer
from PySide6.QtGui import QIcon, QAction

from app.config import Config
from ui.styles import apply_dark_theme
from ui.widgets.chart_widget import ChartWidget
from ui.widgets.watchlist_panel import WatchlistPanel
from ui.widgets.signal_panel import SignalPanel
from ui.widgets.analysis_panel import AnalysisPanel

logger = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    """
    Main application window.
    
    Implements the primary UI layout with multiple panels and real-time data.
    """
    
    def __init__(self, config: Config):
        """Initialize main window."""
        super().__init__()
        
        self.config = config
        self.setWindowTitle("AI Trading Signal Pro v1.0.0")
        self.setWindowIcon(self._get_icon())
        
        # Window size
        self.setGeometry(
            config.ui.window_x,
            config.ui.window_y,
            config.ui.window_width,
            config.ui.window_height
        )
        
        # Setup UI
        self._setup_ui()
        self._setup_menu_bar()
        self._setup_toolbars()
        self._setup_status_bar()
        self._setup_signals()
        
        logger.info("Main window initialized")
    
    def _setup_ui(self) -> None:
        """Setup main UI layout."""
        # Central widget
        central_widget = QWidget()
        layout = QHBoxLayout()
        central_widget.setLayout(layout)
        
        # Left panel: Watchlist
        self.watchlist_panel = WatchlistPanel(self.config)
        left_dock = self._create_dock_widget("Watchlist", self.watchlist_panel, Qt.DockWidgetArea.LeftDockWidgetArea)
        
        # Center: Chart
        self.chart_widget = ChartWidget(self.config)
        
        # Right panel: Signals
        self.signal_panel = SignalPanel(self.config)
        right_dock = self._create_dock_widget("Signals", self.signal_panel, Qt.DockWidgetArea.RightDockWidgetArea)
        
        # Bottom panel: Analysis
        self.analysis_panel = AnalysisPanel(self.config)
        bottom_dock = self._create_dock_widget("Analysis", self.analysis_panel, Qt.DockWidgetArea.BottomDockWidgetArea)
        
        # Add chart to central area
        layout.addWidget(self.chart_widget)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        logger.info("UI layout setup complete")
    
    def _create_dock_widget(self, title: str, widget: QWidget, area: Qt.DockWidgetArea) -> QDockWidget:
        """Create and setup dock widget."""
        dock = QDockWidget(title)
        dock.setWidget(widget)
        self.addDockWidget(area, dock)
        return dock
    
    def _setup_menu_bar(self) -> None:
        """Setup application menu bar."""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("&File")
        
        new_action = QAction("&New Window", self)
        new_action.setShortcut("Ctrl+N")
        file_menu.addAction(new_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("&Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # View menu
        view_menu = menubar.addMenu("&View")
        
        refresh_action = QAction("&Refresh Data", self)
        refresh_action.setShortcut("F5")
        refresh_action.triggered.connect(self._refresh_data)
        view_menu.addAction(refresh_action)
        
        # Tools menu
        tools_menu = menubar.addMenu("&Tools")
        
        settings_action = QAction("&Settings", self)
        settings_action.setShortcut("F2")
        settings_action.triggered.connect(self._open_settings)
        tools_menu.addAction(settings_action)
        
        # Help menu
        help_menu = menubar.addMenu("&Help")
        
        about_action = QAction("&About", self)
        about_action.triggered.connect(self._show_about)
        help_menu.addAction(about_action)
        
        logger.info("Menu bar setup complete")
    
    def _setup_toolbars(self) -> None:
        """Setup application toolbars."""
        # Timeframe toolbar
        timeframe_bar = self.addToolBar("Timeframe")
        timeframe_bar.setObjectName("TimeframeToolBar")
        
        timeframe_label = QLabel("Timeframe: ")
        timeframe_bar.addWidget(timeframe_label)
        
        self.timeframe_combo = QComboBox()
        self.timeframe_combo.addItems(["1m", "5m", "15m", "1H", "4H", "1D", "1W"])
        self.timeframe_combo.setCurrentText(self.config.trading.default_timeframe)
        self.timeframe_combo.currentTextChanged.connect(self._on_timeframe_changed)
        timeframe_bar.addWidget(self.timeframe_combo)
        
        timeframe_bar.addSeparator()
        
        # Pair search
        pair_label = QLabel("Pair: ")
        timeframe_bar.addWidget(pair_label)
        
        self.pair_input = QLineEdit()
        self.pair_input.setPlaceholderText("Search pair...")
        self.pair_input.setMaximumWidth(150)
        self.pair_input.returnPressed.connect(self._on_pair_search)
        timeframe_bar.addWidget(self.pair_input)
        
        search_btn = QPushButton("Search")
        search_btn.clicked.connect(self._on_pair_search)
        timeframe_bar.addWidget(search_btn)
        
        timeframe_bar.addStretch()
        
        logger.info("Toolbars setup complete")
    
    def _setup_status_bar(self) -> None:
        """Setup status bar."""
        status = self.statusBar()
        
        self.status_label = QLabel("Ready")
        status.addWidget(self.status_label, 1)
        
        self.connection_label = QLabel("● Disconnected")
        self.connection_label.setStyleSheet("color: #ff0033;")
        status.addPermanentWidget(self.connection_label)
        
        logger.info("Status bar setup complete")
    
    def _setup_signals(self) -> None:
        """Setup signal connections."""
        # Update timer
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self._update_data)
        self.update_timer.start(self.config.data.refresh_interval)
    
    def _get_icon(self) -> QIcon:
        """Get application icon."""
        icon_path = Path(__file__).parent.parent / "assets" / "icons" / "app_icon.png"
        if icon_path.exists():
            return QIcon(str(icon_path))
        return QIcon()
    
    def _refresh_data(self) -> None:
        """Refresh market data."""
        self.status_label.setText("Refreshing data...")
        logger.info("Data refresh triggered")
    
    def _open_settings(self) -> None:
        """Open settings dialog."""
        logger.info("Settings dialog requested")
    
    def _show_about(self) -> None:
        """Show about dialog."""
        logger.info("About dialog requested")
    
    def _on_timeframe_changed(self, timeframe: str) -> None:
        """Handle timeframe change."""
        logger.info(f"Timeframe changed to: {timeframe}")
        self.chart_widget.set_timeframe(timeframe)
    
    def _on_pair_search(self) -> None:
        """Handle pair search."""
        pair = self.pair_input.text().strip()
        if pair:
            logger.info(f"Searching for pair: {pair}")
            self.chart_widget.load_pair(pair)
    
    def _update_data(self) -> None:
        """Update data periodically."""
        # This would be called periodically to update charts and signals
        pass
    
    def closeEvent(self, event) -> None:
        """Handle window close event."""
        logger.info("Closing application...")
        self.config.save()
        super().closeEvent(event)
