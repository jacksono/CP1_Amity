"""Amity.

Usage:
  main.py create_room <room_type> <room_name>...
  main.py add_person <name>  <person_type> [wants_accommodation]
  main.py reallocate_person <name> <room_name>
  main.py
  main.py (-h | --help | --version)

Options:
  -i, --interactive Interactive Mode
  -h, --help  Show this screen and exit.

"""

import sys
import cmd
from docopt import docopt, DocoptExit
from amity import Amity

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
            # We do not need to do the print here.
            return

        return func(self, opt)
    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class Amity(cmd.Cmd):
    """Docstring for Amity in docopt."""

    intro = '\n\tWelcome to Amity!\n' \
        + '\tProduct by Jxn\n' \
        + '\t(type help for a list of commands.)\n'
    prompt = 'Amity: '
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        room_type = arg["<room_type>"]
        room_name = arg["<room_name>"]
        print("\n" + "*" * 15)
        amity.create_room(room_name, room_type)
        print("*" * 15)
        print()

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <first_name> <second_name> <person_type> [<wants_accommodation>]"""
        person_type = arg["<person_type>"]
        person_name = arg["<first_name>"] + " " + arg["<second_name>"]
        print("\n" + "*" * 15)
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
        print("*" * 15)
        print()

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [<file_name>]"""
        file_name = arg["<file_name>"]
        print
        print("\n" + "*" * 15)
        if amity.amity_offices:
            print("Offices")
            print("____________________________")
            for room, occupants in amity.amity_offices.items():
                print(room)
                print("-" * 6 * (len(occupants) + 1))
                if occupants:
                    print(", ".join(occupants))
                    print()
                else:
                    print("No occupants yet")
                    print()
        else:
            print("There are currently no offices allocated")
        if amity.amity_living_spaces:
            print("Living spaces")
            print("____________________________")
            for room, occupants in amity.amity_living_spaces.items():
                print(room)
                print("-" * 6 * (len(occupants) + 1))
                if occupants:
                    print(", ".join(occupants))
                    print()
                else:
                    print("No occupants yet")
                    print()
        else:
            print("There are currently no Living Spaces allocated")
        if file_name:
            amity.load_allocations_to_file(file_name)
            print("\n\nAllocations have been loaded to the text file: {}".format(
                                                                    file_name))
        print("*" * 15)
        print()

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [<file_name>]"""
        file_name = arg["<file_name>"]
        amity.print_unallocated()
        print("\n" + "*" * 15)
        if amity.unallocated_offices:
            print("People who need offices")
            print("-" * 15)
            print(", ".join(amity.unallocated_offices))
            print()
        else:
            print("There are currently no people who need Offices")
        if amity.unallocated_living_spaces:
            print("People who need Living spaces")
            print("-" * 15)
            print(", ".join(amity.unallocated_living_spaces))
            print()
        else:
            print("There are currently no people who need Living Spaces")
        if file_name:
            amity.load_unallocated_to_file(file_name)
            print("\n\nUnallocated list has been loaded to: {}".format(
                                                                file_name))
        print("*" * 15)
        print()

    @docopt_cmd
    def do_reallocate(self, arg):
        """Usage: reallocate <person_name> <new_room>"""
        new_room = arg["<new_room>"]
        person_name = arg["<person_name>"]
        if person_name in (list(amity.amity_fellows.keys()) +
                           list(amity.amity_staff.keys())):
            print("\n" + "*" * 15)
            amity.reallocate(person_name, new_room)
            print("*" * 15 + "\n")
        else:
            print("\n{} is int a person in Amity".format(person_name))
            print("*" * 15 + "\n")

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""
        room_name = arg["<room_name>"]
        print("\n" + "*" * 15)
        if (room_name in amity.amity_offices or
                room_name in amity.amity_living_spaces):
            if amity.amity_offices or amity.amity_living_spaces:
                for room, occupants in amity.amity_offices.items():
                    if room == room_name:
                        print(room)
                        print("-" * 6 * (len(occupants) + 1))
                        if occupants:
                            print(", ".join(occupants))
                            print()
                        else:
                            print("No occupants yet\n")
            else:
                print("There are currently no rooms in Amity\n")
        else:
            print("{} is not a room in Amity\n".format(room_name))

    @docopt_cmd
    def do_load_people(self, arg):
        """Usage: load_people <file_name>"""
        file_name = arg["<file_name>"]
        f = open(file_name, mode="rt")
        for line in f:
            print("\n" + "*" * 15)
            args = line.split()
            person_name = args[0] + " " + args[1]
            if len(args) > 3:
                if args[3] == 'Y' or args[3] == 'y':
                    amity.add_person(person_name, args[2], True)
                elif args[3] == 'N' or args[3] == 'n':
                    amity.add_person(person_name, args[2])
                else:
                    print("Please use 'Y/N' or 'y/n' for accomodation option")
                print("*" * 15)
            else:
                amity.add_person(person_name, args[2])
                print("*" * 15)
        f.close()

    @docopt_cmd
    def do_save_state(self, arg):
        """Usage: save_state [<db_name>]"""
        print("\n" + "*" * 15)
        amity.save_state()

        print("*" * 15)

opt = docopt(__doc__, sys.argv[1:])
Amity().cmdloop()
