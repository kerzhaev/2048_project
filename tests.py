import unittest
from logics import get_number_from_index, get_index_from_number, move_left, move_up

class Test_2048(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_number_from_index(1,2),7)
    def test_2(self):
        self.assertEqual(get_number_from_index(3,3),16)


    def test_6(self):
        self.assertEqual(get_index_from_number(7),(1,2))
    def test_7(self):
        self.assertEqual(get_index_from_number(16),(3,3))

    def test_13(self):
        mas = [
            [2, 4, 4, 2],
            [4, 0, 0, 2],
            [0, 0, 0, 0],
            [8, 8, 4, 4],
            ]
        rez = [
            [2, 8, 2, 0],
            [4, 2, 0, 0],
            [0, 0, 0, 0],
            [16, 8, 0, 0],
            ]
        self.assertEqual(move_left(mas), rez )

    def test_14(self):
        mas = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0],
            ]
        rez = [
            [4, 8, 4, 2],
            [8, 0, 0, 0],
            [0, 0, 0, 4],
            [0, 0, 0, 0],
            ]
        self.assertEqual(move_up(mas), rez )

