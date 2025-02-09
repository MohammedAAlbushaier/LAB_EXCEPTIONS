'''Write a function celsius_to_fahrenheit(celsius) that takes a Celsius temperature as an argument and returns the equivalent temperature in Fahrenheit. Use the formula fahrenheit = (celsius * 9/5) + 32.

Write a function fahrenheit_to_celsius(fahrenheit) that takes a Fahrenheit temperature as an argument and returns the equivalent temperature in Celsius. Use the formula celsius = (fahrenheit - 32) * 5/9.

Write a main function that:

a. Prompts the user for input, asking them to enter a temperature and its unit (either "C" for Celsius or "F" for Fahrenheit), separated by a space (e.g., "25 C" or "77 F").
b. Splits the input string into a temperature value and its unit.
c. Tries to convert the input temperature to its opposite unit using the appropriate function
(e.g., if the user enters a Celsius temperature, convert it to Fahrenheit).
d. Riases & handles the following exceptions:
ValueError: If the user enters an invalid temperature value, display an error message and prompt the user to try again.
TypeError: raise this error If the user enters an invalid unit, display an error message and prompt the user to try again.
e. If the conversion is successful, print the converted temperature and its unit.
Call the main function to run the program. The user should be able to enter temperatures repeatedly until they enter a valid input.

Example Output:

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 100 F
Temperature in Celsius: 37.78 C

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 50 C
Temperature in Fahrenheit: 122.0 F

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 25 X
Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 100.5 F
Temperature in Celsius: 38.06 C
'''

def celsius_to_fahrenheit(celsius)->float:
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit)->float:
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def main():

    tempreture= input("Enter a temperature and its unit (e.g., \"25 C\" or \"77 F\"):")
    convertureSign= tempreture.split(" ")
    try:
        if convertureSign[1]=='C':
            fahrenheit=celsius_to_fahrenheit(float (convertureSign[0]))
            print(f"Temperature in Fahrenheit: {fahrenheit} F")
        elif convertureSign[1]=='F':
            celsius=fahrenheit_to_celsius(float(convertureSign[0]))
            print(f"Temperature in Celsius: {celsius} C")
        else:
            print ("Invaled Entry !!")
            main()
    except TypeError as e:
        print (e.__class__)
        print ("unsupported operand")
        main()

    except ValueError as e:
        print (e.__class__)
        print ("You have provided an invaled value !!")
        main()

    except Exception as e:
        print(e.__class__)
        print("Something went Wrong  !!")
        main()


while True:
    main()
    choice=input ("Would you like to exit the program? enter\"e\"")
    if choice =='e' or choice=='E':
        break
