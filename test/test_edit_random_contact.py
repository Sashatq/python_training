from model.contact import Contact
from random import randrange


def test_edit_random_contact(app):
    count = app.contact.count()
    if count == 0:
        app.contact.create(Contact(name="U", mname="C", lname="F"))
    old_contact = app.contact.get_contact_list()
    contact = Contact(name="edited", mname="edited", lname="edited")
    index = randrange(len(old_contact))
    contact.id_contact = old_contact[index].id_contact
    app.contact.edit_contact_by_index(index, contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[index] = contact
    g = old_contact
    old_contact2 = sorted(old_contact, key=Contact.id_or_max)
    contact2 = sorted(new_contact, key=Contact.id_or_max)
    pass
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
