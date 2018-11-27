from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create.contact(Contact(name='for_group', lname="for_group"))
    app.group.create(Group(name="add_contact_here", header="add_contact_here", footer="add_contact_here"))
    app.contact.add_to_group()
    new_contact_in_group_page = app.contact.contact_in_group_list()
    assert len(new_contact_in_group_page) > 0
    assert db.get_contact_in_group != db.get_contact_not_in_group















#Главная
#Выбираем контакт
#Выбираем группу
#Нажимаем добавить
#Нажимаем перейти в группу
#Получаем ид группы
#-
#Записываем из базы не пустую группу с нашим айдишником
#Сравниваем