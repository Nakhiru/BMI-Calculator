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

def main():
    print("Hello, BMI Calculator user !")

if __name__ == "__main__":
    main()