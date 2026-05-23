"""
GET STARTED - Quick Start Guide

This guide will help you get the AI Trading Signal Pro application up and running
on Windows 10/11 in just a few minutes using GitHub Desktop.
"""

# ============================================================================
# STEP 1: INSTALL PREREQUISITES
# ============================================================================

## 1.1 Install GitHub Desktop

1. Go to https://desktop.github.com/
2. Click "Download for Windows"
3. Run the installer
4. Follow the installation steps
5. Sign in with your GitHub account (villanuevaaaron058-jpg)

## 1.2 Install Python 3.10+

1. Go to https://www.python.org/downloads/
2. Download "Python 3.11" (Latest)
3. Run the installer
4. **IMPORTANT: Check "Add Python to PATH"**
5. Click "Install Now"
6. Verify installation:
   - Open Command Prompt
   - Type: `python --version`
   - Should show: Python 3.11.x

## 1.3 Install Git (if not included)

Git usually comes with GitHub Desktop, but verify:
- Open Command Prompt
- Type: `git --version`
- Should show: git version x.x.x

# ============================================================================
# STEP 2: CLONE THE REPOSITORY USING GITHUB DESKTOP
# ============================================================================

### 2.1 Open GitHub Desktop

1. Launch GitHub Desktop (search in Start Menu)
2. Click "Sign in" and log in with your GitHub account
3. You should see your "AI-Trading-Signal-Pro" repository listed

### 2.2 Clone the Repository

1. In GitHub Desktop, click "File" → "Clone Repository"
2. Select "villanuevaaaron058-jpg/AI-Trading-Signal-Pro"
3. Choose a location to clone (e.g., C:\Projects\AI-Trading-Signal-Pro)
4. Click "Clone"
5. Wait for the download to complete

### 2.3 Verify the Clone

1. Navigate to your clone folder
2. Open in File Explorer
3. You should see:
   - main.py
   - requirements.txt
   - build.py
   - .gitignore
   - README.md
   - app/ folder
   - ui/ folder
   - data/ folder
   - indicators/ folder
   - strategies/ folder
   - utils/ folder

# ============================================================================
# STEP 3: SETUP PYTHON ENVIRONMENT
# ============================================================================

### 3.1 Open Command Prompt in Project Folder

1. Navigate to your clone folder (C:\Projects\AI-Trading-Signal-Pro)
2. Hold Shift + Right-click in empty space
3. Select "Open PowerShell window here" (or "Open command window here")

### 3.2 Create Virtual Environment

Type this command:
```powershell
python -m venv venv
```

This creates an isolated Python environment for the project.

### 3.3 Activate Virtual Environment

On Windows, type:
```powershell
.\venv\Scripts\Activate.ps1
```

If you get an error about execution policies, try:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then run activate again:
```powershell
.\venv\Scripts\Activate.ps1
```

You should see `(venv)` at the start of your command prompt.

### 3.4 Upgrade pip

Type:
```powershell
python -m pip install --upgrade pip
```

### 3.5 Install Dependencies

Type:
```powershell
pip install -r requirements.txt
```

This will install all necessary packages (PySide6, pandas, numpy, etc.).
This may take 5-10 minutes.

# ============================================================================
# STEP 4: RUN THE APPLICATION
# ============================================================================

### 4.1 Run Main Application

With virtual environment activated, type:
```powershell
python main.py
```

The application should launch in a new window!

### 4.2 Verify It Works

You should see:
- Modern dark-themed window titled "AI Trading Signal Pro v1.0.0"
- Menu bar with File, View, Tools, Help
- Toolbars for timeframe selection and pair search
- Left panel for watchlist
- Center area for charts
- Right panel for signals
- Bottom area for analysis

# ============================================================================
# STEP 5: BUILD WINDOWS EXECUTABLE (.EXE)
# ============================================================================

### 5.1 Install PyInstaller (if not already)

```powershell
pip install PyInstaller
```

### 5.2 Run Build Script

With virtual environment activated:
```powershell
python build.py
```

This will:
1. Clean previous builds
2. Create PyInstaller spec file
3. Compile Python code
4. Bundle all dependencies
5. Generate standalone .exe file

This takes 3-10 minutes depending on your computer.

### 5.3 Find Your .exe

After build completes:
1. Navigate to: `C:\Projects\AI-Trading-Signal-Pro\dist`
2. You'll see: `AI-Trading-Signal-Pro.exe`
3. Double-click to run the application!

The .exe will work on any Windows 10/11 PC without needing Python installed.

# ============================================================================
# STEP 6: MAKE CHANGES AND COMMIT TO GITHUB
# ============================================================================

### 6.1 Make a Change

