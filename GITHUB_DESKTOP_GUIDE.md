# STEP-BY-STEP GITHUB DESKTOP GUIDE FOR AI TRADING SIGNAL PRO

**Complete Visual Guide with Screenshot Instructions**

---

## TABLE OF CONTENTS

1. [Prerequisites Installation](#prerequisites)
2. [GitHub Desktop Setup](#github-desktop-setup)
3. [Clone Repository](#clone-repository)
4. [Python Environment Setup](#python-environment)
5. [Install Dependencies](#install-dependencies)
6. [Run Application](#run-application)
7. [Build Executable](#build-executable)
8. [Commit and Push Changes](#commit-push)
9. [Troubleshooting](#troubleshooting)

---

## PREREQUISITES INSTALLATION

### Step 1: Install Python 3.10+

**Why?** Python is the programming language that runs the application.

#### On Windows 10/11:

1. Open your web browser
2. Go to: https://www.python.org/downloads/
3. Click the yellow "Download Python 3.11" button
4. Run the installer file (python-3.11.x.exe)
5. **CRITICAL:** Check the box that says "Add Python 3.11 to PATH"
6. Click "Install Now"
7. Wait for installation (2-3 minutes)

**Verify Installation:**

Press Win + R, type `cmd`, then type:
```
python --version
```
Should show: `Python 3.11.x` ✓

---

### Step 2: Install GitHub Desktop

1. Go to: https://desktop.github.com/
2. Click "Download for Windows"
3. Run the installer
4. Sign in with your GitHub account
5. Click Finish

---

### Step 3: Verify Git Installation

Press Win + R, type `cmd`, then type:
```
git --version
```
Should show: `git version x.x.x` ✓

---

## GITHUB DESKTOP SETUP

### Step 4: Configure GitHub Desktop

1. Open GitHub Desktop
2. Click File → Options
3. Sign in with your GitHub account
4. Go to Git tab and configure:
   - Name: Your Name
   - Email: villanuevaaaron058@gmail.com

---

## CLONE REPOSITORY

### Step 5: Clone the Project

1. Open GitHub Desktop
2. Click File → Clone Repository
3. Search for: `AI-Trading-Signal-Pro`
4. Select: `villanuevaaaron058-jpg/AI-Trading-Signal-Pro`
5. Choose local path: `C:\Projects\AI-Trading-Signal-Pro`
6. Click Clone

Wait for download to complete (~30 seconds)

**Verify clone:**
Open File Explorer and navigate to C:\Projects\AI-Trading-Signal-Pro
You should see all the project folders and files.

---

## PYTHON ENVIRONMENT SETUP

### Step 6: Create Virtual Environment

1. Press Win + R
2. Type: `powershell` and press Enter
3. Navigate to project:
```powershell
cd C:\Projects\AI-Trading-Signal-Pro
```

4. Create virtual environment:
```powershell
python -m venv venv
```

5. Activate it:
```powershell
.\venv\Scripts\Activate.ps1
```

If you get an error about execution policies:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then activate again.

**Verify:** Your prompt should show `(venv)` at the start ✓

---

## INSTALL DEPENDENCIES

### Step 7: Install Required Packages

With virtual environment active, type:
```powershell
pip install -r requirements.txt
```

This installs all packages (PySide6, pandas, numpy, etc.)
Takes 5-15 minutes. You'll see lots of text scrolling - this is normal!

Wait until you see confirmation message, then command prompt returns.

---

## RUN APPLICATION

### Step 8: Launch the Application

Make sure `(venv)` shows in your command prompt!

Type:
```powershell
python main.py
```

**The application should launch in 3-5 seconds!**

You should see:
- Dark-themed window
- Title: "AI Trading Signal Pro v1.0.0"
- Multiple panels and toolbars

**Success!** ✓✓✓

To exit: Close the window normally.

---

## BUILD EXECUTABLE

### Step 9: Create .exe File

Make sure virtual environment is active.

Type:
```powershell
python build.py
```

This bundles the application into a standalone .exe file.
Takes 5-15 minutes.

**Find your .exe:**
1. Open File Explorer
2. Navigate to: `C:\Projects\AI-Trading-Signal-Pro\dist`
3. You'll see: `AI-Trading-Signal-Pro.exe` (150-200 MB)

**This .exe can be:**
- Moved to any Windows 10/11 PC
- Run standalone (no Python needed)
- Shared with others
- Double-click to launch

---

## COMMIT AND PUSH CHANGES

### Step 10: Make Changes and Commit

**Example: Edit a file**

1. Open any file with notepad
2. Make a change and save (Ctrl+S)

**Commit in GitHub Desktop:**

1. Open GitHub Desktop
2. You'll see your changes listed
3. Check the checkbox to stage changes
4. Write commit message in "Summary" field
   Example: "Update: Add new trading pairs"
5. Click "Commit to main"

**Commit saved locally!** ✓

### Step 11: Push Changes to GitHub

1. Click "Push origin" button in GitHub Desktop
2. Wait for upload to complete
3. Your changes are now on GitHub!

**Verify on GitHub:**
1. Go to: https://github.com/villanuevaaaron058-jpg/AI-Trading-Signal-Pro
2. You should see your commit message

### Step 12: Pull Latest Changes

Before making changes, check for updates:
1. Click "Fetch origin" in GitHub Desktop
2. If there are changes, click "Pull origin"
3. Your local files are up-to-date

---

## YOUR WORKFLOW

After setup, your typical workflow is:

```
1. Open GitHub Desktop
2. Click "Fetch origin"
3. Click "Pull origin"
4. Make changes to files
5. See changes in GitHub Desktop
6. Write commit message
7. Click "Commit to main"
8. Click "Push origin"
Done! Changes are on GitHub.
```

---

## USEFUL COMMANDS REFERENCE

### Virtual Environment
```powershell
# Create
python -m venv venv

# Activate (Windows)
.\venv\Scripts\Activate.ps1

# Deactivate
deactivate
```

### Package Management
```powershell
# Install dependencies
pip install -r requirements.txt

# Install single package
pip install package_name

# List installed packages
pip list

# Upgrade pip
python -m pip install --upgrade pip
```

### Running the Application
```powershell
# Run from source
python main.py

# Build executable
python build.py
```

---

## TROUBLESHOOTING

### Issue 1: "python: command not found"

**Solution:**
1. Reinstall Python from https://www.python.org/downloads/
2. CHECK "Add Python to PATH"
3. Close and reopen command prompt
4. Try `python --version` again

### Issue 2: "No module named 'PySide6'"

**Solution:**
1. Make sure `(venv)` shows in prompt
2. If not, activate: `.\venv\Scripts\Activate.ps1`
3. Reinstall: `pip install -r requirements.txt`

### Issue 3: PyInstaller build fails

**Solution:**
1. Delete: `build/`, `dist/`, `*.spec` folders
2. Run: `pip cache purge`
3. Run: `python build.py` again

### Issue 4: Virtual environment won't activate

**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

### Issue 5: GitHub Desktop won't authenticate

**Solution:**
1. Make sure GitHub account exists
2. Reset password if needed: https://github.com/login
3. Try signing in again

---

## KEYBOARD SHORTCUTS IN APP

| Shortcut | Action |
|----------|--------|
| F1 | Help |
| F2 | Settings |
| F3 | Toggle Watchlist |
| F5 | Refresh Data |
| Ctrl+N | New Window |
| Ctrl+L | Clear Cache |
| Ctrl+H | Show History |
| Ctrl+Q | Exit |

---

## NEXT STEPS

1. **Configure API Keys:**
   - Launch app
   - Tools → Settings
   - Enter API keys
   - Click Save

2. **Add Trading Pairs:**
   - Use watchlist panel
   - Search for pairs
   - Click to add

3. **View Signals:**
   - Select timeframe
   - Choose pair
   - Signals update in real-time

4. **Share Your .exe:**
   - Located in dist/AI-Trading-Signal-Pro.exe
   - Works on any Windows 10/11 PC
   - No Python installation needed

---

## GETTING HELP

1. Check files:
   - README.md
   - GET_STARTED.md
   - GITHUB_DESKTOP_GUIDE.md (this file)

2. Check logs:
   - logs/ folder contains error details

3. GitHub Repository:
   - https://github.com/villanuevaaaron058-jpg/AI-Trading-Signal-Pro

---

## CONGRATULATIONS! 🎉

You now have:
- ✅ Complete Python environment
- ✅ AI Trading Signal Pro running
- ✅ Ability to build .exe
- ✅ Git/GitHub version control
- ✅ Knowledge to extend the app

**Happy Trading!** 📈

---

**Last Updated:** May 23, 2026  
**Version:** 1.0.0
