"""
Simple Browser Context Manager - Minimal Code
"""

from playwright.sync_api import sync_playwright
import time

# Global storage for contexts and pages
playwright_instance = None
browser = None
contexts = {}  # Will store: {"AmazonContext": context, "FlipkartContext": context, etc.}
pages = {}     # Will store: {"AmazonContext": page, "FlipkartContext": page, etc.}

# App URLs
app_urls = {
    'amazon': 'https://www.amazon.com',
    'flipkart': 'https://www.flipkart.com',
    'ebay': 'https://www.ebay.com'
}

def start_browser():
    """Start browser if not already started"""
    global playwright_instance, browser
    if not browser:
        playwright_instance = sync_playwright().start()
        browser = playwright_instance.chromium.launch(headless=False, args=['--start-maximized'])
        print("🚀 Browser started")

def OpenApplication(app_name):
    """
    Open application and return context name
    Usage: OpenApplication("Amazon") returns "AmazonContext"
    """
    global contexts, pages
    
    start_browser()
    
    context_name = f"{app_name}Context"
    app_url = app_urls[app_name.lower()]
    
    # Create context and page
    context = browser.new_context(viewport={'width': 1920, 'height': 1080})
    page = context.new_page()
    page.goto(app_url)
    
    # Store for later use
    contexts[context_name] = context
    pages[context_name] = page
    
    print(f"✅ Opened {app_name} - Context: {context_name}")
    return context_name

def cleanup():
    """Close everything"""
    global playwright_instance, browser, contexts, pages
    for context in contexts.values():
        context.close()
    if browser:
        browser.close()
    if playwright_instance:
        playwright_instance.stop()
    contexts.clear()
    pages.clear()
    print("🛑 Cleanup completed")

if __name__ == "__main__":
    # Demo
    OpenApplication("Amazon")
    OpenApplication("Flipkart")
    OpenApplication("Ebay")
    time.sleep(3)
    cleanup() 

"""
Simple pytest for browser contexts
"""

import pytest
import time
from _02_InvokeBrowserAdvance import OpenApplication, contexts, pages, cleanup

def test_open_applications_and_use_contexts():
    """Test opening apps and using contexts later"""
    
    # Open applications
    amazon_context = OpenApplication("Amazon")
    flipkart_context = OpenApplication("Flipkart") 
    ebay_context = OpenApplication("Ebay")
    
    time.sleep(2)
    
    # Now use the contexts later in code
    print("\n🔄 Using contexts later...")
    
    # Reload Amazon using AmazonContext
    pages[amazon_context].reload()
    pages[amazon_context].title()
    print(f"📄 Amazon Title: {pages[amazon_context].title()}")

    # Use flipkart_context to reload and get title
    pages[flipkart_context].reload()
    flipkart_title = pages[flipkart_context].title()
    print(f"📄 Flipkart Title: {flipkart_title}")

    # Use ebay_context to reload and get title
    pages[ebay_context].reload()
    ebay_title = pages[ebay_context].title()
    print(f"📄 eBay Title: {ebay_title}")
    time.sleep(3)
    # You can also use contexts directly for other actions:
    # contexts[amazon_context].new_page()  # Create new page in Amazon context
    # pages[flipkart_context].click("button")  # Click something in Flipkart
    # pages[ebay_context].fill("input", "text")  # Fill input in eBay
    cleanup()

if __name__ == "__main__":
    test_open_applications_and_use_contexts()