from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app):
    count1 = app.contact.count_groups()
    if count1 < 3:
        app.group.create(Group(name="zxc", header="zxc", footer="zxc"))
    app.contact.choose_group()
