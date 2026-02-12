# Complete Setup Guide - Microsoft Rewards Automation (8 Browsers)

**Complete step-by-step guide to set up 8-browser parallel Microsoft Rewards automation on ANY Windows device.**

---

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Initial Setup](#initial-setup)
3. [Browser Installation](#browser-installation)
4. [Python Environment Setup](#python-environment-setup)
5. [First Run & Account Setup](#first-run--account-setup)
6. [Running the Script](#running-the-script)
7. [Scheduling (Optional)](#scheduling-optional)

---

## System Requirements

### Minimum Requirements
- **OS**: Windows 10/11 (64-bit)
- **RAM**: 8GB minimum, 16GB recommended
- **Disk Space**: 5GB free space
- **Internet**: Stable broadband connection
- **Python**: 3.8 or higher (Python 3.13.7 recommended)

### Supported Browsers
The script supports 8 browsers running in parallel:
1. Microsoft Edge (Pre-installed on Windows)
2. Google Chrome
3. Mozilla Firefox
4. Brave Browser
5. Opera
6. Microsoft Edge Dev
7. Opera GX
8. Chromium

---

## Initial Setup

### Step 1: Download the Repository

**Option A: Using Git (Recommended)**
```cmd
cd C:\Users\%USERNAME%\Desktop
git clone https://github.com/YOUR_USERNAME/edge-search.git
cd edge-search
```

**Option B: Download ZIP**
1. Download ZIP from GitHub
2. Extract to `C:\Users\YourName\Desktop\edge-search`
3. Open Command Prompt in that folder

### Step 2: Verify Python Installation

Open Command Prompt (CMD) and run:
```cmd
python --version
```

**Expected output**: `Python 3.x.x` (3.8 or higher)

**If Python is not installed:**
1. Download from: https://www.python.org/downloads/
2. During installation, **CHECK** ✅ "Add Python to PATH"
3. Click "Install Now"
4. Restart Command Prompt and verify again

---

## Browser Installation

### Quick Install All Browsers

You can install browsers manually or use the commands below:

#### 1. Microsoft Edge
**Already installed on Windows 10/11** ✅

#### 2. Google Chrome
**Download**: https://www.google.com/chrome/
- Run installer
- Complete setup

#### 3. Mozilla Firefox
**Download**: https://www.mozilla.org/firefox/
- Run installer
- Choose "Standard" installation

#### 4. Brave Browser
**Download**: https://brave.com/download/
- Run installer
- Complete setup

#### 5. Opera
**Download**: https://www.opera.com/download
- Run installer
- Install to default location

#### 6. Microsoft Edge Dev
**Download**: https://www.microsoft.com/edge/download/insider
- Select "Dev Channel"
- Run installer

#### 7. Opera GX
**Download**: https://www.opera.com/gx
- Run installer
- Install to default location

#### 8. Chromium
**Download**: https://download-chromium.appspot.com/
- Download latest stable build
- Extract to `C:\Users\YourName\AppData\Local\Chromium`

### Verify Browser Installations

Run this command to check which browsers are detected:
```cmd
"C:\Users\%USERNAME%\Desktop\edge-search\.venv\Scripts\python.exe" run_all_browsers_parallel.py
```
The script will show which browsers are found before running.

---

## Python Environment Setup

### Step 1: Create Virtual Environment

Open Command Prompt in the project folder:
```cmd
cd "C:\Users\%USERNAME%\Desktop\edge-search"
python -m venv .venv
```

**Expected**: Creates `.venv` folder

### Step 2: Activate Virtual Environment

```cmd
.venv\Scripts\activate
```

**Expected**: Command prompt shows `(.venv)` prefix

### Step 3: Install Dependencies

```cmd
pip install -r requirements.txt
```

**Expected output**:
```
Successfully installed selenium-4.39.0 webdriver-manager-4.0.2 pytrends-4.9.2
```

### Step 4: Verify Installation

```cmd
pip list
```

**Expected**: Shows selenium, webdriver-manager, pytrends

---

## First Run & Account Setup

### Step 1: Run the Script (First Time)

From the project folder:
```cmd
.venv\Scripts\python.exe run_all_browsers_parallel.py
```

**OR** use the PowerShell launcher:
```powershell
.\RUN_BROWSERS.ps1
```

### Step 2: Sign In to Microsoft Account

**IMPORTANT**: On the first run, each browser will open. You need to:

1. **Wait for all 8 browsers to open**
2. **Go to each browser window**
3. **Sign in to your Microsoft account** (or create separate accounts)
4. **Allow the script to complete** (browsers will search automatically after login)

### Browser-Specific Notes:

#### Edge & Edge Dev
- Edge Dev is **completely separate** from Edge
- You can use different Microsoft accounts
- Edge Dev won't sync with regular Edge

#### Opera & Opera GX
- Use persistent profiles (stays logged in)
- Opera GX is gaming-focused variant
- Both support separate Microsoft accounts

#### Chrome, Brave, Chromium
- All Chromium-based browsers
- Profiles are isolated from each other
- Each maintains separate login

#### Firefox
- Independent from Chromium browsers
- Uses own profile system

### Step 3: Verify Searches Complete

After signing in, the script will:
- Perform 30 searches per browser
- Show progress: `[1/30] Searching: topic name`
- Display final summary: `Successful: X/8 browsers`

**Expected**: All 8 browsers complete 30 searches each = 240 total searches

---

## Running the Script

### Quick Run Methods

#### Method 1: PowerShell Script (Easiest)
```powershell
.\RUN_BROWSERS.ps1
```

#### Method 2: Direct Python Command
```cmd
.venv\Scripts\python.exe run_all_browsers_parallel.py
```

#### Method 3: From Any Directory (CMD)
```cmd
"C:\Users\%USERNAME%\Desktop\edge-search\.venv\Scripts\python.exe" "C:\Users\%USERNAME%\Desktop\edge-search\run_all_browsers_parallel.py"
```

### What to Expect

**Startup (30-60 seconds)**:
- Script detects installed browsers
- Opens 8 browser windows simultaneously
- Shows browser detection messages

**Search Phase (15-20 minutes)**:
- Each browser performs 30 searches
- Waits 10-15 seconds between searches
- Shows progress for each browser

**Completion**:
```
========================================
          FINAL RESULTS
========================================
Successful: 8/8 browsers
Failed: 0/8 browsers
Total searches: 240
```

---

## Scheduling (Optional)

### Run Automatically Every Day

#### Option 1: Windows Task Scheduler (Recommended)

1. **Open Task Scheduler**: Press `Win + R`, type `taskschd.msc`, press Enter

2. **Create Basic Task**:
   - Click "Create Basic Task"
   - Name: `Microsoft Rewards Automation`
   - Click Next

3. **Trigger**:
   - Select "Daily"
   - Set time (e.g., 9:00 AM)
   - Click Next

4. **Action**:
   - Select "Start a program"
   - Program/script: `C:\Users\YourName\Desktop\edge-search\RUN_BROWSERS.ps1`
   - Start in: `C:\Users\YourName\Desktop\edge-search`
   - Click Next, then Finish

5. **Configure for Background**:
   - Right-click task → Properties
   - Check "Run whether user is logged on or not"
   - Check "Run with highest privileges"
   - Click OK

#### Option 2: Automated Setup Script

Run this PowerShell command as Administrator:
```powershell
.\setup_scheduled_task.ps1
```

This creates a scheduled task automatically.

---

## Profile Locations

Each browser uses persistent profiles to maintain login:

```
Edge:          %LOCALAPPDATA%\Microsoft\Edge\User Data Automation
Chrome:        %LOCALAPPDATA%\Google\Chrome\User Data Automation
Firefox:       %LOCALAPPDATA%\Mozilla\Firefox\Profiles\Automation
Brave:         %LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data Automation
Opera:         %LOCALAPPDATA%\Opera Software\Opera Stable Automation
Edge Dev:      %LOCALAPPDATA%\Microsoft\EdgeDevAutomation\UserData
Opera GX:      %LOCALAPPDATA%\Opera Software\Opera GX Stable Automation
Chromium:      %LOCALAPPDATA%\Chromium\User Data Automation
```

**Why persistent profiles?**
- Stays logged in between runs
- No need to sign in every time
- Maintains Microsoft Rewards progress

---

## Next Steps

1. ✅ **Complete First Run**: Ensure all 8 browsers work
2. ✅ **Check Microsoft Rewards**: Verify points are credited
3. ✅ **Set Up Scheduling**: Automate daily runs
4. 📖 **Read Troubleshooting**: See [FAQ.md](FAQ.md) for common issues

---

## Important Notes

### Browser Updates
- Browsers auto-update regularly
- WebDriver versions are auto-downloaded
- No manual driver management needed

### Multiple Accounts
- You can use same Microsoft account in all browsers
- OR use different accounts (recommended for Opera browsers)
- Edge Dev is isolated from Edge stable

### Performance Tips
- Close unnecessary programs before running
- Ensure stable internet connection
- Don't use browsers while script is running
- 16GB RAM recommended for smooth operation

### Microsoft Rewards Limits
- Daily search limit: ~150 searches per account
- Using 8 browsers = 240 searches (may exceed limit)
- Script automatically handles rate limiting
- Points may take 24 hours to appear

---

## Getting Help

**If you encounter any issues:**

1. Check [FAQ.md](FAQ.md) - Common problems and solutions
2. Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Detailed debugging
3. Open GitHub Issue with:
   - Error message
   - Browser name
   - Python version
   - Windows version

---

## Success Checklist

Before daily use, verify:
- [ ] All 8 browsers installed
- [ ] Python virtual environment activated
- [ ] All dependencies installed (`pip list`)
- [ ] First run completed successfully
- [ ] All browsers stayed logged in
- [ ] Microsoft Rewards points credited
- [ ] (Optional) Scheduled task created

**Your setup is complete! 🎉**

Run `.\RUN_BROWSERS.ps1` anytime to earn Microsoft Rewards points across 8 browsers!
