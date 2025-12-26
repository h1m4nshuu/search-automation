// Topic categories and data
const TOPIC_CATEGORIES = {
  technology: ["artificial intelligence", "machine learning", "blockchain", "5G network", "virtual reality", 
               "augmented reality", "IoT devices", "cloud computing", "cybersecurity", "quantum computing",
               "robotics", "smart home", "autonomous cars", "drone technology", "3D printing"],
  
  news_current: ["breaking news", "world news", "political updates", "economic forecast", "social media trends",
                 "viral videos", "celebrity gossip", "sports highlights", "weather alerts", "stock market"],
  
  lifestyle: ["healthy recipes", "fitness workout", "yoga poses", "meditation guide", "home decor",
              "fashion trends", "beauty tips", "skincare routine", "hair care", "makeup tutorial"],
  
  education: ["online courses", "study tips", "language learning", "programming tutorial", "math help",
              "science facts", "history timeline", "geography quiz", "literature review", "exam preparation"],
  
  entertainment: ["movie reviews", "TV shows", "music playlist", "podcast recommendations", "book reviews",
                  "gaming news", "streaming services", "concert tickets", "theater shows", "art exhibitions"],
  
  travel: ["travel destinations", "flight deals", "hotel booking", "travel tips", "local cuisine",
           "tourist attractions", "travel insurance", "packing tips", "budget travel", "adventure sports"],
  
  shopping: ["product reviews", "best deals", "shopping guide", "price comparison", "gift ideas",
             "online shopping", "discount codes", "product recommendations", "brand comparison", "sales alerts"],
  
  health: ["medical advice", "nutrition facts", "mental health", "exercise benefits", "sleep tips",
           "vitamin supplements", "disease prevention", "health insurance", "doctor consultation", "wellness tips"]
};

const MODIFIERS = [
  "2024", "2025", "latest", "best", "top", "new", "trending", "popular", "guide", "tips",
  "review", "comparison", "how to", "benefits of", "facts about", "news", "updates", 
  "today", "this week", "explained", "tutorial", "beginner", "advanced", "free", "cheap"
];

// Generate dynamic topics
function generateTopics(count = 30) {
  const topics = [];
  const used = new Set();
  
  // Time-based topics
  const now = new Date();
  const timeTopics = [
    `news ${now.toLocaleDateString('en-US', { month: 'long', year: 'numeric' })}`,
    `weather ${now.toLocaleDateString('en-US', { weekday: 'long' })}`,
    `trending ${now.getFullYear()}`,
    `updates ${now.toLocaleDateString('en-US', { month: 'long' })}`
  ];
  
  timeTopics.forEach(topic => {
    if (topics.length < count && !used.has(topic)) {
      topics.push(topic);
      used.add(topic);
    }
  });
  
  // Category topics
  const categories = Object.keys(TOPIC_CATEGORIES);
  shuffleArray(categories);
  
  categories.forEach(category => {
    if (topics.length >= count) return;
    
    const categoryTopics = [...TOPIC_CATEGORIES[category]];
    shuffleArray(categoryTopics);
    
    categoryTopics.slice(0, 3).forEach(topic => {
      if (topics.length >= count) return;
      
      let finalTopic = topic;
      if (Math.random() < 0.6) {
        const modifier = MODIFIERS[Math.floor(Math.random() * MODIFIERS.length)];
        finalTopic = Math.random() < 0.5 ? `${modifier} ${topic}` : `${topic} ${modifier}`;
      }
      
      if (!used.has(finalTopic)) {
        topics.push(finalTopic);
        used.add(finalTopic);
      }
    });
  });
  
  return topics;
}

function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}

// State management
let state = {
  topics: [],
  currentIndex: 0,
  searchCount: 0,
  usedTopics: new Set(),
  autoMode: false,
  lastSearchTime: null,
  timerInterval: null,
  autoModeSearchCount: 0,  // Track searches in current auto mode session
  delay: 15  // Default delay in seconds (fixed at 15s)
};

// Load state from storage
async function loadState() {
  const data = await chrome.storage.local.get(['topics', 'currentIndex', 'searchCount', 'usedTopics', 'lastSearchTime', 'delay']);
  
  // Check if we have topics from today
  const today = new Date().toDateString();
  const topicsDate = data.topicsDate || '';
  
  if (data.topics && data.topics.length > 0 && topicsDate === today) {
    // Use existing topics from today
    state.topics = data.topics;
    state.currentIndex = data.currentIndex || 0;
    state.searchCount = data.searchCount || 0;
    state.usedTopics = new Set(data.usedTopics || []);
    state.lastSearchTime = data.lastSearchTime;
  } else {
    // Generate new topics for today
    state.topics = generateTopics(30);
    state.currentIndex = 0;
    state.usedTopics = new Set();
    await saveState();
  }
  
  // Keep delay fixed at 15 seconds
  state.delay = 15;
  
  updateUI();
}

