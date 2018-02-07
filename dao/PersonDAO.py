# -*- coding: utf-8 -*-


import sqlite3


conn = sqlite3.connect("example.db")
conn.row_factory = sqlite3.Row


def get_username_password(username, password):
    cursor = conn.cursor()
    results = cursor.execute('''SELECT * FROM person WHERE username = ? AND password = ?''', (username, password))
    return results.fetchone()


def get_id_or_username(person_id):
    cursor = conn.cursor()
    results = cursor.execute('''SELECT * FROM person WHERE id = ?1 OR username = ?1''', (person_id,))
    return results.fetchone()


def get_all(first_name, last_name):
    query = "SELECT id, first_name, last_name, username FROM PERSON"
    if first_name is not None or last_name is not None:
        query += " WHERE "
        if first_name is not None:
            query += "first_name LIKE '%" + first_name + "%'"
            if last_name is not None:
                query += " AND "
        if last_name is not None:
            query += "last_name LIKE '%" + last_name + "%'"

    cursor = conn.cursor()
    return cursor.execute(query)


def add_person(first_name, last_name, username, password):
    cursor = conn.cursor()

    found = cursor.execute("SELECT * FROM person WHERE username = ?", (username,)).fetchone()

    if found is not None:
        print("ERROR: User with username '" + username + "' already exists.")
        return False

    conn.execute("INSERT INTO person(first_name, last_name, username, password) VALUES (?,?,?,?)",
                   (first_name, last_name, username, password))

    conn.commit()

    person = get_id_or_username(username)

    conn.execute("INSERT INTO person_permission(person_id, permission_id) VALUES (?, ?)", (person['id'], 1))

    conn.commit()
    return True