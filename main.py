#!/usr/bin/env python3
"""
AI Trading Signal Pro - Main Application Entry Point

Professional trading signal application with real-time market analysis,
multi-timeframe support, and AI-powered signal generation.

Author: AI Trading Team
Version: 1.0.0
License: MIT
"""

import sys
import logging
from pathlib import Path
from typing import Optional

try:
    from PySide6.QtWidgets import QApplication
    from PySide6.QtCore import Qt
except ImportError:
    print("❌ PySide6 not installed. Install with: pip install -r requirements.txt")
    sys.exit(1)

# Add project root to path
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

from app.logger import setup_logger, get_logger
from app.config import Config
from ui.main_window import MainWindow

# Global logger
logger: Optional[logging.Logger] = None

def setup_application() -> QApplication:
    """
    Initialize QApplication with proper settings.
    
    Returns:
        QApplication: Configured Qt application instance
    """
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    
    # Set application metadata
    app.setApplicationName("AI Trading Signal Pro")
    app.setApplicationVersion("1.0.0")
    app.setApplicationAuthor("Trading Team")
    app.setOrganizationName("AI-Trading")
    
    # Enable high DPI scaling
    app.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
    app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)
    
    return app

def setup_paths() -> None:
    """
    Create necessary application directories if they don't exist.
    """
    required_dirs = [
        PROJECT_ROOT / "logs",
        PROJECT_ROOT / "cache",
        PROJECT_ROOT / "db",
        PROJECT_ROOT / "config",
    ]
    
    for directory in required_dirs:
        directory.mkdir(parents=True, exist_ok=True)
        logger.debug(f"Directory ready: {directory}")

def main() -> int:
    """
    Main application entry point.
    
    Returns:
        int: Application exit code (0 = success, non-zero = error)
    """
    global logger
    
    try:
        # Setup logging first
        setup_logger()
        logger = get_logger(__name__)
        
        logger.info("="*60)
        logger.info("Starting AI Trading Signal Pro v1.0.0")
        logger.info("="*60)
        
        # Setup directories
        setup_paths()
        
        # Load configuration
        logger.info("Loading application configuration...")
        config = Config()
        config.load()
        
        # Initialize Qt Application
        logger.info("Initializing Qt Application...")
        app = setup_application()
        
        # Create main window
        logger.info("Creating main window...")
        main_window = MainWindow(config)
        
        # Show window
        logger.info("Displaying main window...")
        main_window.show()
        
        logger.info("Application started successfully ✓")
        logger.info("Entering event loop...")
        
        # Run application
        exit_code = app.exec()
        
        logger.info(f"Application exiting with code: {exit_code}")
        logger.info("="*60)
        
        return exit_code
        
    except Exception as e:
        error_msg = f"Fatal error: {type(e).__name__}: {str(e)}"
        if logger:
            logger.critical(error_msg, exc_info=True)
        else:
            print(f"❌ {error_msg}")
            import traceback
            traceback.print_exc()
        
        # Show error dialog
        try:
            from PySide6.QtWidgets import QMessageBox
            app = QApplication.instance()
            if app is None:
                app = QApplication(sys.argv)
            
            QMessageBox.critical(
                None,
                "Application Error",
                f"A critical error occurred:\n\n{error_msg}\n\nCheck logs for details.",
                QMessageBox.StandardButton.Ok
            )
        except:
            pass
        
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
