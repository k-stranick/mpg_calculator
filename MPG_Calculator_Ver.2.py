#########################################################
#Author : Kyle Stranick                                 #
#Class : ITN160                                         #
#Class Section : 401                                    #
#Date : 9/27/2023                                       #
#Assignment:Assignment 5 - MPG calculation program      #
#Version : 2.033                                        #
#########################################################

###################
#Syntax References:
###################
#Cannon, Jason. (2016). Python Succinctly., Syncfusion Inc.
#Gupta, Anubhav. Slither into Python. (2021?)
#Murach, Mike. (2021). Murach's Python Programming (2nd Ed.), Mike Murach & Associates, Inc.
#https://docs.python.org/3/library/exceptions.html#bltin-exceptions
#https://www.tutorialspoint.com/python/python_if_else.htm
#https://www.tutorialspoint.com/python/python_functions.htm
#https://www.w3schools.com/python/
#https://www.pluralsight.com  I have a subscription
#https://stackoverflow.com/questions/29460405/checking-if-string-is-only-letters-and-spaces-python
################
# Version Notes:
################
#Version 1.01: Define weekly fuel cost and build main program
#Version 1.02: Setting input prompts for each car and weekly cost
#Version 1.03: Use of abs() in cost difference equation to make sure the value returned is always positive
#Version 2.00: Added new Def functions to improve readability
#Version 2.01: Created a get_float_input function that returns entered values and checks for negative inputs
#Version 2.011:Replaced each instance of float(input()) with get_float function
#Version 2.02: Created get_car_info function to store input information on each car
#Version 2.021:Replaced input car info blocks(1&2) with get_car function, made sure variables were able to be identified
#Version 2.022:Needed to set car info variables equal to get_car function to be utilized
#Version 2.023:Tested call of get_car function added .strip() to account for all letters and spaces
#Version 2.030:Defined an exit loop to mitigate multiple while loops in program
#Version 2.031:Set if value < 0 to if <= 0 to handle any division by 0 errors in get_float_input function
#Version 2.032:Checking if string has only spaces and alphabet characters
#Version 2.033: replaced repeating while loops in get_car funtion with one loop and if statements to make more readable
def weekly_fuel_cost(weekly_highway_driving, weekly_city_driving, cost_per_gallon, highway_mpg, city_mpg):
    # calculating total weekly fuel cost
    highway_fuel = weekly_highway_driving / highway_mpg
    city_fuel = weekly_city_driving / city_mpg
    total_fuel = highway_fuel + city_fuel
    total_cost = total_fuel * cost_per_gallon
    return total_cost


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:  # Checks if value is negative
                print('\nInvalid entry. The value must be positive.\n')
            else:
                return value
        except ValueError:
            print('\nPlease Enter Valid Number.\n')


def get_car_info(car_num):
    while True:
        car_name = input(f'\nEnter make and model of car {car_num}: ').strip()
        valid_name = all(char.isalpha() or char.isspace() for char in car_name)
        if not car_name or not valid_name:
            print('\nInvalid entry. Must enter letters and spaces. Please Try Again.\n')
            continue  # Skip to the next iteration to re-enter car name.
        car_highway_mpg = get_float_input(f'Enter Highway MPG for {car_name} (MPG): ')
        if car_highway_mpg <= 0:
            print('MPG must be greater than 0')
            continue  # Skip to the next iteration to re-enter highway mpg.
        car_city_mpg = get_float_input(f'Enter City MPG for {car_name} (MPG): ')
        if car_city_mpg <= 0:
            print('MPG must be greater than 0')
            continue  # Skip to the next iteration to re-enter city mpg.
        return car_name, car_highway_mpg, car_city_mpg


def get_exit(prompt):
    while True:
        response = input(prompt).upper()
        if response in ['Y', 'N']:
            return response
        else:
            print("\nInvalid input. Please enter 'Y' or 'N'\n")


def main():
    print('\nWelcome to The New Car Fuel Costs Program\n')
    while True:

        #prompt user for information
        weekly_highway_driving = get_float_input('Enter estimated weekly highway driving (Miles): ')
        weekly_city_driving = get_float_input('Enter estimated weekly city driving (Miles): ')
        cost_per_gallon = get_float_input('Enter estimated cost per gallon ($): ')

        # Calculating weekly cost car 1
        car1_name, car1_highway_mpg, car1_city_mpg = get_car_info(1)
        car1_weekly_cost = weekly_fuel_cost(weekly_highway_driving, weekly_city_driving, cost_per_gallon,
                                            car1_highway_mpg, car1_city_mpg)
        print(f'Weekly fuel cost for {car1_name}:\n${car1_weekly_cost:.2f}')

        #Calculating weekly cost car 2
        car2_name, car2_highway_mpg, car2_city_mpg = get_car_info(2)
        car2_weekly_cost = weekly_fuel_cost(weekly_highway_driving, weekly_city_driving, cost_per_gallon,
                                            car2_highway_mpg, car2_city_mpg)
        print(f'Weekly fuel cost for {car2_name}:\n${car2_weekly_cost:.2f}')

        #Cost difference
        cost_difference = abs(car1_weekly_cost - car2_weekly_cost)
        print(f'\nThe cost difference between {car1_name} and {car2_name} is: ${cost_difference:.2f}')

        quit_program = get_exit('\nWould you like to exit (Y/N): ')
        if quit_program == 'Y':
            print('Goodbye!')
            return


if __name__ == '__main__':
    main()
