from model.contact import Contact
from random import randrange


def test_delete_first_contact(app):
    count = app.contact.count()
    if count == 0:
        app.contact.create(Contact(name="for_delete", mname="for_delete", lname="for_delete", nick="for_delete"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    app.contact.delete_contact_by_index(index)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
    old_contact[index:index+1] = []
    assert old_contact == new_contact
