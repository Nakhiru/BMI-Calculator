import json


def calculate_bmi(weight, height):
    """Calculate BMI given weight and height."""
    try:
        weight = float(weight)
        height = float(height)
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be strictly positive.")
    except (ValueError, TypeError) as e:
        raise ValueError(f"Invalid input: {e}")
    return weight / (height ** 2)

def load_existing_data(output_file):
    """Load existing data from the output JSON file."""
    try:
        with open(output_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # If the file doesn't exist, return an empty list
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON from {output_file}: {e}")

def main():
    print("Hello, BMI Calculator user !")

if __name__ == "__main__":
    main()