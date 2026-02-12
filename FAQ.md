# Frequently Asked Questions (FAQ) & Solutions

**Solutions to all recurring problems encountered during setup and daily use.**

---

## Table of Contents
1. [Browser Issues](#browser-issues)
2. [Login & Account Issues](#login--account-issues)
3. [Search Execution Issues](#search-execution-issues)
4. [ChromeDriver & WebDriver Issues](#chromedriver--webdriver-issues)
5. [Python & Environment Issues](#python--environment-issues)
6. [Performance Issues](#performance-issues)
7. [Microsoft Rewards Issues](#microsoft-rewards-issues)

---

## Browser Issues

### Q1: Browsers keep logging out every time I run the script

**Problem**: Selenium launches browsers in temporary/clean state by default.

**Solution**: ✅ **FIXED** - All 8 browsers now use persistent profiles:
- Opera: `%LOCALAPPDATA%\Opera Software\Opera Stable Automation`
- Opera GX: `%LOCALAPPDATA%\Opera Software\Opera GX Stable Automation`
- Chromium: `%LOCALAPPDATA%\Chromium\User Data Automation`
- Edge Dev: `%LOCALAPPDATA%\Microsoft\EdgeDevAutomation\UserData`
- Chrome, Brave, Firefox, Edge: All have persistent profiles

**Action needed**:
1. Run script once
2. Sign in to Microsoft account in each browser
3. All future runs will stay logged in automatically

---

### Q2: Opera and Opera GX close automatically after some time

**Problem**: Opera browsers have aggressive memory/process management.

**Solution**: ✅ **FIXED** - Added stability flags:
```python
--disable-background-timer-throttling
--disable-renderer-backgrounding
--disable-backgrounding-occluded-windows
--disable-ipc-flooding-protection
--disable-hang-monitor
```

**If still happening**:
1. Update Opera/Opera GX to latest version
2. Ensure no antivirus is killing browser processes
3. Check Task Manager for memory issues (need 8GB+ RAM)

---

### Q3: Opera GX opens a new tab for each search instead of searching in same tab

**Problem**: Opera GX's popup handling opens links in new tabs.

**Solution**: ✅ **FIXED** - Script now:
- Detects and closes extra tabs automatically
- Forces searches in main tab using `driver.get()`
- Switches back to main window before each search

**Verify fix**:
- Run script and watch Opera GX
- Should see only 1 tab throughout all 30 searches

---

### Q4: Edge Dev syncs account from Edge stable automatically

**Problem**: Edge Dev shares profile data with Edge by default.

**Solution**: ✅ **FIXED** - Completely isolated Edge Dev:
- Uses separate profile: `%LOCALAPPDATA%\Microsoft\EdgeDevAutomation\UserData`
- Disabled all sync features: `--disable-sync`, `--disable-features=msEdgeSyncEnabled`
- Disabled auto sign-in: `--disable-features=ImplicitSignin,msEdgeAutoSignIn`
- No import from Edge stable

**To reset Edge Dev profile**:
```powershell
.\CLEAR_EDGEDEV_PROFILE.ps1
```
Then sign in again with different account.

---

### Q5: Browser not detected - "Could not find [Browser] browser"

**Problem**: Browser installed in non-standard location.

**Solution**:

**Check browser paths**:
- Edge: `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`
- Chrome: `C:\Program Files\Google\Chrome\Application\chrome.exe`
- Firefox: `C:\Program Files\Mozilla Firefox\firefox.exe`
- Brave: `C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe`
- Opera: `%LOCALAPPDATA%\Programs\Opera\opera.exe`
- Opera GX: `%LOCALAPPDATA%\Programs\Opera GX\opera.exe`
- Edge Dev: `C:\Program Files (x86)\Microsoft\Edge Dev\Application\msedge.exe`
- Chromium: `%LOCALAPPDATA%\Chromium\Application\chrome.exe`

**Manual verification**:
```cmd
dir "C:\Program Files\Google\Chrome\Application\chrome.exe"
```

**If browser is elsewhere**, update path in `search_trending_edge.py`:
```python
# Example for Chrome
chrome_paths = [
    'C:\\Your\\Custom\\Path\\chrome.exe',  # Add your path here
    os.path.join(os.environ.get('PROGRAMFILES', 'C:\\Program Files'), 'Google', 'Chrome', 'Application', 'chrome.exe'),
]
```

---

### Q6: Vivaldi browser crashes or doesn't work

**Problem**: Vivaldi uses custom versioning (7.8.x) incompatible with ChromeDriver.

**Solution**: ✅ **Vivaldi replaced with Edge Dev** (more stable).

**If you must use Vivaldi**:
1. Not recommended due to version incompatibility
2. Consider using Chromium instead (similar features, better compatibility)

---

## Login & Account Issues

### Q7: Microsoft account asks to verify identity every run

**Problem**: Browser fingerprint changes or security challenge.

**Solution**:

1. **Complete verification once** (phone/email code)
2. **Check "Don't ask again on this device"** ✅
3. Wait 24 hours for Microsoft to trust the device
4. Ensure persistent profiles are enabled (see Q1)

**Additional security tips**:
- Don't use VPN while running script
- Run from same IP address consistently
- Complete Microsoft Rewards tasks manually first time
- Wait few seconds between searches (built into script)

---

### Q8: Can I use different Microsoft accounts in each browser?

**Answer**: YES! ✅

**Recommended setup**:
- **Same account**: Works fine, all points go to one account
- **Different accounts**: Each browser maintains separate login
  - Edge: Account A
  - Chrome: Account A or B
  - Firefox: Account C
  - Opera: Account D
  - etc.

**Note**: Edge Dev is completely isolated from Edge, so you can use different accounts there.

---

### Q9: Browser asks to save password every search

**Problem**: Password manager prompts interrupt automation.

**Solution**: Disable password save prompts:

**Chrome/Brave/Opera/Opera GX/Edge/Edge Dev**:
1. Open browser manually
2. Settings → Passwords
3. Uncheck "Offer to save passwords"
4. Uncheck "Auto Sign-in"

**Firefox**:
1. Settings → Privacy & Security
2. Logins and Passwords
3. Uncheck "Ask to save logins and passwords for websites"

**Note**: Script already tries to suppress these, but manual disabling helps.

---

## Search Execution Issues

### Q10: Error "move target out of bounds" - Search gets skipped

**Problem**: Search box is outside visible browser window.

**Solution**: ✅ **FIXED** - Added 4-level fallback:
1. Scroll element into view + mouse movement
2. Direct element.click()
3. JavaScript click()
4. Graceful skip with warning

**Should not skip searches anymore**. If still happening:
1. Update script to latest version
2. Increase window size in code (default: 1200x800)
3. Don't minimize browser windows during run

---

### Q11: Searches are too fast - Microsoft might detect automation

**Problem**: Unnaturally fast searches trigger detection.

**Solution**: ✅ **BUILT-IN** - Script includes:
- Random wait: 10-15 seconds between searches
- Human-like typing speed (100-200ms per character)
- Random scrolling patterns
- Mouse movement simulation
- Random pauses and reading behavior

**Current timing**:
- 30 searches × 15 seconds avg = ~7-8 minutes per browser
- Total time: 15-20 minutes for all 8 browsers

**To increase delays** (if concerned):
Edit `run_all_browsers_parallel.py`:
```python
min_wait=50,  # Change from 10 to 50
max_wait=55,  # Change from 15 to 55
```

---

### Q12: Some searches show "No results found" or fail

**Problem**: Topic generation creates invalid search terms or network issues.

**Solution**: Script uses pytrends for real trending topics.

**If many searches fail**:
1. Check internet connection
2. Verify Bing.com is accessible
3. Check if Microsoft Rewards is blocked in your region
4. Run manual search test: Open browser → Go to Bing → Search "test"

**Verify pytrends is working**:
```cmd
python -c "from pytrends.request import TrendReq; print('OK')"
```
Expected: `OK`

---

### Q13: Browser disconnects mid-search - "Browser session lost"

**Problem**: Browser crashes or user closes window manually.

**Solution**:
- **Don't close browser windows** during script execution
- **Don't use browsers** while script is running
- Ensure enough RAM (8GB minimum, 16GB recommended)

**If browsers crash automatically**:
1. Update browsers to latest version
2. Update graphics drivers
3. Disable browser extensions
4. Check Windows Event Viewer for crash details

---

## ChromeDriver & WebDriver Issues

### Q14: ChromeDriver version mismatch errors

**Example error**:
```
Chrome version 143.0.7449.194 is not compatible with ChromeDriver 144.0.7494.58
```

**Solution**: ✅ **AUTO-FIXED** for Opera/Opera GX - Script automatically:
1. Detects browser version from error message
2. Downloads matching ChromeDriver version
3. Retries connection

**For other browsers**:
- Chrome/Edge: webdriver-manager handles this
- Firefox: GeckoDriver is version-agnostic

**Manual fix if needed**:
```cmd
pip install --upgrade webdriver-manager
```

---

### Q15: "EdgeDriver/ChromeDriver not found in PATH"

**Problem**: WebDriver executable not in system PATH.

**Solution**: ✅ **AUTO-DOWNLOAD** - Script uses webdriver-manager:
```python
EdgeChromiumDriverManager().install()  # Auto-downloads EdgeDriver
ChromeDriverManager().install()        # Auto-downloads ChromeDriver
GeckoDriverManager().install()         # Auto-downloads GeckoDriver
```

**If auto-download fails**:
1. Check internet connection
2. Verify webdriver-manager is installed: `pip list | findstr webdriver`
3. Manual download:
   - EdgeDriver: https://developer.microsoft.com/microsoft-edge/tools/webdriver/
   - ChromeDriver: https://chromedriver.chromium.org/downloads
   - GeckoDriver: https://github.com/mozilla/geckodriver/releases

---

### Q16: Opera/Opera GX - "This version of ChromeDriver only supports Chrome version X"

**Problem**: Opera version doesn't match installed ChromeDriver.

**Solution**: ✅ **AUTO-FIXED** - Script now:
```python
# Extracts Opera version: 143.0.7499.194
# Downloads ChromeDriver version 143
ChromeDriverManager(driver_version=opera_major_version).install()
```

**If still failing**:
1. Update Opera/Opera GX to latest version
2. Clear driver cache:
   ```cmd
   rmdir /s /q "%USERPROFILE%\.wdm"
   ```
3. Run script again (will re-download correct version)

---

## Python & Environment Issues

### Q17: "No module named 'selenium'" or "No module named 'webdriver_manager'"

**Problem**: Dependencies not installed or wrong Python environment.

**Solution**:

**Check if virtual environment is activated**:
```cmd
where python
```
Expected: `C:\Users\...\edge-search\.venv\Scripts\python.exe`

**If not activated**:
```cmd
cd "C:\Users\%USERNAME%\Desktop\edge-search"
.venv\Scripts\activate
pip install -r requirements.txt
```

**Verify installation**:
```cmd
pip list
```
Should show: selenium, webdriver-manager, pytrends

---

### Q18: "Python is not recognized as an internal or external command"

**Problem**: Python not installed or not in PATH.

**Solution**:

**Option 1: Add Python to PATH** (if installed)
1. Search Windows: "Environment Variables"
2. System Properties → Environment Variables
3. Under "System Variables", find "Path"
4. Click Edit → New
5. Add: `C:\Users\YourName\AppData\Local\Programs\Python\Python3xx\`
6. Add: `C:\Users\YourName\AppData\Local\Programs\Python\Python3xx\Scripts\`
7. Click OK
8. **Restart Command Prompt**

**Option 2: Reinstall Python**
1. Download from: https://www.python.org/downloads/
2. Run installer
3. **CHECK** ✅ "Add Python to PATH"
4. Click "Install Now"

---

### Q19: ModuleNotFoundError despite pip install

**Problem**: Multiple Python installations or wrong pip.

**Solution**:

**Use explicit Python path**:
```cmd
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**Verify pip is using correct Python**:
```cmd
.venv\Scripts\python.exe -m pip --version
```
Expected: `pip 24.x from ...\edge-search\.venv\...`

---

### Q20: SyntaxError with Unicode characters

**Example**: `SyntaxError: invalid character '█' (U+2588)`

**Problem**: Python file encoding issue.

**Solution**: ✅ **FIXED** - All files now use:
```python
# -*- coding: utf-8 -*-
```

**If error persists**:
1. Update Python to 3.8+
2. Check file encoding: Should be UTF-8
3. Avoid copying code from sources with special characters

---

## Performance Issues

### Q21: Computer becomes very slow during execution

**Problem**: 8 browsers + searches = high resource usage.

**Solution**:

**System Requirements**:
- 8GB RAM minimum → Upgrade to 16GB recommended
- Close unnecessary programs
- Close browser extensions (may consume resources)

**Reduce browser count**:
Edit `run_all_browsers_parallel.py`:
```python
browsers = ['edge', 'chrome', 'firefox', 'brave']  # Run only 4 browsers
```

**Run browsers sequentially** (slower but less resource-intensive):
```cmd
python search_trending_edge.py edge
python search_trending_edge.py chrome
python search_trending_edge.py firefox
```

---

### Q22: Script takes too long to complete (>30 minutes)

**Problem**: Wait times too long or network delays.

**Solution**:

**Current timing**: ~15-20 minutes for 8 browsers (240 searches)

**Reduce wait times**:
Edit `run_all_browsers_parallel.py`:
```python
min_wait=8,   # Reduce from 10
max_wait=12,  # Reduce from 15
```

**⚠️ Warning**: Too fast may trigger Microsoft detection.

**Recommended**: Keep default 10-15 second delays for safety.

---

### Q23: Browsers consume too much RAM/CPU

**Problem**: Browser processes accumulate memory over time.

**Solution**:

**Built-in**: Script closes browsers after completion.

**If browsers stay open**:
1. Check Task Manager
2. End all browser processes manually
3. Run script again

**Prevent memory leaks**:
- Update browsers to latest version
- Disable unnecessary browser extensions
- Restart computer before important runs

---

## Microsoft Rewards Issues

### Q24: Points not showing up after searches

**Problem**: Microsoft Rewards has verification delays.

**Solution**:

**Normal behavior**:
- Points may take up to 24 hours to appear
- First-time searches may not count (needs verification)
- Daily limit: ~150 searches per account

**Verify searches are counting**:
1. Go to: https://rewards.microsoft.com/
2. Check "Daily activities"
3. Look for "PC search" progress bar

**If no points after 48 hours**:
1. Ensure you're signed into Microsoft account
2. Check if Microsoft Rewards is available in your country
3. Verify account is not suspended
4. Complete profile setup on rewards website

---

### Q25: "This activity is not available" on Microsoft Rewards

**Problem**: Microsoft detected automation or account issue.

**Solution**:

**Prevention**:
- Use realistic delays (default: 10-15 seconds)
- Don't run script multiple times per day
- Manually complete some searches daily
- Don't use VPN

**If flagged**:
1. Stop automation for 7 days
2. Complete manual searches daily
3. Contact Microsoft Rewards support
4. Wait for account review

**Safer approach**:
- Run once per day maximum
- Use only 4 browsers instead of 8
- Increase wait times to 30-60 seconds

---

### Q26: Can I earn more points by running script multiple times per day?

**Answer**: **NO** - Microsoft Rewards has daily limits:
- PC Search: ~150 points per day (~90 searches)
- Running 8 browsers = 240 searches (exceeds limit)
- Extra searches beyond limit = 0 points

**Recommendation**:
- Run once per day
- Some browsers won't earn points (already at limit)
- Consider using only 4-5 browsers

---

### Q27: Are there any risks of account ban?

**Risk assessment**:
- **Low risk** with default settings (human-like behavior)
- **Medium risk** if run multiple times daily
- **High risk** if combined with VPN or suspicious activity

**Mitigation**:
- Use default delays (10-15 seconds)
- Run once per day max
- Don't use multiple accounts from same IP
- Complete other rewards activities manually
- Keep browser profiles (don't clear cookies)

**Microsoft's stance**:
- Automation is against Terms of Service
- Detection methods are improving
- Use at your own risk

---

## Additional Tips

### Q28: How do I update the script to latest version?

**If using Git**:
```cmd
cd "C:\Users\%USERNAME%\Desktop\edge-search"
git pull origin main
```

**If downloaded ZIP**:
1. Download new ZIP from GitHub
2. Extract files
3. Replace all files EXCEPT:
   - `.venv` folder (keep your Python environment)
   - Browser profiles (automatic, no action needed)

---

### Q29: Can I run this on Mac or Linux?

**Answer**: **Windows only** currently.

**Why**: Browser paths, WebDriver management, and scheduled tasks are Windows-specific.

**For Mac/Linux**:
- Would need to modify all browser paths
- Change PowerShell scripts to Bash
- Adjust profile locations
- Test all browsers (not planned currently)

---

### Q30: Script output shows "Browser disconnected! Skipping remaining searches"

**Problem**: Browser closed manually or crashed.

**Solution**:
- Don't close browser windows during execution
- Let script complete automatically
- If browser crashes, check Task Manager for resource usage
- Update browser to latest version

**Prevention**:
- Ensure stable internet connection
- Close resource-heavy programs
- Don't interact with browsers during run

---

## Still Having Issues?

If your problem isn't listed here:

1. Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for detailed debugging
2. Check GitHub Issues: https://github.com/YOUR_USERNAME/edge-search/issues
3. Open new issue with:
   - Exact error message
   - Browser name and version
   - Python version (`python --version`)
   - Windows version
   - What you've tried already

---

**Last Updated**: February 12, 2026  
**Script Version**: 2.0 (8-Browser Support)
