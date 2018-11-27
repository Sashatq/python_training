from selenium.webdriver.support.ui import Select
from model.contact import Contact
from model.group import Group


def test_select(app):
    app.contact.select()
