"""Module to contain classes and methods related rooms in Amity."""


class Room:
    """Parent class to LivingSpace class and Office class.

    Contains attribute and methods to be inherited
    """

    def __init__(self, room_name, room_type, room_capacity=0):
        """Set Initialiser of the Room class."""
        self.room_name = room_name
        self.room_type = room_type
        self.room_capacity = room_capacity
        self.rooms_list = []
