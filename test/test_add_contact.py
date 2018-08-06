# -*- coding: utf-8 -*-
from model.contact import Contact


def test_test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.fill_form(Contact(name="Alex", midname="Piter", lastname="Pop", nick="DVP", title="Sec",
                                  company="IBM", address_main="Moscow, mihaylov str 11", home_tel="+74655556612",
                                  mobile_tel="+79994561111", work_tel="+74995552312",
                                  fax="258963147", mail1="asd@mail.ru", mail2="asd@mail.com", mail3="asd@mail.net",
                                  home_page="https://home.com/", address_second="Moscow, Pochats str",
                                  second_tel="123", notes="TEST"))
    app.contact.add_anniversary(day=10, month=7, year="2000") # day -1
    app.session.logout()
