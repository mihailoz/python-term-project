# -*- coding: utf-8 -*-


import sqlite3


conn = sqlite3.connect("example.db")
conn.row_factory = sqlite3.Row


def get_all_with_options(options):
    cursor = conn.cursor()
    query = "SELECT * FROM hotel"
    option_query = " WHERE "
    valid_options = 0
    for option in options:
        if option[0] == 'name':
            if valid_options != 0:
                option_query += " AND "
            option_query += "name LIKE '%" + option[1] + "%'"
            valid_options += 1
        elif option[0] == 'city':
            if valid_options != 0:
                option_query += " AND "
            option_query += "city LIKE '%" + option[1] + "%'"
            valid_options += 1
        elif option[0] == 'country':
            if valid_options != 0:
                option_query += " AND "
            option_query += "country LIKE '%" + option[1] + "%'"
            valid_options += 1
        elif option[0] == 'min_rating':
            if valid_options != 0:
                option_query += " AND "
            option_query += "rating >= " + option[1]
            valid_options += 1
        else:
            print("Unrecognized option (" + option[0] + ", " + option[1] + "), ignoring...")

    if valid_options > 0:
        query += option_query

    return cursor.execute(query)


def add_hotel(name, city, country):
    cursor = conn.cursor()
    result = cursor.execute('''SELECT * FROM hotel WHERE name = ? AND city = ? AND country = ?''',
                            (name, city, country)).fetchone()

    if result is None:
        conn.execute("INSERT INTO hotel(name, city, country, rating) VALUES (?, ?, ?, 0)", (name, city, country))
        conn.commit()
        print(name + " successfully added to hotels.")
    else:
        print(name + " located in " + city + ", " + country + " already exists.")


def get_by_id(hotel_id):
    cursor = conn.cursor()
    result = cursor.execute('''SELECT * FROM hotel WHERE id = ?''', (hotel_id, )).fetchone()

    if result is None:
        print("Hotel with id '" + hotel_id + "' doesn't exist.")
        return False
    else:
        return result