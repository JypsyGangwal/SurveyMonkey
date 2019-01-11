import pytest
import os
from selenium import webdriver

@pytest.yield_fixture(scope="class")
def oneTimeSetUp():
        print("running one time setup")
        driverLocation = "C:\Python35\Lib\site-packages\selenium\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        baseURL = "https://www.monkeytest1.com/"
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.get(baseURL)
        yield driver
        driver.quit()



