@echo off
echo ========================================
echo   lastframe Installer for Windows
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH!
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

echo [1/3] Python found:
python --version
echo.

echo [2/3] Installing lastframe and dependencies...
echo This may take a few minutes...
echo.

pip install -e .
if errorlevel 1 (
    echo.
    echo [ERROR] Installation failed!
    echo.
    echo Try running this script as Administrator:
    echo Right-click on install_windows.bat and select "Run as administrator"
    echo.
    pause
    exit /b 1
)

echo.
echo [3/3] Verifying installation...
echo.

lastframe --help >nul 2>&1
if errorlevel 1 (
    echo.
    echo [WARNING] lastframe command not found in PATH!
    echo.
    echo The installation was successful, but you may need to:
    echo 1. Close and reopen your terminal/command prompt
    echo 2. Add Python Scripts folder to your PATH
    echo 3. Or use: python -m lastframe.cli instead of lastframe
    echo.
    echo See INSTALL_WINDOWS.md for detailed troubleshooting.
    echo.
    pause
    exit /b 0
)

echo ========================================
echo   Installation Complete!
echo ========================================
echo.
echo You can now use lastframe from anywhere:
echo.
echo   lastframe movie.mp4
echo   lastframe --help
echo.
echo For more info, see INSTALL_WINDOWS.md
echo.
pause
