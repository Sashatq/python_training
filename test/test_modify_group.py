from model.group import Group
import random


def test_modify_group_name(app, db, check_ui, data_groups):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="asd", header="asd", footer="asd"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    groups = data_groups
    app.group.modify_group_by_id(group.id, groups)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

