# -*- coding: utf-8 -*-
from model.group import Group


def test_test_add_group(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()  # читаем из бд
    app.group.create(group)
    new_groups = db.get_group_list()  # читаем из бд
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
