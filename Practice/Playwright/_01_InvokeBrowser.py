"""
Comprehensive Guide: All Ways to Launch Browsers in Playwright Python
Target Website: SauceLabs (https://saucelabs.com)
"""

import asyncio
from playwright.async_api import async_playwright, Playwright
from playwright.sync_api import sync_playwright, Playwright as SyncPlaywright
import time

# =============================================================================
# 1. BASIC BROWSER LAUNCHING - SYNCHRONOUS API
# =============================================================================

def basic_sync_browser_launch():
    """
    Basic synchronous browser launching with different browsers
    """
    print("=== BASIC SYNCHRONOUS BROWSER LAUNCHING ===")
    
    with sync_playwright() as p:
        # Method 1: Launch Chromium (Default)
        print("1. Launching Chromium...")
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://saucelabs.com")
        print(f"Title: {page.title()}")
        time.sleep(2)
        browser.close()
        
        # Method 2: Launch Firefox
        print("2. Launching Firefox...")
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://saucelabs.com")
        print(f"Title: {page.title()}")
        time.sleep(2)
        browser.close()
        
        # Method 3: Launch WebKit (Safari)
        print("3. Launching WebKit...")
        browser = p.webkit.launch(headless=False)
        page = browser.new_page()
        page.goto("https://saucelabs.com")
        print(f"Title: {page.title()}")
        time.sleep(2)
        browser.close()

# =============================================================================
# 2. BASIC BROWSER LAUNCHING - ASYNCHRONOUS API
# =============================================================================

async def basic_async_browser_launch():
    """
    Basic asynchronous browser launching
    """
    print("=== BASIC ASYNCHRONOUS BROWSER LAUNCHING ===")
    
    async with async_playwright() as p:
        # Launch Chromium asynchronously
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://saucelabs.com")
        print(f"Async Title: {await page.title()}")
        await asyncio.sleep(2)
        await browser.close()

# =============================================================================
# 3. HEADLESS vs HEADED MODE
# =============================================================================

def headless_vs_headed():
    """
    Demonstrating headless vs headed browser launching
    """
    print("=== HEADLESS vs HEADED MODE ===")
    
    with sync_playwright() as p:
        # Headless mode (default) - browser runs in background
        print("1. Headless mode (invisible)...")
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://saucelabs.com")
        print(f"Headless Title: {page.title()}")
        browser.close()
        
        # Headed mode - browser window visible
        print("2. Headed mode (visible)...")
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://saucelabs.com")
        print(f"Headed Title: {page.title()}")
        time.sleep(3)
        browser.close()

# =============================================================================
# 4. COMPREHENSIVE LAUNCH OPTIONS
# =============================================================================

def comprehensive_launch_options():
    """
    All possible launch options for browser configuration
    """
    print("=== COMPREHENSIVE LAUNCH OPTIONS ===")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,                    # Show browser window
            slow_mo=1000,                      # Slow down operations by 1000ms
            devtools=True,                     # Open DevTools
            timeout=60000,                     # Launch timeout (60 seconds)
            args=[                             # Custom browser arguments
                '--start-maximized',           # Start maximized
                '--disable-blink-features=AutomationControlled',  # Hide automation
                '--disable-web-security',      # Disable web security
                '--disable-features=VizDisplayCompositor',
                '--no-sandbox',               # No sandbox (for Linux)
                '--disable-dev-shm-usage',    # Overcome limited resource problems
            ],
            ignore_default_args=[              # Ignore specific default arguments
                '--enable-automation',
                '--enable-blink-features=AutomationControlled'
            ],
            env={                             # Environment variables
                'DISPLAY': ':0'
            },
            executable_path=None,             # Custom browser executable path
            proxy={                           # Proxy configuration
                'server': 'http://proxy.example.com:8080',
                # 'username': 'user',
                # 'password': 'pass'
            } if False else None,  # Set to True to enable proxy
            downloads_path='./downloads',     # Downloads directory
            traces_dir='./traces',           # Traces directory
        )
        
        page = browser.new_page()
        page.goto("https://saucelabs.com")
        print(f"Advanced Launch Title: {page.title()}")
        time.sleep(3)
        browser.close()

# =============================================================================
# 5. BROWSER CONTEXT CREATION
# =============================================================================

def browser_context_examples():
    """
    Different ways to create and configure browser contexts
    """
    print("=== BROWSER CONTEXT EXAMPLES ===")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        
        # Basic context
        context1 = browser.new_context()
        page1 = context1.new_page()
        page1.goto("https://saucelabs.com")
        print(f"Basic Context: {page1.title()}")
        
        # Context with viewport and user agent
        context2 = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
        page2 = context2.new_page()
        page2.goto("https://saucelabs.com")
        print(f"Custom Context: {page2.title()}")
        
        # Context with geolocation
        context3 = browser.new_context(
            geolocation={'latitude': 37.7749, 'longitude': -122.4194},  # San Francisco
            permissions=['geolocation']
        )
        page3 = context3.new_page()
        page3.goto("https://saucelabs.com")
        print(f"Geo Context: {page3.title()}")
        
        time.sleep(3)
        browser.close()

