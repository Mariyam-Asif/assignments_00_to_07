# Project 2: E = m * C^2

def main():
    # Speed of light
    C = 299792458 # m/s

    # Take user input for the mass in kg
    mass_in_kg = float(input("Enter kilos of mass: ")) # Converts input to float

    # Einstein's Equation E = m * c ^ 2
    energy_in_joules = mass_in_kg * (C ** 2)

    # Display the formula and result
    print("e = m * C^2...")
    print(f"m = {mass_in_kg} kg")
    print(f"C = {C} m/s")
    print(f"{energy_in_joules} joules of energy!")

if __name__ == '__main__':
    main()