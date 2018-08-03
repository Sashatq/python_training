# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import time, unittest
from contact import Contact


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
        self.login(wd, username="admin", password="secret")
        self.add_new_contact(wd)
        self.fill_form(wd, Contact(name="Alex", midname="Piter", lastname="Pop", nick="DVP", title="Sec", company="IBM", address_main="Moscow, mihaylov str 11", home_tel="+74655556612",
                       mobile_tel="+79994561111", work_tel="+74995552312", fax="258963147", mail1="asd@mail.ru", mail2="asd@mail.com", mail3="asd@mail.net",
                       home_page="https://home.com/", address_second="Moscow, Pochats str", second_tel="123", notes="TEST"))
        self.add_birthday(wd)
        self.add_anniversary(wd)
        self.create_contact(wd)
        self.check_contact(wd)
        self.logout(wd)
        self.assertTrue(success)

    def login(self, wd, username, password):
        # Login
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def add_new_contact(self, wd):
        # Init contact creation
        wd.find_element_by_link_text("add new").click()

    def fill_form(self, wd, contact):
        # General info
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("middlename").send_keys(contact.midname)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nick)
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address_main)
        # Telephone info
        wd.find_element_by_name("home").send_keys(contact.home_tel)
        wd.find_element_by_name("mobile").send_keys(contact.mobile_tel)
        wd.find_element_by_name("work").send_keys(contact.work_tel)
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").send_keys(contact.mail1)
        wd.find_element_by_name("email2").send_keys(contact.mail2)
        wd.find_element_by_name("email3").send_keys(contact.mail3)
        wd.find_element_by_name("homepage").send_keys(contact.home_page)
        # Secondary info
        wd.find_element_by_name("address2").send_keys(contact.address_second)
        wd.find_element_by_name("phone2").send_keys(contact.second_tel)
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def add_birthday(self, wd):
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[5]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[5]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[8]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[8]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1990")

    def add_anniversary(self, wd):
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[10]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[10]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[11]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[11]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2000")

    def create_contact(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def check_contact(self, wd):
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[7]/a/img").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
