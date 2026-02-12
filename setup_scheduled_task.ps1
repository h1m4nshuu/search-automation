# PowerShell Script to Setup Automatic Daily Search Task
# This creates a Windows Task Scheduler task that runs at startup

$TaskName = "DailyBrowserSearchAutomation"
$ScriptPath = "$PSScriptRoot\auto_daily_search.py"
$PythonPath = (Get-Command python).Source

# Check if task already exists
$ExistingTask = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue

if ($ExistingTask) {
    Write-Host "Task already exists. Removing old task..." -ForegroundColor Yellow
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
}

Write-Host "Creating scheduled task..." -ForegroundColor Cyan

# Create task action - run Python script in background (headless)
$Action = New-ScheduledTaskAction `
    -Execute $PythonPath `
    -Argument "`"$ScriptPath`"" `
    -WorkingDirectory $PSScriptRoot

# Create trigger - run at user logon with 2 minute delay
$Trigger = New-ScheduledTaskTrigger `
    -AtLogOn `
    -User $env:USERNAME

# Add delay to trigger
$Trigger.Delay = "PT2M"  # 2 minute delay after logon

# Task settings
$Settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -RunOnlyIfNetworkAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Hours 2) `
    -Priority 7

# Create the principal (run as current user)
$Principal = New-ScheduledTaskPrincipal `
    -UserId $env:USERNAME `
    -LogonType Interactive `
    -RunLevel Limited

# Register the task
$Task = Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $Action `
    -Trigger $Trigger `
    -Settings $Settings `
    -Principal $Principal `
    -Description "Automatically runs 30 browser searches once per day when system starts and internet is available."

Write-Host "`n✅ Scheduled task created successfully!" -ForegroundColor Green
Write-Host "`nTask Details:" -ForegroundColor Cyan
Write-Host "  Name: $TaskName"
Write-Host "  Runs: At user logon (2 minute delay)"
Write-Host "  Frequency: Once per day"
Write-Host "  Requires: Internet connection"
Write-Host "  Mode: Background/Headless"
Write-Host "`nThe task will run automatically when you start your computer."
Write-Host "You can manage it in Task Scheduler (taskschd.msc)"

# Ask if user wants to test now
Write-Host "`n" -NoNewline
$Response = Read-Host "Do you want to test the task now? (y/n)"
if ($Response -eq 'y' -or $Response -eq 'Y') {
    Write-Host "`nRunning test..." -ForegroundColor Cyan
    Start-ScheduledTask -TaskName $TaskName
    Write-Host "Task started! Check the progress in the console windows that appear."
}
