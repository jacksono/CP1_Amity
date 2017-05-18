"""Module to contain classes and methods related people in Amity."""


class Person:
    """Parent class to Staff class and Fello class."""

    def __init__(self):
        """Initialise the Person class."""
        self.all_people = {}

    def add_person(self, person_name, person_type, wants_acc=False):
        """Create a new person with correct details."""
        self.all_people[person_name] = person_type


class Staff:
    """Class to create staff members."""

    def add_person(self, person_name):
        """Create a new staff member with correct details."""
        super(Staff, self).add_person(person_name, "Staff")
