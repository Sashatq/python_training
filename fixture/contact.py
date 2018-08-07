class ContactHelper:

    def __init__(self, app1):
        self.app = app1

    def add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_form(self, contact):
        wd = self.app.wd
        self.add_new_contact()
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

    def add_birthday(self, year="1990"):
        wd = self.app.wd
        self.add_birthday()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[5]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[5]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[8]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[8]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(year)

    def add_anniversary(self, day, month, year):
        wd = self.app.wd
        list_of_day = wd.find_elements_by_xpath("//div[@id='content']/form/select[3]//option")
        list_of_day[day].click()
        list_of_month = wd.find_elements_by_xpath("//div[@id='content']/form/select[4]//option")
        list_of_month[month].click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(year)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def create_contact(self):
        wd = self.app.wd
        self.create_contact()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


    def test_edit_first_contact(self, nick="EDIT", lastname="EDIT", middlename="EDIT", firstname="EDIT"):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nick)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()

    def test_delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td/input").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()



