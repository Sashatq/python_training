from model.contact import Contact


def test_delete_first_contact(app):
    count = app.contact.count()
    if count == 0:
        app.contact.create(Contact(name="for_delete", mname="for_delete", lname="for_delete", nick="for_delete"))
    app.contact.delete_first_contact()
