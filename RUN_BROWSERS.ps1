# PowerShell script to run parallel browser automation with proper environment
Write-Host "`n=== Browser Automation Launcher ===" -ForegroundColor Cyan
Write-Host "Activating virtual environment...`n" -ForegroundColor Yellow

# Activate virtual environment
& "$PSScriptRoot\.venv\Scripts\Activate.ps1"

# Check if activation was successful
if ($LASTEXITCODE -eq 0 -or $env:VIRTUAL_ENV) {
    Write-Host "[OK] Virtual environment activated" -ForegroundColor Green
} else {
    Write-Host "[WARNING] Could not activate virtual environment, trying anyway..." -ForegroundColor Yellow
}

Write-Host "`nStarting parallel browser automation...`n" -ForegroundColor Cyan

# Run the Python script using the venv Python
& "$PSScriptRoot\.venv\Scripts\python.exe" "$PSScriptRoot\run_all_browsers_parallel.py"

# Check exit code
if ($LASTEXITCODE -eq 0) {
    Write-Host "`n[SUCCESS] Script completed successfully!" -ForegroundColor Green
} else {
    Write-Host "`n[ERROR] Script failed with exit code: $LASTEXITCODE" -ForegroundColor Red
}

Write-Host "`nPress any key to exit..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
