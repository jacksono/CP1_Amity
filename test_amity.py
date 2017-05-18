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
        self.assertEqual(self.amity.amity_offices['Tsavo'][0], 'Office',
                         msg="Correct office name and type should be returned")

    def test_correct_living_space_created(self):
        """Tests if correct living space name and type are created."""
        self.amity.create_room('Go', 'l')
        self.assertEqual(self.amity.amity_living_spaces['Go'][0], 'Living Space',
                         msg="Correct living space name and type should be"
                         " returned")

    def test_person_created_successfully(self):
        """Tests if one person is created succesfully."""
        initial_person_no = len(self.amity.amity_all_people)
        self.amity.add_person("Daniel", "Staff")
        final_person_no = len(self.amity.amity_all_people)
        self.assertEqual(1, final_person_no - initial_person_no,
                         msg="Total number of people should increase by 1 if a"
                         " new person is creted succesfully")

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


if __name__ == '__main__':
    unittest.main()
