"""Amity.

Usage:
  main.py create_room <room_type> <room_name>...
  main.py add_person <name>  <person_type> [wants_accommodation]
  main.py reallocate_person <name> <room_name>
  main.py
  main.py (-h | --help )

Options:
  -i, --interactive Interactive Mode
  -h, --help  Show this screen and exit.

"""

import sys
import cmd
from docopt import docopt, DocoptExit
from amity import Amity
from termcolor import colored

# Create an instance of AMity to be used for the commands
amity = Amity()


def docopt_cmd(func):
    """Simplify the try/except block and pass result to the called action."""
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            return

        return func(self, opt)
    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class Amity(cmd.Cmd):
    """Docstring for Amity in docopt."""

    intro = colored('\n\tWelcome to Amity Allocations!\n'
                    + '\tWritten by Jxn\n'
                      + '\t(type help for a list of commands.)\n', "green")
    prompt = colored('Amity: ', "green")
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        room_type = arg["<room_type>"]
        room_name = arg["<room_name>"]
        print(colored("\n" + "*" * 15, "cyan"))
        amity.create_room(room_name, room_type)
        print(colored("*" * 15 + "\n", "cyan"))

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <first_name> <second_name> <person_type> [<wants_accommodation>]"""
        person_type = arg["<person_type>"]
        person_name = arg["<first_name>"] + " " + arg["<second_name>"]
        print(colored("\n" + "*" * 15, "cyan"))
        if arg["<wants_accommodation>"]:
            wants_acc = arg["<wants_accommodation>"]
            if wants_acc == 'Y' or wants_acc == 'y':
                amity.add_person(person_name, person_type, True)
            elif wants_acc == 'N' or wants_acc == 'n':
                amity.add_person(person_name, person_type)
            else:
                print("Please use 'Y / N' or 'y / n' for accomodation option")
        else:
            amity.add_person(person_name, person_type)
        print(colored("*" * 15 + "\n", "cyan"))

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [<file_name>]"""
        file_name = arg["<file_name>"]
        print(colored("\n" + "*" * 15, "cyan"))
        if amity.amity_offices:
            print(colored("Offices", "magenta"))
            print(colored("____________________________", "cyan"))
            for room, occupants in amity.amity_offices.items():
                print(colored(room, "blue"))
                print(colored("-" * 6 * (len(occupants) + 1), "cyan"))
                if occupants:
                    print(colored(", ".join(occupants) + "\n", "blue"))
                else:
                    print(colored("No occupants yet\n", "red"))
        else:
            print(colored("There are currently no offices allocated", "red"))
        if amity.amity_living_spaces:
            print(colored("\nLiving spaces", "magenta"))
            print(colored("____________________________", "cyan"))
            for room, occupants in amity.amity_living_spaces.items():
                print(colored(room, "blue"))
                print(colored("-" * 6 * (len(occupants) + 1), "cyan"))
                if occupants:
                    print(colored(", ".join(occupants) + "\n", "blue"))
                else:
                    print(colored("No occupants yet\n", "red"))
        else:
            print(colored("There are currently no Living Spaces allocated",
                          "red"))
        if file_name:
            amity.load_allocations_to_file(file_name)
            print(colored("\n\nAllocations have been loaded to the"
                  " text file: {}".format(file_name), "blue"))
        print(colored("*" * 15 + "\n", "cyan"))

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [<file_name>]"""
        file_name = arg["<file_name>"]
        amity.print_unallocated()
        print(colored("\n" + "*" * 15, "cyan"))
        if amity.unallocated_offices:
            print(colored("People who need offices", "magenta"))
            print(colored("-" * 15, "cyan"))
            print(colored(", ".join(amity.unallocated_offices) + "\n", "blue"))
        else:
            print(colored("There are currently no people who need Offices",
                          "red"))
        if amity.unallocated_living_spaces:
            print(colored("\nPeople who need Living spaces", "magenta"))
            print(colored("-" * 15, "cyan"))
            print(colored(", ".join(amity.unallocated_living_spaces) + "\n",
                          "blue"))
        else:
            print(colored("There are currently no people who need"
                          " Living Spaces", "red"))
        if file_name:
            amity.load_unallocated_to_file(file_name)
            print(colored("\n\nUnallocated list has been loaded to: {}".format(
                                                        file_name), "blue"))
        print(colored("*" * 15 + "\n", "cyan"))

    @docopt_cmd
    def do_reallocate(self, arg):
        """Usage: reallocate <first_name> <second_name> <new_room>"""
        new_room = arg["<new_room>"]
        person_name = arg["<first_name>"] + " " + arg["<second_name>"]
        if person_name in (list(amity.amity_fellows.keys()) +
                           list(amity.amity_staff.keys())):
            print(colored("\n" + "*" * 15, "cyan"))
            amity.reallocate(person_name, new_room)
            print(colored("\n" + "*" * 15, "cyan"))
        else:
            print(colored("\n{} is not a person in Amity".format(
                                                    person_name), "red"))
            print(colored("*" * 15 + "\n", "cyan"))

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""
        room_name = arg["<room_name>"]
        print(colored("\n" + "*" * 15, "cyan"))
        if (room_name in amity.amity_offices or
                room_name in amity.amity_living_spaces):
            if amity.amity_offices or amity.amity_living_spaces:
                for room, occupants in amity.amity_offices.items():
                    if room == room_name:
                        print(colored(room, "blue"))
                        print(colored("-" * 6 * (len(occupants) + 1), "cyan"))
                        if occupants:
                            print(colored(", ".join(occupants) + "\n", "blue"))
                        else:
                            print(colored("No occupants yet\n", "red"))
            else:
                print(colored("There're currently no rooms in Amity\n", "red"))
        else:
            print(colored("{} is not a room in Amity\n".format(room_name),
                          "red"))
        print(colored("*" * 15 + "\n", "cyan"))

    @docopt_cmd
    def do_load_people(self, arg):
        """Usage: load_people <file_name>"""
        print(colored("\n" + "*" * 15, "cyan"))
        file_name = arg["<file_name>"]
        try:
            f = open(file_name, mode="rt")
            for line in f:
                print(colored("\n" + "*" * 15, "cyan"))
                args = line.split()
                person_name = args[0] + " " + args[1]
                if len(args) > 3:
                    if args[3] == 'Y' or args[3] == 'y':
                        amity.add_person(person_name, args[2], True)
                    elif args[3] == 'N' or args[3] == 'n':
                        amity.add_person(person_name, args[2])
                    else:
                        print(colored("Please use 'Y/N' or 'y/n' for"
                              " accomodation option", "red"))
                    print(colored("*" * 15 + "\n", "cyan"))
                else:
                    amity.add_person(person_name, args[2])
                    print(colored("*" * 15 + "\n", "cyan"))
            f.close()
        except:
            print(colored("File doesnt exist!", "red"))
        print(colored("*" * 15 + "\n", "cyan"))

    @docopt_cmd
    def do_save_state(self, arg):
        """Usage: save_state [<db_name>]"""
        db_name = arg["<db_name>"]
        print(colored("\n" + "*" * 15, "cyan"))
        try:
            if db_name:
                amity.save_state(db_name)
            else:
                amity.save_state()
        except:
            print(colored("Database error!!", "red"))
        print(colored("*" * 15 + "\n", "cyan"))

    @docopt_cmd
    def do_load_state(self, arg):
        """Usage: load_state <db_name>"""
        db_name = arg["<db_name>"]
        print(colored("\n" + "*" * 15, "cyan"))
        amity.load_state(db_name)
        print("State Loaded")
        print(colored("*" * 15 + "\n", "cyan"))

    @docopt_cmd
    def do_remove_occupant(self, arg):
        """Usage: remove_occupant <first_name> <second_name> <room_name>"""
        person_name = arg["<first_name>"] + " " + arg["<second_name>"]
        room_name = arg["<room_name>"]
        print(colored("\n" + "*" * 15, "cyan"))
        print(colored(amity.remove_occupant(person_name, room_name), "red"))
        print(colored("*" * 15 + "\n", "cyan"))

    @docopt_cmd
    def do_quit(self, arg):
        """Exits the Interactive Mode."""
        print(colored("\n" + "*" * 15, "cyan"))
        print(colored("\nGoodBye!\n", "yellow"))
        print(colored("*" * 15 + "\n", "cyan"))
        exit()

    @docopt_cmd
    def do_print_people(self, arg):
        """Usage: print_people"""
        print(colored("\n" + "*" * 15, "cyan"))
        if amity.amity_staff:
            print(colored("List of Staff", "magenta"))
            print(colored("-" * 20, "cyan"))
            for staff in amity.amity_staff.keys():
                print(colored("> " + staff, "blue"))
        else:
            print(colored("There are no staff members in Amity", "blue"))
        if amity.amity_fellows:
            print(colored("\nList of Fellows", "magenta"))
            print(colored("-" * 20, "cyan"))
            for fellow in amity.amity_fellows.keys():
                print(colored("> " + fellow, "blue"))
        else:
            print(colored("There are no fellows in Amity", "blue"))

        print(colored("*" * 15 + "\n", "cyan"))

    @docopt_cmd
    def do_print_rooms(self, arg):
        """Usage: print_rooms"""
        print(colored("\n" + "*" * 15, "cyan"))
        if amity.amity_offices:
            print(colored("List of Offices", "magenta"))
            print(colored("-" * 20, "cyan"))
            for office in amity.amity_offices.keys():
                print(colored("> " + office, "blue"))
        else:
            print(colored("There are no offices in Amity", "blue"))
        if amity.amity_living_spaces:
            print(colored("\nList of Living Spaces", "magenta"))
            print(colored("-" * 20, "cyan"))
            for lspace in amity.amity_living_spaces.keys():
                print(colored("> " + lspace, "blue"))
        else:
            print(colored("There are no Living Spaces in Amity", "blue"))

        print(colored("*" * 15 + "\n", "cyan"))

    @docopt_cmd
    def do_delete_person(self, arg):
        """Usage: delete_person <first_name> <second_name>"""
        person_name = arg["<first_name>"] + " " + arg["<second_name>"]
        print(colored("\n" + "*" * 15, "cyan"))
        print(amity.delete_person(person_name))
        print(colored("*" * 15 + "\n", "cyan"))

    @docopt_cmd
    def do_delete_room(self, arg):
        """Usage: delete_room <room_name>"""
        room_name = arg["<room_name>"]
        print(colored("\n" + "*" * 15, "cyan"))
        print(amity.delete_room(room_name))
        print(colored("*" * 15 + "\n", "cyan"))

    @docopt_cmd
    def do_convert_room(self, arg):
        """Usage: convert_room <room_name> <new_room_type>"""
        room_name = arg["<room_name>"]
        room_type = arg["<new_room_type>"]
        print(colored("\n" + "*" * 15, "cyan"))
        print(amity.convert_room(room_name, room_type))
        print(colored("*" * 15 + "\n", "cyan"))


opt = docopt(__doc__, sys.argv[1:])
Amity().cmdloop()
