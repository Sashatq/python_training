from model.contact import Contact
import pytest
import random
import string
import time


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Contact(lname=random_string("l", 8), name=random_string("n", 4), work=random_string("7888", 5))
             for i in range(5)]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_create_contact(app, contact):
    old_contact = app.contact.get_contact_list()
    app.contact.create(contact)
    time.sleep(2)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
