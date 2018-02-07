# -*- coding: utf-8 -*-


import sqlite3


conn = sqlite3.connect("example.db")
conn.row_factory = sqlite3.Row


def get_all():
    cursor = conn.cursor()
    return cursor.execute("SELECT * FROM service")


def get_all_by_name(name):
    cursor = conn.cursor()
    return cursor.execute("SELECT * FROM service WHERE name LIKE '%" + name + "%'")


def get_by_hotel(hotel_id):
    cursor = conn.cursor()
    return cursor.execute("SELECT s.*, hs.price FROM hotel_service hs, service s WHERE hs.hotel_id = ? AND s.id = hs.service_id", (hotel_id, ))


def add_service(name, description):
    cursor = conn.cursor()
    result = cursor.execute('''SELECT * FROM service WHERE name = ? AND description = ?''',
                            (name, description)).fetchone()

    if result is None:
        conn.execute("INSERT INTO service(name, description) VALUES (?, ?)", (name, description))
        conn.commit()
        print(name + " successfully added to services.")
    else:
        print(name + " with description '" + description + "' already exists.")


def add_service_to_hotel(hotel_id, service_id, price):
    cursor = conn.cursor()
    result = cursor.execute('''SELECT * FROM service WHERE id = ?''', (service_id,)).fetchone()

    if result is None:
        print("Service with id '" + service_id + "' doesn't exist.")
    else:
        hotel = cursor.execute('''SELECT * FROM hotel WHERE id = ?''', (hotel_id,)).fetchone()
        if hotel is None:
            print("Hotel with id '" + hotel_id + "' doesn't exist.")
        else:
            hotel_service = cursor.execute('''SELECT * FROM hotel_service WHERE service_id = ? AND hotel_id = ?''', (service_id, hotel_id)).fetchone()
            if hotel_service is None:
                conn.execute("INSERT INTO hotel_service(price, hotel_id, service_id) VALUES (?, ?, ?)",
                             (price, hotel_id, service_id))
                conn.commit()
                print("Service " + result['name'] + " added to hotel " + hotel['name'] + " with price: " + price + ".")
            else:
                print("Service with id '" + service_id + "' already exists for hotel with id '" + hotel_id + "'.")
    return True