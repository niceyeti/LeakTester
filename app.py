from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep

def get_chrome_options():
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

# copied from stinger.rendered_conn for initial testing
def get(driver, url, render_timeout=-1):
    if render_timeout <= 0:
        render_timeout = 5
    print("Rendered conn getting: "+url)
    driver.get(url)
    #print(driver.page_source)
    sleep(render_timeout)
    #print("Scroll one")
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #print("Scroll two")
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    return html, True

if __name__ == "__main__":
    chrome_options = get_chrome_options()
    driver = webdriver.Chrome(options=chrome_options)
    html, success = get(driver, "https://www.example.com", 5)
    print(html)
    print("Success=",success)
    # Do stuff with your driver
    driver.close()
