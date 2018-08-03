# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_add_contact(self):
        success = True
        wd = self.wd
        self.login(wd)
        self.add_new_contact(wd)
        self.fill_form(wd)
        self.add_birthday(wd)
        self.add_anniversary(wd)
        self.create_contact(wd)
        self.check_contact(wd)
        self.logout(wd)
        self.assertTrue(success)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def check_contact(self, wd):
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[7]/a/img").click()

    def create_contact(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def add_anniversary(self, wd):
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[10]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[10]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[11]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[11]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2000")

    def add_birthday(self, wd):
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[5]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[5]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[8]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[8]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1990")

    def fill_form(self, wd):
        # General info
        wd.find_element_by_name("firstname").send_keys("Alex")
        wd.find_element_by_name("middlename").send_keys("Piter")
        wd.find_element_by_name("lastname").send_keys("Pop")
        wd.find_element_by_name("nickname").send_keys("DVP")
        wd.find_element_by_name("title").send_keys("Sec")
        wd.find_element_by_name("company").send_keys("IBM")
        wd.find_element_by_name("address").send_keys("Moscow, mihaylov str 11")
        # Telephone info
        wd.find_element_by_name("home").send_keys("+74655556612")
        wd.find_element_by_name("mobile").send_keys("+79994561111")
        wd.find_element_by_name("work").send_keys("+74995552312")
        wd.find_element_by_name("fax").send_keys("258963147")
        wd.find_element_by_name("email").send_keys("asd@mail.ru")
        wd.find_element_by_name("email2").send_keys("asd@mail.com")
        wd.find_element_by_name("email3").send_keys("asd@mail.net")
        wd.find_element_by_name("homepage").send_keys("https://home.com/")
        # Secondary info
        wd.find_element_by_name("address2").send_keys("Moscow, Pochats str")
        wd.find_element_by_name("phone2").send_keys("123")
        wd.find_element_by_name("notes").send_keys("TEST")

    def add_new_contact(self, wd):
        # Init contact creation
        wd.find_element_by_link_text("add new").click()

    def login(self, wd):
        # Login
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