# =============================================================================
# 6. DEVICE EMULATION
# =============================================================================

def device_emulation():
    """
    Emulating different devices
    """
    print("=== DEVICE EMULATION ===")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        
        # iPhone 12 emulation
        iphone = p.devices['iPhone 12']
        context = browser.new_context(**iphone)
        page = context.new_page()
        page.goto("https://saucelabs.com")
        print(f"iPhone 12: {page.title()}")
        time.sleep(2)
        
        # iPad emulation
        context.close()
        ipad = p.devices['iPad Pro']
        context = browser.new_context(**ipad)
        page = context.new_page()
        page.goto("https://saucelabs.com")
        print(f"iPad Pro: {page.title()}")
        time.sleep(2)
        
        # Custom mobile device
        context.close()
        context = browser.new_context(
            viewport={'width': 375, 'height': 667},
            user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)',
            device_scale_factor=2,
            is_mobile=True,
            has_touch=True
        )
        page = context.new_page()
        page.goto("https://saucelabs.com")
        print(f"Custom Mobile: {page.title()}")
        time.sleep(2)
        
        browser.close()

# =============================================================================
# 7. PERSISTENT CONTEXT (USER DATA DIRECTORY)
# =============================================================================

def persistent_context():
    """
    Using persistent context with user data directory
    """
    print("=== PERSISTENT CONTEXT ===")
    
    with sync_playwright() as p:
        # Launch with persistent context (like a real user session)
        context = p.chromium.launch_persistent_context(
            user_data_dir='./user-data',     # User data directory
            headless=False,
            viewport={'width': 1280, 'height': 720},
            args=['--start-maximized']
        )
        
        page = context.pages[0] if context.pages else context.new_page()
        page.goto("https://saucelabs.com")
        print(f"Persistent Context: {page.title()}")
        time.sleep(3)
        context.close()

# =============================================================================
# 8. BROWSER CHANNEL SELECTION
# =============================================================================

def browser_channels():
    """
    Using different browser channels
    """
    print("=== BROWSER CHANNELS ===")
    
    with sync_playwright() as p:
        try:
            # Chrome stable
            browser = p.chromium.launch(
                channel='chrome',  # Options: 'chrome', 'chrome-beta', 'chrome-dev', 'chrome-canary'
                headless=False
            )
            page = browser.new_page()
            page.goto("https://saucelabs.com")
            print(f"Chrome Channel: {page.title()}")
            time.sleep(2)
            browser.close()
        except Exception as e:
            print(f"Chrome channel not available: {e}")
        
        try:
            # Edge
            browser = p.chromium.launch(
                channel='msedge',  # Microsoft Edge
                headless=False
            )
            page = browser.new_page()
            page.goto("https://saucelabs.com")
            print(f"Edge Channel: {page.title()}")
            time.sleep(2)
            browser.close()
        except Exception as e:
            print(f"Edge channel not available: {e}")

# =============================================================================
# 9. MULTIPLE PAGES AND CONTEXTS
# =============================================================================

def multiple_pages_contexts():
    """
    Working with multiple pages and contexts
    """
    print("=== MULTIPLE PAGES AND CONTEXTS ===")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        
        # Context 1 with multiple pages
        context1 = browser.new_context()
        page1 = context1.new_page()
        page2 = context1.new_page()
        
        page1.goto("https://saucelabs.com")
        page2.goto("https://saucelabs.com/platform")
        
        print(f"Page 1: {page1.title()}")
        print(f"Page 2: {page2.title()}")
        
        # Context 2 (isolated from context 1)
        context2 = browser.new_context()
        page3 = context2.new_page()
        page3.goto("https://saucelabs.com/solutions")
        print(f"Page 3 (Different Context): {page3.title()}")
        
        time.sleep(3)
        browser.close()

# =============================================================================
# 10. BROWSER STATE AND STORAGE
# =============================================================================

def browser_state_storage():
    """
    Managing browser state and storage
    """
    print("=== BROWSER STATE AND STORAGE ===")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        
        context = browser.new_context(
            # Pre-populate storage state
            storage_state={
                'cookies': [
                    {
                        'name': 'test_cookie',
                        'value': 'test_value',
                        'domain': 'saucelabs.com',
                        'path': '/'
                    }
                ],
                'origins': [
                    {
                        'origin': 'https://saucelabs.com',
                        'localStorage': [
                            {'name': 'test_key', 'value': 'test_value'}
                        ]
                    }
                ]
            },
            # Accept downloads
            accept_downloads=True,
            # Record HAR
            record_har_path='./network.har',
            # Record video
            record_video_dir='./videos/',
            record_video_size={'width': 1280, 'height': 720}
        )
        
        page = context.new_page()
        page.goto("https://saucelabs.com")
        print(f"State Management: {page.title()}")
        
        # Save storage state
        storage_state = context.storage_state(path='./storage-state.json')
        print(f"Storage state saved")
        
        time.sleep(3)
        browser.close()

