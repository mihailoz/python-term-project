# -*- coding: utf-8 -*-

import manager.PermissionManager as PermissionManager
import dao.ServiceDAO as ServiceDAO


def get_all(person):
    if PermissionManager.has_permission_view_hotel(person):
        results = ServiceDAO.get_all()
        print(format_service_header())
        for row in results:
            print(format_service(row))
    else:
        print("Forbidden. You are missing necessary permissions.")


def get_all_by_name(person, name):
    if PermissionManager.has_permission_view_hotel(person):
        results = ServiceDAO.get_all_by_name(name)
        print(format_service_header())
        for row in results:
            print(format_service(row))
    else:
        print("Forbidden. You are missing necessary permissions.")


def get_by_hotel(person, hotel_id):
    if PermissionManager.has_permission_view_hotel(person):
        results = ServiceDAO.get_by_hotel(hotel_id)
        print("Services this hotel has to offer:")
        print(format_hotel_service_header())
        for row in results:
            print(format_hotel_service(row))
    else:
        print("Forbidden. You are missing necessary permissions.")


def add_service(person):
    if PermissionManager.has_permission_add_hotel(person):
        print('''You will be guided to enter the new service's data, if you want to cancel type /cancel''')
        name = input("Name >> ")
        if name != '/cancel':
            description = input("Description >> ")
            if description != '/cancel':
                print("Hotel data"
                      "\n========================"
                      "\nName: " + name,
                      "\nDescription: " + description)
                answer = input("Do you want to add service with data above (yes/no) >> ")
                while answer != "yes" and answer != "no":
                    answer = input("Unrecognized '"
                                   + answer + "'\nDo you want to add service with data above (yes/no) >> ")
                if answer == "yes":
                    return ServiceDAO.add_service(name, description)
    else:
        print("Forbidden. You are missing necessary permissions.")
    return False


def remove_service():
    print("TODO removes service from database (flags it)")


def format_service_header():
    return \
        "   ID| Name                | Description                                               \n" \
        "-----+---------------------+-------------------------------------------------------------"


def format_service(service):
    return u"{0:5}| {1:20}| {2:60}".format(
        service['id'],
        service['name'],
        service['description'])


def format_hotel_service_header():
    return \
        "   ID| Name                | Description                                               |    Price\n" \
        "-----+---------------------+-----------------------------------------------------------|---------"


def format_hotel_service(service):
    return u"{0:5}| {1:20}| {2:58}| {3:8}".format(
        service['id'],
        service['name'],
        service['description'],
        service['price'])