# -*- coding: utf-8 -*-


import sqlite3


conn = sqlite3.connect("example.db")
conn.row_factory = sqlite3.Row


def get_all():
    cursor = conn.cursor()
    return cursor.execute('''SELECT * FROM permission''')


def get_for_person(person_id):
    cursor = conn.cursor()
    person = cursor.execute('''SELECT * FROM person WHERE id = ?1 OR username = ?1''', (person_id,)).fetchone()
    if person is not None:
        return cursor.execute('''SELECT pm.* FROM permission pm, person_permission pp WHERE pp.person_id = ?1
        AND pm.id = pp.permission_id''', (person['id'],))
    else:
        print("User with '" + person_id + "' as ID or username does not exist.")
        return None


def has_permission(person_id, permission_name):
    cursor = conn.cursor()
    result = cursor.execute('''SELECT pp.* FROM person_permission pp, permission pm, person p
    WHERE pp.person_id = p.id AND pm.id = pp.permission_id AND (p.id = ?1 OR p.username = ?1) AND (pm.name = ?2)''',
                            (person_id, permission_name))
    if result.fetchone() is not None:
        return True
    return False


def give_permission(person_id, permission):
    cursor = conn.cursor()

    found = has_permission(person_id, permission)
    if found:
        print("User already has that permission.")
        return True
    else:
        result = cursor.execute('''SELECT * FROM permission WHERE id = ?1 OR name = ?1''', (permission, )).fetchone()
        if result is not None:
            person = cursor.execute('''SELECT * FROM person WHERE id = ?1 OR username = ?1''', (person_id, )).fetchone()
            if person is not None:
                conn.execute('''INSERT INTO person_permission(person_id, permission_id) VALUES (?, ?)''',
                             (person['id'], result['id']))
                conn.commit()
                print("Permission " + result['name'] + " has been given to " + person['first_name'] + " " + person['last_name'])
            else:
                print("Person with '" + person_id + "' as id or username does not exist.")
        else:
            print("ERROR: Permission '" + permission + "' does not exist")
            return False
    return True
