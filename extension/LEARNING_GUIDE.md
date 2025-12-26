# 🎓 Extension Learning Guide

## Understanding the Code

This guide explains how each part works so you can modify and learn from it.

---

## 📁 File Structure

```
extension/
├── manifest.json      → Extension blueprint
├── popup.html        → User interface
├── popup.js          → Brain of the extension
├── styles.css        → Makes it pretty
├── background.js     → Background worker
└── icon*.png         → Icons for toolbar
```

---

## 🔧 manifest.json - The Blueprint

```json
{
  "manifest_version": 3,        // Latest version (required)
  "name": "Search Topic Helper", // Shows in browser
  "version": "1.0.0",           // Your version number
  
  "permissions": [
    "tabs",                      // Create/modify tabs
    "storage"                    // Save data persistently
  ],
  
  "action": {
    "default_popup": "popup.html" // What opens when clicked
  },
  
  "background": {
    "service_worker": "background.js" // Runs in background
  }
}
```

**What you can change:**
- `name`: Your extension's name
- `description`: What it does
- Add permissions: `"notifications"`, `"bookmarks"`, etc.
- `version`: Bump when you update

**Learn more:**
- [Manifest V3 Docs](https://developer.chrome.com/docs/extensions/mv3/manifest/)

---

## 🎨 popup.html - The Interface

**Key parts:**

```html
<!-- Header -->
<div class="header">
  <h1>🔍 Search Topic Helper</h1>
</div>

<!-- Stats display -->
<div class="stats">
  <span id="searchCount">0</span>  <!-- Updated by JS -->
</div>

<!-- Buttons -->
<button id="searchBtn">Search</button>  <!-- Triggers JS function -->

<script src="popup.js"></script>  <!-- Links to logic -->
```

**What you can change:**
- Add new sections (`<div>`)
- Add new buttons
- Change text and emojis
- Add input fields
- Add checkboxes for settings

**Try this:**
```html
<!-- Add a custom search input -->
<input type="text" id="customQuery" placeholder="Enter topic...">
<button id="customSearch">Search Custom</button>
```

Then in `popup.js`:
```javascript
document.getElementById('customSearch').addEventListener('click', () => {
  const query = document.getElementById('customQuery').value;
  performSearch(query);
});
```

---

## 💻 popup.js - The Brain

### Key Concepts:

#### 1. **State Management**
```javascript
let state = {
  topics: [],           // List of search topics
  currentIndex: 0,      // Which topic we're on
  searchCount: 0,       // How many searches done
  usedTopics: new Set() // Which topics used
};
```

#### 2. **Storage API**
```javascript
// Save data (persists even after closing browser)
await chrome.storage.local.set({
  topics: state.topics,
  searchCount: state.searchCount
});

// Load data
const data = await chrome.storage.local.get(['topics', 'searchCount']);
state.topics = data.topics || [];
```

#### 3. **Tabs API**
```javascript
// Open new tab
await chrome.tabs.create({ 
  url: 'https://www.bing.com/search?q=...' 
});

// Update current tab
const [tab] = await chrome.tabs.query({ active: true });
await chrome.tabs.update(tab.id, { url: '...' });
```

#### 4. **Event Listeners**
```javascript
// When button clicked
document.getElementById('searchBtn').addEventListener('click', async () => {
  await performSearch(currentTopic);
});
```

### Functions You Can Modify:

#### **generateTopics(count)**
```javascript
function generateTopics(count = 30) {
  const topics = [];
  
  // Add your own categories here!
  const myTopics = [
    "your topic 1",
    "your topic 2"
  ];
  
  // Logic to generate topics
  return topics;
}
```

**Try:** Add your own topic categories!

#### **performSearch(topic)**
```javascript
async function performSearch(topic) {
  // Change search engine here:
  const searchUrl = `https://www.bing.com/search?q=${encodeURIComponent(topic)}`;
  
  // Or use Google:
  // const searchUrl = `https://www.google.com/search?q=${encodeURIComponent(topic)}`;
  
  await chrome.tabs.create({ url: searchUrl });
  
  // Update stats
  state.searchCount++;
  state.usedTopics.add(state.currentIndex);
  
  await saveState();
  updateUI();
}
```

**Try:** 
- Change to different search engine
- Add delay before opening
- Open multiple tabs at once

---

## 🎨 styles.css - The Styling

**Key classes:**

```css
.btn-primary {
  background: #667eea;  /* Purple background */
  color: white;
  padding: 12px 20px;
  border-radius: 6px;
}

.btn-primary:hover {
  background: #5568d3;  /* Darker on hover */
  transform: translateY(-2px);  /* Lift effect */
}
```

**Easy changes:**
- Change colors: `background: #ff0000;` (red)
- Change sizes: `padding: 20px;` (bigger)
- Change fonts: `font-family: 'Comic Sans MS';`
- Add animations: `animation: bounce 1s;`

