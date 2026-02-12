# Automatic Daily Search Scheduling Setup

## Overview
This setup allows your browser searches to run automatically once per day when you start your computer, only when internet is available.

## Features
- ✅ Runs automatically at system startup
- ✅ Only runs once per 24 hours
- ✅ Checks for internet connectivity before running
- ✅ Runs in background (headless mode)
- ✅ 30 searches across all 4 browsers (Edge, Chrome, Firefox, Brave)
- ✅ Smart scheduling - won't run if already completed today

## Quick Setup (Recommended)

### Step 1: Run the Setup Script
Open PowerShell in this directory and run:

```powershell
.\setup_scheduled_task.ps1
```

This will create a Windows Task Scheduler task that runs automatically.

### Step 2: Done!
The task is now configured. It will run automatically:
- When you log into Windows
- After a 2-minute delay (to let system fully load)
- Only if internet is connected
- Only once per day

## Manual Setup (Alternative)

If you prefer to set it up manually:

1. **Open Task Scheduler**: Press `Win + R`, type `taskschd.msc`, press Enter

2. **Create Basic Task**:
   - Click "Create Task" (not "Create Basic Task")
   - Name: "DailyBrowserSearchAutomation"
   - Description: "Runs 30 browser searches once daily"

3. **Triggers Tab**:
   - Click "New"
   - Begin the task: "At log on"
   - Specific user: Your username
   - Delay task for: 2 minutes
   - Check "Enabled"

4. **Actions Tab**:
   - Click "New"
   - Action: "Start a program"
   - Program/script: `python` (or full path to python.exe)
   - Arguments: `"C:\Users\himan\Desktop\edge search\auto_daily_search.py"`
   - Start in: `C:\Users\himan\Desktop\edge search`

5. **Conditions Tab**:
   - Check "Start only if the following network connection is available"
   - Select "Any connection"

6. **Settings Tab**:
   - Check "Allow task to be run on demand"
   - Check "Run task as soon as possible after a scheduled start is missed"
   - Check "If the task fails, restart every: 10 minutes"
   - Uncheck "Stop the task if it runs longer than: 3 days"

## Managing the Scheduled Task

### View Task Status
```powershell
Get-ScheduledTask -TaskName "DailyBrowserSearchAutomation"
```

### Run Task Manually (for testing)
```powershell
Start-ScheduledTask -TaskName "DailyBrowserSearchAutomation"
```

### Disable Task
```powershell
Disable-ScheduledTask -TaskName "DailyBrowserSearchAutomation"
```

### Enable Task
```powershell
Enable-ScheduledTask -TaskName "DailyBrowserSearchAutomation"
```

### Remove Task
```powershell
Unregister-ScheduledTask -TaskName "DailyBrowserSearchAutomation" -Confirm:$false
```

## How It Works

1. **At Startup**: Task scheduler waits 2 minutes after you log in
2. **Internet Check**: Script checks if internet is available
3. **Daily Check**: Script checks if it already ran today (using `.last_run_timestamp` file)
4. **Run Searches**: If all checks pass, runs 30 searches on each browser (120 total)
5. **Update Timestamp**: Marks today as completed
6. **Next Day**: Will run again the next time you start your computer (after midnight)

## Headless Mode

To run browsers in background (no visible windows):

Edit `auto_daily_search.py` line 78, change:
```python
run_all_browsers_parallel()
```

To run with headless mode enabled in each browser function.

## Logs and Monitoring

- **Last Run Timestamp**: Stored in `.last_run_timestamp` file
- **Task History**: View in Task Scheduler → Task Scheduler Library → Find your task → History tab

## Troubleshooting

### Task doesn't run
1. Check Task Scheduler → Task Scheduler Library
2. Right-click task → Run
3. Check if "Last Run Result" shows error code

### Internet check fails
- Script checks connectivity to Google DNS (8.8.8.8)
- If behind firewall, edit `check_internet_connection()` function

### Already ran today but need to run again
Delete the timestamp file:
```powershell
Remove-Item ".\.last_run_timestamp"
```

### Want to change run frequency
Edit `has_run_today()` function in `auto_daily_search.py` to change time window.

## Customization

### Change number of searches per browser
Edit `run_all_browsers_parallel.py`:
```python
TOPIC_COUNT = 30  # Change this number
```

### Change browsers
Edit `run_all_browsers_parallel.py`:
```python
browsers = ['edge', 'chrome', 'firefox', 'brave']  # Remove browsers you don't want
```

### Change startup delay
Edit `setup_scheduled_task.ps1`:
```powershell
$Trigger.Delay = "PT2M"  # PT2M = 2 minutes, PT5M = 5 minutes
```

### Add email notifications
Install and configure email notifications in Windows Task Scheduler settings.

## Notes

- First run may take longer as it copies browser profiles (one-time setup)
- Ensure all browsers have logged in at least once manually
- Script uses randomized delays between searches (appears more human)
- All browsers run in parallel for faster execution
