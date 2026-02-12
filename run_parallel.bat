@echo off
REM Activate virtual environment and run the parallel browser script
echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo.
echo Starting parallel browser automation...
echo.

python run_all_browsers_parallel.py

pause
