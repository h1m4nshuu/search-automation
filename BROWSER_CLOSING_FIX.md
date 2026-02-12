# 🔧 BROWSER CLOSING FIX - Complete Solution

## Problem
**Edge Dev, Opera, Opera GX, and Chromium close automatically after 2-3 test runs**

This happens because:
1. **Profile locks** - Previous browser instances didn't fully close, locking profile files
2. **Lingering processes** - Driver executables (msedgedriver.exe, operadriver.exe, etc.) stay running
3. **Rapid automation detection** - Running too quickly triggers browser anti-bot systems
4. **Incomplete cleanup** - driver.quit() sometimes fails to kill all processes

---

## ✅ Solutions Implemented

### 1. **Automatic Pre-Run Cleanup**
The script now automatically cleans up before every run:
- Kills all lingering browser processes
- Removes profile lock files
- Waits for processes to fully terminate

**File**: `run_all_browsers_parallel.py`
- Runs cleanup before launching browsers
- Ensures clean state every time

---

### 2. **Cooldown Detection System**
Warns you if running too frequently (< 5 minutes):

```
⚠ WARNING: RAPID RE-RUN DETECTED!
   Last run: 2.3 minutes ago
   Cooldown: 5 minutes recommended
   Wait: 2.7 more minutes
```

**Why 5 minutes?**
- Gives browsers time to fully close
- Prevents Microsoft detection
- Allows profile locks to clear

**File**: `check_run_cooldown.py`

---

### 3. **Force-Kill on Cleanup Failure**
If `driver.quit()` fails, the script now:
1. Tries graceful quit first
2. Force-kills browser process if that fails
3. Kills driver executable (msedgedriver, operadriver, etc.)

**File**: `search_trending_edge.py` (finally block)

---

### 4. **Manual Cleanup Tool**
Run this if browsers won't start:

**Windows**: Double-click `CLEANUP_BROWSERS.bat`

**Python**: `python cleanup_browser_processes.py`

This will:
- Kill all browser/driver processes
- Unlock all profile directories
- Give you a clean slate

**File**: `cleanup_browser_processes.py`

---

## 📋 Usage Guide

### Normal Workflow (Recommended)
```powershell
# Run automation (auto-cleanup included)
.\RUN_BROWSERS.ps1

# Or with Python:
python run_all_browsers_parallel.py
```

The script will:
1. ✅ Check cooldown (5 minutes)
2. ✅ Kill lingering processes
3. ✅ Unlock profiles
4. ✅ Launch all 8 browsers
5. ✅ Clean up after completion

---

### If You Run Too Quickly

**Scenario**: You just ran the script 2 minutes ago and want to run again

**What happens**:
```
⚠ WARNING: RAPID RE-RUN DETECTED!
   Last run: 2.0 minutes ago
   Wait: 3.0 more minutes

⚠ Continue anyway? (yes/no):
```

**Your options**:
1. **Type `no`** - Wait 3 more minutes (RECOMMENDED)
2. **Type `yes`** - Run anyway (may cause closures)
3. **Run cleanup first** - Then try again immediately

---

### If Browsers Still Close

**Step 1**: Run manual cleanup
```batch
CLEANUP_BROWSERS.bat
```

**Step 2**: Wait 30 seconds

**Step 3**: Try again
```powershell
.\RUN_BROWSERS.ps1
```

**Step 4**: If still failing, check Task Manager
- Look for stuck processes: `msedge.exe`, `opera.exe`, `chromium.exe`
- Kill them manually
- Try again

---

## 🛠️ Advanced Troubleshooting

### Reset Cooldown (After Manual Cleanup)
```bash
python check_run_cooldown.py reset
```

This allows you to run immediately without the 5-minute wait.

---

### Check What's Running
```powershell
# Check for browser processes
tasklist | findstr /i "edge chrome firefox brave opera chromium"

# Check for driver processes
tasklist | findstr /i "driver"
```

---

