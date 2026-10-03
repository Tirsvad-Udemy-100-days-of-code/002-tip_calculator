import unittest

from tip_calculator.calculator import bill_per_person


class BillPerPersonTests(unittest.TestCase):
    def test_course_example(self):
        self.assertEqual(bill_per_person(124.56, 12, 7), 19.93)

    def test_tip_split_five_ways(self):
        self.assertEqual(bill_per_person(150, 12, 5), 33.6)

    def test_zero_people_raises(self):
        with self.assertRaises(ValueError):
            bill_per_person(100, 10, 0)


if __name__ == "__main__":
    unittest.main()
