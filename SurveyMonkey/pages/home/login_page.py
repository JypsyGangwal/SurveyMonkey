from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):
    # locators ---------
    login_link = "//a[@class='log-in static-buttons']"
    user_name = "//input[@id='username']"
    password = "//input[@id='password']"
    submit = "//button[@type='submit']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_login_link(self):
        self.elementClick(self.login_link, locatorType="xpath")

    def enter_username_field(self, username):
        self.set_value(username, self.user_name, locatorType="xpath")

    def enter_password_field(self, password):
        self.set_value(password, self.password, locatorType="xpath")

    def click_submit_button(self):
        self.elementClick(self.submit, locatorType="xpath")

    def login(self, username=None, password=None):
            self.click_login_link()
            self.enter_username_field(username)
            self.enter_password_field(password)
            self.click_submit_button()

    def verify_login_Success(self, exp_title):
        title = self.driver.title
        print(title)

        if title == exp_title:
            print("login successs")
        else:
            print("login fail")

    def verify_login_failed(self):

        result = self.isElementPresent("//div[@class='error-message']/ul/li[contains(text(),'"
                                       "The username or password you entered is incorrect."
                                       " Please try again--and remember that passwords "
                                       "are case sensitive.')]", "xpath")
        print (result)
        return result
