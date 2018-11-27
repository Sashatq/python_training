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
            cursor.execute("select id, firstname, lastname, work from addressbook where deprecated='0000-00-00 00:00:00'")  # столбец из бд, который заполняется датой при удалении контакта
            for row in cursor:
                (id_contact, name, lname, work) = row  # магия! можно заменить на for row in cursor.fetchall():
                list.append(Contact(id_contact=str(id_contact), name=name, lname=lname, work=work))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def get_phones_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, work from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id_contact, name, lname, work) = row
                list.append(Contact(id_contact=str(id_contact), name=name, lname=lname, work=work))
        finally:
            cursor.close()
        return list

    def get_contact_in_group(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id from address_in_groups")
            for row in cursor:
                (id_contact) = row  # магия! можно заменить на for row in cursor.fetchall():
                list.append(Contact(id_contact=str(id_contact)))
        finally:
            cursor.close()
        return list

    def get_contact_not_in_group(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id from address_in_groups")
            for row in cursor:
                (id_contact) = row  # магия! можно заменить на for row in cursor.fetchall():
                list.append(Contact(id_contact=str(id_contact)))
        finally:
            cursor.close()
        return list


