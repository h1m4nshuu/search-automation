// Background service worker for the extension

// Listen for extension install/update
chrome.runtime.onInstalled.addListener((details) => {
  if (details.reason === 'install') {
    console.log('Search Topic Helper installed!');
    
    // Initialize storage with default values
    chrome.storage.local.set({
      topics: [],
      currentIndex: 0,
      searchCount: 0,
      usedTopics: [],
      lastSearchTime: null
    });
  } else if (details.reason === 'update') {
    console.log('Search Topic Helper updated!');
  }
});

// Listen for messages from popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'performSearch') {
    // Could add additional background logic here
    sendResponse({ success: true });
  }
  return true;
});

// Badge update (optional - shows search count)
chrome.storage.onChanged.addListener((changes, namespace) => {
  if (changes.searchCount) {
    const count = changes.searchCount.newValue || 0;
    chrome.action.setBadgeText({ text: count > 0 ? count.toString() : '' });
    chrome.action.setBadgeBackgroundColor({ color: '#667eea' });
  }
});
