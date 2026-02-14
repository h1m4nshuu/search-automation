# 4-Browser Parallel Search Setup

## Supported Browsers

The script now supports **4 browsers** running in parallel:

### Currently Supported
1. **Microsoft Edge** - Default Windows browser
2. **Google Chrome** - Popular Chromium-based browser
3. **Mozilla Firefox** - Popular Gecko-based browser
4. **Brave Browser** - Privacy-focused Chromium browser

## Installation Requirements

### Python Requirements
No changes needed - all browsers use their respective WebDrivers (already installed).

## Usage

### Run All 4 Browsers in Parallel
```powershell
python run_all_browsers_parallel.py
```

This will:
- Launch all 4 browsers in 2 batches
- Run 30 searches per browser
- Total: **120 searches** across all browsers

### Run Individual Browser
```powershell
python search_trending_edge.py edge
python search_trending_edge.py chrome
python search_trending_edge.py firefox
python search_trending_edge.py brave
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
batch1 = ['edge', 'chrome']
batch2 = ['firefox', 'brave']
```

## Browser Detection

The script automatically detects installed browsers:
- ✅ If browser is found: Script will use it
- ❌ If browser is not found: Script will show error and skip

## Performance Notes

### System Requirements for 4 Browsers
- **RAM**: 8GB recommended (each browser uses ~500MB-1GB)
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
If running all 4 browsers causes memory issues:
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
- Chrome: `chrome.exe`
- Brave: `brave.exe`
- Chromium: `chrome.exe`

### Firefox-Based Browsers
Use GeckoDriver:
- Firefox only

### Edge Browser
Uses EdgeDriver:
- Microsoft Edge: `msedge.exe`

## Summary

**Current Setup (4 browsers):**
- Edge, Chrome, Firefox, Brave
- 30 searches × 4 = **120 total searches**

**Execution Time:**
- ~15 seconds per search
- 30 searches per browser ≈ 7.5 minutes
- All run in parallel (2 batches) ≈ **7.5 minutes total**
