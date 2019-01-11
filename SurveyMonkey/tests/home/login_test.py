import unittest
from selenium import webdriver
import pytest

from pages.home.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self,oneTimeSetUp):
        self.lp = LoginPage(self.driver)


    @pytest.fixture(autouse=True)
    def test_invalid_login(self,oneTimeSetUp):
        print("enter invalif fucny")
        self.lp.login("automt1","test123")
        result = self.lp.verify_login_failed()
        print (result)
        assert result == True
        print("Error message verified")


    def test__valid_login(self,oneTimeSetUp):
        self.lp.login("auto_mt1", "test$123")
        self.lp.verify_login_Success("Welcome to SurveyMonkey!")











