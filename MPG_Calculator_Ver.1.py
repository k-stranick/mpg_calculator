#########################################################
#Author : Kyle Stranick                                 #
#Class : ITN160                                         #
#Class Section : 401                                    #
#Date : 9/27/2023                                       #
#Assignment:Assignment 5 - MGP calculation program      #
#Version : 1.03                                         #
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
################
# Version Notes:
################
#Version 1.01: Define weekly fuel cost and build main program
#Version 1.02: Setting input prompts for each car and weekly cost
#Version 1.03: Use of abs() in cost difference equation to make sure the value returned is always positive

def weekly_fuel_cost(weekly_highway_driving, weekly_city_driving, cost_per_gallon, highway_mpg, city_mpg):
    # calculating total weekly fuel cost
    highway_fuel = weekly_highway_driving / highway_mpg
    city_fuel = weekly_city_driving / city_mpg
    total_fuel = highway_fuel + city_fuel
    total_cost = total_fuel * cost_per_gallon
    return total_cost


def main():
    print('\nWelcome to The New Car Fuel Costs Program')
    # prompt user for information
    weekly_highway_driving = float(input(f'\nEnter estimated weekly highway driving: '))
    weekly_city_driving = float(input('Enter estimated weekly city driving: '))
    cost_per_gallon = float(input('Enter estimated cost per gallon: '))

    # Input car information for car 1
    car1_name = input('Enter make and model of first car: ')
    car1_highway_mpg = float(input(f'Enter highway mpg for {car1_name}: '))
    car1_city_mpg = float(input(f'Enter city mpg for {car1_name}: '))

    # Input car information for car 2
    car2_name = input('Enter make and model of second car: ')
    car2_highway_mpg = float(input(f'Enter highway mpg for {car2_name}: '))
    car2_city_mpg = float(input(f'Enter city mpg for {car2_name}: '))

    # Calculating weekly cost
    car1_weekly_cost = weekly_fuel_cost(weekly_highway_driving, weekly_city_driving, cost_per_gallon, car1_highway_mpg,
                                        car1_city_mpg)
    car2_weekly_cost = weekly_fuel_cost(weekly_highway_driving, weekly_city_driving, cost_per_gallon, car2_highway_mpg,
                                        car2_city_mpg)

    # Display results
    print(f'Weekly fuel cost for {car1_name}:\n${car1_weekly_cost:.2f}')
    print(f'Weekly fuel cost for {car2_name}:\n${car2_weekly_cost:.2f}')

    # Cost difference
    cost_difference = abs(car1_weekly_cost - car2_weekly_cost)
    print(f'The cost difference between {car1_name} and {car2_name} is: ${cost_difference:.2f}')


if __name__ == '__main__':
    main()
