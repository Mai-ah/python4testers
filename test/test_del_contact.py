# -*- coding: utf-8 -*-


def test_dell_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.del_first()
    app.session.logout()

