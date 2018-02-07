# -*- coding: utf-8 -*-


import sqlite3
import dao.PermissionDAO as PermissionDAO

conn = sqlite3.connect("example.db")
conn.row_factory = sqlite3.Row


def get_all(person):
    if has_permission_edit(person):
        results = PermissionDAO.get_all()
        print(format_permission_header())
        for row in results:
            print(format_permission(row))
        return True
    return False


def get_all_for_person(person, person_id):
    if has_permission_edit(person):
        results = PermissionDAO.get_for_person(person_id)
        if results is not None:
            print(format_permission_header())
            for row in results:
                print(format_permission(row))
    else:
        print("Forbidden. You are missing necessary permissions.")


def has_permission_add_user(person):
    return PermissionDAO.has_permission(person['id'], "ADD_USERS")


def has_permission_view_users(person):
    return PermissionDAO.has_permission(person['id'], "VIEW_USERS")


def has_permission_view_hotel(person):
    return PermissionDAO.has_permission(person['id'], "VIEW_HOTEL")


def has_permission_add_hotel(person):
    return PermissionDAO.has_permission(person['id'], "ADD_HOTEL")


def has_permission_edit(person):
    return PermissionDAO.has_permission(person['id'], "EDIT_PERMISSIONS")


def give_permission(person, person_to_give_permission, permission):
    if has_permission_edit(person):
        return PermissionDAO.give_permission(person_to_give_permission, permission)
    else:
        print("Forbidden. You are missing necessary permissions.")
        return False


def remove_permission():
    print("TODO remove permission from user")


def format_permission_header():
    return \
        "   ID| Name                | Description\n" \
        "-----+---------------------+---------------------------------------------------------------------------------"


def format_permission(permission):
    return u"{0:5}| {1:20}| {2:80}".format(
        permission['id'],
        permission['name'],
        permission['description'])
