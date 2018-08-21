from model.group import Group


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    app.group.test_modify_first_group(Group(name="NEW Group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    old_groups = app.group.get_group_list()
    app.group.test_modify_first_group(Group(header="NEW header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

