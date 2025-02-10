import unittest
from bmi_calculator import calculate_bmi

class TestBMICalculator(unittest.TestCase):

    """ Test BMI calculation for valid inputs (1.1) """
    def test_calculate_bmi_valid(self):
        # Arrange
        weight = 70
        height = 1.75

        expected_bmi = round(70 / (1.75 ** 2), 2)

        # Act
        calculated_bmi = round(calculate_bmi(weight, height), 2)

        # Assert
        self.assertEqual(calculated_bmi, expected_bmi)


    """ Test BMI calculation with invalid (negative) inputs (1.2) """
    def test_calculate_bmi_invalid_negative(self):
        # Arrange
        weight = -70
        height = 1.75

        # Act and assert
        with self.assertRaises(ValueError):
            calculate_bmi(weight, height)


if __name__ == "__main__":
    unittest.main()