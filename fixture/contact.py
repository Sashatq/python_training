# -*- coding: utf-8 -*-
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("./") and len(wd.find_elements_by_name("add")) > 0:
            return
        wd.find_element_by_link_text("home").click()

    def create(self):
        wd = self.app.wd
        self.open_contact_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill form
        self.fill_form()


        wd.find_element_by_link_text("add new").click()
        self.fill_form(wd, "ALEX", "ALEX", "ALEX", "ALEX")
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.assertTrue(success)

    def fill_form(self, wd, name, mname, lname, nick):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(mname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nick)

