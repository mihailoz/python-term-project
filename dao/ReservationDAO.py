# -*- coding: utf-8 -*-


import sqlite3


conn = sqlite3.connect("example.db")
conn.row_factory = sqlite3.Row


def count_reservations(hotel_room_id, from_date, to_date):
    cursor = conn.cursor()
    return cursor.execute("SELECT COUNT(*) FROM reservation WHERE hotel_room_id = ?1 AND "
                          "((from_date <= ?3 AND from_date >= ?2) OR "
                          "(to_date >= ?2 AND to_date <= ?3) OR "
                          "(to_date >= ?3 AND from_date <= ?2))", (hotel_room_id, from_date, to_date)).fetchone()


def make_reservation(person, hotel_room_id, from_date, to_date):
    res_count = count_reservations(hotel_room_id, from_date, to_date)
    room = conn.cursor().execute("SELECT * FROM hotel_room WHERE id = ?", (hotel_room_id,)).fetchone()

    if room['room_count'] > res_count[0]:
        conn.execute("INSERT INTO reservation(hotel_room_id, person_id, from_date, to_date) VALUES (?,?,?,?)",
                     (hotel_room_id, person['id'], from_date, to_date))
        conn.commit()
        return True
    else:
        print("Could not make reservation, no more available rooms.")
        return False

def list_reservations(person):
    return conn.cursor().execute("SELECT r.from_date, r.to_date, (hr.price_per_day * (julianday(r.to_date) - julianday(r.from_date))) as total_price, h.name "
                                 "FROM reservation r, hotel_room hr, hotel h "
                                 "WHERE r.hotel_room_id = hr.id AND h.id = hr.hotel_id AND ? = r.person_id", (person['id'],))