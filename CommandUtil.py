# -*- coding: utf-8 -*-

import manager
import HelpUtil

f = open("command_help.txt", "r")
command_help = f.read()
f.close()

person = None


def print_help():
    HelpUtil.person = person
    HelpUtil.print_help()


def run_command(command_str):
    if command_str == "exit":
        return False

    if command_str == 'help':
        print_help()
        return True

    command_split = command_str.split()

    if command_split[0] == "user":
        command_split.pop(0)
        if not run_user_command(command_split):
            unsupported_command(command_str)
    elif command_split[0] == "permission":
        command_split.pop(0)
        if not run_permission_command(command_split):
            unsupported_command(command_str)
    elif command_split[0] == "hotel":
        command_split.pop(0)
        if not run_hotel_command(command_split):
            unsupported_command(command_str)
    elif command_split[0] == "service":
        command_split.pop(0)
        if not run_service_command(command_split):
            unsupported_command(command_str)
    elif command_split[0] == "room":
        command_split.pop(0)
        if not run_room_command(command_split):
            unsupported_command(command_str)
    elif command_split[0] == "reservation":
        command_split.pop(0)
        if not run_reservation_command(command_split):
            unsupported_command(command_str)
    return True


def run_reservation_command(command_split):
    if len(command_split) == 1:
        if command_split[0] == "list":
            return manager.ReservationManager.list_reservations(person)
        elif command_split[0] == "make":
            return manager.ReservationManager.make_reservation(person)
    return False



def run_room_command(command_split):
    if len(command_split) == 1:
        if command_split[0] == "list":
            return manager.RoomManager.get_all(person)
        elif command_split[0] == "add":
            return manager.RoomManager.add_room(person)
    else:
        return False


def run_service_command(command_split):
    if command_split[0] == "list":
        if len(command_split) == 1:
            manager.ServiceManager.get_all(person)
            return True
        elif len(command_split) == 2:
            splitted = command_split[1].split("=")
            if splitted[0] == 'name' and len(splitted) == 2:
                manager.ServiceManager.get_all_by_name(person, splitted[1])
                return True
            else:
                return False
        else:
            return False
    elif command_split[0] == "add" and len(command_split) == 1:
        manager.ServiceManager.add_service(person)
        return True
    else:
        return False


def run_hotel_command(command_split):
    if command_split[0] == "list":
        command_split.pop(0)
        options = []
        for option in command_split:
            parsed = parse_hotel_option(option)
            if parsed is not None:
                options.append(parsed)

        manager.HotelManager.get_with_options(person, options)
        return True
    elif command_split[0] == "add" and len(command_split) == 1:
        manager.HotelManager.add_hotel(person)
        return True
    elif command_split[0] == "add-service" and len(command_split) == 4:
        manager.HotelManager.add_service(person, command_split[2], command_split[1], command_split[3])
        return True
    elif command_split[0] == "add-rooms" and len(command_split) == 5:
        manager.HotelManager.add_room(person, command_split[1], command_split[2], command_split[3], command_split[4])
        return True
    elif len(command_split) == 1:
        manager.HotelManager.get(person, command_split[0])
        return True
    return False


def parse_hotel_option(option):
    splitted = option.split("=")
    if len(splitted) == 2:
        return splitted[0], splitted[1]
    print("Option '" + option + "' not recognized. Ignoring it...")
    return None


def run_permission_command(command_split):
    if command_split[0] == "give":
        if len(command_split) == 3:
            result = manager.PermissionManager.give_permission(person, command_split[1], command_split[2])
            return result
    elif command_split[0] == "list":
        if len(command_split) == 1:
            manager.PermissionManager.get_all(person)
            return True
        elif len(command_split) == 2:
            manager.PermissionManager.get_all_for_person(person, command_split[1])
            return True
        else:
            return False
    else:
        return False
    return True


def run_user_command(command_split):
    if len(command_split) == 0:
        manager.PersonManager.get_id_username(str(person['id']))
    elif command_split[0] == "add" and len(command_split) == 1:
        result = manager.PersonManager.add_person(person)
        if result:
            print("User added successfully.")
        else:
            print("Failed to add user!")
    elif command_split[0] == "list":
        if len(command_split) == 1:
            manager.PersonManager.get_all()
        elif len(command_split) == 2:
            arg = parse_firstname_lastname(command_split[1])
            if arg is not None:
                if arg[0] == 'firstname':
                    manager.PersonManager.get_first_name(arg[1])
                else:
                    manager.PersonManager.get_last_name(arg[1])
            else:
                print("ERROR: Unrecognized option '" + command_split[1] + "' for command 'user list'.")
                return False
        elif len(command_split) == 3:
            arg1 = parse_firstname_lastname(command_split[1])
            arg2 = parse_firstname_lastname(command_split[2])
            if arg1 is not None and arg2 is not None:
                if arg1[0] == 'id':
                    print("ERROR: option 'id' cannot be combined with '" + arg2[0] + "'.")
                    return False
                elif arg2[0] == 'id':
                    print("ERROR: option 'id' cannot be combined with '" + arg1[0] + "'.")
                    return False
                elif arg1[0] == arg2[0]:
                    print("ERROR: option '" + arg1[0] + "' used multiple times.")
                    return False
                elif arg1[0] == 'firstname' and arg2[0] == 'lastname':
                    manager.PersonManager.get_first_name_last_name(arg1[1], arg2[1])
                else:
                    manager.PersonManager.get_first_name_last_name(arg2[1], arg1[1])
            else:
                if arg1 is None:
                    print("ERROR: Unrecognized option '" + command_split[1] + "' for command 'user list'.")
                if arg2 is None:
                    print("ERROR: Unrecognized option '" + command_split[2] + "' for command 'user list'.")
                return False
    elif len(command_split) == 1:
        manager.PersonManager.get_id_username(command_split[0])
    else:
        return False

    return True


def parse_firstname_lastname(arg):
    args_split = arg.split('=')
    if len(args_split) == 1:
        return 'id', arg
    elif len(args_split) == 2:
        if args_split[0] == 'firstname':
            return 'firstname', args_split[1]
        elif args_split[0] == 'lastname':
            return 'lastname', args_split[1]
        else:
            return None


def unsupported_command(command_str):
    print("ERROR: Unrecognized command '" + command_str + "', to list commands type 'help'")