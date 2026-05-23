#!/usr/bin/env python3
"""
PyInstaller Build Script for AI Trading Signal Pro
Generates standalone Windows .exe executable
"""

import os
import sys
import subprocess
from pathlib import Path

# Build configuration
APP_NAME = "AI-Trading-Signal-Pro"
APP_VERSION = "1.0.0"
BUILD_DIR = "build"
DIST_DIR = "dist"
SPEC_FILE = f"{APP_NAME}.spec"

def get_project_root():
    """Get project root directory"""
    return Path(__file__).parent

def clean_build():
    """Clean previous build artifacts"""
    print("🧹 Cleaning previous builds...")
    dirs_to_remove = [BUILD_DIR, DIST_DIR, "__pycache__", ".pytest_cache"]
    
    for dir_name in dirs_to_remove:
        dir_path = get_project_root() / dir_name
        if dir_path.exists():
            import shutil
            shutil.rmtree(dir_path)
            print(f"   ✓ Removed {dir_name}/")

def create_spec_file():
    """Create PyInstaller spec file"""
    print("📝 Creating PyInstaller spec file...")
    
    spec_content = f'''# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('assets', 'assets'), ('config', 'config')],
    hiddenimports=[
        'PySide6',
        'pandas',
        'numpy',
        'talib',
        'scipy',
        'sklearn',
    ],
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludedimports=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='{APP_NAME}',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/icons/app_icon.ico',
)
'''
    
    spec_file = get_project_root() / SPEC_FILE
    with open(spec_file, 'w') as f:
        f.write(spec_content)
    
    print(f"   ✓ Created {SPEC_FILE}")
    return str(spec_file)

def build_executable(spec_file):
    """Build executable using PyInstaller"""
    print("\n🔨 Building executable...")
    print("   This may take a few minutes...\n")
    
    cmd = [
        sys.executable,
        '-m',
        'PyInstaller',
        '--onefile',
        '--windowed',
        '--name', APP_NAME,
        '--distpath', DIST_DIR,
        '--buildpath', BUILD_DIR,
        '--specpath', '.',
        'main.py'
    ]
    
    result = subprocess.run(cmd, cwd=str(get_project_root()))
    return result.returncode == 0

def verify_build():
    """Verify build was successful"""
    print("\n✅ Verifying build...")
    
    exe_path = get_project_root() / DIST_DIR / f"{APP_NAME}.exe"
    
    if exe_path.exists():
        size_mb = exe_path.stat().st_size / (1024 * 1024)
        print(f"   ✓ Executable created: {exe_path}")
        print(f"   ✓ File size: {size_mb:.1f} MB")
        return True
    else:
        print(f"   ✗ Build failed: Executable not found")
        return False

def print_summary():
    """Print build summary"""
    exe_path = get_project_root() / DIST_DIR / f"{APP_NAME}.exe"
    
    if exe_path.exists():
        print(f"""
╔══════════════════════════════════════════════════════════╗
║           BUILD COMPLETED SUCCESSFULLY! ✨                ║
╚══════════════════════════════════════════════════════════╝

📦 Executable: {exe_path}

🚀 Next Steps:
   1. Test the application:
      {exe_path}
   
   2. Create installer (optional):
      pip install pyinstaller-versionfile
      python build.py --installer
   
   3. Distribute:
      - Share {exe_path} directly
      - Or create installer using NSIS

💾 Build Details:
   - Python Version: {sys.version.split()[0]}
   - PyInstaller Version: {get_pyinstaller_version()}
   - Output Directory: {DIST_DIR}/

⚙️ Configuration:
   - App Name: {APP_NAME}
   - Version: {APP_VERSION}
   - Mode: Production Release
""")

def get_pyinstaller_version():
    """Get PyInstaller version"""
    try:
        import PyInstaller
        return PyInstaller.__version__
    except:
        return "Unknown"

def main():
    """Main build process"""
    print(f"""
╔══════════════════════════════════════════════════════════╗
║     {APP_NAME} v{APP_VERSION}
║           PyInstaller Build Script
╚══════════════════════════════════════════════════════════╝
""")
    
    # Check Python version
    if sys.version_info < (3, 9):
        print("❌ Python 3.9+ required")
        return 1
    
    # Check PyInstaller
    try:
        import PyInstaller
    except ImportError:
        print("❌ PyInstaller not found. Install with: pip install PyInstaller")
        return 1
    
    # Build process
    clean_build()
    spec_file = create_spec_file()
    
    if build_executable(spec_file):
        if verify_build():
            print_summary()
            return 0
    
    print("\n❌ Build failed. Check output above for errors.")
    return 1

if __name__ == "__main__":
    sys.exit(main())
