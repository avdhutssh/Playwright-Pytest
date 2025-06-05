from playwright.sync_api import Page, expect


def test_handleFrames(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    frame = page.frame_locator("#courses-iframe")
    frame.get_by_role("link", name="All Access plan").click()
    expect(frame.locator("body")).to_contain_text("Unlimited Life time Access")
    print("✅ Successfully interacted with the frame")