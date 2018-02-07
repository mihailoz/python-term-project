# -*- coding: utf-8 -*-

import manager.PermissionManager as PermissionManager


person = None


def print_help():
    print_start_text()
    print_reservation_help()
    print_hotel_help()
    print_room_help()
    print_service_help()
    print_user_help()
    print_permission_help()
    print_end_text()


def print_reservation_help():
    print("\treservation\n"
        "\t\tmake                                                    | guides you through making a reservation\n"
        "\t\tlist                                                    | lists your reservations")
    print_divider()


def print_hotel_help():
    if PermissionManager.has_permission_view_hotel(person):
        print("\thotel <id>                                                      | shows data for hotel with id <id>")
        if PermissionManager.has_permission_add_hotel(person):
            print("\t\tadd                                                     | goes through the create hotel wizard")
        print("\t\tlist                                                    | shows a list of hotels, can be used with none, some or all\n"
              "\t\t\t[name=<name>] [city=<city>]                     | the options provided (name, city, country, min_rating\n"
              "\t\t\t[country=<country>] [min_rating=<min_rating>]   |")
        if PermissionManager.has_permission_add_hotel(person):
            print("\t\tadd-service <hotel_id> <service_id> <price>             | adds <service_id> to <hotel_id> with price <price>\n"
                  "\t\tadd-rooms <hotel_id> <room_id> <price> <room count>     | adds <room count> rooms(<room_id>) to <hotel_id> with <price> per day of stay")
        print_divider()


def print_room_help():
    if PermissionManager.has_permission_add_hotel(person):
        print("\troom\n"
              "\t\tlist                                                    | lists all room types\n"
              "\t\tadd                                                     | goes through the create room type wizard")
        print_divider()


def print_service_help():
    if PermissionManager.has_permission_add_hotel(person):
        print("\tservice\n"
              "\t\tadd                                                     | goes through the create service wizard\n"
              "\t\tlist                                                    | shows list of available services\n"
              "\t\t\t[name=<name>]                                   | option searches by <name>")
        print_divider()


def print_user_help():
    if PermissionManager.has_permission_view_users(person):
        print("\tuser [<id>]                                                     | shows data for user with id or username <id> (if not passed shows for logged user)\n"
              "\t\tlist                                                    | lists all users\n"
              "\t\t\t[firstname=<firstname>] [lastname=<lastname>]   | searches users by <firstname>, <lastname>, or both")
        if PermissionManager.has_permission_add_user(person):
            print("\t\tadd                                                     | goes through the create user wizard")

        print_divider()


def print_permission_help():
    if PermissionManager.has_permission_edit(person):
        print("\tpermission                                                      | does nothing on its own\n"
              "\t\tgive <person_id> <permission_id>                        | gives permission with id or name <permission_id> to user with id or username <person_id>\n"
              "\t\tlist                                                    | lists all permissions\n"
              "\t\t\t<person_id>                                     | lists permission of user with id or username <person_id>")
        print_divider()


def print_start_text():
    print("\nCOMMAND HELP")
    print("These commands are available to you, indentations are used to represent chaining commands for instance 'hotel add-service...' is a chained command.")
    print("===================================================================================================================================================")


def print_end_text():
    print("\thelp                                                            | shows list of commands and options\n"
          "\texit                                                            | exits the program and logs off user\n")


def print_divider():
    print("---------------------------------------------------------------------------------------------------------------------------------------------------")