import sys
import json
from datetime import datetime


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


def update_bmi_for_user(user, existing_data):
    """Update BMI measures for the user, or add them if new."""
    found_user = False
    for existing_user in existing_data:
        if existing_user['userId'] == user['userId']:
            bmi = calculate_bmi(user['weight'], user['height'])
            current_date = datetime.now().strftime('%Y-%m-%d')
            existing_user['bmiMeasures'].append({
                'date': current_date,
                'bmi': round(bmi, 2)
            })
            found_user = True
            break

    if not found_user:
        add_new_user(user, existing_data)
    return existing_data


def add_new_user(user, existing_data):
    # Add the new user to the existing data
    existing_data.append({
        "userId": user["userId"],
        "firstname": user["firstname"],
        "lastname": user["lastname"],
        "bmiMeasures": [{
            "date": datetime.now().strftime("%Y-%m-%d"),
            "bmi": round(user["weight"] / (user["height"] ** 2), 2)
        }]
    })
    return existing_data


def write_to_file(data, output_file):
    """Write the updated data to the output JSON file."""
    try:
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        raise IOError(f"Error writing to {output_file}: {e}")


def process_input_data(json_input, existing_data):
    """Process the input data and update existing data."""
    try:
        users = json.loads(json_input)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding input JSON: {e}")

    for user in users:
        if not all(k in user for k in ('userId', 'firstname', 'lastname', 'weight', 'height')):
            raise ValueError("Missing required user fields in input data.")
        existing_data = update_bmi_for_user(user, existing_data)
    return existing_data


def read_input_file(input_file):
    """Read the input file and return its content."""
    try:
        with open(input_file, 'r') as file:
            return file.read()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error reading input file {input_file}: {e}")


def main():
    if len(sys.argv) < 2:
        raise ValueError("No input file provided")
        
    input_file = sys.argv[1]
    output_file = 'output_bmi_data.json'

    try:
        # Read the JSON content from the input file using the new function
        json_input = read_input_file(input_file)

        # Load the existing data from the output file
        existing_data = load_existing_data(output_file)

        # Process the new input data
        updated_data = process_input_data(json_input, existing_data)

        # Write the updated data to the output file
        write_to_file(updated_data, output_file)

        print(f"Results have been written to {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
