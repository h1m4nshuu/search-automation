// Content script - runs on Bing pages to simulate human typing

// Global flag to stop scrolling
let stopScrolling = false;

// Configuration for human-like behavior
const TYPING_CONFIG = {
  minDelay: 80,           // Minimum ms between keystrokes
  maxDelay: 200,          // Maximum ms between keystrokes
  typoChance: 0.005,      // 0.5% chance of making a typo (very rare)
  pauseChance: 0.08,      // 8% chance of brief pause
  pauseDuration: [300, 600], // Pause length range
  backspaceDelay: [150, 250], // Delay before correcting typo
  spaceDelay: [150, 250], // Pause after spaces
  submitDelay: [600, 1000] // Delay before hitting enter
};

// Common typo patterns (neighboring keys)
const TYPO_MAP = {
  'a': ['s', 'q', 'w', 'z'],
  'b': ['v', 'g', 'h', 'n'],
  'c': ['x', 'd', 'f', 'v'],
  'd': ['s', 'e', 'r', 'f', 'c', 'x'],
  'e': ['w', 'r', 'd', 's'],
  'f': ['d', 'r', 't', 'g', 'v', 'c'],
  'g': ['f', 't', 'y', 'h', 'b', 'v'],
  'h': ['g', 'y', 'u', 'j', 'n', 'b'],
  'i': ['u', 'o', 'k', 'j'],
  'j': ['h', 'u', 'i', 'k', 'm', 'n'],
  'k': ['j', 'i', 'o', 'l', 'm'],
  'l': ['k', 'o', 'p'],
  'm': ['n', 'j', 'k'],
  'n': ['b', 'h', 'j', 'm'],
  'o': ['i', 'p', 'l', 'k'],
  'p': ['o', 'l'],
  'q': ['w', 'a'],
  'r': ['e', 't', 'f', 'd'],
  's': ['a', 'w', 'e', 'd', 'x', 'z'],
  't': ['r', 'y', 'g', 'f'],
  'u': ['y', 'i', 'j', 'h'],
  'v': ['c', 'f', 'g', 'b'],
  'w': ['q', 'e', 's', 'a'],
  'x': ['z', 's', 'd', 'c'],
  'y': ['t', 'u', 'h', 'g'],
  'z': ['a', 's', 'x']
};

