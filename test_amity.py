"""Module to contain test cases for the amity class."""

import unittest
from amity import Amity


class TestAmityFunctions(unittest.TestCase):
    """Definiation of test cases for Amity functions."""

    def setUp(self):
        """Set up for the test cases."""
        self.amity = Amity()

    def test_office_created_succesfully(self):
        """Tests if one office room is created succesfully."""
        initial_room_no = len(self.amity.amity_all_rooms)
        self.amity.create_room("Tsavo", "o")
        final_room_no = len(self.amity.amity_all_rooms)
        self.assertEqual(1, final_room_no - initial_room_no)

    def test_correct_office_room_created(self):
        """Tests if correct office name and type are created."""
        self.amity.create_room('Tsavo', 'o')
        self.assertEqual(self.amity.amity_offices['Tsavo'], 'Office')

    def test_correct_living_space_created(self):
        """Tests if correct living space name and type are created."""
        self.amity.create_room('Go', 'l')
        self.assertEqual(self.amity.amity_living_spaces['Go'], 'Living Space')


if __name__ == '__main__':
    unittest.main()
