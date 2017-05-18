"""Module to contain classes and methods related rooms in Amity."""


class Room:
    """Parent class to LivingSpace class and Office class.

    Contains attribute and methods to be inherited
    """

    def __init__(self):
        """Set Initialiser of the Room class."""
        self.room_capacity = 0
        self.all_rooms = {}

    def create_room(self, room_name, room_type):
        """Create a new room and add it to the all rooms dictionary."""
        # do i need new args for room name and room type?
        self.all_rooms[room_name] = room_type


class Office(Room):
    """Class to create office rooms."""

    def __init__(self):
        """Initialise the Office object."""
        super(Office, self).__init__()
        self.room_capacity = 6

    def create_room(self, room_name):
        """Create a new Office room."""
        super(Office, self).create_room(room_name, 'Office')


class LivingSpace(Room):
    """Class to create living space rooms."""

    def __init__(self):
        """Initialise the LivingSpcae object."""
        super(LivingSpace, self).__init__()
        self.room_capacity = 4

    def create_room(self, room_name):
        """Create a new Living space room."""
        super(LivingSpace, self).create_room(room_name, 'Living Space')
