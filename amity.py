"""Module to contain the amity class and methods  for all amity operations."""
from room import Office, LivingSpace
from person import Fellow, Staff
import random
from db.db import Rooms, People, create_db, Allocations, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from termcolor import colored
import os


class Amity:
    """Definition of Amity class."""

    def __init__(self):
        """Initialise  the Amity class."""
        self.amity_offices = {}
        self.amity_living_spaces = {}
        self.office = Office()
        self.living_space = LivingSpace()
        self.amity_staff = {}
        self.amity_fellows = {}
        self.staff = Staff()
        self.fellow = Fellow()
        self.unallocated_offices = []
        self.unallocated_living_spaces = []

    def create_room(self, room_names, type, occupant=''):
        """Create rooms given room names and room type."""
        for room_name in room_names:
            if room_name in self.amity_offices or\
                    room_name in self.amity_living_spaces:
                print(colored("A room named {} already exists,"
                      " please choose another name".format(room_name), 'red'))
            elif type == 'O' or type == "o":
                self.office.create_room(room_name)
                self.amity_offices.update(self.office.all_rooms)
                print(colored("{} has been created as an Office".format(
                    room_name), "blue"))
            elif type == 'l' or type == "L":
                self.living_space.create_room(room_name)
                self.amity_living_spaces.update(self.living_space.all_rooms)
                print(colored("{} has been created as a Living Space".format(
                                                        room_name), "blue"))
            else:
                print(colored("Please use 'o' or 'O' for Office type and 'l'"
                      " or 'L' for Living Space type", "red"))

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
        if (person_type.lower() == "staff" or person_type.lower() == "fellow"):
            if (person_name in self.amity_staff or
                    person_name in self.amity_fellows):
                print(colored("{} already exists, Please use another"
                              " name".format(person_name), "red"))
            elif person_type.lower() == 'staff':
                if wants_acc:
                    print(colored("A staff member cannot be allocated "
                                  " accomodation", "red"))
                else:
                    self.staff.add_person(person_name)
                    self.amity_staff.update(self.staff.all_people)
                    print(colored("{} has been created as a Staff".format(
                                                        person_name), "blue"))
                    print(colored(self.allocate(person_name, "O"), "blue"))
            elif person_type.lower() == 'fellow':
                self.fellow.add_person(person_name, wants_acc)
                self.amity_fellows.update(self.fellow.all_people)
                print(colored("{} has been created as a Fellow".format(
                                                        person_name), "blue"))
                if not wants_acc:
                    print(colored(self.allocate(person_name, "O"), "blue"))
                elif wants_acc:
                    print(colored(self.allocate(person_name, "O"), "blue"))
                    print(colored(self.allocate(person_name, "L"), "blue"))
        else:
            print(colored("Please use 'Staff'or 'Fellow' or for person type.",
                          "red"))

    def reallocate(self, person_name, new_room):
        """Reallocate people from old room to a new one."""
        old_room = ""
        if new_room in self.amity_offices:
            if len(self.amity_offices[new_room])\
                    >= self.office.room_capacity:
                    print(colored("{} is currently fully occupied, cannot"
                                  " reallocate".format(new_room), "red"))
            else:
                for room, people in self.amity_offices.items():
                    if person_name in people:
                        old_room = room
                        if old_room == new_room:
                            print(colored("{0} is already in {1}".format(
                                person_name, new_room), "red"))
                            return "{0} is already in {1}".format(person_name,
                                                                  new_room)
                        elif old_room != "":
                            self.amity_offices[old_room].remove(person_name)
                            self.amity_offices[new_room].append(person_name)
                            print(colored("{0} has been reallocated"
                                  " to {1}".format(person_name, new_room),
                                          "blue"))
                            break
                        elif old_room == "":
                            self.amity_offices[new_room].append(person_name)
                            if person_name in self.unallocated_offices:
                                self.unallocated_offices.remove(person_name)
                            print(colored("{0} has been allocated"
                                          " to {1}".format(
                                           person_name, new_room), "blue"))
                            break
        elif new_room in self.amity_living_spaces:
            if len(self.amity_living_spaces[new_room])\
                    >= self.living_space.room_capacity:
                    print(colored("{} is currently fully occupied, cannot"
                                  " reallocate".format(new_room), "red"))
            else:
                wants_acc = []
                for person, option in self.amity_fellows.items():
                    if option[1]:
                        wants_acc.append(person)
                if person_name in wants_acc:
                    for room, people in self.amity_living_spaces.items():
                        if person_name in people:
                            old_room = room
                            if old_room == new_room:
                                print(colored("{0} is already in {1}".format(
                                    person_name, new_room), "red"))
                                return "{0} is already in {1}".format(
                                    person_name, new_room)
                            elif old_room != "":
                                self.amity_living_spaces[new_room].append(
                                    person_name)
                                self.amity_living_spaces[old_room].remove(
                                    person_name)
                                print(colored("{0} has been reallocated"
                                              " to {1}".format(
                                               person_name, new_room), "blue"))
                                break
                            elif old_room == "":
                                self.amity_living_spaces[new_room].append(
                                    person_name)
                                if person_name in\
                                   self.unallocated_living_spaces:
                                    self.unallocated_living_spaces.remove(
                                        person_name)
                                print(colored("{0} has been allocated"
                                              " to {1}".format(
                                               person_name, new_room), "blue"))
                                break

                else:
                    print(colored("{} does not qualify for a living"
                                  " space".format(person_name), "red"))
        else:
            print(colored("{} is not a room in Amity".format(new_room), "red"))

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
                if occupant not in office_allocated:
                    office_allocated.append(occupant)
        for occupants in self.amity_living_spaces.values():
            for occupant in occupants:
                if occupant not in living_space_allocated:
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

    def load_allocations_to_file(self, file_name):
        """Load the allocations to a text file."""
        f = open(file_name, mode='wt')
        if self.amity_offices:
            f.write("\nOffices\n")
            f.write("____________________________\n")
            for room, occupants in self.amity_offices.items():
                f.write("\n" + room + "\n")
                f.write("-" * 6 * (len(occupants) + 1) + "\n")
                if occupants:
                    f.write(", ".join(occupants) + "\n")
                else:
                    f.write("No occupants yet\n")
        else:
            f.write("\nThere are currently no offices allocated\n")
        if self.amity_living_spaces:
            f.write("\n\nLiving spaces\n")
            f.write("____________________________\n")
            for room, occupants in self.amity_living_spaces.items():
                f.write("\n" + room + "\n")
                f.write("-" * 6 * (len(occupants) + 1) + "\n")
                if occupants:
                    f.write(", ".join(occupants) + "\n")
                else:
                    f.write("No occupants yet\n")
        else:
            f.write("\nThere are currently no Living Spaces allocated")
        f.close()

    def load_unallocated_to_file(self, file_name):
        """Load list of unallocated people to a text file."""
        f = open(file_name, mode="wt")
        if self.unallocated_offices:
            f.write("\nPeople who need offices\n")
            f.write("-" * 15 + "\n")
            for person in self.unallocated_offices:
                f.write("> " + person + "\n")
        else:
            f.write("\nThere are currently no people who need Offices\n")
        if self.unallocated_living_spaces:
            f.write("\n\nPeople who need Living spaces\n")
            f.write("-" * 15 + "\n")
            for person in self.unallocated_living_spaces:
                f.write("> " + person + "\n")
        else:
            f.write("\nThere are currently no people who need Living Spaces\n")
        f.close()

    def save_state(self, db_name='amity.db'):
        """Save amity data into db tables."""
        engine = create_db(db_name)
        Base.metadata.bind = engine
        Session = sessionmaker()
        session = Session()
        allocated_rooms = {}

        for name, occupants in self.amity_offices.items():
            new_office = Rooms(room_name=name, room_type="O",
                               no_of_occupants=len(occupants))
            session.add(new_office)
            session.commit()

        for name, occupants in self.amity_living_spaces.items():
            new_living_space = Rooms(room_name=name, room_type="L",
                                     no_of_occupants=len(occupants))
            session.add(new_living_space)
            session.commit()

        for name in self.amity_staff.keys():
            new_staff = People(name=name, category='Staff', wants_acc="N")
            session.add(new_staff)
            session.commit()

        for name, details in self.amity_fellows.items():
            if details[1]:
                new_staff = People(name=name, category='Fellow', wants_acc="Y")
            else:
                new_staff = People(name=name, category='Fellow', wants_acc="N")
            session.add(new_staff)
            session.commit()

        for name, occupants in self.amity_offices.items():
            for occupant in occupants:
                allocated_rooms[occupant] = [name, None]
        for name, occupants in self.amity_living_spaces.items():
            for occupant in occupants:
                if allocated_rooms[occupant][0]:
                    allocated_rooms[occupant][1] = name
                else:
                    allocated_rooms[occupant] = [None, name]
        for name, rooms in allocated_rooms.items():
            new_allocation = Allocations(name=name,
                                         office_allocated_to=rooms[0],
                                         living_allocated_to=rooms[1])
            session.add(new_allocation)
            session.commit()

        print(colored("Application data successfully saved to the"
                      " database >> {}".format(db_name), "blue"))

    def load_state(self, db_name):
        """Load data from a db to the app."""
        if not os.path.isfile(db_name):
            print("Database does not exist")
        else:
            engine = create_engine('sqlite:///' + db_name)
            Base.metadata.bind = engine
            Session = sessionmaker(bind=engine)
            session = Session()

            staff = session.query(People).filter_by(category="Staff").all()
            for person in staff:
                self.amity_staff[person.name] = [person.category,
                                                 person.wants_acc]

            fellows = session.query(People).filter_by(category="Fellow").all()
            for person in fellows:
                self.amity_fellows[person.name] = [person.category,
                                                   person.wants_acc]
            offices = session.query(Rooms).filter_by(room_type="O").all()
            for office in offices:
                self.amity_offices[office.room_name] = []

            l_spaces = session.query(Rooms).filter_by(room_type="L").all()
            for l_space in l_spaces:
                self.amity_living_spaces[l_space.room_name] = []

            occupants = session.query(Allocations).all()
            for occupant in occupants:
                if occupant.office_allocated_to:
                    self.amity_offices[occupant.office_allocated_to].append(
                                                                occupant.name)
                if occupant.living_allocated_to:
                    (self.amity_living_spaces[occupant.living_allocated_to].
                     append(occupant.name))
