def is_valid_unit(unit):
    valid_units = ['km', 'm', 'cm', 'mm', 'mi', 'yd', 'ft', 'in']
    return unit.lower() in valid_units

def convert_units(value, from_unit, to_unit):
    # Conversion factors to meters
    to_meter = {
        'km': 1000,
        'm': 1,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.34,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254
    }
    
    # Convert to meters first
    meters = value * to_meter[from_unit.lower()]
    
    # Then convert from meters to the target unit
    return meters / to_meter[to_unit.lower()]

def unit_converter():
    print("Unit Converter")
    print("Supported units: km, m, cm, mm, mi, yd, ft, in")
    
    while True:
        # Enter value and units
        try:
            value = float(input("Enter the value: "))
            from_unit = input("Enter the source unit: ")
            to_unit = input("Enter the target unit: ")
            
            # Are units valid?
            if is_valid_unit(from_unit) and is_valid_unit(to_unit):
                # Convert units
                result = convert_units(value, from_unit, to_unit)
                # Display converted value
                print(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
            else:
                # Display error message
                print("Error: Invalid units. Please use supported units.")
            
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")
        
        # Ask if the user wants to continue
        continue_convert = input("Do you want to convert another value? (y/n): ")
        if continue_convert.lower() != 'y':
            break
    
    print("Thank you for using the Unit Converter!")

if __name__ == "__main__":
    unit_converter()
