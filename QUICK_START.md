# 🚀 QUICK START - Fixed Browser Closing Issues

## ⚡ Run Automation (Recommended Method)

```powershell
# Double-click this file:
RUN_BROWSERS.ps1

# Or run manually:
.\RUN_BROWSERS.ps1
```

**The script now automatically**:
- ✅ Checks if you're running too quickly (< 5 minutes)
- ✅ Kills lingering browser processes
- ✅ Unlocks profile directories
- ✅ Launches all 8 browsers cleanly
- ✅ Cleans up after completion

---

## 🛠️ If Browsers Close Unexpectedly

### Option 1: Manual Cleanup (Fastest)
```batch
# Double-click this file:
CLEANUP_BROWSERS.bat

# Wait 30 seconds, then run again:
RUN_BROWSERS.ps1
```

### Option 2: Python Cleanup
```bash
python cleanup_browser_processes.py
# Then run main script
python run_all_browsers_parallel.py
```

---

## ⏱️ Cooldown System

**If you run within 5 minutes**, you'll see:
```
⚠ WARNING: RAPID RE-RUN DETECTED!
   Wait: 3.2 more minutes
⚠ Continue anyway? (yes/no):
```

**Your choices**:
- Type `no` → Wait 3 more minutes (RECOMMENDED)
- Type `yes` → Run anyway (may cause issues)
- Run cleanup → Then you can run immediately

**Why 5 minutes?**
- Prevents profile locks
- Avoids Microsoft automation detection
- Ensures clean browser state

---

## 🔧 Troubleshooting Commands

### Reset Cooldown (After Cleanup)
```bash
python check_run_cooldown.py reset
```

### Manual Process Kill
```powershell
# Check what's running
tasklist | findstr /i "edge opera chromium driver"

# Kill specific browser
taskkill /F /IM msedge.exe
taskkill /F /IM opera.exe

# Kill all browsers (nuclear option)
CLEANUP_BROWSERS.bat
```

### Check Profile Locks
Look for lock files in:
```
%LOCALAPPDATA%\Microsoft\Edge\User Data Automation
%LOCALAPPDATA%\Opera Software\Opera Stable Automation
%LOCALAPPDATA%\Opera Software\Opera GX Stable Automation
%LOCALAPPDATA%\Chromium\User Data Automation
```

Delete files named: `SingletonLock`, `SingletonSocket`, `LOCK`

---

## 📋 Testing Workflow

```bash
# Test 1
python run_all_browsers_parallel.py
✓ Works

# Test 2 (immediately after)
python run_all_browsers_parallel.py
⚠ Cooldown warning → Type "yes" to continue

# Test 3 (after cleanup)
python cleanup_browser_processes.py
python check_run_cooldown.py reset
python run_all_browsers_parallel.py
✓ Works
```

---

## 🎯 Daily Use (No Issues)

```bash
# Schedule once per day - no cooldown problems
# Just run normally:
RUN_BROWSERS.ps1
```

The 5-minute cooldown only matters if you're:
- Testing multiple times rapidly
- Debugging code changes
- Running manually many times per hour

For normal daily automation, you'll never see the warning.

---

## ✅ Fixed Issues

| Problem | Solution |
|---------|----------|
| Browsers close after 2-3 runs | Auto-cleanup + cooldown |
| Profile locks | Automatic unlock before run |
| Lingering driver processes | Force-kill in finally block |
| Automation detection | 5-minute cooldown warning |

---

## 📞 Still Stuck?

1. Run cleanup: `CLEANUP_BROWSERS.bat`
2. Restart computer
3. Check [BROWSER_CLOSING_FIX.md](BROWSER_CLOSING_FIX.md) for details
4. Check [FAQ.md](FAQ.md) for more solutions

---

**Files You Need**:
- `RUN_BROWSERS.ps1` - Main launcher
- `CLEANUP_BROWSERS.bat` - Manual cleanup
- `run_all_browsers_parallel.py` - Python script
- `cleanup_browser_processes.py` - Cleanup utility
- `check_run_cooldown.py` - Cooldown detector

All files automatically included with the project.

---

**Created by**: H1M  
**Last Updated**: January 2025
