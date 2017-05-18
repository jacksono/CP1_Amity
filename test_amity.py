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
        initial_room_no = len(self.amity.all_rooms)
        tsavo_office = self.amity.create_room(["Tsavo"], "office")
        final_room_no = len(self.amity.all_rooms)
        self.assertTrue(tsavo_office)
        self.assertEqual(1, final_room_no - initial_room_no)

    def test_correct_office_room_created(self):
        """Tests if correct office name and type are created."""
        self.amity.create_room(['Tsavo'], 'office')
        self.assertEqual(self.amity.all_rooms['Tsavo'], 'office')

    def test_correct_living_space_created(self):
        """Tests if correct living space name and type are created."""
        self.amity.create_room(['Go'], 'living_space')
        self.assertEqual(self.amity.all_rooms['Go'], 'living_space')

    def test_can_create_multiple_rooms(self):
        """Tests if multiple rooms can be created."""
        initial_room_no = len(self.amity.all_rooms)
        self.amity.create_room(['Narnia', 'Krpton', 'Valhala'], 'office')
        final_room_no = len(self.amity.all_rooms)
        self.assertEqual(3, final_room_no - initial_room_no)


if __name__ == '__main__':
    unittest.main()
