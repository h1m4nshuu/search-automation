# 8-Browser Parallel Search Setup

## Supported Browsers

The script now supports **8 browsers** running in parallel:

### Currently Supported (Original 4)
1. **Microsoft Edge** - Default Windows browser
2. **Google Chrome** - Popular Chromium-based browser
3. **Mozilla Firefox** - Popular Gecko-based browser
4. **Brave Browser** - Privacy-focused Chromium browser

### Newly Added (4 More)
5. **Opera** - Feature-rich Chromium-based browser
6. **Vivaldi** - Customizable Chromium-based browser
7. **Opera GX** - Gaming-focused variant of Opera
8. **Chromium** - Open-source base for Chrome

## Installation Requirements

### Install Browsers

**Opera:**
- Download from: https://www.opera.com/
- Default install location: `C:\Users\<user>\AppData\Local\Programs\Opera`

**Vivaldi:**
- Download from: https://vivaldi.com/
- Default install location: `C:\Users\<user>\AppData\Local\Vivaldi`

**Opera GX:**
- Download from: https://www.opera.com/gx
- Default install location: `C:\Users\<user>\AppData\Local\Programs\Opera GX`

**Chromium:**
- Download from: https://www.chromium.org/getting-involved/download-chromium/
- Or: https://download-chromium.appspot.com/
- Default install location: `C:\Users\<user>\AppData\Local\Chromium`

### Python Requirements
No changes needed - all new browsers use ChromeDriver (already installed).

## Usage

### Run All 8 Browsers in Parallel
```powershell
python run_all_browsers_parallel.py
```

This will:
- Launch all 8 browsers simultaneously
- Run 30 searches per browser
- Total: **240 searches** across all browsers

### Run Individual Browser
```powershell
# Original browsers
python search_trending_edge.py edge
python search_trending_edge.py chrome
python search_trending_edge.py firefox
python search_trending_edge.py brave

# New browsers
python search_trending_edge.py opera
python search_trending_edge.py vivaldi
python search_trending_edge.py operagx
python search_trending_edge.py chromium
```

## Configuration

### Modify Search Count
Edit `run_all_browsers_parallel.py`:
```python
TOPIC_COUNT = 30  # Change to desired number
```

### Modify Browser List
Edit `run_all_browsers_parallel.py`:
```python
# Use only specific browsers
browsers = ['edge', 'chrome', 'opera', 'vivaldi']  # 4 browsers
browsers = ['edge', 'chrome', 'firefox', 'brave', 'opera', 'vivaldi']  # 6 browsers
browsers = ['edge', 'chrome', 'firefox', 'brave', 'opera', 'vivaldi', 'operagx', 'chromium']  # All 8
```

## Browser Detection

The script automatically detects installed browsers:
- ✅ If browser is found: Script will use it
- ❌ If browser is not found: Script will show error and skip

## Performance Notes

### System Requirements for 8 Browsers
- **RAM**: 16GB+ recommended (each browser uses ~500MB-1GB)
- **CPU**: 4+ cores recommended
- **Disk**: Ensure sufficient space for browser profiles

### Delay Between Browser Launches
Default: 2 seconds between each browser launch
- Prevents system overload
- Allows proper initialization

Modify in `run_all_browsers_parallel.py`:
```python
time.sleep(2)  # Change to adjust delay
```

## Troubleshooting

### Browser Not Found
If you see "Could not find [Browser] browser":
1. Verify browser is installed
2. Check installation path matches script paths
3. Install from official website

### ChromeDriver Issues
All Chromium-based browsers (Chrome, Brave, Opera, Vivaldi, Opera GX, Chromium) use ChromeDriver.

If you encounter driver issues:
```powershell
pip install --upgrade selenium webdriver-manager
```

### Out of Memory
If running all 8 browsers causes memory issues:
1. Reduce `TOPIC_COUNT` (e.g., from 30 to 15)
2. Run fewer browsers at once
3. Close other applications
4. Increase system RAM

### Browser Profile Conflicts
If browsers fail to launch:
1. Close all browser instances
2. Delete automation profile directories:
   - Edge: `%LOCALAPPDATA%\Microsoft\Edge\User Data Automation`
   - Chrome: `%LOCALAPPDATA%\Google\Chrome\User Data Automation`
   - Brave: `%LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data Automation`
3. Restart script

## Technical Details

### Chromium-Based Browsers
Use ChromeDriver with custom binary paths:
- Opera: `launcher.exe`
- Vivaldi: `vivaldi.exe`
- Opera GX: `launcher.exe`
- Chromium: `chrome.exe`

### Firefox-Based Browsers
Use GeckoDriver:
- Firefox only (no other Firefox variants added)

### Why These 4 Browsers?
1. **Opera** - Popular, Chromium-based, easy to automate
2. **Vivaldi** - Power user favorite, Chromium-based
3. **Opera GX** - Different variant, gaming-focused
4. **Chromium** - Pure open-source base

### Alternative Browsers Considered
- ❌ Tor Browser - Too slow for automation
- ❌ Yandex - Less common, regional
- ❌ Waterfox - Firefox variant, less mainstream
- ❌ Edge Beta/Dev - Could cause conflicts with Edge stable

## Summary

**Before (4 browsers):**
- Edge, Chrome, Firefox, Brave
- 30 searches × 4 = **120 total searches**

**After (8 browsers):**
- Edge, Chrome, Firefox, Brave, Opera, Vivaldi, Opera GX, Chromium
- 30 searches × 8 = **240 total searches**

**Execution Time:**
- ~15 seconds per search
- 30 searches per browser ≈ 7.5 minutes
- All run in parallel ≈ **7.5 minutes total** (instead of 60 minutes sequential)
