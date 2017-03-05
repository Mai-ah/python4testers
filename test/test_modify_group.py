# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="2", header="3", footer="4"))
    app.session.logout()

def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="5"))
    app.session.logout()
