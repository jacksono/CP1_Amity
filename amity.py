"""Module to contain the amity class and methods  for all amity operations."""
from room import Office, LivingSpace
from person import Fellow, Staff


class Amity:
    """Definition of Amity class."""

    def __init__(self):
        """Initialise  the Amity class."""
        self.amity_offices = {}
        self.amity_living_spaces = {}
        self.office = Office()
        self.living_space = LivingSpace()
        self.amity_all_rooms = {}
        self.amity_all_people = {}
        self.amity_staff = {}
        self.amity_fellows = {}
        self.staff = Staff()
        self.fellow = Fellow()

    def create_room(self, room_name, type):
        """Create rooms given room names and room type."""
        if type == 'o':
            self.office.create_room(room_name)
            self.amity_offices.update(self.office.all_rooms)
            self.amity_all_rooms.update(self.office.all_rooms)
        elif type == 'l':
            self.living_space.create_room(room_name)
            self.amity_living_spaces.update(self.living_space.all_rooms)
            self.amity_all_rooms.update(self.living_space.all_rooms)

    def add_person(self, person_name, person_type, wants_acc=False):
        """Create people given name, type and accomodation option."""
        if person_type == 'Staff':
            self.staff.add_person(person_name)
            self.amity_staff.update(self.staff.all_people)
            self.amity_all_people.update(self.staff.all_people)
        elif person_type == 'Fellow':
            self.fellow.add_person(person_name, wants_acc)
            self.amity_fellows.update(self.fellow.all_people)
            self.amity_all_people.update(self.fellow.all_peolple)
