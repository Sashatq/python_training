# -*- coding: utf-8 -*-
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contacts_cache = []
            for element in wd.find_elements_by_name("entry"):
                string = element.find_elements_by_css_selector("td")
                name = string[2].text
                lname = string[1].text
                address = string[3].text
                email = string[4].text
                phones = string[5].text
                id_contact = element.find_element_by_name("selected[]").get_attribute("value")
                self.contacts_cache.append(Contact(name=name, id_contact=id_contact, lname=lname, address=address, email=email, mobile=phones))
        return list(self.contacts_cache)

    def open_contact_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("./") and len(wd.find_elements_by_name("add")) > 0:
            return
        wd.find_element_by_link_text("home").click()

    def count_groups(self):
        wd = self.app.wd
        self.open_contact_page()
        groups = wd.find_elements_by_name("group")
        len_groups = len(groups)
        return len_groups
    # не верный метод, доработать метод определения отсутствия групп

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        contacts = wd.find_elements_by_name("selected[]")
        len_contact = len(contacts)
        return len_contact

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def fill_form(self, contact):
        self.change_field_value("firstname", contact.name)
        self.change_field_value("middlename", contact.mname)
        self.change_field_value("lastname", contact.lname)
        self.change_field_value("nickname", contact.nick)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill form
        self.fill_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def modify_first_contact(self, index, contact):
        self.edit_contact_by_index(index, contact)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        # open modify page
        button = wd.find_elements_by_xpath("//img[@alt='Edit']")
        button[index].click()
        # fill form
        self.fill_form(contact)
        # update
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def choose_group(self):  # Доработать!!!
        wd = self.app.wd
        self.open_contact_page()
        # select contact
        self.select_first_contact()
        # choose first group for contact
        wd.find_element_by_name("to_group").click()
        # press add to %group%
        wd.find_element_by_name("add").click()
        # look for new contact group
