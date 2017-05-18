"""Module to contain classes and methods related rooms in Amity."""


class Room:
    """Parent class to LivingSpace class and Office class.

    Contains attribute and methods to be inherited
    """

    def __init__(self):
        """Set Initialiser of the Room class."""
        self.room_capacity = 0
        self.all_rooms = {}

    def create_room(self, room_name, occupant=''):
        """Create a new room and add it to the all rooms dictionary."""
        self.all_rooms[room_name] = []


class Office(Room):
    """Class to create office rooms."""

    def __init__(self):
        """Initialise the Office object."""
        super(Office, self).__init__()
        self.room_capacity = 6


class LivingSpace(Room):
    """Class to create living space rooms."""

    def __init__(self):
        """Initialise the LivingSpcae object."""
        super(LivingSpace, self).__init__()
        self.room_capacity = 4
