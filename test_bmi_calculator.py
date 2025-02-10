import sys
import unittest
import json
from unittest.mock import patch, mock_open
from io import StringIO
from datetime import datetime
from bmi_calculator import calculate_bmi, load_existing_data, main, update_bmi_for_user, add_new_user, write_to_file, process_input_data, read_input_file

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

    
    """ Test output file does not exist (2.1) """
    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_load_existing_data_file_not_found(self, mock_file):
        # Act
        result = load_existing_data("non_existent_file.json")

        # Assert
        self.assertEqual(result, [])


    """ Test output file exists but user is not found (2.2) """
    def test_update_bmi_for_user_new_user(self):
        # Arrange
        user = {
            "userId": 1,
            "firstname": "John",
            "lastname": "Doe",
            "weight": 70,
            "height": 1.75
        }

        existing_data = []

        # Act
        result = update_bmi_for_user(user, existing_data)

        # Assert
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["userId"], user["userId"])


    """ Test output file exists and user is found (2.3) """
    def test_update_bmi_for_user_existing_user(self):
        # Arrange
        user = {
            "userId": 1,
            "firstname": "John",
            "lastname": "Doe",
            "weight": 70,
            "height": 1.75
        }

        existing_data = [{
            "userId": 1,
            "firstname": "John",
            "lastname": "Doe",
            "bmiMeasures": []
        }]

        # Act
        result = update_bmi_for_user(user, existing_data)

        # Assert
        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]["bmiMeasures"]), 1)

    
    """ Test input file is found and contains valid JSON (3.1) """
    @patch("builtins.open", mock_open(read_data='{"userId": 1, "firstname": "John", "lastname": "Doe", "weight": 70, "height": 1.75}'))
    def test_read_valid_json(self):
        # Arrange
        expected_result = '{"userId": 1, "firstname": "John", "lastname": "Doe", "weight": 70, "height": 1.75}'
        
        # Act
        result = read_input_file("input.json")
        
        # Assert
        self.assertEqual(result, expected_result)


    """ Test input file is not found (3.2) """
    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_input_file_not_found(self, mock_file):
        # Act and assert
        with self.assertRaises(FileNotFoundError):
            read_input_file("non_existent_input.json")
    

    """ Test no input file provided (3.3) """
    @patch('sys.argv', ["bmi_calculator.py"])
    def test_main_no_input_file(self):
        # Act and assert
        with self.assertRaises(ValueError):
            main()




if __name__ == "__main__":
    unittest.main()