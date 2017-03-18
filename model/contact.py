from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, phone1=None, phone2=None, phone3=None, fax=None, email1=None, email2=None, email3=None,
                 homepage=None, birthday_y=None, anniversary_y=None, alt_address=None, alt_phone=None, notes=None,
                 id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.phone1 = phone1
        self.phone2 = phone2
        self.phone3 = phone3
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birthday_y = birthday_y
        self.anniversary_y = anniversary_y
        self.alt_address = alt_address
        self.alt_phone = alt_phone
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

