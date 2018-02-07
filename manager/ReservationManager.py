# -*- coding: utf-8 -*-


import dao.ReservationDAO as ReservationDAO
import manager.PermissionManager as PermissionManager
import manager.HotelManager as HotelManager
import manager.RoomManager as RoomManager
import dao.HotelDAO as HotelDAO


def make_reservation(person):
    if PermissionManager.has_permission_view_hotel(person):
        print("You will be guided step by step to make your reservation. If you want to cancel at any point type '/cancel'")
        HotelManager.get_with_options(person, [])
        hotel_id = input("Choose a hotel by entering its ID >> ")

        if hotel_id != '/cancel':
            hotel = HotelDAO.get_by_id(hotel_id)
            if hotel is not None:
                from_date = input("Choose first day of your reservation (YYYY-MM-DD format) >> ")
                if from_date != '/cancel':
                    to_date = input("Choose last day of your reservation (YYYY-MM-DD format) >> ")
                    if to_date != '/cancel':
                        RoomManager.get_rooms_by_hotel(person, hotel_id)
                        room_id = input("Choose room by entering its ID >> ")
                        if room_id != '/cancel':
                            result = ReservationDAO.make_reservation(person, room_id, from_date, to_date)
                            if result:
                                print("Reservation made successfully.")
                            else:
                                print("Reservation unsuccessful.")
                            return result

        return False
    else:
        print("Forbidden. You are missing necessary permissions.")
    return False


def list_reservations(person):
    results = ReservationDAO.list_reservations(person)
    print(format_reservation_header())
    for result in results:
        print(format_reservation(result))
    return True


def format_reservation_header():
    return \
        "| Hotel name                  | From       | To         | Total price\n" \
        "|-----------------------------+------------+------------+------------"


def format_reservation(reservation):
    return u"| {0:28.28}| {1:11}| {2:11}| {3:9.2f}".format(
        reservation['name'],
        reservation['from_date'],
        reservation['to_date'],
        reservation['total_price'])