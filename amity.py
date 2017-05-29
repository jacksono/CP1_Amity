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
        self.amity_all_people = {}
        self.amity_staff = {}
        self.amity_fellows = {}
        self.staff = Staff()
        self.fellow = Fellow()
        self.unallocated_offices = []
        self.unallocated_living_spaces = []

    def create_room(self, room_name, type, occupant=''):
        """Create rooms given room names and room type."""
        if room_name in self.amity_offices or\
                room_name in self.amity_living_spaces:
            print("A room with that name already exists,"
                  " please choose another name")
        elif type == 'O' or type == "o":
            self.office.create_room(room_name)
            self.amity_offices.update(self.office.all_rooms)
            print("{} has been created as an Office".format(room_name))
        elif type == 'l' or type == "L":
            self.living_space.create_room(room_name)
            self.amity_living_spaces.update(self.living_space.all_rooms)
            print("{} has been created as a Living Space".format(room_name))
        else:
            print("Please use 'o' or 'O' for Office type and 'l' or 'L' "
                  " for Living Space type")

    def allocate(self, person_name, room_type):
        """Allocate a person to a room."""
        if room_type == "o" or room_type == "O":
            if self.amity_offices:
                allocated_room = random.choice(list(self.amity_offices.keys()))
                if len(self.amity_offices[allocated_room])\
                        < self.office.room_capacity:
                    self.amity_offices[allocated_room].append(person_name)
                    return("{0} has been allocated to the Office: {1}".format(
                                                  person_name, allocated_room))
                else:
                    return ("Allocated room: {} is fully occupied."
                            " Please use reallocate to find a new room".format(
                                allocated_room))
            else:
                return("There are currently no Offices to"
                       " allocate {} to.".format(person_name))
        elif room_type == "l" or room_type == "L":
            if self.amity_living_spaces:
                allocated_room = random.choice(list(
                    self.amity_living_spaces.keys()))
                if len(self.amity_living_spaces[allocated_room])\
                        < self.living_space.room_capacity:
                    self.amity_living_spaces[allocated_room].append(
                                                               person_name)
                    return("{0} has been allocated to the Living space:"
                           " {1}".format(person_name, allocated_room))
                else:
                    return ("Allocated room: {} is fully occupied."
                            " Please use reallocate to find a new room".format(
                                allocated_room))
            else:
                return("There are currently no Living Spaces to"
                       " allocate {} to.".format(person_name))

    def add_person(self, person_name, person_type, wants_acc=False):
        """Create people given name, type and accomodation option."""
        if person_type == "Staff" or person_type == "Fellow":
            if (person_name in self.amity_staff or
                    person_name in self.amity_fellows):
                print("That name already exists, Please use another name")
            elif person_type == 'Staff':
                self.staff.add_person(person_name)
                self.amity_staff.update(self.staff.all_people)
                print("{} has been created as a Staff".format(person_name))
                print(self.allocate(person_name, "O"))
            elif person_type == 'Fellow':
                self.fellow.add_person(person_name, wants_acc)
                self.amity_fellows.update(self.fellow.all_people)
                print("{} has been created as a Fellow".format(person_name))
                if not wants_acc:
                    print(self.allocate(person_name, "O"))
                elif wants_acc:
                    print(self.allocate(person_name, "O"))
                    print(self.allocate(person_name, "L"))
        else:
            print("Please use 'Staff' or 'Fellow' for person types.")

    def reallocate(self, person_name, new_room):
        """Reallocate people from old room to a new one."""
        if new_room in self.amity_offices:
            for room, people in self.amity_offices.items():
                if person_name in people:
                    old_room = room
                    if old_room == new_room:
                        print("{0} is already in {1}".format(person_name,
                                                             new_room))
                        return "{0} is already in {1}".format(person_name,
                                                              new_room)
            self.amity_offices[new_room].append(person_name)
            if old_room:
                self.amity_offices[old_room].remove(person_name)
            print("{0} has been reallocated to {1}".format(person_name,
                                                           new_room))
        elif new_room in self.amity_living_spaces:
            wants_acc = []
            for person, option in self.amity_fellows.items():
                if option[1]:
                    wants_acc.append(person)
            if person_name in wants_acc:
                for room, people in self.amity_living_spaces.items():
                    if person_name in people:
                        old_room = room
                        if old_room == new_room:
                            print("{0} is already in {1}".format(person_name,
                                                                 new_room))
                            return "{0} is already in {1}".format(person_name,
                                                                  new_room)
                self.amity_living_spaces[new_room].append(person_name)
                if old_room:
                    self.amity_living_spaces[old_room].remove(person_name)
                print("{0} has been reallocated to {1}".format(person_name,
                                                               new_room))
            else:
                print("{} does not qualify for a living space".format(
                                                                person_name))
        else:
            print("{} is not a room in Amity".format(new_room))

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
        elif new_type == 'o':
            if room_name in self.amity_living_spaces:
                del(self.amity_living_spaces[room_name])
                self.amity_offices[room_name] = []
            else:
                return "{} is not a living space".format(room_name)

    def promote_fellow(self, fellow_name):
        """Promote a fellow to a staff member."""
        if fellow_name in self.amity_fellows:
            del(self.amity_fellows[fellow_name])
            self.add_person(fellow_name, "Staff")

    def remove_occupant(self, person_name, room_name):
        """Remove a person from a specified room."""
        if room_name in self.amity_offices:
            self.amity_offices[room_name].remove(person_name)
        elif room_name in self.amity_living_spaces:
            self.amity_living_spaces[room_name].remove(person_name)
        else:
            return "That Room doesnot exist"

    def print_unallocated(self):
        """Retrieve a list of unallocated people."""
        staff_set = set(self.amity_staff.keys())
        fellow_set = set(self.amity_fellows.keys())
        fellow_living = []
        office_allocated = []
        living_space_allocated = []
        for occupants in self.amity_offices.values():
            for occupant in occupants:
                office_allocated.append(occupant)
        for occupants in self.amity_living_spaces.values():
            for occupant in occupants:
                living_space_allocated.append(occupant)
        staff_with_no_offices = staff_set.difference(office_allocated)
        fellows_with_no_offices = fellow_set.difference(office_allocated)
        for fellow, option in self.amity_fellows.items():
            if option[1]:
                fellow_living.append(fellow)
        fellows_with_no_living = set(fellow_living).difference(
                                                      living_space_allocated)
        for person in staff_with_no_offices.union(fellows_with_no_offices):
            if person not in self.unallocated_offices:
                self.unallocated_offices.append(person)
        for person in fellows_with_no_living:
            if person not in self.unallocated_living_spaces:
                self.unallocated_living_spaces.append(person)
        return self.unallocated_offices + self.unallocated_living_spaces