// Utility functions
function randomDelay(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function getTypo(char) {
  const lower = char.toLowerCase();
  const typos = TYPO_MAP[lower];
  if (typos && typos.length > 0) {
    const typo = typos[Math.floor(Math.random() * typos.length)];
    return char === char.toUpperCase() ? typo.toUpperCase() : typo;
  }
  return char;
}

// Find search input on page
function findSearchInput() {
  // Try multiple selectors for Bing search
  const selectors = [
    'input[name="q"]',           // Bing main search
    'input#sb_form_q',           // Bing search box
    'input.sb_form_q',           // Bing alternative
    'textarea[name="q"]',        // Bing on some pages
    'input[type="search"]',      // Generic search
    'input[aria-label*="Search"]', // Accessible search
    'input[title*="Search"]'     // Title-based search
  ];

  for (const selector of selectors) {
    const input = document.querySelector(selector);
    if (input) {
      return input;
    }
  }
  
  return null;
}

// Simulate human-like mouse movement to element
async function moveMouseToElement(element) {
  // Create and dispatch mouse events for realism
  const rect = element.getBoundingClientRect();
  const x = rect.left + rect.width / 2;
  const y = rect.top + rect.height / 2;
  
  // Simulate mouse move
  const moveEvent = new MouseEvent('mousemove', {
    bubbles: true,
    cancelable: true,
    clientX: x,
    clientY: y
  });
  document.dispatchEvent(moveEvent);
  
  await sleep(randomDelay(50, 150));
}

// Type character with realistic input events
async function typeCharacter(input, char) {
  // Focus if not already focused
  if (document.activeElement !== input) {
    input.focus();
    await sleep(randomDelay(50, 100));
  }

  // Store current value
  const currentValue = input.value;
  
  // Create realistic keyboard events (but don't let them type)
  const keyDownEvent = new KeyboardEvent('keydown', {
    key: char,
    code: `Key${char.toUpperCase()}`,
    bubbles: true,
    cancelable: false
  });
  
  const keyUpEvent = new KeyboardEvent('keyup', {
    key: char,
    code: `Key${char.toUpperCase()}`,
    bubbles: true,
    cancelable: false
  });

  // Dispatch keydown
  input.dispatchEvent(keyDownEvent);
  await sleep(randomDelay(10, 30));
  
  // Manually update value (this is what actually changes the text)
  input.value = currentValue + char;
  
  // Create and dispatch input event to notify that value changed
  const inputEvent = new InputEvent('input', {
    bubbles: true,
    cancelable: false,
    data: char,
    inputType: 'insertText'
  });
  input.dispatchEvent(inputEvent);
  
  await sleep(randomDelay(10, 30));
  input.dispatchEvent(keyUpEvent);
}

// Simulate backspace
async function pressBackspace(input) {
  const keyDownEvent = new KeyboardEvent('keydown', {
    key: 'Backspace',
    code: 'Backspace',
    keyCode: 8,
    bubbles: true,
    cancelable: true
  });
  
  const inputEvent = new InputEvent('input', {
    bubbles: true,
    cancelable: true,
    inputType: 'deleteContentBackward'
  });
  
  const keyUpEvent = new KeyboardEvent('keyup', {
    key: 'Backspace',
    code: 'Backspace',
    keyCode: 8,
    bubbles: true,
    cancelable: true
  });

  input.dispatchEvent(keyDownEvent);
  await sleep(randomDelay(10, 30));
  
  // Remove last character
  input.value = input.value.slice(0, -1);
  input.dispatchEvent(inputEvent);
  
  await sleep(randomDelay(10, 30));
  input.dispatchEvent(keyUpEvent);
}

// Main typing function with human-like behavior
async function humanType(input, text, options = {}) {
  // Clear existing text first (if any)
  if (input.value) {
    input.value = '';
    input.dispatchEvent(new Event('input', { bubbles: true }));
    await sleep(randomDelay(100, 200));
  }

  // Move mouse to input first
  await moveMouseToElement(input);
  
  // Click on input
  input.click();
  await sleep(randomDelay(100, 200));

  // Split into words to avoid typos on short words
  const words = text.split(' ');
  let charIndex = 0;
  
  // Type each character
  for (let wordIdx = 0; wordIdx < words.length; wordIdx++) {
    const word = words[wordIdx];
    
    // Type each character in the word
    for (let i = 0; i < word.length; i++) {
      const char = word[i];
      charIndex++;
      
      // Random pause (thinking)
      if (Math.random() < TYPING_CONFIG.pauseChance) {
        const pauseTime = randomDelay(...TYPING_CONFIG.pauseDuration);
        await sleep(pauseTime);
      }
      
      // Random typo - but only on longer words (5+ chars) and only letters
      const shouldMakeTypo = 
        Math.random() < TYPING_CONFIG.typoChance && 
        char.match(/[a-z]/i) && 
        word.length >= 6 &&  // Only on words with 6+ characters
        i > 1 &&             // Not first or second letter
        i < word.length - 2; // Not last or second-to-last letter
      
      if (shouldMakeTypo) {
        const typo = getTypo(char);
        await typeCharacter(input, typo);
        
        // Delay before noticing mistake
        await sleep(randomDelay(...TYPING_CONFIG.backspaceDelay));
        
        // Backspace to correct
        await pressBackspace(input);
        await sleep(randomDelay(50, 100));
        
        // Type correct character
        await typeCharacter(input, char);
      } else {
        // Normal typing
        await typeCharacter(input, char);
      }
      
      // Variable delay based on character
      let delay = randomDelay(TYPING_CONFIG.minDelay, TYPING_CONFIG.maxDelay);
      await sleep(delay);
    }
    
    // Add space after word (except last word)
    if (wordIdx < words.length - 1) {
      await typeCharacter(input, ' ');
      const spaceDelay = randomDelay(...TYPING_CONFIG.spaceDelay);
      await sleep(spaceDelay);
    }
  }
  
  // Brief pause before submitting
  await sleep(randomDelay(...TYPING_CONFIG.submitDelay));
  
  // Submit the search
  if (options.autoSubmit !== false) {
    await submitSearch(input);
  }
}

// Submit search (press Enter)
async function submitSearch(input) {
  const enterDown = new KeyboardEvent('keydown', {
    key: 'Enter',
    code: 'Enter',
    keyCode: 13,
    bubbles: true,
    cancelable: true
  });
  
  const enterPress = new KeyboardEvent('keypress', {
    key: 'Enter',
    code: 'Enter',
    keyCode: 13,
    bubbles: true,
    cancelable: true
  });
  
  const enterUp = new KeyboardEvent('keyup', {
    key: 'Enter',
    code: 'Enter',
    keyCode: 13,
    bubbles: true,
    cancelable: true
  });

  input.dispatchEvent(enterDown);
  await sleep(20);
  input.dispatchEvent(enterPress);
  await sleep(20);
  input.dispatchEvent(enterUp);
  
  // Also try form submit as fallback
  const form = input.closest('form');
  if (form) {
    form.submit();
  }
}

// Listen for messages from popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'typeSearch') {
    const input = findSearchInput();
    
    if (!input) {
      sendResponse({ 
        success: false, 
        error: 'Search input not found on page' 
      });
      return true;
    }
    
    // Perform human-like typing
    humanType(input, request.query, request.options || {})
      .then(() => {
        sendResponse({ success: true });
      })
      .catch((error) => {
        sendResponse({ 
          success: false, 
          error: error.message 
        });
      });
    
    // Return true to indicate async response
    return true;
  }
  
  if (request.action === 'checkSearchBox') {
    const input = findSearchInput();
    sendResponse({ 
      found: !!input,
      selector: input ? input.tagName + '#' + input.id : null
    });
    return true;
  }
});

