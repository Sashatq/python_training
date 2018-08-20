from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app):
    count1 = app.contact.count_groups()
    if count1 == 0:
        app.group.create(Group(name="FOR TEST", header="FOR TEST", footer="FOR TEST"))
    app.contact.choose_group()
    # не верный тест, доработать метод определения отсутствия групп