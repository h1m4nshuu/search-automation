# -*- coding: utf-8 -*-
"""
   ██╗  ██╗  ██╗  ███╗   ███╗
   ██║  ██║ ███║  ████╗ ████║
   ███████║ ╚██║  ██╔████╔██║
   ██╔══██║  ██║  ██║╚██╔╝██║
   ██║  ██║  ██║  ██║ ╚═╝ ██║
   ╚═╝  ╚═╝  ╚═╝  ╚═╝     ╚═╝
   ═══════════════════════════
   Microsoft Rewards v2.0
   
Run 30 searches across all 8 browsers (Edge, Chrome, Firefox, Brave, Opera, Edge Dev, Opera GX, Chromium) IN PARALLEL
"""

import sys
import os
import time
import threading
sys.path.append(r'C:\Users\himan\Desktop\edge search')

from search_trending_edge import run_search_sequence, generate_dynamic_topics, fetch_trending_queries
import random

# Thread-safe results tracking
results_lock = threading.Lock()
browser_results = {}

def run_browser_searches(browser, topics, browser_num):
    """Run searches on a single browser (called in separate thread)"""
    TOPIC_COUNT = 30
    MIN_WAIT = 10
    MAX_WAIT = 10
    
    try:
        print(f"\n[{browser.upper()}] Starting {TOPIC_COUNT} searches...")
        
        run_search_sequence(
            topics,
            browser=browser,
            headless=False,
            min_wait=MIN_WAIT,
            max_wait=MAX_WAIT,
            use_existing=False
        )
        
        with results_lock:
            browser_results[browser] = {'status': 'success', 'count': len(topics)}
        
        print(f"\n[SUCCESS] [{browser.upper()}] Completed {TOPIC_COUNT} searches!")
        
    except Exception as e:
        print(f"\n[ERROR] [{browser.upper()}] Error: {e}")
        with results_lock:
            browser_results[browser] = {'status': 'failed', 'error': str(e)}

