from sys import maxsize


class Contact:

    def __init__(self, name=None, mname=None, lname=None, nick=None, company=None, address=None, home=None, mobile=None,
                 work=None, fax=None, email=None, email2=None, email3=None, homepage=None, address2=None,
                 phone2=None, notes=None, id_contact=None):
        self.name = name
        self.mname = mname
        self.lname = lname
        self.nick = nick
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id_contact = id_contact

    def __repr__(self):
        return "%s:%s:%s" % (self.id_contact, self.name, self.lname)

    def __eq__(self, other):
        return (self.id_contact is None or other.id_contact is None or self.id_contact == other.id_contact) \
               and self.name == other.name and self.lname == other.lname

    def id_or_max(self):
        if self.id_contact:
            return int(self.id_contact)
        else:
            return maxsize

