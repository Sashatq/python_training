from model.contact import Contact
import random
import time


def test_delete_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(name="for_delete", mname="for_delete", lname="for_delete", nick="for_delete"))
    old_contact = db.get_contact_list()
    contact = random.choice(old_contact)
    app.contact.delete_contact_by_id(contact.id_contact)
    new_contact = db.get_contact_list()
    #time.sleep(2)
    assert len(old_contact) - 1 == len(new_contact)
    old_contact.remove(contact)
    assert old_contact == new_contact
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
