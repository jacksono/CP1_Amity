"""Module to contain the amity class and methods  for all amity operations."""


class Amity:
    """Definition of Amity class."""

    def __init__(self):
        """Initialise  the Amity class."""
        self.all_rooms = {}

    def create_room(self, room_name, room_type):
        """Create rooms given room names and room type."""
        for name in room_name:
            self.all_rooms[name] = room_type
            print("{} has been created".format(name))
        return "Command completed succesfully"
