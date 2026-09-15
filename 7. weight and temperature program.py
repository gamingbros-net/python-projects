while True:
    conversion_type = input("What do you want to convert? (weight/temperature): ").lower()

    if conversion_type == "weight":
        conversion_unit = input("Convert from (lbs/kg): ").lower()
        
        if conversion_unit not in ["lbs", "kg"]:
            print("Please enter lbs or kg")
            continue
        
        while True:
            value_input = input("Enter weight: ")
            try:
                value = float(value_input)
            except ValueError:
                print("Please enter a valid number!")
                continue
            
            if value < 0 or value > 1000:  # Weight validation
                print("Please enter a valid weight (0-1000)!")
                continue
            
            if conversion_unit == "lbs":
                result = value / 2.205
                print(f"{value} lbs = {result:.2f} kg")
            else:
                result = value * 2.205
                print(f"{value} kg = {result:.2f} lbs")
            break
        break

    elif conversion_type == "temperature":
        conversion_unit = input("Convert from (c/f): ").lower()
        
        if conversion_unit not in ["c", "f"]:
            print("Please enter c or f")
            continue
        
        while True:
            value_input = input("Enter temperature: ")
            try:
                value = float(value_input)
            except ValueError:
                print("Please enter a valid number!")
                continue
            
            if value < -273.15:  # Absolute zero validation
                print("Temperature cannot be below -273.15°C!")
                continue
            
            if conversion_unit == "c":
                result = ((value * 9) / 5) + 32
                print(f"{value}°C = {result:.2f}°F")
            else:
                result = ((value - 32) * 5) / 9
                print(f"{value}°F = {result:.2f}°C")
            break
        break

    else:
        print("Please enter weight or temperature")
