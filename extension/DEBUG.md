## 🐛 Extension Not Working? Debug Guide

### Quick Fix Steps:

**1. Open Extension Console:**
   - Click the extension icon (purple S)
   - **Right-click anywhere in the popup**
   - Click **"Inspect"**
   - Go to **"Console"** tab
   - Look for RED error messages

**2. Check What Error Shows:**

Common errors and fixes:

**Error: "chrome is not defined"**
- Fix: Reload extension

**Error: "Cannot read property 'checked'"**  
- Fix: HTML element missing, need to verify popup.html

**Error: "getElementById returns null"**
- Fix: Button ID mismatch

**Nothing happens, no errors:**
- Fix: Event listeners not attached

---

### Quick Fix (Try This First):

1. Go to `edge://extensions/`
2. Find "Search Topic Helper"
3. Click **"Remove"**
4. Close Edge completely
5. Reopen Edge
6. Go to `edge://extensions/`
7. Enable Developer mode
8. Click "Load unpacked"
9. Select: `C:\Users\himan\Desktop\edge search\extension`

---

### Test Basic Functionality:

Open console (F12 on popup) and type:
```javascript
// Test if elements exist
console.log(document.getElementById('nextTopic'));
console.log(document.getElementById('searchBtn'));
console.log(document.getElementById('humanSearchBtn'));
```

Should show elements, not null.

---

### If Still Not Working:

Reply with:
1. What error shows in Console (Red text)
2. What happens when you click a button (nothing? error?)
3. Does the popup open at all?
