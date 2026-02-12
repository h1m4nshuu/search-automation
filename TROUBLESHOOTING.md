# Troubleshooting Guide

**Detailed debugging steps for common and uncommon issues.**

---

## Quick Diagnostics

Run these commands to quickly diagnose issues:

```cmd
REM Check Python version
python --version

REM Check if in correct directory
cd

REM Check virtual environment
where python

REM Check installed packages
pip list

REM Check browser detection
python -c "import os; print('Edge:', os.path.exists(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'))"
```

---

## Browser-Specific Debugging

### Edge Issues

**Check Edge installation**:
```cmd
dir "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
```

**Check EdgeDriver**:
```cmd
.venv\Scripts\python.exe -c "from webdriver_manager.microsoft import EdgeChromiumDriverManager; print(EdgeChromiumDriverManager().install())"
```

**Test Edge standalone**:
```cmd
.venv\Scripts\python.exe search_trending_edge.py edge
```

**Common Edge errors**:

1. **"EdgeDriver not found"**
   - Solution: `pip install --upgrade webdriver-manager`
   - Manual download: https://developer.microsoft.com/microsoft-edge/tools/webdriver/

2. **"Edge session not created"**
   - Close all Edge windows
   - Restart computer
   - Run as Administrator

---

### Chrome Issues

**Check Chrome installation**:
```cmd
dir "C:\Program Files\Google\Chrome\Application\chrome.exe"
```

**Test Chrome standalone**:
```cmd
.venv\Scripts\python.exe search_trending_edge.py chrome
```

**Clear Chrome profile** (if persistent login fails):
```cmd
rmdir /s /q "%LOCALAPPDATA%\Google\Chrome\User Data Automation"
```

**Common Chrome errors**:

1. **"Chrome failed to start"**
   - Update Chrome: chrome://settings/help
   - Disable Chrome extensions
   - Check antivirus isn't blocking

2. **"ChromeDriver version mismatch"**
   ```cmd
   pip uninstall webdriver-manager
   pip install webdriver-manager
   rmdir /s /q "%USERPROFILE%\.wdm"
   ```

---

### Firefox Issues

**Check Firefox installation**:
```cmd
dir "C:\Program Files\Mozilla Firefox\firefox.exe"
```

**Test Firefox standalone**:
```cmd
.venv\Scripts\python.exe search_trending_edge.py firefox
```

**Clear Firefox profile**:
```cmd
rmdir /s /q "%LOCALAPPDATA%\Mozilla\Firefox\Profiles\Automation"
```

**Common Firefox errors**:

1. **"GeckoDriver not found"**
   ```cmd
   pip install --upgrade webdriver-manager
   ```

2. **"Firefox is already running"**
   - Open Task Manager
   - End all firefox.exe processes
   - Run script again

3. **"Profile is locked"**
   - Close Firefox
   - Delete: `%LOCALAPPDATA%\Mozilla\Firefox\Profiles\Automation\lock`

---

### Brave Issues

**Check Brave installation**:
```cmd
dir "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
```

**Test Brave standalone**:
```cmd
.venv\Scripts\python.exe search_trending_edge.py brave
```

**Common Brave errors**:

1. **"Brave browser not found"**
   - Reinstall Brave: https://brave.com/download/
   - Install to default location

2. **"ChromeDriver incompatible with Brave"**
   - Update Brave: brave://settings/help
   - Clear driver cache: `rmdir /s /q "%USERPROFILE%\.wdm"`

---

### Opera Issues

**Check Opera installation**:
```cmd
dir "%LOCALAPPDATA%\Programs\Opera\opera.exe"
```

**Test Opera standalone**:
```cmd
.venv\Scripts\python.exe search_trending_edge.py opera
```

**Verify Opera version**:
1. Open Opera manually
2. Go to: opera://about
3. Note version (e.g., 143.0.7499.194)

**Common Opera errors**:

1. **"Opera closes automatically"**
   - ✅ FIXED in latest version
   - Verify you're using latest script
   - Update Opera to latest version

2. **"ChromeDriver version mismatch"**
   - ✅ AUTO-FIXED in script
   - Script auto-downloads matching ChromeDriver
   - If fails, clear cache: `rmdir /s /q "%USERPROFILE%\.wdm"`

