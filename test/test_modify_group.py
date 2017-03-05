# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    app.group.modify(Group(name="2", header="3", footer="4"))


def test_modify_group_name(app):
    app.group.modify(Group(name="5"))

