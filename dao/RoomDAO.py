# -*- coding: utf-8 -*-


import sqlite3


conn = sqlite3.connect("example.db")
conn.row_factory = sqlite3.Row


def get_all():
    cursor = conn.cursor()
    return cursor.execute('''SELECT * FROM room''')


def add_room(desc, number_of_people):
    conn.execute("INSERT INTO room(description, number_of_people) VALUES (?, ?)", (desc, number_of_people))
    conn.commit()
    print("Room type added.")
    return True


def get_rooms_by_hotel(hotel_id):
    cursor = conn.cursor()
    hotel = cursor.execute("SELECT * FROM hotel WHERE id = ?", (hotel_id,)).fetchone()

    if hotel is not None:
        return cursor.execute("SELECT hr.*, r.description, r.number_of_people FROM hotel_room hr, room r WHERE hotel_id = ? AND r.id = hr.room_id", (hotel_id, ))
    else:
        print("Hotel with id '" + hotel_id + "' does not exist.")
        return False


def add_room_hotel(hotel_id, room_id, count, price):
    cursor = conn.cursor()
    hotel = cursor.execute("SELECT * FROM hotel WHERE id = ?", (hotel_id,)).fetchone()
    room = cursor.execute('''SELECT * FROM room WHERE id = ?''', (room_id,)).fetchone()
    hotel_room = cursor.execute('''SELECT * FROM hotel_room WHERE hotel_id = ? AND room_id = ?''', (hotel_id, room_id)).fetchone()

    if hotel is not None:
        if room is not None:
            if hotel_room is None:
                conn.execute("INSERT INTO hotel_room(hotel_id, room_id, price_per_day, room_count) VALUES (?, ?, ?, ?)", (hotel_id, room_id, price, count))
                conn.commit()
                print("Rooms added to hotel successfully.")
                return True
            else:
                print("Rooms already exist in hotel")
        else:
            print("Room doesn't exist.")
    else:
        print("Hotel does not exist.")
    return False