3. **"Opera opens new tabs for each search"**
   - ✅ FIXED in latest version
   - Update script to latest version
   - Restart Opera

**Manual ChromeDriver installation for Opera**:
```cmd
REM Find your Opera version first (e.g., 143)
.venv\Scripts\python.exe -c "from webdriver_manager.chrome import ChromeDriverManager; print(ChromeDriverManager(driver_version='143').install())"
```

---

### Opera GX Issues

**Check Opera GX installation**:
```cmd
dir "%LOCALAPPDATA%\Programs\Opera GX\opera.exe"
```

**Test Opera GX standalone**:
```cmd
.venv\Scripts\python.exe search_trending_edge.py operagx
```

**Common Opera GX errors**:

1. **Same as Opera** - All Opera solutions apply to Opera GX
2. **"Opera GX not found"** - Install from: https://www.opera.com/gx

---

### Edge Dev Issues

**Check Edge Dev installation**:
```cmd
dir "C:\Program Files (x86)\Microsoft\Edge Dev\Application\msedge.exe"
```

**Test Edge Dev standalone**:
```cmd
.venv\Scripts\python.exe search_trending_edge.py edgedev
```

**Clear Edge Dev profile** (if syncing with Edge):
```powershell
.\CLEAR_EDGEDEV_PROFILE.ps1
```

**OR manually**:
```cmd
rmdir /s /q "%LOCALAPPDATA%\Microsoft\EdgeDevAutomation"
```

**Common Edge Dev errors**:

1. **"Edge Dev syncs with Edge stable"**
   - ✅ FIXED in latest version
   - Clear profile using script above
   - Sign in again with different account

2. **"Edge Dev not found"**
   - Install from: https://www.microsoft.com/edge/download/insider
   - Select "Dev Channel"

---

### Chromium Issues

**Check Chromium installation**:
```cmd
dir "%LOCALAPPDATA%\Chromium\Application\chrome.exe"
```

**Test Chromium standalone**:
```cmd
.venv\Scripts\python.exe search_trending_edge.py chromium
```

**Install Chromium** (if missing):
1. Download: https://download-chromium.appspot.com/
2. Extract to: `%LOCALAPPDATA%\Chromium\Application\`
3. Verify chrome.exe exists in that folder

**Common Chromium errors**:

1. **"Chromium browser not found"**
   - Install to correct location (see above)
   - Or update path in `search_trending_edge.py`

---

## Python Environment Issues

### Virtual Environment Not Activating

**Symptom**: `(.venv)` doesn't appear in command prompt

**Solution**:
```cmd
cd "C:\Users\%USERNAME%\Desktop\edge-search"
.venv\Scripts\activate.bat
```

**If activation fails**:
```cmd
REM Recreate virtual environment
rmdir /s /q .venv
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

---

### Wrong Python Version Running

**Check current Python**:
```cmd
where python
python --version
```

**Should show**: `.venv\Scripts\python.exe` and `Python 3.x`

**If wrong Python**:
```cmd
REM Force use venv Python
.venv\Scripts\python.exe run_all_browsers_parallel.py
```

**Set venv as default** (in current session):
```cmd
set PATH=C:\Users\%USERNAME%\Desktop\edge-search\.venv\Scripts;%PATH%
python --version
```

---

### Pip Installing to Wrong Location

**Problem**: `pip install` installs to global Python, not venv

**Solution**:
```cmd
REM Always use explicit path
.venv\Scripts\python.exe -m pip install -r requirements.txt

REM Verify installation location
.venv\Scripts\python.exe -m pip list
```

---

## Execution Issues

### Script Starts But No Browsers Open

**Check script output**:
- Does it say "Found [Browser] at: ..."?
- Or says "Browser not found"?

**Debug browser detection**:
```cmd
.venv\Scripts\python.exe -c "from search_trending_edge import build_browser_driver; build_browser_driver('edge')"
```

**If no errors but no browser**:
1. Check Task Manager for browser processes
2. Try running as Administrator
3. Disable antivirus temporarily
4. Check Windows Event Viewer for errors

---

### Browsers Open But Searches Don't Start

**Possible causes**:

1. **Not signed into Microsoft account**
   - Sign in manually in each browser
   - Check "Stay signed in"
   - Wait for script to continue

