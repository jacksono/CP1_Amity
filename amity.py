"""Module to contain the amity class and methods  for all amity operations."""
from room import Office, LivingSpace
from person import Fellow, Staff
import random


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

    def create_room(self, room_name, type, occupant=''):
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
            if self.amity_offices:
                allocated_room = random.choice(list(self.amity_offices.keys()))
                if len(self.amity_offices[allocated_room])\
                        < self.office.room_capacity:
                    self.amity_offices[allocated_room].append(person_name)
                    self.amity_all_rooms.update(self.amity_offices)
                else:
                    return "All available Offices are fully occupied"
        elif person_type == 'Fellow':
            self.fellow.add_person(person_name, wants_acc)
            self.amity_fellows.update(self.fellow.all_people)
            self.amity_all_people.update(self.fellow.all_people)
            if self.amity_offices and not wants_acc:
                allocated_room = random.choice(list(self.amity_offices.keys()))
                if len(self.amity_offices[allocated_room])\
                        < self.office.room_capacity:
                    self.amity_offices[allocated_room].append(person_name)
                    self.amity_all_rooms.update(self.amity_offices)
                else:
                    return "All available Offices are fully occupied"
            elif self.amity_offices and self.amity_living_spaces and wants_acc:
                allocated_office =\
                 random.choice(list(self.amity_offices.keys()))
                allocated_living_space =\
                    random.choice(list(self.amity_living_spaces.keys()))
                if len(self.amity_offices[allocated_office])\
                        < self.office.room_capacity:
                    self.amity_offices[allocated_office].append(person_name)
                    self.amity_all_rooms.update(self.amity_offices)
                else:
                    return "All available offices are fully occupied"
                if len(self.amity_living_spaces[allocated_living_space])\
                        < self.living_space.room_capacity:
                    self.amity_living_spaces[allocated_living_space].\
                      append(person_name)
                    self.amity_all_rooms.update(self.amity_living_spaces)
                else:
                    return "All available living spaces are fully occupied"

    def reallocate(self, person_name, new_room):
        """Reallocate people from old room to a new one."""
        if new_room in self.amity_offices:
            for room, people in self.amity_offices.items():
                if person_name in people:
                    old_room = room
                    if old_room == new_room:
                        return "{} is already in {}".format(person_name,
                                                            new_room)
            self.amity_offices[new_room].append(person_name)
            self.amity_offices[old_room].remove(person_name)
        elif new_room in self.amity_living_spaces:
            for room, people in self.amity_living_spaces.items():
                if person_name in people:
                    old_room = room
                    if old_room == new_room:
                        return "{} is already in {}".format(person_name,
                                                            new_room)
            self.amity_living_spaces[new_room].append(person_name)
            self.amity_living_spaces[old_room].remove(person_name)

    def delete_room(self, room_name):
        """Delete room specified."""
        if room_name in self.amity_offices:
            del(self.amity_offices[room_name])
        elif room_name in self.amity_living_spaces:
            del(self.amity_living_spaces[room_name])
        else:
            return "That room does not exist"

    def delete_person(self, person_name):
        """Delete person specified."""
        if person_name in self.amity_staff:
            del(self.amity_staff[person_name])
        elif person_name in self.amity_fellows:
            del(self.amity_fellows[person_name])
        else:
            return "That person does not exist"

    def convert_room(self, room_name, new_type):
        """Convert a room to the new type specified."""
        if new_type == 'l':
            if room_name in self.amity_offices:
                del(self.amity_offices[room_name])
                self.amity_living_spaces[room_name] = []
            else:
                return "{} is not an office".format(room_name)
