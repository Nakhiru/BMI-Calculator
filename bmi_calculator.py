from datetime import datetime
import json
import sys


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

def main():
    print("Hello, BMI Calculator user !")
    output_file = 'output_bmi_data.json'

    try:
        # Load the existing data from the output file
        existing_data = load_existing_data(output_file)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()