// Save state to storage
async function saveState() {
  await chrome.storage.local.set({
    topics: state.topics,
    topicsDate: new Date().toDateString(),
    currentIndex: state.currentIndex,
    searchCount: state.searchCount,
    usedTopics: Array.from(state.usedTopics),
    lastSearchTime: state.lastSearchTime,
    delay: state.delay
  });
}

// Update UI
function updateUI() {
  document.getElementById('searchCount').textContent = state.searchCount;
  document.getElementById('topicCount').textContent = state.topics.length;
  
  const currentTopic = state.topics[state.currentIndex] || "No more topics";
  document.getElementById('currentTopic').textContent = currentTopic;
  
  // Update topic list
  const container = document.getElementById('topicListContainer');
  container.innerHTML = '';
  
  state.topics.forEach((topic, index) => {
    const div = document.createElement('div');
    div.className = `topic-item ${state.usedTopics.has(index) ? 'used' : ''}`;
    div.innerHTML = `
      <span><span class="index">${index + 1}.</span> ${topic}</span>
      ${state.usedTopics.has(index) ? '✓' : ''}
    `;
    div.addEventListener('click', () => {
      state.currentIndex = index;
      updateUI();
      saveState();
    });
    container.appendChild(div);
  });
  
  // Update scroll depth display
  const scrollDepth = document.getElementById('scrollDepth');
  const scrollDepthValue = document.getElementById('scrollDepthValue');
  if (scrollDepth && scrollDepthValue) {
    scrollDepthValue.textContent = Math.round(scrollDepth.value * 100) + '%';
  }
  
  // Update timer
  updateTimer();
}

// Update timer display
function updateTimer() {
  if (!state.lastSearchTime) {
    document.getElementById('timer').textContent = '--';
    return;
  }
  
  const delay = state.delay * 1000;
  const elapsed = Date.now() - state.lastSearchTime;
  const remaining = Math.max(0, delay - elapsed);
  
  if (remaining > 0) {
    const seconds = Math.ceil(remaining / 1000);
    document.getElementById('timer').textContent = `${seconds}s`;
  } else {
    document.getElementById('timer').textContent = 'Ready!';
  }
}