2. **Bing.com not loading**
   - Check internet connection
   - Try opening Bing manually
   - Check firewall/proxy settings

3. **Search box not found**
   - Wait longer for page load
   - Check Bing isn't showing CAPTCHA
   - Try manually on Bing to verify account

**Debug search execution**:
```cmd
.venv\Scripts\python.exe search_trending_edge.py edge
```
Watch the browser - where does it stop?

---

### "Move target out of bounds" Error

**Example**:
```
Message: move target out of bounds
```

**Solution**: ✅ FIXED in latest version

**If still occurring**:
1. Update script: `git pull` or re-download
2. Don't minimize browser windows
3. Ensure browser window is large enough (1200x800+)

**Manual fix** (temporary):
Edit `search_trending_edge.py`, find `human_click` function and add:
```python
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
time.sleep(0.5)
```

---

### "Session not created" or "Browser failed to start"

**Full error example**:
```
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 143
```

**Solution**:

1. **Update webdriver-manager**:
   ```cmd
   pip install --upgrade webdriver-manager
   ```

2. **Clear driver cache**:
   ```cmd
   rmdir /s /q "%USERPROFILE%\.wdm"
   ```

3. **Update browser**:
   - Open browser manually
   - Go to Settings → About
   - Let it update
   - Restart browser

4. **Reinstall selenium**:
   ```cmd
   pip uninstall selenium
   pip install selenium==4.39.0
   ```

---

## Network Issues

### "Connection refused" or "timeout"

**Causes**:
- No internet connection
- Firewall blocking
- Proxy misconfiguration

**Check connectivity**:
```cmd
ping bing.com
curl https://www.bing.com
```

**Check firewall**:
1. Windows Defender Firewall → Allow an app
2. Add Python: `.venv\Scripts\python.exe`
3. Allow both Private and Public networks

**If behind proxy**:
Edit `search_trending_edge.py` and add proxy settings:
```python
options.add_argument('--proxy-server=http://proxy.example.com:8080')
```

---

### "SSL Certificate verification failed"

**Solution**:
```cmd
pip install --upgrade certifi
pip install --upgrade requests
```

**Temporary workaround** (not recommended):
```cmd
set PYTHONHTTPSVERIFY=0
```

---

## Performance Issues

### High CPU Usage

**Normal**: 8 browsers = high CPU usage

**Reduce CPU usage**:
1. Run fewer browsers:
   ```python
   browsers = ['edge', 'chrome', 'firefox', 'brave']  # Only 4
   ```

2. Close unnecessary programs
3. Upgrade CPU (if <4 cores)

**Check CPU usage**:
- Open Task Manager
- Sort by CPU
- Check which browser is using most

---

### High RAM Usage

**Normal**: 8 browsers = ~4-6 GB RAM

**Reduce RAM usage**:
1. Close unused programs
2. Restart computer before running
3. Run browsers sequentially (slower but less RAM):
   ```cmd
   for %b in (edge chrome firefox brave) do .venv\Scripts\python.exe search_trending_edge.py %b
   ```

**Check RAM usage**:
- Task Manager → Performance → Memory
- Should have 2GB+ free while running

---

### Script Runs Slowly

**Expected times**:
- Single browser: 8-10 minutes (30 searches × 15-20 sec each)
- 8 browsers parallel: 15-20 minutes

**If slower**:
1. Check internet speed: https://fast.com/
2. Reduce delays (see FAQ Q22)
3. Check antivirus isn't scanning browsers
4. Close bandwidth-heavy programs

---

## Microsoft Rewards Issues

### Points Not Counting

**Verify**:
1. Go to: https://rewards.microsoft.com/
2. Click "Daily activities"
3. Check "PC search" progress

**Diagnostic search**:
1. Open Edge manually
2. Sign in to Microsoft account
3. Search "test" on Bing
4. Check if rewards counter increases

**If manual search doesn't count**:
- Account may be suspended
- Not eligible in your region
- Need to complete profile setup

**If manual works but script doesn't**:
- Searches too fast (increase delays)
- Automation detected (stop for 7 days)
- Use fewer browsers

---

### Account Suspended

**Symptoms**:
- "This activity is not available"
- Points not counting
- Rewards dashboard shows error

