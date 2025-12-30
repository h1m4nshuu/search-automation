# 🚀 Search Automation - Multi-Browser Parallel Search Tool

```
    ██╗  ██╗ ██╗ ███╗   ███╗
    ██║  ██║███║ ████╗ ████║
    ███████║╚██║ ██╔████╔██║
    ██╔══██║ ██║ ██║╚██╔╝██║
    ██║  ██║ ██║ ██║ ╚═╝ ██║
    ╚═╝  ╚═╝ ╚═╝ ╚═╝     ╚═╝
```

Automated search tool that performs 30 searches across 4 browsers (Edge, Chrome, Firefox, Brave) **simultaneously** with human-like behavior patterns.

---

## 📋 Table of Contents

- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Troubleshooting](#-troubleshooting)
- [How It Works](#-how-it-works)

---

## ✨ Features

- 🌐 **4 Browser Support**: Edge, Chrome, Firefox, and Brave
- ⚡ **Parallel Execution**: All browsers run simultaneously
- 🎯 **30 Searches Per Browser**: Total 120 searches in one run
- 🤖 **Human-Like Behavior**: 
  - Natural typing with realistic delays
  - Random mouse movements and scrolling
  - Variable wait times between searches
  - Engagement with search results
- 🔄 **Dynamic Topics**: Generates unique search queries each run
- 📊 **Progress Tracking**: Real-time status for each browser

---

## 📦 Prerequisites

### Required Software

1. **Python 3.7 or higher**
   - Download: https://www.python.org/downloads/
   - Make sure to check "Add Python to PATH" during installation

2. **Browsers** (Install at least one, all four recommended):
   - **Microsoft Edge**: https://www.microsoft.com/edge
   - **Google Chrome**: https://www.google.com/chrome/
   - **Mozilla Firefox**: https://www.mozilla.org/firefox/
   - **Brave Browser**: https://brave.com/download/

3. **Git** (for cloning the repository):
   - Download: https://git-scm.com/downloads

---

## 🛠️ Installation

### Step 1: Clone the Repository

Open **PowerShell** or **Command Prompt** and run:

```powershell
git clone https://github.com/YOUR_USERNAME/search-automation.git
cd search-automation
```

### Step 2: Create Virtual Environment

```powershell
python -m venv .venv
```

### Step 3: Activate Virtual Environment

**On Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

### Step 4: Install Dependencies

```powershell
pip install -r requirements.txt
```

---

## 🚀 Usage

### Quick Start (Windows PowerShell)

Simply run this **single command**:

```powershell
& ".\run_parallel.ps1"
```

### Alternative: Direct Python Command

```powershell
& ".\.venv\Scripts\python.exe" "run_all_browsers_parallel.py"
```

### For macOS/Linux

```bash
source .venv/bin/activate
python run_all_browsers_parallel.py
```

---

## 📖 Step-by-Step Usage Guide

### For Windows Users:

1. **Open PowerShell**
   - Press `Windows Key + X`
   - Select "Windows PowerShell" or "Terminal"

2. **Navigate to the project folder**
   ```powershell
   cd path\to\search-automation
   ```

3. **Run the automation**
   ```powershell
   & ".\run_parallel.ps1"
   ```

4. **What happens next:**
   - Script generates 120+ unique search topics
   - Launches all 4 browsers simultaneously
   - Each browser performs 30 searches with 10-second intervals
   - Shows real-time progress for each browser
   - Displays summary when complete

### Expected Output:

```
======================================================================
    ██╗  ██╗ ██╗ ███╗   ███╗
    ██║  ██║███║ ████╗ ████║
    ███████║╚██║ ██╔████╔██║
    ██╔══██║ ██║ ██║╚██╔╝██║
    ██║  ██║ ██║ ██║ ╚═╝ ██║
    ╚═╝  ╚═╝ ╚═╝ ╚═╝     ╚═╝
======================================================================
🌐 PARALLEL MULTI-BROWSER SEARCH AUTOMATION
======================================================================
Configuration:
  - Browsers: Edge, Chrome, Firefox, Brave
  - Searches per browser: 30
  - Total searches: 120
  - Execution: PARALLEL (all browsers at once)
======================================================================

📝 Generating search topics...
✅ Generated 120 unique topics

🔥 LAUNCHING ALL BROWSERS IN PARALLEL...
🚀 [EDGE] Starting 30 searches...
🚀 [CHROME] Starting 30 searches...
🚀 [FIREFOX] Starting 30 searches...
🚀 [BRAVE] Starting 30 searches...

⏳ Waiting for all 4 browsers to complete...
```

---

## ⚙️ Configuration

### Customize Search Count

Edit `run_all_browsers_parallel.py` and modify:

```python
TOPIC_COUNT = 30  # Change to your desired number
```

### Adjust Wait Time Between Searches

Edit `run_all_browsers_parallel.py`:

```python
MIN_WAIT = 10  # Minimum seconds between searches
MAX_WAIT = 10  # Maximum seconds between searches
```

### Run Specific Browsers Only

Edit the `browsers` list in `run_all_browsers_parallel.py`:

```python
# Run only Edge and Chrome
browsers = ['edge', 'chrome']

# Run only Firefox and Brave
browsers = ['firefox', 'brave']
```

---

## 🔧 Troubleshooting

### Issue: "Execution Policy" Error on Windows

**Error:**
```
run_parallel.ps1 cannot be loaded because running scripts is disabled
```

**Solution:**
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then run the script again.

---

### Issue: Browser Driver Not Found

**Error:**
```
Could not initialize EdgeDriver/ChromeDriver/GeckoDriver
```

**Solution:**

1. **Make sure the browser is installed** at its default location
2. **Update webdriver-manager:**
   ```powershell
   pip install --upgrade webdriver-manager
   ```
3. **Manual driver installation** (if auto-download fails):
   - **Edge**: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
   - **Chrome**: https://chromedriver.chromium.org/
   - **Firefox**: https://github.com/mozilla/geckodriver/releases

---

### Issue: Multiple Browser Instances Open

**Problem:** Old browser windows from previous runs

**Solution:**
```powershell
# Close all browser instances
Get-Process edge,chrome,firefox,brave -ErrorAction SilentlyContinue | Stop-Process -Force
```

Then run the script again.

---

### Issue: Virtual Environment Not Found

**Error:**
```
The term '.venv\Scripts\python.exe' is not recognized
```

**Solution:**

Recreate the virtual environment:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

### Issue: Python Not Found

**Error:**
```
'python' is not recognized as an internal or external command
```

**Solution:**

1. Install Python from https://www.python.org/downloads/
2. During installation, check "Add Python to PATH"
3. Restart PowerShell/Terminal
4. Verify: `python --version`

---

## 🧠 How It Works

### Architecture

```
run_parallel.ps1 (Quick launcher)
    ↓
run_all_browsers_parallel.py (Main orchestrator)
    ↓
search_trending_edge.py (Browser automation engine)
    ↓
Threading (Parallel execution)
    ↓
[Edge] [Chrome] [Firefox] [Brave]
  30      30        30        30    searches
```

### Human-Like Behavior Features

1. **Variable Typing Speed**
   - Random delays between keystrokes (50-150ms)
   - Occasionally makes "mistakes" and corrects them

2. **Natural Mouse Movement**
   - Smooth cursor movements
   - Random hover over search results
   - Clicks on various elements

3. **Realistic Scrolling**
   - Variable scroll amounts (100-300px)
   - Pauses while scrolling (800-2000ms)
   - Sometimes scrolls back up
   - 30% chance to "read" content

4. **Wait Time Variation**
   - 10% chance of longer pauses (simulating distraction)
   - Random wait times between actions
   - Progressive slowdown over time

### Search Topic Generation

Topics are generated using:
- **PyTrends** (when available): Real-time trending searches
- **Dynamic Generation**: Category-based topics with timestamps
- **Random Variations**: Adds "2025", "news", "today", etc.

Example topics:
- "AI news today"
- "best programming languages 2025"
- "weather update minute 45"
- "latest tech trends"

---

## 📁 Project Structure

```
search-automation/
│
├── run_parallel.ps1                    # Quick launch script (Windows)
├── run_all_browsers_parallel.py       # Main parallel execution script
├── search_trending_edge.py            # Core automation engine
├── requirements.txt                   # Python dependencies
├── README.md                          # This file
│
├── .venv/                             # Virtual environment (created during setup)
└── .git/                              # Git repository data
```

---

## 🔐 Privacy & Safety

- ✅ All searches are performed on **Bing**
- ✅ No personal data is collected or transmitted
- ✅ Human-like behavior prevents detection
- ✅ Random topics ensure variety
- ⚠️ Ensure you're logged into your Microsoft account for rewards

---

## 📝 Requirements File

The `requirements.txt` includes:

```
selenium
webdriver-manager
pytrends
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

---

## 📜 License

This project is open source and available under the MIT License.

---

## 💡 Tips for Best Results

1. **Login First**: Sign into your Microsoft account in each browser before running
2. **Stable Internet**: Ensure good internet connection
3. **Close Duplicates**: Close any open browser instances before starting
4. **Run Regularly**: Works best when run at different times
5. **Check Results**: Monitor the console output for any errors

---

## 🎯 Use Cases

- **Microsoft Rewards**: Automate daily search quota
- **Testing**: Test search functionality across browsers
- **SEO Research**: Analyze search result patterns
- **Browser Comparison**: Compare search experiences

---

## ⚡ Performance

- **Total Time**: ~5-10 minutes (all browsers parallel)
- **Total Searches**: 120 (30 per browser)
- **CPU Usage**: Moderate (4 browsers running)
- **Memory Usage**: ~500MB-1GB total

---

## 📞 Support

If you encounter any issues:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Ensure all prerequisites are installed
3. Verify browser versions are up-to-date
4. Check that drivers are compatible

---

## 🌟 Acknowledgments

Built with:
- [Selenium](https://www.selenium.dev/) - Browser automation
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager) - Automatic driver management
- [PyTrends](https://github.com/GeneralMills/pytrends) - Google Trends data

---

Made with ❤️ by H1M

**⭐ Star this repo if you find it useful!**
