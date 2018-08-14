from model.contact import Contact


def create_contact(app):
    app.contact.create(Contact(name="asd", mname="asd", lname="asd", nick="asd"))
