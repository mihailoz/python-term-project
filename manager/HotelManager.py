# -*- coding: utf-8 -*-


import manager.PermissionManager as PermissionManager
import dao.HotelDAO as HotelDAO
import dao.RoomDAO as RoomDAO
import dao.ServiceDAO as ServiceDAO
import manager.ServiceManager as ServiceManager
import manager.RoomManager as RoomManager


def get_with_options(person, options):
    if PermissionManager.has_permission_view_hotel(person):
        results = HotelDAO.get_all_with_options(options)
        print(format_hotel_header())
        for row in results:
            print(format_hotel(row))
    else:
        print("You don't have the necessary permissions")


def get(person, hotel_id):
    if PermissionManager.has_permission_view_hotel(person):
        hotel = HotelDAO.get_by_id(hotel_id)

        if hotel:
            print("Name: " + hotel['name'])
            print("City: " + hotel['city'])
            print("Country: " + hotel['country'])
            print("Rating: " + str(hotel['rating']))
            
            ServiceManager.get_by_hotel(person, hotel_id)
            RoomManager.get_rooms_by_hotel(person, hotel_id)
        else:
            return False
    else:
        print("Forbidden. You are missing necessary permissions.")
    return False


def add_hotel(person):
    if PermissionManager.has_permission_add_hotel(person):
        print('''You will be guided to enter the new hotel's data, if you want to cancel type /cancel''')
        name = input("Name >> ")
        if name != '/cancel':
            city = input("City >> ")
            if city != '/cancel':
                country = input("Country >> ")
                if country != '/cancel':
                    print("Hotel data"
                          "\n========================"
                          "\nName: " + name,
                          "\nCity: " + city,
                          "\nCountry: " + country)
                    answer = input("Do you want to add hotel with data above (yes/no) >> ")
                    while answer != "yes" and answer != "no":
                        answer = input("Unrecognized '"
                                       + answer + "'\nDo you want to add hotel with data above (yes/no) >> ")
                    if answer == "yes":
                        return HotelDAO.add_hotel(name, city, country)
    else:
        print("Forbidden. You are missing necessary permissions.")
    return False


def add_service(person, service_id, hotel_id, price):
    if PermissionManager.has_permission_add_hotel(person):
        ServiceDAO.add_service_to_hotel(hotel_id, service_id, price)
        return True
    else:
        print("Forbidden. You are missing necessary permissions.")
    return False


def add_room(person, hotel_id, room_id, price, count):
    if PermissionManager.has_permission_add_hotel(person):
        return RoomDAO.add_room_hotel(hotel_id, room_id, count, price)
    else:
        print("Forbidden. You are missing necessary permissions.")
    return False


def format_hotel_header():
    return \
        "   ID| Name                          | City              | Country           | Rating\n" \
        "-----+-------------------------------+-------------------+-------------------+--------"


def format_hotel(hotel):
    return u"{0:5}| {1:30.30}| {2:18}| {3:18}| {4:7}".format(
        hotel['id'],
        hotel['name'],
        hotel['city'],
        hotel['country'],
        hotel['rating'])