// Human-like scrolling configuration
const SCROLL_CONFIG = {
  enabled: true,
  minScrollAmount: 100,      // Minimum pixels per scroll
  maxScrollAmount: 300,      // Maximum pixels per scroll
  scrollDelay: [800, 2000],  // Delay between scrolls (ms)
  readingPause: [2000, 4000], // Pause to "read" content
  pauseChance: 0.3,          // 30% chance to pause and read
  scrollBackChance: 0.1,     // 10% chance to scroll back up
  hoverDelay: [500, 1500],   // Hover on links delay
  scrollToBottom: 0.7,       // Scroll to 70% of page (not always to bottom)
  variableSpeed: true        // Use variable scrolling speeds
};

// Smooth scroll with human-like behavior
async function humanScroll(targetY, duration = 1000) {
  const startY = window.scrollY;
  const distance = targetY - startY;
  const startTime = performance.now();
  
  // Ease in-out function for natural movement
  function easeInOutCubic(t) {
    return t < 0.5 
      ? 4 * t * t * t 
      : 1 - Math.pow(-2 * t + 2, 3) / 2;
  }
  
  function scroll() {
    const currentTime = performance.now();
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);
    
    const easeProgress = easeInOutCubic(progress);
    const currentY = startY + (distance * easeProgress);
    
    window.scrollTo(0, currentY);
    
    if (progress < 1) {
      requestAnimationFrame(scroll);
    }
  }
  
  scroll();
  await sleep(duration);
}

// Simulate reading by hovering over elements
async function simulateReading() {
  // Find search result items
  const results = document.querySelectorAll(
    'li.b_algo, .b_algo, #b_results > li, .b_ans, article'
  );
  
  if (results.length === 0) return;
  
  // Randomly hover over 2-4 results
  const numToHover = Math.floor(Math.random() * 3) + 2;
  const shuffled = Array.from(results).sort(() => Math.random() - 0.5);
  
  for (let i = 0; i < Math.min(numToHover, shuffled.length); i++) {
    const result = shuffled[i];
    
    // Scroll element into view smoothly
    result.scrollIntoView({ behavior: 'smooth', block: 'center' });
    await sleep(randomDelay(300, 600));
    
    // Simulate mouse hover
    const rect = result.getBoundingClientRect();
    const mouseEvent = new MouseEvent('mouseover', {
      bubbles: true,
      cancelable: true,
      clientX: rect.left + rect.width / 2,
      clientY: rect.top + rect.height / 2
    });
    result.dispatchEvent(mouseEvent);
    
    // "Read" the result
    await sleep(randomDelay(...SCROLL_CONFIG.hoverDelay));
    
    // Mouse out
    const mouseOutEvent = new MouseEvent('mouseout', { bubbles: true });
    result.dispatchEvent(mouseOutEvent);
    
    await sleep(randomDelay(200, 500));
  }
}

