# -*- coding: utf-8 -*-


import dao.PersonDAO as PersonDAO
import manager.PermissionManager as PermissionManager


def get_all():
    get_first_name_last_name(None, None)


def get_first_name(first_name):
    get_first_name_last_name(first_name, None)


def get_last_name(last_name):
    get_first_name_last_name(None, last_name)


def get_first_name_last_name(first_name, last_name):
    results = PersonDAO.get_all(first_name, last_name)
    print(format_person_header())
    for person in results:
        print(format_person(person))


def get_id_username(person_id):
    result = PersonDAO.get_id_or_username(person_id)
    if result:
        print(format_person_header())
        print(format_person(result))
    else:
        print("User with '" + person_id + "' as ID or username not found!")


def login(username, password):
    user = PersonDAO.get_username_password(username, password)
    if user:
        print("Welcome " + user['first_name'] + " " + user['last_name'])
        return user
    else:
        print("Invalid username or password")
        return None


def add_person(person):
    if PermissionManager.has_permission_add_user(person):
        print('''You will be guided to enter the new user's data, if you want to cancel type /cancel''')
        first_name = input("First name >> ")
        if first_name != '/cancel':
            last_name = input("Last name >> ")
            if last_name != '/cancel':
                username = input("Username used to login >> ")
                if username != '/cancel':
                    password = input("Password used to login >> ")
                    if password != '/cancel':
                        print("User data"
                              "\n========================"
                              "\nFirst name: " + first_name,
                              "\nLast name: " + last_name,
                              "\nUsername: " + username,
                              "\nPassword: " + password)
                        answer = input("Do you want to add user with data above (yes/no) >> ")
                        while answer != "yes" and answer != "no":
                            answer = input("Unrecognized '"
                                           + answer + "'\nDo you want to add user with data above (yes/no) >> ")
                        if answer == "yes":
                            return PersonDAO.add_person(first_name, last_name, username, password)
    else:
        print("Forbidden. You are missing necessary permissions.")
    return False


def format_person_header():
    return \
        "   ID| First name          | Last name                | Username       \n" \
        "-----+---------------------+--------------------------+----------------"


def format_person(person):
    return u"{0:5}| {1:20}| {2:25}| {3:15}".format(
        person['id'],
        person['first_name'],
        person['last_name'],
        person['username'])