### Manual Process Kill
```powershell
# Kill specific browser
taskkill /F /IM msedge.exe

# Kill specific driver
taskkill /F /IM msedgedriver.exe

# Kill all (nuclear option)
taskkill /F /IM msedge.exe
taskkill /F /IM opera.exe
taskkill /F /IM chromium.exe
taskkill /F /IM msedgedriver.exe
taskkill /F /IM operadriver.exe
taskkill /F /IM chromedriver.exe
```

---

### Check Profile Locks
Profile directories (check for lock files):
```
%LOCALAPPDATA%\Microsoft\Edge\User Data Automation
%LOCALAPPDATA%\Microsoft\Edge Dev\User Data Automation
%LOCALAPPDATA%\Opera Software\Opera Stable Automation
%LOCALAPPDATA%\Opera Software\Opera GX Stable Automation
%LOCALAPPDATA%\Chromium\User Data Automation
```

Lock files to look for:
- `SingletonLock`
- `SingletonSocket`
- `SingletonCookie`
- `LOCK`

**Delete these if found** (only when browser is NOT running)

---

## 🔍 Technical Details

### What the Cleanup Does

**File**: `cleanup_browser_processes.py`

1. **Kill Processes**:
   ```python
   taskkill /F /IM msedge.exe
   taskkill /F /IM chrome.exe
   taskkill /F /IM firefox.exe
   taskkill /F /IM brave.exe
   taskkill /F /IM opera.exe
   taskkill /F /IM chromium.exe
   taskkill /F /IM msedgedriver.exe
   taskkill /F /IM chromedriver.exe
   taskkill /F /IM geckodriver.exe
   taskkill /F /IM operadriver.exe
   ```

2. **Unlock Profiles**:
   - Scans all automation profile directories
   - Removes lock files (SingletonLock, etc.)
   - Handles permission errors gracefully

3. **Wait & Verify**:
   - Waits 3 seconds for termination
   - Verifies processes are gone
   - Reports cleanup summary

---

### Why Browsers Close on Repeat Runs

**Root causes**:

1. **Profile Corruption**
   - Browser crashes leave lock files
   - Next run can't open profile → instant close

2. **Driver Process Buildup**
   - Each run spawns driver process (operadriver.exe)
   - Old processes don't always quit
   - 3rd run may have 2 zombie processes interfering

3. **Automation Detection**
   - Running same browser 3x in 5 minutes looks suspicious
   - Browser self-protects by closing
   - Microsoft Rewards may flag account

4. **Incomplete Quit**
   - driver.quit() sometimes fails silently
   - Browser window closes but process stays running
   - Profile remains locked

---

### How the Fix Works

**Before** (Old behavior):
```
Run 1: ✅ Works (clean state)
Run 2: ⚠️ Works (some locks)
Run 3: ❌ Fails (profile locked, process conflicts)
```

**After** (New behavior):
```
Run 1: ✅ Auto-cleanup → Works
Run 2: ⏸️ Cooldown warning → User waits → ✅ Works
Run 3: ✅ Auto-cleanup → Works
```

Every run now:
1. Kills old processes
2. Unlocks profiles
3. Checks cooldown
4. Starts fresh

---

## 📊 Cooldown Benefits

| Scenario | Without Cooldown | With Cooldown |
|----------|------------------|---------------|
| Testing (3 rapid runs) | ❌ Browsers close on run 3 | ✅ Warns, then works |
| Daily automation | ✅ Works fine | ✅ Works fine |
| Debugging (10+ runs/hour) | ❌ Multiple failures | ⚠️ Warnings, but stable |
| Profile locks | ❌ Frequent | ✅ Rare |

---

## 🎯 Best Practices

### For Testing
1. Run once → Check results
2. **Wait 5 minutes** → Run again
3. Or run cleanup → Immediate retry OK

### For Daily Use
1. Schedule once per day (no cooldown issues)
2. Let script auto-cleanup
3. No manual intervention needed

