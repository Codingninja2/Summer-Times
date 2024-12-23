def clothing_suggestion():
    try:
        # Ask user for the temperature
        temperature = float(input("Enter the current temperature (in °C): "))
        
        # Suggest clothing based on the temperature
        if temperature >= 25:
            print("It's warm enough to wear light clothes. Enjoy!")
        elif 15 <= temperature < 25:
            print("It's a bit cool. You might need a light jacket or sweater.")
        else:
            print("It's quite cold. Better stick to jackets and pullovers.")
    except ValueError:
        print("Please enter a valid numerical temperature.")

# Run the clothing suggestion program
clothing_suggestion()
