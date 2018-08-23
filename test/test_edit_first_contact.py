from model.contact import Contact
from random import randrange


def test_edit_first_contact(app):
    count = app.contact.count()
    if count == 0:
        app.contact.edit_first_contact(Contact(name="U", mname="C", lname="F"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact = Contact(name="i_modify")
    contact.id = old_contact[index].id
    app.contact.edit_first_contact_by_index(index, contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

