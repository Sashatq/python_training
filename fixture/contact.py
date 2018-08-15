# -*- coding: utf-8 -*-
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("./") and len(wd.find_elements_by_name("add")) > 0:
            return
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        elemets = wd.find_elements_by_css_selector("li > a")
        contacts = wd.find_elements_by_name("selected[]")
        len_contact = len(contacts)
        return len_contact

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.name)
        self.change_field_value("middlename", contact.mname)
        self.change_field_value("lastname", contact.lname)
        self.change_field_value("nickname", contact.nick)

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill form
        self.fill_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def edit_first_contact(self, new_group_data):
        wd = self.app.wd
        self.open_contact_page()
        # open modify page
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill form
        self.fill_form(new_group_data)
        # update
        wd.find_element_by_name("update").click()
