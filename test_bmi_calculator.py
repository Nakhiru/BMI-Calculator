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


if __name__ == "__main__":
    unittest.main()