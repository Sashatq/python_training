import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True  # Сбрасывает кэш после выполнения каждого запроса

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row  # магия! можно заменить на for row in cursor.fetchall():
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")  # столбец из бд, который заполняется датой при удалении контакта
            for row in cursor:
                (id_contact, name, lname) = row  # магия! можно заменить на for row in cursor.fetchall():
                list.append(Contact(id_contact=str(id_contact), name=name, lname=lname))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
