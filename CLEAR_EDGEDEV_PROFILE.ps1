# Clear Edge Dev automation profile to remove any synced account data
# Run this if Edge Dev keeps syncing from Edge stable

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Edge Dev Profile Cleaner" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

$profilePath = "$env:LOCALAPPDATA\Microsoft\EdgeDevAutomation"

if (Test-Path $profilePath) {
    Write-Host "Found Edge Dev automation profile at:" -ForegroundColor Yellow
    Write-Host "$profilePath`n" -ForegroundColor Yellow
    
    $confirmation = Read-Host "Delete this profile to remove synced account data? (Y/N)"
    
    if ($confirmation -eq 'Y' -or $confirmation -eq 'y') {
        Write-Host "`nDeleting Edge Dev profile..." -ForegroundColor Yellow
        
        try {
            Remove-Item -Path $profilePath -Recurse -Force -ErrorAction Stop
            Write-Host "`n[SUCCESS] Edge Dev profile deleted!" -ForegroundColor Green
            Write-Host "Next time you run the script, Edge Dev will start fresh with no synced data.`n" -ForegroundColor Green
        }
        catch {
            Write-Host "`n[ERROR] Could not delete profile: $($_.Exception.Message)" -ForegroundColor Red
            Write-Host "Make sure Edge Dev is closed and try again.`n" -ForegroundColor Red
        }
    }
    else {
        Write-Host "`nProfile deletion cancelled.`n" -ForegroundColor Yellow
    }
}
else {
    Write-Host "[INFO] No Edge Dev automation profile found." -ForegroundColor Green
    Write-Host "Edge Dev will create a fresh profile on next run.`n" -ForegroundColor Green
}

Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
