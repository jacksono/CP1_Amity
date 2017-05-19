"""Module to contain test cases for the amity class."""

import unittest
from amity import Amity


class TestAmityFunctions(unittest.TestCase):
    """Definiation of test cases for Amity functions."""

    def setUp(self):
        """Fixture to setup an object of the Amity class for the test cases."""
        self.amity = Amity()

    def test_room_created_succesfully(self):
        """Tests if one office room is created succesfully."""
        initial_room_no = len(self.amity.amity_all_rooms)
        self.amity.create_room("Tsavo", "o")
        final_room_no = len(self.amity.amity_all_rooms)
        self.assertEqual(1, final_room_no - initial_room_no,
                         msg="Number of rooms must increase by 1 if the room"
                         " was created succesfully")

    def test_correct_office_room_created(self):
        """Tests if correct office name and type are created."""
        self.amity.create_room('Tsavo', 'o')
        self.assertIn("Tsavo", self.amity.amity_offices,
                      msg="Correct office name and type should be returned")

    def test_correct_living_space_created(self):
        """Tests if correct living space name and type are created."""
        self.amity.create_room('Go', 'l')
        self.assertIn("Go", self.amity.amity_living_spaces, msg="Correct"
                      " living space name and type should be returned")

    def test_person_created_successfully(self):
        """Tests if one person is created succesfully."""
        initial_person_no = len(self.amity.amity_all_people)
        self.amity.add_person("Daniel", "Staff")
        final_person_no = len(self.amity.amity_all_people)
        self.assertEqual(1, final_person_no - initial_person_no,
                         msg="Total number of people should increase by 1 if a"
                         " new person is created successfully")

    def test_correct_staff_member_added(self):
        """Tests if a staff member can be created with right details."""
        self.amity.add_person("Roger", "Staff")
        self.assertEqual(self.amity.amity_staff["Roger"][0], "Staff",
                         msg="Correct details of the staff should be added")

    def test_correct_fellow_added(self):
        """Tests if a fellow can be created with right details."""
        self.amity.add_person("Joseph", "Fellow", True)
        self.amity.add_person("Ritah", "Fellow")
        self.assertEqual(self.amity.amity_fellows["Joseph"][0], "Fellow")
        self.assertEqual(self.amity.amity_fellows["Ritah"][0], "Fellow",
                         msg="Correct details of the fellow shoud be added")

    def test_fellow_accomodation_option_picked_correctly(self):
        """Tests if fellow's accomodatio option is correctly picked."""
        self.amity.add_person("Joseph", "Fellow", True)
        self.amity.add_person("Ritah", "Fellow")
        self.amity.add_person("Sharon", "Fellow", False)
        self.assertTrue(self.amity.amity_fellows["Joseph"][1],
                        msg="Correct accomodation option for the fellow should"
                        "be saved")
        self.assertFalse(self.amity.amity_fellows["Ritah"][1],
                         msg="Correct accomodation option for the fellow"
                         " should be saved")
        self.assertFalse(self.amity.amity_fellows["Sharon"][1],
                         msg="Correct accomodation option for the fellow"
                         " should be saved")

    def test_new_staff_added_and_allocated_to_a_room(self):
        """Tests if a staff member is allocated an office after being added."""
        self.amity.create_room("new", "o")
        self.amity.add_person("Steve", "Staff")
        self.assertIn(["Steve"],
                      list(self.amity.amity_offices.values()),
                      msg="New staff added should be allocated an office room")

    def test_office_room_maximum_capacity_is_not_exceeded(self):
        """Tests maximum capacity of an office is maintained."""
        self.amity.create_room("new", "o")
        for person in ["Steve", "Resty", "Paul", "John", "Jackie", "Mendis"]:
            self.amity.add_person(person, "Staff")
        self.assertEqual("All available Offices are fully occupied",
                         self.amity.add_person("Kimmy", "Staff"),
                         msg="Maximum capacity of office shouldnt be exceeded")

    def test_fellow_added_and_allocated_office_room_only(self):
        """Tests if a fellow is allocated a room.

        The fellow is allocated an office only if he chooses not to have
        accomodation.
        """
        self.amity.create_room("Office", "o")
        self.amity.create_room("LivingSpace", "l")
        self.amity.add_person("Joe", "Fellow")
        self.assertIn(["Joe"], list(self.amity.amity_offices.values()),
                      msg="Fellow added should be allocated only an office"
                      " if he chooses not to have accomodation")
        self.assertNotIn(["Joe"],
                         list(self.amity.amity_living_spaces.values()),
                         msg="Fellow added should not be allocated"
                         " LivingSpaceif he cooses not to have accomodation")

    def test_fellow_added_and_allocated_office_room_and_living_space(self):
        """Tests if a fellow is allocated an office and living space.

        The fellow is allocated an office and living spcae if he chooses
        to have accomodation.
        """
        self.amity.create_room("Office", "o")
        self.amity.create_room("LivingSpace", "l")
        self.amity.add_person("Joe", "Fellow", True)
        self.assertIn(["Joe"], list(self.amity.amity_offices.values()),
                      msg="Fellow should be allocated both an office and"
                      " living spcae if he chooses to have accomodation")
        self.assertIn(["Joe"],
                      list(self.amity.amity_living_spaces.values()),
                      msg="Fellow should be allocated both an office and"
                      " living space if he chooses to have accomodation")

    def test_living_space_room_maximum_capacity_is_not_exceeded(self):
        """Tests maximum capacity of a living space  is maintained."""
        self.amity.create_room("new", "l")
        self.amity.create_room("new", "o")
        for person in ["Steve", "Resty", "Paul", "John"]:
            self.amity.add_person(person, "Fellow", True)
        self.assertEqual("All available living spaces are fully occupied",
                         self.amity.add_person("Kimmy", "Fellow", True),
                         msg="Maximum capacity of living space shouldnt be"
                         " exceeded")

    def test_staff_member_reallocated_correctly(self):
        """Tests staff reallocated to correct room from old room."""
        self.amity.create_room("Room1", "o")
        self.amity.add_person("Carlos", "Staff")
        self.amity.create_room("Room2", "o")
        self.amity.reallocate("Carlos", "Room2")
        self.assertIn("Carlos", self.amity.amity_offices["Room2"],
                      msg="Staff should move to new room after reallocation")
        self.assertNotIn("Carlos", self.amity.amity_offices["Room1"],
                         msg="Staff should move from old room after"
                         " reallocation")

    def test_fellow_reallocated_to_office_correctly(self):
        """Tests if a fellow is reallocated to correct office from old one."""
        self.amity.create_room("Room1", "o")
        self.amity.add_person("Brenda", "Fellow")
        self.amity.create_room("Room2", "o")
        self.amity.reallocate("Brenda", "Room2")
        self.assertIn("Brenda", self.amity.amity_offices["Room2"],
                      msg="Fellow should move to new room after reallocation")
        self.assertNotIn("Brenda", self.amity.amity_offices["Room1"],
                         msg="Fellow should move from old room after"
                         " reallocation")

    def test_fellow_reallocated_to_living_space_correctly(self):
        """Tests if a fellow is reallocated to the correct living space."""
        self.amity.create_room("Room1", "o")
        self.amity.create_room("Room2", "l")
        self.amity.add_person("Brenda", "Fellow", True)
        self.amity.create_room("Room3", "l")
        self.amity.reallocate("Brenda", "Room3")
        self.assertIn("Brenda", self.amity.amity_living_spaces["Room3"],
                      msg="Fellow should move to new living space after"
                      " reallocation")
        self.assertNotIn("Brenda", self.amity.amity_living_spaces["Room2"],
                         msg="Fellow should move from old living space after"
                         " reallocation")

    def test_cannot_reallocate_a_person_to_a_full_room(self):
        """Tests a person can't be allocated to a room which is full."""
        pass

    def test_relocating_a_person_to_the_same_room_returns_error_message(self):
        """Tests that an error message is shown when a person is realloacted.

        To a room in which he or she previously was.
        """
        self.amity.create_room("Room1", "o")
        self.amity.add_person("Brenda", "Fellow")
        self.assertEqual("Brenda is already in Room1",
                         self.amity.reallocate("Brenda", "Room1"),
                         msg="Shouldn't reallocate someone to the same room")

    def test_can_delete_a_room(self):
        """Tests if the delete room method correctly deletes a room."""
        self.amity.create_room("Room1", "o")
        self.amity.create_room("Room2", "l")
        self.amity.delete_room("Room1")
        self.amity.delete_room("Room2")
        self.assertNotIn("Room1", self.amity.amity_offices,
                         msg="Room should be removed from rooms list after"
                         " being deleted")
        self.assertNotIn("Room2", self.amity.amity_living_spaces,
                         msg="Room should be removed from rooms list after"
                         " being deleted")

    def test_can_delete_a_person(self):
        """Tests if the delete person method correctly deletes a person."""
        self.amity.create_room("Room1", "o")
        self.amity.add_person("Kate", "Staff")
        self.amity.add_person("Bruce", "Fellow")
        self.amity.delete_person("Kate")
        self.amity.delete_person("Bruce")
        self.assertNotIn("Kate", self.amity.amity_staff,
                         msg="Person should be removed from  staff list after"
                         " being deleted")
        self.assertNotIn("Bruce", self.amity.amity_fellows,
                         msg="Person should be removed from fellow list after"
                         " being deleted")

    def test_can_convert_office_to_living_space(self):
        """Tests if the convert_room method works correctly.

        Should be able to convert an office to a living space
        """
        self.amity.create_room("Oculus", "o")
        self.amity.create_room("Python", "l")
        self.amity.convert_room("Oculus", "l")
        self.assertIn("Oculus", self.amity.amity_living_spaces,
                      msg="Oculus should now be a living space")
        self.assertNotIn("Oculus", self.amity.amity_offices,
                         msg="Oculus should nolonger be  an office")





if __name__ == '__main__':
    unittest.main()
