@echo off
REM Quick Browser Cleanup - Run this if browsers won't start
REM Kills all browser processes and unlocks profiles
REM Author: H1M

echo.
echo ========================================================
echo   BROWSER CLEANUP UTILITY - BY H1M
echo ========================================================
echo.
echo This will:
echo   1. Kill all browser and driver processes
echo   2. Unlock browser profiles
echo   3. Prepare system for fresh automation run
echo.
echo Press Ctrl+C to cancel, or
pause

echo.
echo Activating Python environment...
call .venv\Scripts\activate.bat

echo.
echo Running cleanup...
python cleanup_browser_processes.py

echo.
echo ========================================================
echo CLEANUP COMPLETE!
echo ========================================================
echo.
echo You can now run your automation again:
echo   - Double-click: RUN_BROWSERS.ps1
echo   - Or use: python run_all_browsers_parallel.py
echo.
pause
