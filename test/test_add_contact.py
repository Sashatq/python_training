# -*- coding: utf-8 -*-
from model.contact import Contact


def test_test_add_contact(app):
    app.contact.fill_form(Contact(name="Alex", midname="Piter", lastname="Pop"))

