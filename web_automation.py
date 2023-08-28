from appium import webdriver
from appium.webdriver.common.mobileby import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoAlertPresentException
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import subprocess

import time
import os

desired_caps = {
    "deviceName": "Galaxy Note20 Ultra 5G",
    "platformName": "Android",
    "platformVersion": "11",
    "isRealMobile": True,
    "build": "Python Vanilla Android",
    "name": "Sample Test - Python",
    "browserName":"Chrome",
    "version":"latest",
    "network": False,
    "visual": True,
    "video": True,
    "autoGrantPermissions":True,
    "gpsEnabled":True
}

def accept_location_permission(driver):
    try:
        # Switch to the native app context
        driver.switch_to.context("NATIVE_APP")
        
        # Find and interact with the "Allow" button on the location permission popup
        allow_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.android.package:id/allow_button_id"))
        )
        allow_button.click()
        
        # Switch back to the web context
        driver.switch_to.context("WEBVIEW")
    except NoAlertPresentException:
        print("Location permission popup not found or already handled.")


def scroll_to_percentage(driver, percentage):
    scroll_command = "window.scrollTo(0, document.body.scrollHeight * %f);" % percentage
    driver.execute_script(scroll_command)

def startingTest():

    if os.environ.get("LT_USERNAME") is None:
        # Enter LT username here if environment variables have not been added
        username = "username"
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        # Enter LT accesskey here if environment variables have not been added
        accesskey = "accesskey"
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")

    try:
        driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor="https://" +
                                  "ritamg"+":"+"lHWNSA0QECwjeN8DoDb9U6KyXMBgAFXqlIIArkxeOTDSeEdLyG"+"@mobile-hub.lambdatest.com/wd/hub")

        driver.get("https://stg.aemsites:F93bwU8c9G@uat-www.veerboats.com/")
        scroll_to_percentage(driver, 0.2)
        time.sleep(10)
        element=driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[10]/div/div/div/div[1]/button")
        if element.is_displayed():  # Check if the element is visible
            element.click()
        else:
            print("Element is not visible. Performing other operations...")
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[4]/div/div/div[2]/div/div/div[5]/div/div/div[1]/div/div[3]/div/a").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[4]/div[3]").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[4]/div[3]").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[3]/div[1]/ol/li[1]/div/label").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[3]/div[1]/ol/li[2]/div/label").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[3]/div[1]/ol/li[3]/div/label").click()
        print("Moving to acessory track")
        start_x = driver.get_window_size()['width'] // 2
        start_y = driver.get_window_size()['height'] // 2
        end_x = start_x
        end_y = driver.get_window_size()['height'] // 8  # Adjust the fraction as needed

        driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[3]/div[2]/ol/li[1]/div/label").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[4]/div[3]").click()
        start_x = driver.get_window_size()['width'] // 2
        start_y = driver.get_window_size()['height'] // 2
        end_x = start_x
        end_y = driver.get_window_size()['height'] // 8  # Adjust the fraction as needed

        driver.swipe(start_x, start_y, end_x, end_y, duration=1000)

        start_x = driver.get_window_size()['width'] // 2
        start_y = driver.get_window_size()['height'] // 2
        end_x = start_x
        end_y = driver.get_window_size()['height'] // 8  # Adjust the fraction as needed

        driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[2]/a").click()
        driver.switch_to.context('NATIVE_APP')
        driver.find_element_by_xpath((".//android.widget.Button[@text='Block']")).click()
        time.sleep(10)
        x = 564
        y = 1022

        # Perform the tap action
        action = TouchAction(driver)
        action.tap(x=x, y=y).perform()
        contexts = driver.contexts
        for context in contexts:
            print(context)
        driver.switch_to.context('CHROMIUM')
        print("Content Switched")
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[5]/div/div/div[1]/div[2]/div[2]/input").send_keys("Orland")
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[5]/div/div/div[1]/div[2]/div[2]/div/div[1]").click()
        time.sleep(10)
        start_x = driver.get_window_size()['width'] // 2
        start_y = driver.get_window_size()['height'] // 2
        end_x = start_x
        end_y = driver.get_window_size()['height'] // 8  # Adjust the fraction as needed

        driver.swipe(start_x, start_y, end_x, end_y, duration=1000)

        start_x = driver.get_window_size()['width'] // 2
        start_y = driver.get_window_size()['height'] // 2
        end_x = start_x
        end_y = driver.get_window_size()['height'] // 8  # Adjust the fraction as needed

        driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
        start_x = driver.get_window_size()['width'] // 2
        start_y = driver.get_window_size()['height'] // 2
        end_x = start_x
        end_y = driver.get_window_size()['height'] // 8  # Adjust the fraction as needed

        driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[5]/div/div/div[2]/div[1]/div[4]/div/div[2]/div/div[2]/div[3]/div[1]/button").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/form/div[3]/div/input").send_keys("FTEST")
        driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
        start_x = driver.get_window_size()['width'] // 2
        start_y = driver.get_window_size()['height'] // 2
        end_x = start_x
        end_y = driver.get_window_size()['height'] // 8  # Adjust the fraction as needed

        driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
        driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
        start_x = driver.get_window_size()['width'] // 2
        start_y = driver.get_window_size()['height'] // 2
        end_x = start_x
        end_y = driver.get_window_size()['height'] // 8  # Adjust the fraction as needed

        driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/form/div[4]/div/input").send_keys("LTEST")
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/form/div[6]/div/input").send_keys("test@test.com")
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/form/div[7]/div/input").send_keys("8764783922")
        start_x = driver.get_window_size()['width'] // 2
        start_y = driver.get_window_size()['height'] // 2
        end_x = start_x
        end_y = driver.get_window_size()['height'] // 8  # Adjust the fraction as needed
        driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/form/div[9]/div/input").send_keys("10770 CA-41")
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/form/div[10]/div/input").send_keys("MADISON")
        start_x = driver.get_window_size()['width'] // 2
        start_y = driver.get_window_size()['height'] // 2
        end_x = start_x
        end_y = driver.get_window_size()['height'] // 8  # Adjust the fraction as needed
        driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/form/div[11]/fieldset/div/div[1]/input").click()
        time.sleep(10)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/form/div[12]/div/input").send_keys("35013")
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/form/div[14]/div/input").send_keys("TEST TEST")
        driver.find_element_by_xpath("/html/body/form/input[2]").send_keys("4111111111111111")


        # print("Moving To Forms")
        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/form/div[2]/div/input").send_keys("FTEST")
        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/form/div[3]/div/input").send_keys("LTEST")
        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/form/div[4]/div/input").send_keys("test@test.com")
        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/form/div[5]/div/input").send_keys("8764783922")
        # start_x = driver.get_window_size()['width'] // 2
        # start_y = driver.get_window_size()['height'] // 2
        # end_x = start_x
        # end_y = driver.get_window_size()['height'] // 8  # Adjust the fraction as needed

        # driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/form/div[7]/div/input").send_keys("210309")
        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/form/div[6]").click()
        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/form/div[6]/fieldset").click()
        # x = 992
        # y = 1126

        # # Perform the tap action
        # action = TouchAction(driver)
        # action.tap(x=x, y=y).perform()
        # time.sleep(10)
        # # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/form/div[6]/fieldset/select").click()
        # # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/form/div[8]/fieldset/label/span[1]").click()
        # # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/form/div[9]").click()

        # print("Clicked On Checkmarks")
        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/form/div[8]/fieldset/label/span[1]").click()
        # time.sleep(15)
        # # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/form/div[8]/fieldset/label/span[1]").click()
        # print("moving......")
        # start_x = driver.get_window_size()['width'] // 2
        # start_y = driver.get_window_size()['height'] // 2
        # end_x = start_x
        # end_y = driver.get_window_size()['height'] // 8  # Adjust the fraction as needed

        # driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
        # start_x = driver.get_window_size()['width'] // 2
        # start_y = driver.get_window_size()['height'] // 2
        # end_x = start_x
        # end_y = driver.get_window_size()['height'] // 8  # Adjust the fraction as needed

        # driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
        # start_x = driver.get_window_size()['width'] // 2
        # start_y = driver.get_window_size()['height'] // 2
        # end_x = start_x
        # end_y = driver.get_window_size()['height'] // 8  # Adjust the fraction as needed

        # driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/form/div[9]/fieldset").click()
        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/form/div[9]/fieldset/div/p").click()
        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/form/div[9]/fieldset/div").click()
        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/form/div[9]/fieldset").click()
        # #driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/form/div[9]/fieldset/label/span[1]").click()
        # x = 58
        # y = 1165
        # # Perform the tap action
        # action = TouchAction(driver)
        # action.tap(x=x, y=y).perform()
        # time.sleep(10)
        # print("Clicked On Secound Checkmark")
        # time.sleep(10)
        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/form/div[10]/button").click()
        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/form/div[6]/fieldset").click()
        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/form/div[7]/div/input").send_keys("210309")
        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/form/div[8]/fieldset/label/span[1]").click()
        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/form/div[9]").click()
        
        






