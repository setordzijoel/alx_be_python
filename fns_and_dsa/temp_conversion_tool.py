FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

fahrenheit_to_celsius = None
celsius_to_fahrenheit = None

def convert_to_celsius(fahrenheit):
    global fahrenheit_to_celsius
    fahrenheit_to_celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    return fahrenheit_to_celsius

def convert_to_fahrenheit(celsius):
    global celsius_to_fahrenheit
    celsius_to_fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32
    return celsius_to_fahrenheit

temp = float(input("Enter the temperature to convert: "))
temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if temp_type == "F":
    print(f"{temp}{chr(176)}F is {convert_to_celsius(temp)}{chr(176)}C")
elif temp_type == "C":
    print(f"{temp}{chr(176)}C is {convert_to_fahrenheit(temp)}{chr(176)}F")
else:
    print("Invalid input. Please enter C or F.")
