from model.group import Group
from data.groups import test_data


class GroupHelper:

    def __init__(self, app):
        self.app = app

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creations
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group()
        self.group_cache = None

    def test_modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # open modify form
        wd.find_element_by_name("edit").click()
        # fill form
        self.fill_group_form(new_group_data)
        # submit modify
        wd.find_element_by_name("update").click()
        self.return_to_group()
        self.group_cache = None

    def modify_group_by_id(self, id, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # open modify form
        wd.find_element_by_name("edit").click()
        # fill form
        self.fill_group_form(group)
        # submit modify
        wd.find_element_by_name("update").click()
        self.return_to_group()
        self.group_cache = None

    def modify_first_group(self):
        self.test_modify_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group()
        self.group_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def select_first_group(self):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()

    def return_to_group(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        groups = wd.find_elements_by_name("selected[]")
        len_group = len(groups)
        return len_group

    def open_groups_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0:
            return
        wd.find_element_by_link_text("groups").click()