**Recovery**:
1. Stop all automation immediately
2. Wait 7-14 days
3. Complete manual searches daily
4. Contact Microsoft Rewards support
5. Wait for review

**Prevention**:
- Use default delays (don't speed up)
- Run once per day max
- Complete other activities manually
- Don't use multiple accounts from same IP

---

## Advanced Debugging

### Enable Verbose Logging

Add to top of `search_trending_edge.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Check Selenium Version

```cmd
.venv\Scripts\python.exe -c "import selenium; print(selenium.__version__)"
```
Expected: 4.39.0 or higher

### Test WebDriver Manager

```cmd
.venv\Scripts\python.exe -c "from webdriver_manager.chrome import ChromeDriverManager; print(ChromeDriverManager().install())"
```

### Check All Browser Paths

```cmd
.venv\Scripts\python.exe -c "import os; browsers = {'Edge': r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe', 'Chrome': r'C:\Program Files\Google\Chrome\Application\chrome.exe', 'Firefox': r'C:\Program Files\Mozilla Firefox\firefox.exe', 'Brave': r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe', 'Opera': os.path.join(os.environ['LOCALAPPDATA'], 'Programs', 'Opera', 'opera.exe'), 'Opera GX': os.path.join(os.environ['LOCALAPPDATA'], 'Programs', 'Opera GX', 'opera.exe'), 'Edge Dev': r'C:\Program Files (x86)\Microsoft\Edge Dev\Application\msedge.exe', 'Chromium': os.path.join(os.environ['LOCALAPPDATA'], 'Chromium', 'Application', 'chrome.exe')}; [print(f'{name}: {'Found' if os.path.exists(path) else 'NOT FOUND'}') for name, path in browsers.items()]"
```

---

## Last Resort Solutions

### Complete Reinstall

```cmd
REM Backup profiles first (optional)
xcopy "%LOCALAPPDATA%\Google\Chrome\User Data Automation" C:\backup\chrome\ /E /I
xcopy "%LOCALAPPDATA%\Microsoft\Edge\User Data Automation" C:\backup\edge\ /E /I

REM Remove everything
cd "C:\Users\%USERNAME%\Desktop\edge-search"
rmdir /s /q .venv
rmdir /s /q __pycache__

REM Reinstall
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

REM Clear all caches
rmdir /s /q "%USERPROFILE%\.wdm"
rmdir /s /q "%LOCALAPPDATA%\pip\cache"

REM Test
.venv\Scripts\python.exe run_all_browsers_parallel.py
```

### Reset All Browser Profiles

**⚠️ Warning**: You'll need to sign in again

```cmd
rmdir /s /q "%LOCALAPPDATA%\Microsoft\Edge\User Data Automation"
rmdir /s /q "%LOCALAPPDATA%\Google\Chrome\User Data Automation"
rmdir /s /q "%LOCALAPPDATA%\Mozilla\Firefox\Profiles\Automation"
rmdir /s /q "%LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data Automation"
rmdir /s /q "%LOCALAPPDATA%\Opera Software\Opera Stable Automation"
rmdir /s /q "%LOCALAPPDATA%\Microsoft\EdgeDevAutomation"
rmdir /s /q "%LOCALAPPDATA%\Opera Software\Opera GX Stable Automation"
rmdir /s /q "%LOCALAPPDATA%\Chromium\User Data Automation"
```

---

## Getting Additional Help

If none of these solutions work:

1. **Check GitHub Issues**: https://github.com/YOUR_USERNAME/edge-search/issues
2. **Search closed issues** - someone may have had same problem
3. **Open new issue** with:
   ```
   **Environment:**
   - OS: Windows 10/11
   - Python version: (output of `python --version`)
   - Script version: (latest commit or download date)
   
   **Browser:**
   - Name: Opera
   - Version: (from browser's About page)
   
   **Error:**
   ```
   (paste full error message)
   ```
   
   **What I tried:**
   - Updated webdriver-manager
   - Cleared driver cache
   - etc.
   ```

4. **Include diagnostic output**:
   ```cmd
   .venv\Scripts\python.exe run_all_browsers_parallel.py > debug.txt 2>&1
   ```
   Attach `debug.txt` to your issue

---

**Last Updated**: February 12, 2026  
**Script Version**: 2.0