// Perform search
async function performSearch(topic) {
  const searchUrl = `https://www.bing.com/search?q=${encodeURIComponent(topic)}`;
  const newTab = document.getElementById('newTabCheck').checked;
  const autoScroll = document.getElementById('autoScrollCheck').checked;
  const scrollDepth = parseFloat(document.getElementById('scrollDepth').value);
  let tab;
  
  if (newTab) {
    tab = await chrome.tabs.create({ url: searchUrl });
  } else {
    [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    await chrome.tabs.update(tab.id, { url: searchUrl });
    tab = (await chrome.tabs.query({ active: true, currentWindow: true }))[0];
  }
  
  // If auto-scroll enabled, wait for page load then scroll
  if (autoScroll && tab) {
    // Wait for page to load
    await new Promise(resolve => {
      const listener = (tabId, changeInfo) => {
        if (tabId === tab.id && changeInfo.status === 'complete') {
          chrome.tabs.onUpdated.removeListener(listener);
          resolve();
        }
      };
      chrome.tabs.onUpdated.addListener(listener);
      
      // Timeout after 10 seconds
      setTimeout(() => {
        chrome.tabs.onUpdated.removeListener(listener);
        resolve();
      }, 10000);
    });
    
    // Additional delay to ensure content script is ready
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    // Send message to content script to scroll
    try {
      const response = await chrome.tabs.sendMessage(tab.id, {
        action: 'scrollPage',
        options: {
          scrollToBottom: scrollDepth,
          enabled: true
        }
      });
      console.log('Scroll response:', response);
    } catch (error) {
      console.log('Scroll message failed:', error.message);
      // Content script might not be loaded yet, that's okay
    }
  }
  
  state.usedTopics.add(state.currentIndex);
  state.searchCount++;
  // Don't update lastSearchTime here - let auto mode control it
  
  // Move to next topic
  state.currentIndex = (state.currentIndex + 1) % state.topics.length;
  
  await saveState();
  updateUI();
}

// Event listeners
document.getElementById('nextTopic').addEventListener('click', () => {
  state.currentIndex = (state.currentIndex + 1) % state.topics.length;
  updateUI();
  saveState();
});

document.getElementById('searchBtn').addEventListener('click', async () => {
  const topic = state.topics[state.currentIndex];
  if (topic) {
    state.lastSearchTime = Date.now();
    await performSearch(topic);
  }
});

document.getElementById('autoMode').addEventListener('click', () => {
  const btn = document.getElementById('autoMode');
  
  if (!state.autoMode) {
    // Starting auto mode - generate fresh topics
    state.autoMode = true;
    state.topics = generateTopics(30);
    state.currentIndex = 0;
    state.usedTopics.clear();
    state.autoModeSearchCount = 0;
    saveState();
    updateUI();
    
    btn.textContent = '⏸️ Stop Auto Mode';
    btn.style.background = '#dc3545';
    startAutoMode();
  } else {
    // Stopping auto mode
    state.autoMode = false;
    btn.textContent = '⚡ Semi-Auto Mode';
    btn.style.background = '#ffc107';
  }
});

document.getElementById('generateTopics').addEventListener('click', async () => {
  state.topics = generateTopics(30);
  state.currentIndex = 0;
  state.usedTopics.clear();
  state.autoModeSearchCount = 0;
  await saveState();
  updateUI();
  alert('Generated ' + state.topics.length + ' new search topics!');
});

document.getElementById('resetCount').addEventListener('click', async () => {
  if (confirm('Reset search count?')) {
    state.searchCount = 0;
    state.usedTopics.clear();
    state.lastSearchTime = null;
    await saveState();
    updateUI();
  }
});

document.getElementById('exportTopics').addEventListener('click', () => {
  const data = {
    topics: state.topics,
    searchCount: state.searchCount,
    date: new Date().toISOString()
  };
  
  const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `search-topics-${Date.now()}.json`;
  a.click();
});

// Start auto mode with minimum search requirement
function startAutoMode() {
  const executeSearch = async () => {
    if (!state.autoMode) return;
    
    const topic = state.topics[state.currentIndex];
    const delay = state.delay * 1000; // Get current delay each time
    
    if (!topic) {
      // No more topics - check if we hit 30 searches
      if (state.autoModeSearchCount >= 30) {
        stopAutoMode();
      } else {
        // Generate more topics and continue
        state.topics = generateTopics(30);
        state.currentIndex = 0;
        state.usedTopics.clear();
        await saveState();
        updateUI();
        // Continue
        setTimeout(executeSearch, delay + Math.random() * 5000);
      }
      return;
    }
    
    // Use direct search (no typing)
    await performSearch(topic);
    
    // Increment auto mode search counter
    state.autoModeSearchCount++;
    
    // Update button text with progress
    const btn = document.getElementById('autoMode');
    if (state.autoModeSearchCount < 30) {
      btn.textContent = `⏸️ Stop (${state.autoModeSearchCount}/30)`;
    } else {
      btn.textContent = `⏸️ Stop Auto Mode (${state.autoModeSearchCount})`;
    }
    
    // Schedule next search if still in auto mode and have topics left
    if (state.autoMode && state.topics.length > 0) {
      const randomVariance = Math.random() * 5000; // 0-5s random variance
      const nextSearchTime = delay + randomVariance;
      
      // Update lastSearchTime to when next search will happen (for timer sync)
      state.lastSearchTime = Date.now();
      await saveState();
      
      setTimeout(executeSearch, nextSearchTime);
    } else {
      stopAutoMode();
    }
  };
  
  // Check if enough time has passed since last search
  const delay = state.delay * 1000;
  if (state.lastSearchTime) {
    const timeSinceLastSearch = Date.now() - state.lastSearchTime;
    if (timeSinceLastSearch < delay) {
      const waitTime = delay - timeSinceLastSearch;
      setTimeout(executeSearch, waitTime);
      return;
    }
  }
  
  executeSearch();
}

function stopAutoMode() {
  state.autoMode = false;
  const btn = document.getElementById('autoMode');
  btn.textContent = '⚡ Semi-Auto Mode';
  btn.style.background = '#ffc107';
  
  // Stop any ongoing scrolling in all tabs
  chrome.tabs.query({}, (tabs) => {
    tabs.forEach(tab => {
      chrome.tabs.sendMessage(tab.id, { action: 'stopScroll' }).catch(() => {
        // Ignore errors for tabs without content script
      });
    });
  });
}

// Scroll depth slider update
document.getElementById('scrollDepth')?.addEventListener('input', (e) => {
  const value = Math.round(e.target.value * 100);
  document.getElementById('scrollDepthValue').textContent = value + '%';
});

// Timer update interval
setInterval(updateTimer, 1000);

// Initialize
loadState();
