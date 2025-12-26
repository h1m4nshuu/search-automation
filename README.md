# Edge Search Automation - Fixed for PowerShell

This script automates web searches using Microsoft Edge, Chrome, Brave, or Firefox browsers. The script has been fixed to work properly in PowerShell environments.

## Fixes Applied

### 1. PowerShell Execution Issues
- **Problem**: PowerShell couldn't parse the command with spaces in the file path
- **Solution**: Created PowerShell script (`run_search.ps1`) and batch file (`run_search.bat`) that handle path spaces properly using the `&` operator and proper path quoting

### 2. WebDriver Connection Issues  
- **Problem**: Script failed when it couldn't download EdgeDriver due to network issues
- **Solution**: Added fallback logic to use system-installed EdgeDriver if auto-download fails

### 3. Better Error Handling
- **Problem**: Cryptic error messages when things went wrong
- **Solution**: Added comprehensive error handling and informative messages

## Usage Options

### Option 1: PowerShell Script (Recommended)
```powershell
cd "c:\Users\himan\Desktop\edge search"
.\run_search.ps1
```

### Option 2: Batch File
```cmd
cd "c:\Users\himan\Desktop\edge search"
.\run_search.bat
```

### Option 3: Direct Python (if you prefer)
```powershell
cd "c:\Users\himan\Desktop\edge search"
& ".\.venv\Scripts\python.exe" ".\search_trending_edge.py"
```

## Command Line Options

- `--headless` : Run browser in invisible/headless mode
- `--existing` : Connect to existing Edge browser instead of opening new one
- `--help` or `-h` : Show help message

Examples:
```powershell
.\run_search.ps1 --headless    # Run invisibly
.\run_search.ps1 --existing    # Use existing Edge browser
.\run_search.ps1 --help        # Show help
```

## Using Existing Edge Browser

If you want the script to control your main Edge browser instead of opening a new one:

### Option 1: Automated Setup (Recommended)
```powershell
.\run_with_existing_edge.ps1
```

### Option 2: Manual Setup
1. Close all Edge windows
2. Open PowerShell and run: `msedge.exe --remote-debugging-port=9222`
3. Run the script: `.\run_search.ps1 --existing`

## Requirements

- Microsoft Edge, Chrome, Brave, or Firefox browser installed
- Python virtual environment (`.venv`) in the script directory
- Required Python packages: `selenium`, `webdriver-manager`, `pytrends` (already installed)

## Troubleshooting

### If EdgeDriver Issues Persist:
1. Download EdgeDriver manually from: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
2. Place it in your system PATH or the script directory
3. Ensure it matches your Edge browser version

### If PowerShell Execution Policy Issues:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## What the Script Does

1. Fetches trending search topics (or uses fallback list)
2. Opens each topic in Microsoft Edge via Bing search
3. Performs human-like scrolling on each page
4. Waits 50-55 seconds between searches
5. Processes 30 topics by default

commands.txt
🚀 QUICK START WORKFLOWS
Daily Rewards Earning:
.\standalone_rewards.ps1

Quick   Testing:
.\dynamic_test.ps1

See What Topics Will Be Used:
.\topic_showcase.ps1
