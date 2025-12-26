# 🚀 Quick Installation Guide

## Your Edge Extension is Ready!

All files have been created in: `C:\Users\himan\Desktop\edge search\extension\`

---

## Install in 3 Easy Steps:

### Step 1: Open Edge Extensions
1. Open **Microsoft Edge**
2. Type in address bar: `edge://extensions/`
3. Press Enter

### Step 2: Enable Developer Mode
1. Look for **"Developer mode"** toggle (bottom-left corner)
2. Turn it **ON**

### Step 3: Load Your Extension
1. Click **"Load unpacked"** button (top-left area)
2. Navigate to: `C:\Users\himan\Desktop\edge search\extension`
3. Select the **extension** folder
4. Click **"Select Folder"**

---

## ✅ You're Done!

You should now see:
- "Search Topic Helper" in your extensions list
- A purple icon with "S" in your Edge toolbar

## 🎯 How to Use

1. **Click the extension icon** (S) in your toolbar
2. Click **"Generate New Topics"** to create 30 random search queries
3. **Manual mode**:
   - Click "Search This Topic" to open Bing search
   - Click "Next Topic" to change topics
4. **Semi-Auto mode**:
   - Click "Semi-Auto Mode" to start automated searches
   - It will search with delays (default 50 seconds)
   - Click again to stop

---

## 🎓 What You'll Learn

This extension demonstrates:
- ✅ Manifest V3 (latest extension standard)
- ✅ Popup UI with HTML/CSS/JavaScript
- ✅ Chrome Storage API (save data)
- ✅ Tabs API (open/navigate tabs)
- ✅ Background Service Worker
- ✅ Event handling and state management

---

## 📝 Files Explained

```
extension/
├── manifest.json      → Extension config (name, permissions, etc.)
├── popup.html        → UI that shows when you click icon
├── popup.js          → Main logic (generate topics, handle searches)
├── styles.css        → Pretty styling
├── background.js     → Background tasks (badge updates, etc.)
├── icon16.png        → Small icon
├── icon48.png        → Medium icon
└── icon128.png       → Large icon
```

---

## 🐛 Troubleshooting

### Extension doesn't show up?
- Make sure Developer mode is ON
- Try reloading: click "Reload" button on extension card

### Error loading?
- Check all files are in the extension folder
- Open Developer Tools (F12) and check Console tab

### Searches not working?
- Check if popup blockers are enabled
- Enable "Open in new tab" option in settings

---

## 🔍 Debug Mode

To see what's happening:
1. Go to `edge://extensions/`
2. Find "Search Topic Helper"
3. Click **"Inspect views: popup"** - shows popup console
4. Click **"service worker"** - shows background console

---

## ⚠️ Important Notes

**Educational Purpose Only!**
- This teaches how extensions work
- Automated searching may violate terms of service
- Use responsibly

**Semi-Auto Mode:**
- Still requires YOU to click "start"
- Opens tabs automatically
- You can stop anytime

---

## 🎨 Customize It!

Want to make it yours?

1. **Change colors**: Edit `styles.css`
2. **Add topics**: Edit categories in `popup.js`
3. **Change timing**: Modify delay settings
4. **Better icons**: Replace `icon*.png` files

After changes:
1. Save files
2. Go to `edge://extensions/`
3. Click "Reload" on your extension

---

## 📚 Next Steps

Want to learn more?
- [Edge Extension Docs](https://docs.microsoft.com/microsoft-edge/extensions-chromium/)
- [Chrome Extension Docs](https://developer.chrome.com/docs/extensions/) (Edge uses same APIs)
- Modify this extension to add new features!

---

## 💡 Ideas to Try

1. Add custom topic input
2. Save favorite topics
3. Add statistics/charts
4. Dark mode theme
5. Export search history
6. Import topics from file
7. Category filters

---

**Happy Learning! 🎉**

Any issues? Check the console logs for errors.
