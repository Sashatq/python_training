from model.group import Group


def test_delete_first_group(app):
    count_1 = app.group.count()
    if count_1 == 0:
        app.group.create(Group(name="asd", header="asd", footer="asd"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)

