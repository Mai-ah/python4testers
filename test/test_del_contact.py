# -*- coding: utf-8 -*-
from model.contact import Contact


def test_dell_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Anna", middlename="Katarzyna", lastname="Góra", nickname="Lalala",
                               title="Tytuł", company="Firma", address="Adres1", phone1="123456789",
                               phone2="987654321", phone3="1122334455", fax="9988776655",
                               email1="milena.zahorska@gmail.com", email2="mail2@exsample.com",
                               email3="mail3@exsample.com", homepage="www.wp.pl", birthday_y="1985",
                               anniversary_y="2020", alt_address="Adres2", alt_phone="66554433", notes="uwagi"))
    old_contacts = app.contact.get_contact_list()
    app.contact.del_first()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts



