global FAHRENHEIT_TO_CELSIUS_FACTOR
global CELSIUS_TO_FAHRENHEIT_FACTOR

def convert_to_celsius(fahrenheit):
    FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
    #FAHRENHEIT_TO_CELSIUS_FACTOR = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)

def convert_to_fahrenheit(celsius):
    CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
    #CELSIUS_TO_FAHRENHEIT_FACTOR = CELSIUS_TO_FAHRENHEIT_FACTOR * (celsius + 32)
    return CELSIUS_TO_FAHRENHEIT_FACTOR * (celsius + 32)

temp = float(input("Enter the temperature to convert: "))
temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if temp_type == "F":
    print(f"{temp}{chr(176)}F is {convert_to_celsius(temp)}{chr(176)}C")
elif temp_type == "C":
    print(f"{temp}{chr(176)}C is {convert_to_fahrenheit(temp)}{chr(176)}F")
else:
    print("Invalid input. Please enter C or F.")