// Auto-scroll page with human-like behavior
async function autoScrollPage(options = {}) {
  const config = { ...SCROLL_CONFIG, ...options };
  
  // Reset stop flag at start of new scroll
  stopScrolling = false;
  
  if (!config.enabled) return;
  
  // Wait for page to fully load
  await sleep(randomDelay(1000, 2000));
  
  const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
  const targetScroll = maxScroll * config.scrollToBottom;
  
  let currentScroll = window.scrollY;
  let scrollAttempts = 0;
  const maxAttempts = 15; // Prevent infinite loops
  
  while (currentScroll < targetScroll && scrollAttempts < maxAttempts && !stopScrolling) {
    scrollAttempts++;
    
    // Random scroll amount
    const scrollAmount = randomDelay(
      config.minScrollAmount, 
      config.maxScrollAmount
    );
    
    const nextScroll = Math.min(currentScroll + scrollAmount, targetScroll);
    
    // Variable scroll duration for realism
    const scrollDuration = config.variableSpeed 
      ? randomDelay(300, 800) 
      : 500;
    
    // Smooth scroll to next position
    await humanScroll(nextScroll, scrollDuration);
    currentScroll = window.scrollY;
    
    // Random pause to "read" content
    if (Math.random() < config.pauseChance) {
      await sleep(randomDelay(...config.readingPause));
      
      // Sometimes interact with visible content
      if (Math.random() < 0.5) {
        await simulateReading();
      }
    }
    
    // Occasionally scroll back up (natural behavior)
    if (Math.random() < config.scrollBackChance) {
      const scrollBack = randomDelay(50, 150);
      await humanScroll(currentScroll - scrollBack, 400);
      currentScroll = window.scrollY;
      await sleep(randomDelay(500, 1000));
    }
    
    // Regular delay between scrolls
    await sleep(randomDelay(...config.scrollDelay));
  }
  
  // Final pause at bottom
  await sleep(randomDelay(2000, 4000));
  
  // Sometimes scroll back to top
  if (Math.random() < 0.3) {
    await humanScroll(0, randomDelay(1000, 1500));
    await sleep(randomDelay(1000, 2000));
  }
  
  return { success: true, scrolledTo: currentScroll };
}

// Detect if we're on a search results page
function isSearchResultsPage() {
  return window.location.pathname.includes('/search') || 
         document.querySelector('#b_results, .b_algo') !== null;
}

// Listen for messages from popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'typeSearch') {
    const input = findSearchInput();
    
    if (!input) {
      sendResponse({ 
        success: false, 
        error: 'Search input not found on page' 
      });
      return true;
    }
    
    // Perform human-like typing
    humanType(input, request.query, request.options || {})
      .then(() => {
        sendResponse({ success: true });
        
        // If auto-scroll enabled, start scrolling after search
        if (request.options?.autoScroll !== false) {
          setTimeout(() => {
            if (isSearchResultsPage()) {
              autoScrollPage(request.options?.scrollConfig || {});
            }
          }, 2000); // Wait for results to load
        }
      })
      .catch((error) => {
        sendResponse({ 
          success: false, 
          error: error.message 
        });
      });
    
    // Return true to indicate async response
    return true;
  }
  
  if (request.action === 'scrollPage') {
    if (!isSearchResultsPage()) {
      sendResponse({ 
        success: false, 
        error: 'Not on search results page' 
      });
      return true;
    }
    
    autoScrollPage(request.options || {})
      .then((result) => {
        sendResponse({ success: true, ...result });
      })
      .catch((error) => {
        sendResponse({ 
          success: false, 
          error: error.message 
        });
      });
    
    return true;
  }
  
  if (request.action === 'stopScroll') {
    stopScrolling = true;
    sendResponse({ success: true });
    return true;
  }
  
  if (request.action === 'checkSearchBox') {
    const input = findSearchInput();
    sendResponse({ 
      found: !!input,
      selector: input ? input.tagName + '#' + input.id : null,
      isResultsPage: isSearchResultsPage()
    });
    return true;
  }
});

// Auto-scroll if we land on search results page
if (isSearchResultsPage()) {
  // Check if auto-scroll was requested via URL hash
  if (window.location.hash.includes('autoscroll')) {
    setTimeout(() => {
      autoScrollPage();
    }, 2000);
  }
}

// Notify extension that content script is ready
chrome.runtime.sendMessage({ 
  action: 'contentScriptReady',
  url: window.location.href 
});

console.log('🔍 Search Helper content script loaded');
