from model.contact import Contact


def test_create_contact(app):
    app.contact.create(name="asd", mname="asd", lname="asd", nick="asd")
