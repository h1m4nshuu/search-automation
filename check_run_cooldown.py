"""
Run Cooldown Detector - Warns if running automation too frequently
This prevents profile locks and browser detection issues
Author: H1M
"""

import os
import time
from datetime import datetime, timedelta

LAST_RUN_FILE = ".last_run_timestamp"
MIN_COOLDOWN_MINUTES = 5  # Minimum time between runs


def check_run_cooldown():
    """
    Check if enough time has passed since last run
    Returns: (should_proceed, minutes_since_last_run, message)
    """
    
    if not os.path.exists(LAST_RUN_FILE):
        # First run - no cooldown needed
        save_run_timestamp()
        return True, None, "✓ First run detected - no cooldown needed"
    
    try:
        with open(LAST_RUN_FILE, 'r') as f:
            last_run_str = f.read().strip()
            last_run = datetime.fromisoformat(last_run_str)
    except Exception as e:
        # Corrupt file - reset it
        save_run_timestamp()
        return True, None, f"⚠ Cooldown file corrupted (reset): {e}"
    
    # Calculate time since last run
    now = datetime.now()
    time_diff = now - last_run
    minutes_since = time_diff.total_seconds() / 60
    
    # Check if cooldown period has passed
    if minutes_since < MIN_COOLDOWN_MINUTES:
        minutes_remaining = MIN_COOLDOWN_MINUTES - minutes_since
        
        message = (
            f"\n⚠ WARNING: RAPID RE-RUN DETECTED!\n"
            f"   Last run: {minutes_since:.1f} minutes ago\n"
            f"   Cooldown: {MIN_COOLDOWN_MINUTES} minutes recommended\n"
            f"   Wait: {minutes_remaining:.1f} more minutes\n\n"
            f"   Why this matters:\n"
            f"   • Running too quickly can cause profile locks\n"
            f"   • Browsers may detect automation patterns\n"
            f"   • Microsoft may flag rapid searches as suspicious\n\n"
            f"   You can:\n"
            f"   1. Wait {minutes_remaining:.0f} minutes (RECOMMENDED)\n"
            f"   2. Continue anyway (may cause browser closures)\n"
            f"   3. Run cleanup first: CLEANUP_BROWSERS.bat\n"
        )
        
        return False, minutes_since, message
    else:
        # Cooldown passed - safe to run
        save_run_timestamp()
        return True, minutes_since, f"✓ Cooldown passed ({minutes_since:.1f} minutes since last run)"


def save_run_timestamp():
    """Save current timestamp as last run time"""
    with open(LAST_RUN_FILE, 'w') as f:
        f.write(datetime.now().isoformat())


def reset_cooldown():
    """Manually reset cooldown (useful after cleanup)"""
    if os.path.exists(LAST_RUN_FILE):
        os.remove(LAST_RUN_FILE)
        return "✓ Cooldown reset - you can run immediately"
    return "✓ No cooldown to reset"


if __name__ == "__main__":
    import sys
    
    # Check if user wants to reset
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'reset':
        print(reset_cooldown())
        sys.exit(0)
    
    # Normal cooldown check
    should_proceed, minutes, message = check_run_cooldown()
    print(message)
    
    if not should_proceed:
        response = input("\n⚠ Continue anyway? (yes/no): ").strip().lower()
        if response not in ['yes', 'y']:
            print("\n✓ Run cancelled. Wait for cooldown to complete.")
            sys.exit(1)
        else:
            print("\n⚠ Proceeding despite cooldown warning...")
            save_run_timestamp()
            sys.exit(0)
    else:
        sys.exit(0)
