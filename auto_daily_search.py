"""
Automatic Daily Search Runner
Runs 30 searches across all browsers once per day, only when internet is available.
"""

import os
import sys
import time
import socket
import datetime
from pathlib import Path

# Add parent directory to path
sys.path.append(os.path.dirname(__file__))
from run_all_browsers_parallel import run_all_browsers_parallel

# File to track last run time
TIMESTAMP_FILE = os.path.join(os.path.dirname(__file__), '.last_run_timestamp')

def check_internet_connection(host="8.8.8.8", port=53, timeout=3):
    """
    Check if internet connection is available.
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False

def has_run_today():
    """
    Check if the script has already run today.
    """
    if not os.path.exists(TIMESTAMP_FILE):
        return False
    
    try:
        with open(TIMESTAMP_FILE, 'r') as f:
            last_run_str = f.read().strip()
            last_run = datetime.datetime.fromisoformat(last_run_str)
            now = datetime.datetime.now()
            
            # Check if last run was today
            if last_run.date() == now.date():
                return True
    except Exception as e:
        print(f"Error reading timestamp: {e}")
    
    return False

def update_timestamp():
    """
    Update the timestamp file with current time.
    """
    try:
        with open(TIMESTAMP_FILE, 'w') as f:
            f.write(datetime.datetime.now().isoformat())
    except Exception as e:
        print(f"Error updating timestamp: {e}")

def main():
    print("=" * 70)
    print("🤖 AUTOMATIC DAILY SEARCH RUNNER")
    print("=" * 70)
    print(f"Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Check if already run today
    if has_run_today():
        print("✅ Already ran today. Skipping...")
        print(f"Next run will be available after midnight.")
        return
    
    # Check internet connection
    print("🌐 Checking internet connection...")
    if not check_internet_connection():
        print("❌ No internet connection. Exiting...")
        print("Will retry when you restart your device.")
        return
    
    print("✅ Internet connected!")
    print()
    
    # Wait a bit to ensure system is fully loaded
    print("⏳ Waiting 30 seconds for system to fully load...")
    time.sleep(30)
    
    # Run the searches
    print("🚀 Starting automated searches...")
    print()
    
    try:
        run_all_browsers_parallel()
        
        # Update timestamp after successful run
        update_timestamp()
        print()
        print("=" * 70)
        print("✅ AUTOMATED DAILY SEARCH COMPLETED SUCCESSFULLY!")
        print(f"Next run: Tomorrow after system startup")
        print("=" * 70)
        
    except Exception as e:
        print(f"\n❌ Error during search execution: {e}")
        print("Will retry tomorrow.")

if __name__ == "__main__":
    main()
