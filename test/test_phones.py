from model.contact import Contact
import re


def test_compare_phones(app, db):
    contact_from_home_page = app.contact.get_phones_list()
    contact_from_db = db.get_phones_list()
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)
