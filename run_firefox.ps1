# Firefox Search Automation Script
Write-Host "Starting Firefox Search Automation" -ForegroundColor Green
Write-Host "=====================================" -ForegroundColor Green

# Get script directory and paths
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PythonExe = Join-Path $ScriptDir ".venv\Scripts\python.exe"
$ScriptPath = Join-Path $ScriptDir "search_trending_edge.py"

# Check if Python exists
if (-not (Test-Path $PythonExe)) {
    Write-Host "Python virtual environment not found!" -ForegroundColor Red
    Write-Host "Please create a virtual environment first:" -ForegroundColor Yellow
    Write-Host "  python -m venv .venv" -ForegroundColor White
    Write-Host "  .\.venv\Scripts\python.exe -m pip install -r requirements.txt" -ForegroundColor White
    exit 1
}

# Check if script exists
if (-not (Test-Path $ScriptPath)) {
    Write-Host "Script not found: $ScriptPath" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "This will start automated searches in Firefox browser" -ForegroundColor Cyan
Write-Host ""

# Run the Python script with firefox argument
& $PythonExe $ScriptPath firefox $args

Write-Host ""
Write-Host "Script completed!" -ForegroundColor Green