**Try this (add to styles.css):**
```css
/* Pulse animation for buttons */
@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); }
}

.btn:hover {
  animation: pulse 0.5s infinite;
}
```

---

## 🔄 background.js - Service Worker

Runs in the background, even when popup is closed.

```javascript
// When extension installed
chrome.runtime.onInstalled.addListener((details) => {
  if (details.reason === 'install') {
    // First time install
    console.log('Extension installed!');
  }
});

// Update badge (icon number)
chrome.action.setBadgeText({ text: '5' });
chrome.action.setBadgeBackgroundColor({ color: '#ff0000' });
```

**What you can add:**
1. **Alarms** (scheduled tasks)
```javascript
chrome.alarms.create('dailyReset', { periodInMinutes: 1440 });

chrome.alarms.onAlarm.addListener((alarm) => {
  if (alarm.name === 'dailyReset') {
    // Reset daily count
  }
});
```

2. **Notifications**
```javascript
chrome.notifications.create({
  type: 'basic',
  iconUrl: 'icon48.png',
  title: 'Search Helper',
  message: 'Time for next search!'
});
```

---

## 🚀 Extension Ideas to Try

### Easy (Beginner):
1. **Change colors** - Edit CSS
2. **Add more topics** - Edit topic arrays
3. **Change search engine** - Modify URL in performSearch
4. **Add dark mode** - CSS toggle
5. **Change icon** - Replace PNG files

### Medium (Intermediate):
1. **Add settings page** - Create options.html
2. **Import topics from file** - FileReader API
3. **Add category filters** - Filter topics by category
4. **Statistics page** - Chart daily/weekly searches
5. **Random delay variance** - Add randomness to timers

### Hard (Advanced):
1. **Content script** - Interact with web pages
2. **Context menu** - Right-click "Search this"
3. **Keyboard shortcuts** - `chrome.commands` API
4. **Sync storage** - Sync across devices
5. **Native messaging** - Connect to Python script

---

## 🐛 Debugging Tips

### View Console Logs:

**Popup console:**
1. Open extension
2. Right-click anywhere in popup
3. Click "Inspect"
4. Console tab shows logs

**Background console:**
1. Go to `edge://extensions/`
2. Find your extension
3. Click "service worker"
4. Console opens

### Common Issues:

**"chrome is not defined"**
- You're in wrong context
- Extension APIs only work in extension files

**"Storage is undefined"**
- Add `"storage"` permission to manifest.json

**"Cannot access chrome.tabs"**
- Add `"tabs"` permission to manifest.json

**Changes not showing?**
- Go to `edge://extensions/`
- Click "Reload" button on extension

**Extension won't load?**
- Check manifest.json syntax (JSON validator)
- Check for errors in developer mode

---

## 📚 Learn More APIs

### Useful Chrome Extension APIs:

```javascript
// Tabs
chrome.tabs.create()       // New tab
chrome.tabs.update()       // Modify tab
chrome.tabs.query()        // Find tabs
chrome.tabs.remove()       // Close tab

// Storage
chrome.storage.local.set()     // Save local
chrome.storage.local.get()     // Load local
chrome.storage.sync.set()      // Save (syncs)

// Bookmarks
chrome.bookmarks.create()  // Add bookmark
chrome.bookmarks.search()  // Find bookmarks

// History
chrome.history.search()    // Search history
chrome.history.deleteAll() // Clear history

// Notifications
chrome.notifications.create()  // Show notification

// Windows
chrome.windows.create()    // New window
chrome.windows.update()    // Modify window
```

---

## 🎯 Next Steps

1. **Experiment!** Change things and see what happens
2. **Read docs:** [Chrome Extension Docs](https://developer.chrome.com/docs/extensions/)
3. **Try examples:** Look at open-source extensions
4. **Build something new:** Make your own extension!

---

## 💡 Project Ideas

**Easy projects:**
- Bookmark manager
- Tab organizer
- Color picker tool
- QR code generator
- Unit converter

**Medium projects:**
- Todo list with sync
- Note-taking extension
- Password generator
- Screenshot tool
- Timer/Pomodoro

**Advanced projects:**
- Ad blocker
- Content script injector
- Web scraper dashboard
- Multi-account manager
- Automation suite

---

## 🤝 Need Help?

**Resources:**
- [Chrome Extension Docs](https://developer.chrome.com/docs/extensions/)
- [Edge Extension Docs](https://docs.microsoft.com/microsoft-edge/extensions-chromium/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/chrome-extension)
- [Extension Samples](https://github.com/GoogleChrome/chrome-extensions-samples)

**Debug steps:**
1. Check console for errors
2. Verify permissions in manifest.json
3. Test each function individually
4. Use `console.log()` everywhere!
5. Reload extension after changes

---

**Happy coding! 🚀**

Start small, experiment often, and don't be afraid to break things!
