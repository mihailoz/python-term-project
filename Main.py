# -*- coding: utf-8 -*-


import manager.PersonManager as PersonManager
import CommandUtil


def main():
    username = input("Username >> ")
    password = input("Password >> ")
    result = PersonManager.login(username, password)

    if result is not None:
        CommandUtil.person = result
        CommandUtil.print_help()
        main_menu()
    else:
        main()


def main_menu():
    command = input(">> ")
    result = CommandUtil.run_command(command)
    if result:
        main_menu()
    else:
        print("Goodbye")


if __name__ == '__main__':
    main()
