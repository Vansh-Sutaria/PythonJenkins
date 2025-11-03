import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_google_search():
    # 1. Setup Chrome Options for Headless Mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox") # Good practice for CI
    
    # 2. Instantiate Driver
    # Assumes chromedriver.exe is in the Windows PATH
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.google.com")
        
        # 3. Assertion and Cleanup
        assert "Google" in driver.title
        print(f"Test Passed: Title is {driver.title}")
        
    except Exception as e:
        pytest.fail(f"Test Failed: Could not run test. Error: {e}")
    finally:
        if 'driver' in locals():
            driver.quit()