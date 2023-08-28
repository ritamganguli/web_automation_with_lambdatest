import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# Username: Can be found at the automation dashboard
username = "ritamg"
password = "*****"
# AccessToken: Can be generated from the automation dashboard or profile section
accessToken ="lHWNSA0QECwjeN8DoDb9U6KyXMBgAFXqlIIArkxeOTDSeEdLyG"
gridUrl = "hub.lambdatest.com/wd/hub"

#Generate your capabilities from lambdatest capability generator and select selenium version 3 or 4
capabilities = {
    'LT:Options': {
        "build": "your build name",
        "name": "your test name",
        "platformName": "Windows 10",
        "visual": True,
		"video": True,
    },
    "browserName": "Chrome",
    "browserVersion": "latest",
    "console": "info"
}

url = f"https://{username}:{accessToken}@{gridUrl}"

driver = webdriver.Remote(
    command_executor=url,
    desired_capabilities=capabilities
)

driver.get("https://www.google.com/") #used to search web pages wit .get you can get into the links 
driver.maximize_window() #maximizes the window
time.sleep(3) #waits or stands for n secound for further command to execute
driver.find_element("name", "q").send_keys("LambdaTest Login") 
driver.find_element("name", "q").send_keys(Keys.ENTER) #find_element you can find by id,or you can find by xpath
driver.find_element("partial link text", "Log in - LambdaTest").click()
driver.find_element("id","email").send_keys(username) #send keys is used to used to send elements log or files or text to the web app
driver.find_element("id","password").send_keys(password)
driver.find_element("id", "login-button").click()
time.sleep(10)
driver.quit() #please always quit the driver so that it doent reaches ideal time out
