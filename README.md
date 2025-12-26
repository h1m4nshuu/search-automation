# Microsoft Rewards Search Automation

Automate web searches using Microsoft Edge, Chrome, Brave, or Firefox browsers to earn Microsoft Rewards points. Features human-like behavior, multiple browser support, and browser extension for enhanced automation.

## 🚀 Quick Setup from GitHub

### Step 1: Clone the Repository
```powershell
git clone https://github.com/h1m4nshuu/edge-rewards.git
cd edge-rewards
```

### Step 2: Install Python
- Download and install Python 3.8 or higher from [python.org](https://www.python.org/downloads/)
- Make sure to check "Add Python to PATH" during installation

### Step 3: Create Virtual Environment
```powershell
python -m venv .venv
```

### Step 4: Install Dependencies
```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Step 5: Run the Script
```powershell
# For Edge browser
.\run_search.ps1

# For Chrome browser
& ".\.venv\Scripts\python.exe" ".\search_trending_edge.py" chrome

# For Firefox browser
.\run_firefox.ps1

# For Brave browser
& ".\.venv\Scripts\python.exe" ".\search_trending_edge.py" brave
```

That's it! The browser will open and start performing searches automatically.

---

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

- **Browsers**: Microsoft Edge, Chrome, Brave, or Firefox
- **Python**: Version 3.8 or higher
- **Operating System**: Windows (PowerShell support)
- **Python Packages**: Automatically installed via requirements.txt
  - `selenium` - Browser automation
  - `webdriver-manager` - Automatic driver management
  - `pytrends` - Trending topics fetching

## 🌐 Browser Support

| Browser | Command | Status |
|---------|---------|--------|
| Edge | `.\run_search.ps1` or `python search_trending_edge.py edge` | ✅ Supported |
| Chrome | `python search_trending_edge.py chrome` | ✅ Supported |
| Firefox | `.\run_firefox.ps1` or `python search_trending_edge.py firefox` | ✅ Supported |
| Brave | `python search_trending_edge.py brave` | ✅ Supported |

All browsers use Bing search for Microsoft Rewards compatibility.

## 🎯 Browser Extension (Optional)

The repository includes a Chrome/Edge browser extension with human-like automation features:

**Features:**
- Human-like typing with realistic delays and mistakes
- Auto-scroll with variable speed and pauses
- Click simulation on search results
- Tab switching behavior
- Configurable settings via popup

**Installation:**
1. Open Edge/Chrome and go to `edge://extensions` or `chrome://extensions`
2. Enable "Developer mode"
3. Click "Load unpacked"
4. Select the `extension/` folder from this repository

**Documentation:**
- [START_HERE.md](extension/START_HERE.md) - Quick start guide
- [INSTALLATION.md](extension/INSTALLATION.md) - Detailed installation
- [SCROLLING_GUIDE.md](extension/SCROLLING_GUIDE.md) - Auto-scroll features
- [HUMAN_TYPING_GUIDE.md](extension/HUMAN_TYPING_GUIDE.md) - Typing simulation

## Original Requirements

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
