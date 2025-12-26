# Search Topic Helper - Edge Extension

An educational browser extension that demonstrates how Edge extensions work. Helps manage search topics with a user-friendly interface.

## Features

- 📝 **Topic Generator**: Automatically generates diverse search topics
- 🔍 **Quick Search**: Click to search current topic on Bing
- ⏱️ **Timer**: Shows countdown between searches
- 📊 **Progress Tracking**: Tracks daily search count
- ⚡ **Semi-Auto Mode**: Automated search with configurable delays
- 💾 **Export**: Save topics to JSON file

## Installation

### Method 1: Load Unpacked Extension

1. Open Microsoft Edge
2. Navigate to `edge://extensions/`
3. Enable **Developer mode** (toggle in bottom-left)
4. Click **Load unpacked**
5. Select the `extension` folder

### Method 2: Pack and Install

1. In Edge, go to `edge://extensions/`
2. Enable Developer mode
3. Click **Pack extension**
4. Select the `extension` folder
5. Install the generated `.crx` file

## How to Use

1. **Click the extension icon** in Edge toolbar
2. **Generate Topics**: Click "Generate New Topics" to create 30 random topics
3. **Manual Mode**:
   - Click "Next Topic" to cycle through topics
   - Click "Search This Topic" to open Bing search
4. **Semi-Auto Mode**:
   - Click "Semi-Auto Mode" to start automated searches
   - Extension will search with delays between each one
   - Click again to stop

## Configuration

- **Open in new tab**: Toggle to open searches in new tabs
- **Delay**: Set seconds between searches (10-120 seconds)
- **Reset Count**: Clear search counter and history

## Extension Files

```
extension/
├── manifest.json       # Extension configuration
├── popup.html         # UI interface
├── popup.js           # Main logic
├── background.js      # Background service worker
├── styles.css         # Styling
└── README.md          # Documentation
```

## How It Works

### Manifest V3
Uses the latest Manifest V3 format required by Edge:
- Service worker for background tasks
- Permissions: `tabs`, `storage`
- Action popup for user interface

### Components

**popup.html**: The UI shown when clicking the extension icon
- Displays current topic
- Shows search count and timer
- Lists all topics with status

**popup.js**: Core functionality
- Generates random topics from 8 categories
- Manages state (storage API)
- Handles search execution
- Timer and auto-mode logic

**background.js**: Service worker
- Handles installation events
- Updates badge count
- Could manage long-running tasks

### Key APIs Used

1. **chrome.storage.local**: Persistent data storage
2. **chrome.tabs**: Create/update browser tabs
3. **chrome.action**: Extension icon and badge

## Educational Notes

### What This Demonstrates

✅ **Extension Architecture**: Manifest, popup, background worker
✅ **Storage API**: Saving/loading data persistently
✅ **Tabs API**: Creating and navigating tabs
✅ **UI Components**: HTML/CSS/JS in extension context
✅ **State Management**: Tracking searches and topics
✅ **User Interaction**: Buttons, forms, checkboxes

### Limitations

⚠️ **No True Automation**: Extensions can't auto-click or fill forms
⚠️ **User Action Required**: Each search needs user interaction (click)
⚠️ **No Selenium**: Can't control browser like Selenium does
⚠️ **Sandboxed**: Limited access to browser internals

### Semi-Auto Mode

The "Semi-Auto Mode" demonstrates:
- Timer-based task scheduling
- Automatic tab creation
- State persistence
- Still requires user to start/stop

## Security & Compliance

⚠️ **Educational Purpose Only**

This extension is for learning how browser extensions work. Using automation for earning rewards or similar purposes may violate terms of service of various platforms.

## Development Tips

### Debug the Extension
1. Go to `edge://extensions/`
2. Find your extension
3. Click **Details**
4. Click **Inspect views: popup.html** to debug popup
5. Check **Service worker** to debug background

### View Console Logs
- **Popup**: Right-click extension → Inspect
- **Background**: Extensions page → Service worker → Inspect

### Make Changes
1. Edit files in `extension/` folder
2. Go to `edge://extensions/`
3. Click **Reload** button on your extension

## Topics Generated

The extension generates topics from categories:
- Technology (AI, ML, blockchain, etc.)
- News & Current Events
- Lifestyle & Health
- Education & Learning
- Entertainment
- Travel
- Shopping
- Health & Wellness

Topics are randomized with modifiers like "latest", "best", "2025", etc.

## Export Feature

Click "Export Topics" to save:
```json
{
  "topics": ["topic1", "topic2", ...],
  "searchCount": 15,
  "date": "2025-12-25T..."
}
```

## License

MIT License - Educational use only

## Warning

⚠️ Automated searches may violate terms of service of search engines and reward programs. Use responsibly and at your own risk.
