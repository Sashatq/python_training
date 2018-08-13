def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.test_edit_first_contact(nick="EDIT", firstname="EDIT", middlename="EDIT", lastname="EDIT")


