# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, title=title,
            company=company, address=address, homephone=homephone, mobilephone=mobilephone, workphone=workphone, fax=fax,
            email1=email1, email2=email2, email3=email3, homepage=homepage, birthday_y=birthday_y,
            anniversary_y=anniversary_y, alt_address=alt_address, alt_phone=alt_phone, notes=notes)
    for firstname in ["", random_string ("firstname", 15)]
    for middlename in ["", random_string ("middlename", 15)]
    for lastname in ["", random_string ("lastname", 15)]
    for nickname in ["", random_string ("nickname", 10)]
    for title in ["", random_string ("title", 30)]
    for company in ["", random_string ("company", 20)]
    for address in ["", random_string ("address", 10)]
    for homephone in ["", random_string ("homephone", 10)]
    for mobilephone in ["", random_string ("mobilephone", 10)]
    for workphone in ["", random_string ("workphone", 10)]
    for fax in ["", random_string ("fax", 10)]
    for email1 in ["", random_string ("email1", 10)]
    for homepage in ["", random_string ("homepage", 10)]
    for email2 in ["", random_string("email2", 10)]
    for email3 in ["", random_string("email3", 10)]
    for birthday_y in ["", random_string("birthday_y", 10)]
    for anniversary_y in ["", random_string("anniversary_y", 10)]
    for alt_address in ["", random_string("alt_address", 10)]
    for alt_phone in ["", random_string("alt_phone", 10)]
    for notes in ["", random_string("notes", 10)]
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
