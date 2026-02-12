"""
Browser Process & Profile Cleanup Utility
Fixes: Browsers closing after 2-3 runs due to lingering processes/profile locks
Author: H1M
"""

import subprocess
import time
import os
import sys

def kill_browser_processes():
    """Kill all browser and driver processes that might be lingering"""
    
    processes_to_kill = [
        # Browser executables
        'msedge.exe',
        'chrome.exe',
        'firefox.exe',
        'brave.exe',
        'opera.exe',
        'msedgewebview2.exe',
        'chromium.exe',
        
        # Driver executables
        'msedgedriver.exe',
        'chromedriver.exe',
        'geckodriver.exe',
        'operadriver.exe',
        'chromiumdriver.exe',
        
        # Edge WebDriver service
        'MicrosoftWebDriver.exe',
    ]
    
    print("\n" + "="*60)
    print("🧹 CLEANING UP BROWSER PROCESSES")
    print("="*60)
    
    killed_count = 0
    for process in processes_to_kill:
        try:
            # Use taskkill with /F (force) flag
            result = subprocess.run(
                ['taskkill', '/F', '/IM', process],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            # Check if process was found and killed
            if result.returncode == 0:
                print(f"✓ Killed: {process}")
                killed_count += 1
            # Process not found is not an error for us
            elif "not found" in result.stderr.lower():
                pass  # Silent - process wasn't running
            else:
                # Only show if there was a real error
                if result.stderr and "access is denied" not in result.stderr.lower():
                    print(f"⚠ {process}: {result.stderr.strip()}")
                    
        except subprocess.TimeoutExpired:
            print(f"⏱ Timeout killing {process}")
        except Exception as e:
            print(f"⚠ Error with {process}: {e}")
    
    if killed_count > 0:
        print(f"\n✓ Cleaned up {killed_count} lingering processes")
        print("⏳ Waiting 3 seconds for processes to fully terminate...")
        time.sleep(3)
    else:
        print("\n✓ No lingering processes found - all clean!")
    
    return killed_count


def unlock_browser_profiles():
    """Remove lock files from browser profiles"""
    
    print("\n" + "="*60)
    print("🔓 UNLOCKING BROWSER PROFILES")
    print("="*60)
    
    localappdata = os.environ.get('LOCALAPPDATA', '')
    
    if not localappdata:
        print("⚠ Could not find LOCALAPPDATA path")
        return 0
    
    # Profile paths for each browser
    profile_paths = {
        'Edge': os.path.join(localappdata, 'Microsoft', 'Edge', 'User Data Automation'),
        'Chrome': os.path.join(localappdata, 'Google', 'Chrome', 'User Data Automation'),
        'Firefox': os.path.join(localappdata, 'Mozilla', 'Firefox', 'Profiles'),
        'Brave': os.path.join(localappdata, 'BraveSoftware', 'Brave-Browser', 'User Data Automation'),
        'Opera': os.path.join(localappdata, 'Opera Software', 'Opera Stable Automation'),
        'Edge Dev': os.path.join(localappdata, 'Microsoft', 'Edge Dev', 'User Data Automation'),
        'Opera GX': os.path.join(localappdata, 'Opera Software', 'Opera GX Stable Automation'),
        'Chromium': os.path.join(localappdata, 'Chromium', 'User Data Automation'),
    }
    
    # Lock files to remove
    lock_files = [
        'SingletonLock',
        'SingletonSocket',
        'SingletonCookie',
        'lockfile',
        '.lock',
        'LOCK',
    ]
    
    unlocked_count = 0
    
    for browser_name, profile_path in profile_paths.items():
        if not os.path.exists(profile_path):
            continue  # Profile doesn't exist yet
        
        try:
            # Check for lock files in profile directory
            for root, dirs, files in os.walk(profile_path):
                for lock_file in lock_files:
                    lock_path = os.path.join(root, lock_file)
                    if os.path.exists(lock_path):
                        try:
                            os.remove(lock_path)
                            print(f"✓ Unlocked: {browser_name} ({lock_file})")
                            unlocked_count += 1
                        except PermissionError:
                            print(f"⚠ {browser_name}: {lock_file} is still in use (process running)")
                        except Exception as e:
                            print(f"⚠ {browser_name}: Could not remove {lock_file} - {e}")
                
                # Only check main profile directory, not all subdirectories
                if root == profile_path:
                    break
                    
        except Exception as e:
            print(f"⚠ Error checking {browser_name} profile: {e}")
    
    if unlocked_count > 0:
        print(f"\n✓ Removed {unlocked_count} lock files")
    else:
        print("\n✓ No profile locks found - all clear!")
    
    return unlocked_count


def full_cleanup():
    """Perform full cleanup of processes and profile locks"""
    
    print("\n")
    print("╔══════════════════════════════════════════════════════════╗")
    print("║      BROWSER AUTOMATION CLEANUP UTILITY - BY H1M         ║")
    print("╚══════════════════════════════════════════════════════════╝")
    
    # Step 1: Kill lingering processes
    killed = kill_browser_processes()
    
    # Step 2: Unlock profiles
    unlocked = unlock_browser_profiles()
    
    # Summary
    print("\n" + "="*60)
    print("📊 CLEANUP SUMMARY")
    print("="*60)
    print(f"Processes killed:  {killed}")
    print(f"Profiles unlocked: {unlocked}")
    
    if killed > 0 or unlocked > 0:
        print("\n✅ Cleanup complete! You can now run the automation again.")
    else:
        print("\n✅ System was already clean. No issues found.")
    
    print("="*60 + "\n")


if __name__ == "__main__":
    try:
        full_cleanup()
    except KeyboardInterrupt:
        print("\n\n⚠ Cleanup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Cleanup failed: {e}")
        sys.exit(1)
