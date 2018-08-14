from model.contact import Contact


def test_delete_first_contact(app):
    count_2 = app.contact.count()
    if count_2 == 0:
        app.contact.fill_form(Contact(name="TEST_DELETE", midname="TEST_DELETE2", lastname="TEST_DELETE3"))
    app.contact.test_delete_first_contact()