# =============================================================================
# 11. ERROR HANDLING AND TIMEOUTS
# =============================================================================

def error_handling_timeouts():
    """
    Proper error handling and timeout management
    """
    print("=== ERROR HANDLING AND TIMEOUTS ===")
    
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(
                headless=False,
                timeout=30000  # 30 seconds launch timeout
            )
            
            context = browser.new_context(
                # Page timeout settings
            )
            
            page = context.new_page()
            
            # Set timeouts
            page.set_default_timeout(30000)  # 30 seconds for all operations
            page.set_default_navigation_timeout(60000)  # 60 seconds for navigation
            
            page.goto("https://saucelabs.com", timeout=30000)
            print(f"Timeout Management: {page.title()}")
            
            time.sleep(2)
            
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            if 'browser' in locals():
                browser.close()

# =============================================================================
# 12. MAIN EXECUTION FUNCTION
# =============================================================================

def run_all_examples():
    """
    Run all browser launching examples
    """
    print("🚀 PLAYWRIGHT BROWSER LAUNCHING COMPREHENSIVE GUIDE 🚀")
    print("=" * 60)
    
    # Comment/uncomment the methods you want to run
    
    # 1. Basic launches
    basic_sync_browser_launch()
    print("\n" + "="*60 + "\n")
    
    # 2. Async example
    asyncio.run(basic_async_browser_launch())
    print("\n" + "="*60 + "\n")
    
    # 3. Headless vs headed
    headless_vs_headed()
    print("\n" + "="*60 + "\n")
    
    # 4. Comprehensive options
    comprehensive_launch_options()
    print("\n" + "="*60 + "\n")
    
    # 5. Browser contexts
    browser_context_examples()
    print("\n" + "="*60 + "\n")
    
    # 6. Device emulation
    device_emulation()
    print("\n" + "="*60 + "\n")
    
    # 7. Persistent context
    persistent_context()
    print("\n" + "="*60 + "\n")
    
    # 8. Browser channels
    browser_channels()
    print("\n" + "="*60 + "\n")
    
    # 9. Multiple pages
    multiple_pages_contexts()
    print("\n" + "="*60 + "\n")
    
    # 10. State management
    browser_state_storage()
    print("\n" + "="*60 + "\n")
    
    # 11. Error handling
    error_handling_timeouts()
    print("\n" + "="*60 + "\n")
    
    print("✅ All examples completed!")

# =============================================================================
# SUMMARY OF ALL BROWSER LAUNCH OPTIONS
# =============================================================================

"""
🔍 COMPLETE SUMMARY OF PLAYWRIGHT BROWSER LAUNCH OPTIONS:

1. BROWSER TYPES:
   - p.chromium.launch()  # Google Chrome/Chromium
   - p.firefox.launch()   # Mozilla Firefox  
   - p.webkit.launch()    # Safari/WebKit

2. LAUNCH MODES:
   - headless=True/False  # Invisible/Visible browser
   - slow_mo=milliseconds # Slow down operations
   - devtools=True/False  # Open DevTools

3. BROWSER ARGUMENTS:
   - args=['--start-maximized', '--no-sandbox', ...]
   - ignore_default_args=['--enable-automation', ...]

4. CONTEXT OPTIONS:
   - viewport={'width': 1920, 'height': 1080}
   - user_agent='custom user agent string'
   - geolocation={'latitude': 37.7749, 'longitude': -122.4194}
   - permissions=['geolocation', 'camera', 'microphone']
   - device_scale_factor=2
   - is_mobile=True/False
   - has_touch=True/False

5. STORAGE & STATE:
   - storage_state='path/to/state.json'
   - accept_downloads=True/False
   - downloads_path='./downloads'

6. RECORDING OPTIONS:
   - record_video_dir='./videos'
   - record_video_size={'width': 1280, 'height': 720}
   - record_har_path='./network.har'

7. NETWORK & PROXY:
   - proxy={'server': 'http://proxy:8080', 'username': 'user', 'password': 'pass'}

8. CHANNELS:
   - channel='chrome'     # Use Google Chrome
   - channel='msedge'     # Use Microsoft Edge
   - channel='chrome-beta' # Use Chrome Beta

9. PERSISTENT CONTEXT:
   - launch_persistent_context(user_data_dir='./profile')

10. TIMEOUTS:
    - timeout=60000        # Launch timeout
    - set_default_timeout(30000)  # Operation timeout
    - set_default_navigation_timeout(60000)  # Navigation timeout

🎯 TARGET WEBSITE USED: https://saucelabs.com
📚 API TYPES: Both Synchronous (sync_playwright) and Asynchronous (async_playwright)
"""

if __name__ == "__main__":
    run_all_examples()
