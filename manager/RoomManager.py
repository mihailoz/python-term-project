# -*- coding: utf-8 -*-

import manager.PermissionManager as PermissionManager
import dao.RoomDAO as RoomDAO


def get_all(person):
    if PermissionManager.has_permission_add_hotel(person):
        results = RoomDAO.get_all()
        print(format_room_header())
        for row in results:
            print(format_room(row))
        return True
    else:
        print("Forbidden. You are missing necessary permissions.")
    return False


def add_room(person):
    if PermissionManager.has_permission_add_hotel(person):
        print('''You will be guided to enter the new room's data, if you want to cancel type /cancel''')
        desc = input("Description >> ")
        if desc != '/cancel':
            number_of_people = input("Number of people that can fit in the room >> ")
            if number_of_people != '/cancel':
                print("Room data"
                      "\n========================"
                      "\nDescription: " + desc,
                      "\nNumber of people: " + number_of_people)
                answer = input("Do you want to add hotel with data above (yes/no) >> ")
                while answer != "yes" and answer != "no":
                    answer = input("Unrecognized '"
                                   + answer + "'\nDo you want to add hotel with data above (yes/no) >> ")
                if answer == "yes":
                    return RoomDAO.add_room(desc, number_of_people)
    else:
        print("Forbidden. You are missing necessary permissions.")
    return False


def get_rooms_by_hotel(person, hotel_id):
    if PermissionManager.has_permission_view_hotel(person):
        results = RoomDAO.get_rooms_by_hotel(hotel_id)
        print("Hotel Rooms:")
        print(format_hotel_room_header())
        for row in results:
            print(format_hotel_room(row))
        return True
    else:
        print("Forbidden. You are missing necessary permissions.")
    return False


def format_room_header():
    return \
        "   ID| Description                                                           | Number of people\n" \
        "-----+-----------------------------------------------------------------------+-----------------"


def format_room(room):
    return "{0:5}| {1:70.70}| {2:16}".format(
        room['id'],
        room['description'],
        room['number_of_people'])


def format_hotel_room_header():
    return \
        "   ID| Description                                                 | People | Count | Price per day\n" \
        "-----+-------------------------------------------------------------+--------+-------+--------------"


def format_hotel_room(room):
    return "{0:5}| {1:60.60}| {2:7}| {3:6}| {4:13}".format(
        room['id'],
        room['description'],
        room['number_of_people'],
        room['room_count'],
        room['price_per_day']
    )
