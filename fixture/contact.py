# -*- coding: utf-8 -*-
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lname = cells[1].text
                name = cells[2].text
                id_contact = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id_contact=id_contact, lname=lname, name=name, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_phones_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lname = cells[1].text
                name = cells[2].text
                id_contact = cells[0].find_element_by_tag_name("input").get_attribute("value")
                work = cells[5].text
                self.contact_cache.append(Contact(id_contact=id_contact, lname=lname, name=name, work=work))
        return list(self.contact_cache)

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
        wd.find_element_by_xpath("//a[contains(text(),'home page')]").click()
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

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_contact_page()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_all(self):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_css_selector('#MassCB').click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_contact_page()
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

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(id)
        # open modify page
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
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

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        name = wd.find_element_by_name("firstname").get_attribute("value")
        lname = wd.find_element_by_name("lastname").get_attribute("value")
        id_contact = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(name=name, lname=lname, id_contact=id_contact, home=home, mobile=mobile, work=work, phone2=phone2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work, phone2=phone2)