### For Debugging
1. Run cleanup first: `CLEANUP_BROWSERS.bat`
2. Make code changes
3. Test with cooldown override (type `yes`)
4. After 3-5 tests, wait 5 minutes

### If Stuck in a Loop
1. Close all browser windows manually
2. Run `CLEANUP_BROWSERS.bat`
3. Check Task Manager for stuck processes
4. Reset cooldown: `python check_run_cooldown.py reset`
5. Try again

---

## 🚨 Warning Signs

### Profile Lock Detected
```
⚠ OPERA: SingletonLock is still in use (process running)
```
**Solution**: Run cleanup, wait 30 seconds, try again

### Process Won't Die
```
⚠ Timeout killing opera.exe
```
**Solution**: Manual kill in Task Manager, then cleanup

### Rapid Run Warning
```
⚠ WARNING: RAPID RE-RUN DETECTED!
```
**Solution**: Wait 5 minutes (BEST) or run cleanup

### Browser Closes Immediately
**Symptom**: Browser opens then closes in 2-3 seconds

**Causes**:
- Profile locked from previous run
- Driver process conflict
- Automation detected

**Solution**:
```batch
1. CLEANUP_BROWSERS.bat
2. Wait 30 seconds
3. Try again
```

---

## 📁 Files Reference

| File | Purpose |
|------|---------|
| `cleanup_browser_processes.py` | Kill processes & unlock profiles |
| `check_run_cooldown.py` | Detect rapid re-runs |
| `CLEANUP_BROWSERS.bat` | One-click manual cleanup |
| `run_all_browsers_parallel.py` | Main script (now with auto-cleanup) |
| `search_trending_edge.py` | Browser drivers (now with force-kill) |
| `.last_run_timestamp` | Tracks cooldown (auto-created) |

---

## ✅ Verification

After implementing this fix, you should see:

**Run 1**:
```
✓ First run detected - no cooldown needed
✓ System clean - no lingering processes or locks
[EDGE] Starting 30 searches...
```

**Run 2 (< 5 min later)**:
```
⚠ WARNING: RAPID RE-RUN DETECTED!
   Wait: 3.2 more minutes
⚠ Continue anyway? (yes/no):
```

**Run 2 (> 5 min later)**:
```
✓ Cooldown passed (6.5 minutes since last run)
✓ Cleaned up 2 lingering processes
[EDGE] Starting 30 searches...
```

---

## 📞 Still Having Issues?

If browsers still close after this fix:

1. **Check account status**
   - Is your Microsoft account banned/flagged?
   - Try logging into Bing manually

2. **Verify Python environment**
   ```bash
   python --version  # Should be 3.7+
   pip list | findstr selenium  # Should be 4.0+
   ```

3. **Check browser versions**
   - Update all browsers to latest version
   - Restart computer after updates

4. **Test one browser at a time**
   ```bash
   python search_trending_edge.py edge
   # If edge works, test others individually
   ```

5. **Check antivirus/firewall**
   - Disable temporarily
   - Add exception for Python/browsers

---

## 🎉 Summary

**Problem**: Browsers close after 2-3 rapid test runs
**Cause**: Profile locks + lingering processes + automation detection
**Solution**: Auto-cleanup + cooldown detection + force-kill

**Result**: 
- ✅ No more mysterious closures
- ✅ Stable repeated runs
- ✅ Automatic prevention
- ✅ Manual override available

**Files Added**:
1. `cleanup_browser_processes.py` - Process killer & profile unlocker
2. `check_run_cooldown.py` - Rapid run detector
3. `CLEANUP_BROWSERS.bat` - One-click cleanup
4. `BROWSER_CLOSING_FIX.md` - This documentation

---

**Author**: H1M  
**Date**: January 2025  
**Tested On**: Windows 11, Python 3.13, Selenium 4.39  
**Browsers**: Edge, Chrome, Firefox, Brave, Opera, Edge Dev, Opera GX, Chromium
