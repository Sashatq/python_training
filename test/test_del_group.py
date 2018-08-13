from model.group import Group


def test_delete_first_group(app):
    count_1 = app.group.count()
    if count_1 == 0:
        app.group.create(Group(name="name"))
    app.group.delete_first_group()

