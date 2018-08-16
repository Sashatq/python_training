from model.contact import Contact


def test_create_contact(app):
    app.contact.create(Contact(name="Alex", mname="Peter", lname="Ferguson", nick="DICK", company="IBM",
                               address="1st app", mobile="+7999123", work="GOOGLE",
                               fax="7111444", email="asd@gmail.com", notes="smart"))

