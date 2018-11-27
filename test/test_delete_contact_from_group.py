def test_delete_contact_from_group(app, db):
    app.contact.select_group()
    contact_in_group_page = app.contact.contact_in_group_list()
    assert len(contact_in_group_page) > 0
    app.contact.delete_contact_from_group()
    assert db.get_contact_in_group != db.get_contact_not_in_group
