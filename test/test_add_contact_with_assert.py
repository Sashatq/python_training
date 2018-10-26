from model.contact import Contact
import pytest
import random
import string


test_data = [Contact(name="NEW", lname="LNEW", mobile="mobile", work="work")
             for i in range(1)]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact_with_assert(app, contact):
    old_contact = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)



