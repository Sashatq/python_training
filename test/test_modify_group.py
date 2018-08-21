from model.group import Group
from random import randrange


def test_modify_group_name(app):
    count_1 = app.group.count()
    if count_1 == 0:
        app.group.create(Group(name="asd", header="asd", footer="asd"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="i_modify")
    group.id = old_groups[index].id
    app.group.test_modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
#    old_groups = app.group.get_group_list()
#    app.group.test_modify_first_group(Group(header="NEW header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

