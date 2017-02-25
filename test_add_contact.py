# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="Milena", middlename="Agnieszka", lastname="Zahorska", nickname="Mai-ah",
                                title="Tytuł", company="Firma", address="Adres1", phone1="123456789",
                                phone2="987654321", phone3="1122334455", fax="9988776655",
                                email1="milena.zahorska@gmail.com", email2="mail2@exsample.com",
                                email3="mail3@exsample.com", homepage="www.wp.pl", birthday_y="1985",
                                anniversary_y="2020", alt_address="Adres2", alt_phone="66554433", notes="uwagi"))
    app.logout()

