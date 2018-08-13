from model.group import Group

def test_modify_group_name(app):
    app.group.test_modify_first_group(Group(name="NEW Group"))


def test_modify_group_header(app):
    app.group.test_modify_first_group(Group(header="NEW header"))

