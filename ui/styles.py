"""
Application Styling and Themes

QSS stylesheets for professional dark mode UI.
"""

from pathlib import Path

DARK_STYLESHEET = """
QMainWindow {
    background-color: #1e1e2e;
    color: #ffffff;
}

QWidget {
    background-color: #1e1e2e;
    color: #ffffff;
}

QMenuBar {
    background-color: #2d2d3d;
    color: #ffffff;
    border-bottom: 1px solid #3d3d4d;
}

QMenuBar::item:selected {
    background-color: #3d3d4d;
}

QMenu {
    background-color: #2d2d3d;
    color: #ffffff;
    border: 1px solid #3d3d4d;
}

QMenu::item:selected {
    background-color: #00d4ff;
    color: #1e1e2e;
}

QToolBar {
    background-color: #2d2d3d;
    border-bottom: 1px solid #3d3d4d;
    spacing: 5px;
}

QToolBar::separator {
    background-color: #3d3d4d;
}

QToolButton {
    background-color: #2d2d3d;
    color: #ffffff;
    border: 1px solid #3d3d4d;
    padding: 4px;
    border-radius: 3px;
}

QToolButton:hover {
    background-color: #3d3d4d;
    border: 1px solid #00d4ff;
}

QToolButton:pressed {
    background-color: #00d4ff;
    color: #1e1e2e;
}

QPushButton {
    background-color: #00d4ff;
    color: #1e1e2e;
    border: none;
    padding: 6px 12px;
    border-radius: 3px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #00e8ff;
}

QPushButton:pressed {
    background-color: #0099cc;
}

QLineEdit, QTextEdit, QComboBox, QSpinBox, QDoubleSpinBox {
    background-color: #2d2d3d;
    color: #ffffff;
    border: 1px solid #3d3d4d;
    padding: 6px;
    border-radius: 3px;
    selection-background-color: #00d4ff;
}

QLineEdit:focus, QTextEdit:focus, QComboBox:focus {
    border: 1px solid #00d4ff;
}

QComboBox::drop-down {
    border: none;
    background-color: transparent;
}

QComboBox::down-arrow {
    image: url(:/icons/arrow_down.png);
}

QHeaderView::section {
    background-color: #2d2d3d;
    color: #ffffff;
    padding: 6px;
    border: none;
    border-right: 1px solid #3d3d4d;
}

QTableWidget, QTreeWidget, QListWidget {
    background-color: #1e1e2e;
    alternate-background-color: #2d2d3d;
    color: #ffffff;
    gridline-color: #3d3d4d;
    border: 1px solid #3d3d4d;
}

QTableWidget::item:selected, QTreeWidget::item:selected, QListWidget::item:selected {
    background-color: #00d4ff;
    color: #1e1e2e;
}

QScrollBar:vertical {
    background-color: #1e1e2e;
    width: 12px;
}

QScrollBar::handle:vertical {
    background-color: #3d3d4d;
    border-radius: 6px;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background-color: #4d4d5d;
}

QScrollBar:horizontal {
    background-color: #1e1e2e;
    height: 12px;
}

QScrollBar::handle:horizontal {
    background-color: #3d3d4d;
    border-radius: 6px;
    min-width: 20px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #4d4d5d;
}

QLabel {
    color: #ffffff;
}

QStatusBar {
    background-color: #2d2d3d;
    color: #ffffff;
    border-top: 1px solid #3d3d4d;
}

QDockWidget {
    color: #ffffff;
    border: 1px solid #3d3d4d;
}

QDockWidget::title {
    background-color: #2d2d3d;
    padding: 6px;
}

QGroupBox {
    color: #ffffff;
    border: 1px solid #3d3d4d;
    border-radius: 3px;
    padding-top: 10px;
    margin-top: 10px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 3px 0 3px;
}

QTabBar::tab {
    background-color: #2d2d3d;
    color: #ffffff;
    padding: 6px 20px;
    border: 1px solid #3d3d4d;
}

QTabBar::tab:selected {
    background-color: #00d4ff;
    color: #1e1e2e;
}

QTabBar::tab:hover {
    background-color: #3d3d4d;
}

QTabWidget::pane {
    border: 1px solid #3d3d4d;
}

QProgressBar {
    background-color: #2d2d3d;
    color: #ffffff;
    border: 1px solid #3d3d4d;
    border-radius: 3px;
    text-align: center;
}

QProgressBar::chunk {
    background-color: #00d4ff;
}

QCheckBox, QRadioButton {
    color: #ffffff;
    spacing: 5px;
}

QCheckBox::indicator, QRadioButton::indicator {
    width: 18px;
    height: 18px;
}

QCheckBox::indicator:unchecked {
    background-color: #2d2d3d;
    border: 1px solid #3d3d4d;
}

QCheckBox::indicator:checked {
    background-color: #00d4ff;
    border: 1px solid #00d4ff;
}

QMessageBox {
    background-color: #1e1e2e;
}

QMessageBox QLabel {
    color: #ffffff;
}

QMessageBox QPushButton {
    min-width: 60px;
}
"""

def apply_dark_theme(app) -> None:
    """
    Apply dark theme to application.
    
    Args:
        app: QApplication instance
    """
    app.setStyle('Fusion')
    app.setStyleSheet(DARK_STYLESHEET)

def get_stylesheet() -> str:
    """
    Get dark theme stylesheet.
    
    Returns:
        str: QSS stylesheet
    """
    return DARK_STYLESHEET
