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
        """Usage: create_room <room_type> <room_name>"""
        room_type = arg["<room_type>"]
        room_name = arg["<room_name>"]
        amity.create_room(room_name, room_type)


opt = docopt(__doc__, sys.argv[1:])
Amity().cmdloop()
