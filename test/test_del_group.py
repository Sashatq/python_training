from model.group import Group
import random


def test_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="asd", header="asd", footer="asd"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)  # рандомный выбор
    app.group.delete_group_by_id(group.id)  # в качестве идентификатора выбирается ид
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)  # из списка будет удален элемент равный заданому
    assert old_groups == new_groups
    if check_ui:  # параметр для проверки ui списка групп
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

