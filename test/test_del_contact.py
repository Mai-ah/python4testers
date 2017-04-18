# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_dell_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Anna", middlename="Katarzyna", lastname="Góra", nickname="Lalala",
                               title="Tytuł", company="Firma", address="Adres1", homephone="123456789",
                               mobilephone="987654321", workphone="1122334455", fax="9988776655",
                               email1="milena.zahorska@gmail.com", email2="mail2@exsample.com",
                               email3="mail3@exsample.com", homepage="www.wp.pl", birthday_y="1985",
                               anniversary_y="2020", alt_address="Adres2", alt_phone="66554433", notes="uwagi"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.del_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)



