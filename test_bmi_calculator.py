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

    
    """ Test BMI calculation with invalid (zero) inputs (1.3) """
    def test_calculate_bmi_invalid_zero(self):
        # Arrange
        weight = 0
        height = 1.75

        # Act and assert
        with self.assertRaises(ValueError):
            calculate_bmi(weight, height)


    """ Test BMI calculation with invalid (wrong type) inputs (1.4) """
    def test_calculate_bmi_invalid_type(self):
        # Arrange
        weight = "Invalid value"
        height = 1.75

        # Act and assert
        with self.assertRaises(ValueError):
            calculate_bmi(weight, height)

    
    """ Test BMI calculation with invalid (null) inputs (1.5) """
    def test_calculate_bmi_invalid_null(self):
        # Arrange
        weight = None
        height = None

        # Act and assert
        with self.assertRaises(ValueError):
            calculate_bmi(weight, height)


if __name__ == "__main__":
    unittest.main()