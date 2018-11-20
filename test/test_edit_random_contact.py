from model.contact import Contact
import random


def test_edit_random_contact(app, db, check_ui, data_contacts):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(name="U", mname="C", lname="F"))
    old_contact = db.get_contact_list()
    contact = random.choice(old_contact)
    contacts = data_contacts
    app.contact.edit_contact_by_id(contact.id_contact, contacts)
    new_contact = db.get_contact_list()
    assert len(old_contact) == len(new_contact)
    if check_ui:
        assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
