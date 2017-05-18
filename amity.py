"""Module to contain the amity class and methods  for all amity operations."""
from room import Office, LivingSpace


class Amity:
    """Definition of Amity class."""

    def __init__(self):
        """Initialise  the Amity class."""
        self.amity_offices = {}
        self.amity_living_spaces = {}
        self.office = Office()
        self.living_space = LivingSpace()

    def create_room(self, room_name, type):
        """Create rooms given room names and room type."""
        if type == 'o':
            self.office.create_room(room_name)
            self.amity_offices.update(self.office.all_rooms)
        elif type == 'l':
            self.living_space.create_room(room_name)
            self.amity_living_spaces.update(self.living_space.all_rooms)
