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
   
"""Run 30 searches across 4 browsers (Edge, Chrome, Firefox, Brave) IN PARALLEL
"""

import sys
import os
import time
import threading
sys.path.append(r'C:\Users\himan\Desktop\edge search')

from search_trending_edge import run_search_sequence, generate_dynamic_topics, fetch_trending_queries
from cleanup_browser_processes import kill_browser_processes, unlock_browser_profiles
from check_run_cooldown import check_run_cooldown, save_run_timestamp
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
    """Run 30 searches on each of the 8 browsers in 2 batches (prevents system overload)"""
    
    # Split browsers into 2 batches to prevent resource overload
    batch1 = ['edge', 'chrome']
    batch2 = ['firefox', 'brave']
    all_browsers = batch1 + batch2
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
    print("BATCH MODE: 4 Browsers in 2 Groups (Prevents System Overload)")
    print("=" * 70)
    print(f"Configuration:")
    print(f"  - Batch 1: Edge, Chrome (2 browsers)")
    print(f"  - Batch 2: Firefox, Brave (2 browsers)")
    print(f"  - Searches per browser: {TOPIC_COUNT}")
    print(f"  - Total searches: {TOPIC_COUNT * len(all_browsers)}")
    print(f"  - Execution: 2 browsers per batch (prevents crashes)")
    print("=" * 70)
    print()
    
    # Generate enough topics for all browsers
    print("Generating search topics...")
    total_needed = TOPIC_COUNT * len(all_browsers)
    
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
    
    # **NEW**: Check run cooldown to prevent rapid re-runs
    print("=" * 70)
    print("⏱ CHECKING RUN COOLDOWN")
    print("=" * 70)
    
    should_proceed, minutes_since, cooldown_msg = check_run_cooldown()
    print(cooldown_msg)
    
    if not should_proceed:
        # User ran too quickly - prompt for confirmation
        print("\n" + "!" * 70)
        response = input("\n⚠ Continue anyway? (yes/no): ").strip().lower()
        print("!" * 70 + "\n")
        
        if response not in ['yes', 'y']:
            print("✓ Run cancelled. Recommendation:")
            print("  1. Wait 5 minutes between runs (prevents browser issues)")
            print("  2. Or run: CLEANUP_BROWSERS.bat")
            print("  3. Then try again\n")
            return
        else:
            print("⚠ Proceeding despite cooldown warning...\n")
            save_run_timestamp()  # Update timestamp since user chose to proceed
    
    # All 4 browsers are standard - assume they're installed
    import os
    available_browsers = all_browsers
    
    print("[INFO] Checking browser availability...")
    for browser in all_browsers:
        print(f"  [OK] {browser.upper()}")
    
    # Update batch lists based on available browsers
    batch1 = [b for b in batch1 if b in available_browsers]
    batch2 = [b for b in batch2 if b in available_browsers]
    print(f"\n[INFO] Running with {len(available_browsers)} available browsers")
    print(f"        Batch 1: {len(batch1)} browsers | Batch 2: {len(batch2)} browsers\n")
    
    # Prepare topics for each browser
    browser_topics = {}
    for i, browser in enumerate(available_browsers):
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
    
    # **NEW**: Pre-cleanup to prevent profile locks and lingering processes
    print("\n" + "=" * 70)
    print("🧹 PRE-RUN CLEANUP (Prevents browser closing issues)")
    print("=" * 70)
    
    try:
        killed = kill_browser_processes()
        time.sleep(2)  # Wait for processes to fully terminate
        unlocked = unlock_browser_profiles()
        
        if killed > 0 or unlocked > 0:
            print(f"\n✓ Cleanup complete! Killed {killed} processes, unlocked {unlocked} profiles")
            print("⏳ Waiting 3 seconds before starting browsers...\n")
            time.sleep(3)
        else:
            print("\n✓ System clean - no lingering processes or locks\n")
    except Exception as e:
        print(f"⚠ Cleanup warning: {e}")
        print("Continuing anyway...\n")
    
    # Run browsers in 2 batches
    for batch_num, batch in enumerate([batch1, batch2], 1):
        print("=" * 70)
        print(f"📦 BATCH {batch_num}/2: {', '.join([b.upper() for b in batch])}")
        print("=" * 70)
        print(f"⏱ Starting {len(batch)} browsers with 3-second delays...")
        print()
        
        threads = []
        for i, browser in enumerate(batch, 1):
            thread = threading.Thread(
                target=run_browser_searches,
                args=(browser, browser_topics[browser], i),
                name=f"{browser.upper()}-Thread"
            )
            threads.append(thread)
            thread.start()
            print(f"[{i}/{len(batch)}] ✓ Started {browser.upper()}")
            
            # Stagger browser launches with 3-second delay (except for last one)
            if i < len(batch):
                time.sleep(3)
                print(f"      ⏳ Waiting 3 seconds before starting next browser...")
        
        print()
        print(f"⏳ Waiting for Batch {batch_num} browsers to complete...")
        print("=" * 70)
        
        # Wait for all threads in this batch to complete
        for thread in threads:
            thread.join()
        
        print()
        print(f"✅ BATCH {batch_num} COMPLETE!")
        print("=" * 70)
        
        # Brief pause between batches
        if batch_num == 1:
            print()
            print("⏳ Brief pause before starting Batch 2...")
            time.sleep(5)
            print()
    
    # Display final results
    print("\n" + "=" * 70)
    print("🎉 ALL 4 BROWSERS COMPLETED!")
    print("=" * 70)
    
    successful = 0
    failed = 0
    
    for browser in available_browsers:
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