def run_all_browsers_parallel():
    """Run 30 searches on each of the 8 browsers simultaneously"""
    
    browsers = ['edge', 'chrome', 'firefox', 'brave', 'opera', 'edgedev', 'operagx', 'chromium']
    TOPIC_COUNT = 30
    
    # H1M Watermark
    print("\n")
    print("   ██╗  ██╗  ██╗  ███╗   ███╗")
    print("   ██║  ██║ ███║  ████╗ ████║")
    print("   ███████║ ╚██║  ██╔████╔██║")
    print("   ██╔══██║  ██║  ██║╚██╔╝██║")
    print("   ██║  ██║  ██║  ██║ ╚═╝ ██║")
    print("   ╚═╝  ╚═╝  ╚═╝  ╚═╝     ╚═╝")
    print("   ═══════════════════════════")
    print("   Microsoft Rewards v2.0")
    print("   ═══════════════════════════")
    print()
    print("=" * 70)
    print("PARALLEL MULTI-BROWSER SEARCH AUTOMATION (8 Browsers)")
    print("=" * 70)
    print(f"Configuration:")
    print(f"  - Browsers: Edge, Chrome, Firefox, Brave, Opera, Edge Dev, Opera GX, Chromium")
    print(f"  - Searches per browser: {TOPIC_COUNT}")
    print(f"  - Total searches: {TOPIC_COUNT * len(browsers)}")
    print(f"  - Execution: PARALLEL (all browsers at once)")
    print("=" * 70)
    print()
    
    # Generate enough topics for all browsers
    print("Generating search topics...")
    total_needed = TOPIC_COUNT * len(browsers)
    
    # Fetch trending queries (aim for 2x needed to account for duplicates)
    queries = fetch_trending_queries(limit=total_needed * 2, region='global')
    
    if not queries:
        print("Couldn't fetch live trending queries; generating dynamic topics...")
        queries = generate_dynamic_topics(total_needed * 3)  # Generate 3x to ensure enough after deduplication
    else:
        print(f"Fetched {len(queries)} trending queries from pytrends...")
        # Add dynamic topics to supplement
        dynamic_topics = generate_dynamic_topics(total_needed * 2)
        queries.extend(dynamic_topics)
    
    # Remove duplicates efficiently
    unique_queries = []
    seen = set()
    for query in queries:
        query_lower = query.lower()
        if query_lower not in seen:
            unique_queries.append(query)
            seen.add(query_lower)
            # Stop early if we have enough
            if len(unique_queries) >= total_needed:
                break
    
    queries = unique_queries
    
    # Final check - generate more only if still needed (should rarely happen now)
    if len(queries) < total_needed:
        shortage = total_needed - len(queries)
        additional = generate_dynamic_topics(shortage + 20)  # Generate a bit extra as buffer
        for query in additional:
            query_lower = query.lower()
            if query_lower not in seen:
                queries.append(query)
                seen.add(query_lower)
                if len(queries) >= total_needed:
                    break
    
    print(f"[OK] Prepared {len(queries)} unique topics for {total_needed} searches\n")
    
    # Filter out browsers that aren't installed (check common paths)
    import os
    available_browsers = []
    username = os.environ.get('USERNAME', '')
    browser_paths = {
        'opera': [
            os.path.join(r'C:\Users', username, r'AppData\Local\Programs\Opera\opera.exe'),
            r'C:\Program Files\Opera\opera.exe',
            r'C:\Program Files\Opera\launcher.exe',
            os.path.join(r'C:\Users', username, r'AppData\Roaming\Opera Software\Opera Stable\opera.exe')
        ],
        'edgedev': [
            r'C:\Program Files (x86)\Microsoft\Edge Dev\Application\msedge.exe',
            r'C:\Program Files\Microsoft\Edge Dev\Application\msedge.exe',
            os.path.join(r'C:\Users', username, r'AppData\Local\Microsoft\Edge Dev\Application\msedge.exe')
        ],
        'operagx': [
            os.path.join(r'C:\Users', username, r'AppData\Local\Programs\Opera GX\opera.exe'),
            r'C:\Program Files\Opera GX\opera.exe',
            r'C:\Program Files\Opera GX\launcher.exe'
        ],
        'chromium': [
            os.path.join(r'C:\Users', username, r'AppData\Local\Chromium\Application\chrome.exe'),
            r'C:\Program Files\Chromium\Application\chrome.exe',
            r'C:\Program Files (x86)\Chromium\Application\chrome.exe'
        ]
    }
    
    print("[INFO] Checking browser availability...")
    for browser in browsers:
        # Always include the first 4 browsers (assume they're installed)
        if browser in ['edge', 'chrome', 'firefox', 'brave']:
            available_browsers.append(browser)
            print(f"  [OK] {browser.upper()}")
        # Check if new browsers are installed
        elif browser in browser_paths:
            if any(os.path.exists(path) for path in browser_paths[browser]):
                available_browsers.append(browser)
                print(f"  [OK] {browser.upper()}")
            else:
                print(f"  [SKIP] {browser.upper()} - not installed")
        else:
            available_browsers.append(browser)
    
    browsers = available_browsers
    print(f"\n[INFO] Running with {len(browsers)} available browsers\n")
    
    # Prepare topics for each browser
    browser_topics = {}
    for i, browser in enumerate(browsers):
        start_idx = i * TOPIC_COUNT
        topics = queries[start_idx:start_idx + TOPIC_COUNT]
        
        # Add variations to some topics
        unique_searches = []
        for topic in topics:
            if random.random() < 0.3:  # 30% chance of variation
                variations = [
                    f"{topic} 2025",
                    f"{topic} news",
                    f"{topic} today",
                    f"{topic} latest",
                    f"best {topic}",
                    f"{topic} guide",
                    f"{topic} tips"
                ]
                topic = random.choice(variations)
            unique_searches.append(topic)
        
        browser_topics[browser] = unique_searches
        
        print(f"Topics for {browser.upper()}:")
        for idx, topic in enumerate(unique_searches[:3], 1):
            print(f"  {idx}. {topic}")
        print(f"  ... and {len(unique_searches) - 3} more\n")
    
    # Create threads for each browser
    threads = []
    print("=" * 70)
    print("LAUNCHING ALL BROWSERS IN PARALLEL...")
    print("=" * 70)
    print()
    
    for i, browser in enumerate(browsers, 1):
        thread = threading.Thread(
            target=run_browser_searches,
            args=(browser, browser_topics[browser], i),
            name=f"{browser.upper()}-Thread"
        )
        threads.append(thread)
        thread.start()
        time.sleep(2)  # Small delay to avoid simultaneous browser launches
    
    # Wait for all threads to complete
    print(f"\nWaiting for all {len(browsers)} browsers to complete...\n")
    
    for thread in threads:
        thread.join()
    
    # Display results
    print("\n" + "=" * 70)
    print("ALL BROWSERS COMPLETED!")
    print("=" * 70)
    
    successful = 0
    failed = 0
    
    for browser in browsers:
        result = browser_results.get(browser, {'status': 'unknown'})
        if result['status'] == 'success':
            print(f"[OK] {browser.upper()}: {result['count']} searches completed")
            successful += 1
        elif result['status'] == 'failed':
            print(f"[FAIL] {browser.upper()}: Failed - {result.get('error', 'Unknown error')}")
            failed += 1
        else:
            print(f"[UNKNOWN] {browser.upper()}: Status unknown")
    
    print("=" * 70)
    print(f"Summary:")
    print(f"   Successful: {successful}/{len(browsers)} browsers")
    print(f"   Failed: {failed}/{len(browsers)} browsers")
    print(f"   Total searches: {successful * TOPIC_COUNT}")
    print("=" * 70)

if __name__ == "__main__":
    try:
        run_all_browsers_parallel()
    except KeyboardInterrupt:
        print("\n\n[STOPPED] Automation stopped by user (Ctrl+C)")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n[ERROR] Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
