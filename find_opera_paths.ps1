# Find Opera Browser Paths
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Opera Browser Path Finder" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

$wsh = New-Object -ComObject WScript.Shell

# Opera
$operaShortcut = "C:\Users\himan\Desktop\Opera Browser.lnk"
if (Test-Path $operaShortcut) {
    $opera = $wsh.CreateShortcut($operaShortcut)
    $operaPath = $opera.TargetPath
    Write-Host "[OPERA]" -ForegroundColor Yellow
    Write-Host "  Executable: $operaPath" -ForegroundColor Green
    
    if (Test-Path $operaPath) {
        $operaDir = Split-Path $operaPath -Parent
        Write-Host "  Directory: $operaDir" -ForegroundColor Gray
        Write-Host "  Status: INSTALLED" -ForegroundColor Green
        
        # Copy path to clipboard for easy pasting
        Write-Host "`n  Add this to script:" -ForegroundColor Cyan
        Write-Host "  r'$operaPath'" -ForegroundColor White
    } else {
        Write-Host "  Status: PATH NOT FOUND" -ForegroundColor Red
    }
} else {
    Write-Host "[OPERA] Shortcut not found" -ForegroundColor Red
}

Write-Host ""

# Opera GX
$operaGXShortcut = "C:\Users\himan\Desktop\Opera GX Browser.lnk"
if (Test-Path $operaGXShortcut) {
    $operaGX = $wsh.CreateShortcut($operaGXShortcut)
    $operaGXPath = $operaGX.TargetPath
    Write-Host "[OPERA GX]" -ForegroundColor Yellow
    Write-Host "  Executable: $operaGXPath" -ForegroundColor Green
    
    if (Test-Path $operaGXPath) {
        $operaGXDir = Split-Path $operaGXPath -Parent
        Write-Host "  Directory: $operaGXDir" -ForegroundColor Gray
        Write-Host "  Status: INSTALLED" -ForegroundColor Green
        
        # Copy path to clipboard for easy pasting
        Write-Host "`n  Add this to script:" -ForegroundColor Cyan
        Write-Host "  r'$operaGXPath'" -ForegroundColor White
    } else {
        Write-Host "  Status: PATH NOT FOUND" -ForegroundColor Red
    }
} else {
    Write-Host "[OPERA GX] Shortcut not found" -ForegroundColor Red
}

Write-Host "`n========================================`n" -ForegroundColor Cyan
Write-Host "Press any key to exit..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