1. Edit a file (e.g., app/constants.py)
2. Save the file

### 6.2 Stage Changes in GitHub Desktop

1. Open GitHub Desktop
2. You'll see your changes listed
3. Check the checkbox to stage all changes (or select specific files)
4. Add a commit message in the "Summary" field
   Example: "Update: Add new trading pairs"
5. Click "Commit to main"

### 6.3 Push to GitHub

1. Click "Push origin" button at the top
2. Changes are now on GitHub!

### 6.4 Pull Latest Changes

If changes were made elsewhere:
1. Click "Fetch origin"
2. Click "Pull origin"
3. Your local files are updated

# ============================================================================
# STEP 7: TROUBLESHOOTING
# ============================================================================

### Issue: "python: command not found"
**Solution:** Python not in PATH. Reinstall Python and check "Add Python to PATH"

### Issue: "Module not found" error
**Solution:** Make sure virtual environment is activated (you see "(venv)" in prompt)

### Issue: PySide6 installation fails
**Solution:** Try: `pip install --upgrade pip setuptools wheel`

### Issue: Build fails
**Solution:** 
1. Delete build/ and dist/ folders
2. Clear cache: `pip cache purge`
3. Run: `python build.py` again

### Issue: .exe won't start
**Solution:** 
1. Make sure all dependencies are installed
2. Run from command prompt to see error messages
3. Check logs in the application logs folder

# ============================================================================
# STEP 8: NEXT STEPS
# ============================================================================

1. **Configure API Keys:**
   - Open Settings in the app
   - Add Binance/Finnhub API keys
   - Click Save

2. **Add Trading Pairs:**
   - Use the watchlist to search for pairs
   - Click to add to favorites

3. **View Signals:**
   - Select a timeframe
   - Choose a trading pair
   - Charts will update with signals

4. **Customize Settings:**
   - Press F2 or go to Tools → Settings
   - Configure risk management
   - Set alert preferences

5. **Share Your .exe:**
   - The file in dist/AI-Trading-Signal-Pro.exe can be shared
   - Recipients can run it directly (no Python needed)

# ============================================================================
# USEFUL SHORTCUTS
# ============================================================================

F1 - Help
F2 - Settings
F3 - Toggle Watchlist
F5 - Refresh Data
Ctrl+L - Clear Cache
Ctrl+H - Show History
Ctrl+Q - Exit

# ============================================================================
# PROJECT STRUCTURE REFERENCE
# ============================================================================

AI-Trading-Signal-Pro/
├── main.py                    # Application entry point
├── build.py                   # .exe build script
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variables template
├── README.md                 # Project documentation
├── .gitignore               # Git ignore rules
│
├── app/                      # Core application
│   ├── config.py            # Configuration management
│   ├── logger.py            # Logging system
│   ├── constants.py         # Application constants
│   └── enums.py             # Type enumerations
│
├── ui/                       # User interface
│   ├── main_window.py       # Main window
│   ├── styles.py            # QSS themes
│   ├── widgets/             # UI components
│   └── dialogs/             # Dialog windows
│
├── data/                     # Market data
│   └── market_data.py       # Data manager
│
├── indicators/               # Technical indicators
│   ├── calculator.py        # Unified calculator
│   ├── momentum.py          # RSI, Stochastic
│   ├── trend.py             # EMA, SMA, ADX
│   ├── volatility.py        # Bollinger, ATR
│   └── volume.py            # VWAP, OBV
│
├── strategies/               # Trading logic
│   ├── signal_engine.py     # Signal generation
│   ├── confidence_engine.py # Confidence scoring
│   └── risk_management.py   # Risk calculations
│
├── utils/                    # Utilities
│   ├── time_utils.py        # Time functions
│   ├── math_utils.py        # Math helpers
│   └── validators.py        # Data validation
│
├── config/                   # Configuration files
├── assets/                   # Icons, sounds, styles
├── logs/                     # Application logs (auto-created)
└── dist/                     # Build output (generated by build.py)

# ============================================================================
# GITHUB DESKTOP WORKFLOW
# ============================================================================

1. Make changes locally
2. See changes in GitHub Desktop
3. Write commit message
4. Click "Commit to main"
5. Click "Push origin"
6. Changes appear on GitHub.com

# ============================================================================
# VERSION CONTROL BEST PRACTICES
# ============================================================================

✓ Commit frequently (after small changes)
✓ Write clear commit messages
✓ Pull before making changes
✓ Never commit dist/ or venv/ folders (already in .gitignore)
✓ Keep commits focused on one feature

# ============================================================================

You're all set! Happy trading! 🚀

For questions, check README.md or documentation files.