# Send the text "orland"
        
        # start_x = driver.get_window_size()['width'] // 2
        # start_y = driver.get_window_size()['height'] // 2
        # end_x = start_x
        # end_y = driver.get_window_size()['height'] // 15  # Adjust the fraction as needed

        # driver.swipe(start_x, start_y, end_x, end_y, duration=2000)

        # start_x = driver.get_window_size()['width'] // 2
        # start_y = driver.get_window_size()['height'] // 2
        # end_x = start_x
        # end_y = driver.get_window_size()['height'] // 8  # Adjust the fraction as needed

        # driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
        # start_x = driver.get_window_size()['width'] // 2
        # start_y = driver.get_window_size()['height'] // 2
        # end_x = start_x
        # end_y = driver.get_window_size()['height'] // 15  # Adjust the fraction as needed

        # driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div/div/div[1]/div[9]/div[2]/div[2]/div[4]/div[3]").click()

        # element_to_click = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[7]/div/div/div[2]/div/div/div[2]/div/button")

        # # Scroll to the element and click on it
        # scroll_to_element_and_click(driver, element_to_click)
        # time.sleep(1)
        # driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[10]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/form/div[3]/div").click()
        # driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[10]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/form/div[3]/div/input").send_keys("Ritama")
        # driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[10]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/form/div[4]/div").click()
        # driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[10]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/form/div[4]/div/input").send_keys("Gangulii")
        # driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[10]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/form/div[5]/div").click()
        # driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[10]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/form/div[5]/div/input").send_keys("ritamg1237@xyz.com")
        # scroll_by_percentage(driver, 40)
        # driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[10]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/form/div[6]").click()
        # driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[10]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/form/div[8]/div").click()
        # driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[10]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/form/div[8]/div/input").send_keys("7001522073")
        # driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[10]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/form/div[6]").click()
        # driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[10]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/form/div[9]").click()
        # #driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[10]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/form/div[6]").click()
        # # driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[10]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/form/div[6]/fieldset/label/span[1]").click()
        # driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[10]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/form/div[10]/button").click()
        # driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[10]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/form/div[10]/button").click()
        # driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[10]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/form/div[10]/button").click()
        time.sleep(30)

        driver.quit()
    except:
        driver.quit()


startingTest()
