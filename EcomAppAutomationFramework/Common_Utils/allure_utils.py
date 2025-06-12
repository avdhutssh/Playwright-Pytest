import json
import allure
import os
from datetime import datetime

def attach_screenshot(page, name="Screenshot"):
    """
    Take a screenshot and attach it to the Allure report
    """
    try:
        screenshot = page.screenshot()
        allure.attach(
            screenshot,
            name=f"{name} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            attachment_type=allure.attachment_type.PNG
        )
    except Exception as e:
        print(f"Warning: Could not attach screenshot: {e}")

def attach_html(page, name="HTML"):
    """
    Attach HTML content to the Allure report
    """
    try:
        html_content = page.content()
        allure.attach(
            html_content,
            name=f"{name} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            attachment_type=allure.attachment_type.HTML
        )
    except Exception as e:
        print(f"Warning: Could not attach HTML: {e}")

def attach_text(text, name="Text"):
    """
    Attach text to the Allure report
    """
    try:
        allure.attach(
            str(text),
            name=f"{name} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            attachment_type=allure.attachment_type.TEXT
        )
    except Exception as e:
        print(f"Warning: Could not attach text: {e}")

def attach_json(json_data, name="JSON"):
    """
    Attach JSON data to the Allure report
    """
    try:
        if not isinstance(json_data, str):
            json_data = json.dumps(json_data, indent=4)
        
        allure.attach(
            json_data,
            name=f"{name} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            attachment_type=allure.attachment_type.JSON
        )
    except Exception as e:
        print(f"Warning: Could not attach JSON: {e}")

def attach_api_request(url, method, headers, data=None, json_data=None):
    """
    Attach API request details to the Allure report
    """
    try:
        request_info = f"URL: {url}\nMethod: {method}\nHeaders: {json.dumps(headers, indent=4)}"
        
        if data:
            if isinstance(data, str):
                try:
                    # Try to parse as JSON if it's a string
                    json_obj = json.loads(data)
                    request_info += f"\nData: {json.dumps(json_obj, indent=4)}"
                except:
                    request_info += f"\nData: {data}"
            else:
                request_info += f"\nData: {data}"
                
        if json_data:
            request_info += f"\nJSON: {json.dumps(json_data, indent=4)}"
        
        allure.attach(
            request_info,
            name=f"API Request - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            attachment_type=allure.attachment_type.TEXT
        )
    except Exception as e:
        print(f"Warning: Could not attach API request: {e}")

def attach_api_response(response):
    """
    Attach API response details to the Allure report
    """
    try:
        try:
            response_json = response.json()
            allure.attach(
                json.dumps(response_json, indent=4),
                name=f"API Response JSON - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                attachment_type=allure.attachment_type.JSON
            )
        except:
            # If not JSON, attach as text
            response_text = response.text()
            allure.attach(
                response_text,
                name=f"API Response Text - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                attachment_type=allure.attachment_type.TEXT
            )
        
        # Attach response metadata
        metadata = f"Status: {response.status} {response.status_text}\nHeaders: {json.dumps(dict(response.headers), indent=4)}"
        allure.attach(
            metadata,
            name=f"API Response Metadata - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            attachment_type=allure.attachment_type.TEXT
        )
    except Exception as e:
        print(f"Warning: Could not attach API response: {e}") 