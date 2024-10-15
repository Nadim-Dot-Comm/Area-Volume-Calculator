#TPRG-2131-01
#Assignment 1
#Oct 16, 2024
#Nadim Gutto - 100665657
#This is solely my own work with the help of online resources and this/last years class content.
#All the formulas were taken from google.
'''
*********
A/V calculator

This program calculates the area and volume of various geometric shapes.
It allows the users to choose from a menu of options,
input the necessary dimensions, and then outputs the results.

'''

import math #Imports the math, to use math funtions.

'''Calculates the area of a circle, has two options with formula and without fourmula'''
def area_circle(radius, formula=False): #Defines the area_circle as a function, input parameter(radius), making formula=False a default argument meaning it will not show until chosen.
    calculation = f"π * {radius}cm²" #Creates a string using the formula for area of circle with the given radius and stores it into the variable calculation.
    result = round(math.pi * radius ** 2, 1) #Stores the calculation for area of circle into the variable result, round to 1 decimal place.
    if formula: #Checks if the argument formula=False is True, then it prints the result with formula.
        equation = "πr²" #Formula for area of a circle.
        print(f"Area of Circle: (A = {equation}) {calculation} = {result:.1f} cm²") #Prints as shown, rounds to one decimal place.
    else: #Checks if the argument formula=False is False, then print result without formula.
        print(f"Area of Circle: {calculation} = {result:.1f} cm²") #Prints as shown, rounds to one decimal place.
    return result #Returns the calculated result.

'''Calculates the area of a square, has two options with formula and without fourmula'''
def area_square(side_length, formula=False):#Defines the area_square as a function, parameter(side_length) which is sides of a square, making formula=False a default argument meaning it will not show until chosen.
    calculation = f"{side_length}cm²" #Creates a string using the formula for area of square with the given side lengths and stores it into the variable calculation.
    result = round(side_length ** 2, 1) #Stores the calculation for area of square into the variable result, round to 1 decimal place.
    if formula: #Checks if the argument formula=False is True, then it prints the result with formula.
        equation = "s²" #Formula for area of a square.
        print(f"Area of Square: (A = {equation}) {calculation} = {result:.1f} cm²")#Prints as shown, rounds to one decimal place.
    else: #Checks if the argument formula=False is False, then print result without formula.
        print(f"Area of Square: {calculation} = {result:.1f} cm²")#Prints as shown, rounds to one decimal place.
    return result #Returns the calculated result.

'''Calculates the area of a triangle, has two options with formula and without fourmula'''
def area_triangle(base, height, formula=False):#Defines area_triangle as a function, parameter(base,height), making formula=False a default argument meaning it will not show until chosen.
    calculation = f"0.5 * {base}cm * {height}cm" #Creates a string using the formula for area of triangle with the given base and height and stores it into the variable calculation.
    result = round(0.5 * base * height, 1) #Stores the calculation for area of triangle into the variable result, round to 1 decimal place.
    if formula: #Checks if the argument formula=False is True, then it prints the result with formula.
        equation = "½bh" #Formula for area of triangle.
        print(f"Area of Triangle: (A = {equation}) {calculation} = {result:.1f} cm²")#Prints as shown, rounds to one decimal place.
    else: #Checks if the argument formula=False is False, then print result without formula.
        print(f"Area of Triangle: {calculation} = {result:.1f} cm²")#Prints as shown, rounds to one decimal place.
    return result #Returns the calculated result.

'''Calculates the volume of a rectagular prism, has two options with formula and without fourmula'''
def vol_rect_prism(length, width, height, formula=False):#Defines vol_rect_prism as a function, input parameter(lwh), making formula=False a default argument meaning it will not show until chosen.
    calculation = f"{length}cm * {width}cm * {height}cm" #Creates a string using the formula for rectagular prism with the given dimensions and stores it into the variable calculation.
    result = round(length * width * height, 1) #Stores the calculation for volume of rectagular prism into the variable result, round to 1 decimal place.
    if formula: #Checks if the argument formula=False is True, then it prints the result with formula.
        equation = "l × w × h" #Formula for volume of rectagular prism.
        print(f"Volume of Rectangular Prism: (V = {equation}) {calculation} = {result:.1f} cm³")#Prints as shown, rounds to one decimal place.
    else: #Checks if the argument formula=False is False, then print result without formula.
        print(f"Volume of Rectangular Prism: {calculation} = {result:.1f} cm³")#Prints as shown, rounds to one decimal place.
    return result #Returns the calculated result.

'''Calculates the volume of a cube, has two options with formula and without fourmula'''
def vol_cube(sides, formula=False):#Defines vol_cube as a function, input parameter(sides), making formula=False a default argument meaning it will not show until chosen.
    calculation = f"{sides}cm³" #Creates a string using the formula for volume of a cube with the given sides and stores it into the variable calculation.
    result = round(sides ** 3, 1) #Stores the calculation for volume of cube into the variable result, round to 1 decimal place.
    if formula: #Checks if the argument formula=False is True, then it prints the result with formula.
        equation = "s³" #Formula for volume of cube.
        print(f"Volume of Cube: (V = {equation}) {calculation} = {result:.1f} cm³")#Prints as shown, rounds to one decimal place.
    else: #Checks if the argument formula=False is False, then print result without formula.
        print(f"Volume of Cube: {calculation} = {result:.1f} cm³")#Prints as shown, rounds to one decimal place.
    return result #Returns the calculated result.

'''Function to handle calculations'''
def perform_calculation(formula): #Defines preform_calculation as a function, formula as the parameter and states whether it's True or False controling if it shows the formula or not.  
    while True: #Loops until user exits.  
        
        '''Calculation options + going back to main menu'''
        print("\nCalculation Menu:")
        print("1. Area of Circle")
        print("2. Area of Square")
        print("3. Area of Triangle")
        print("4. Volume of Rectangular Prism")
        print("5. Volume of Cube")
        print("B. Go back to Main Menu")
        
        choice = input("Select a calculation (1-5) or 'B' to go back: ").lower() #Prompts the user to select one of the six options, converts any uppercase letters into lowercase. 
        
        '''Breaks the loop and goes back to main menu'''
        if choice == 'b':
            print("Returning to Main Menu...")
            break

        if choice == '1': #Area of Circle.
            radius = float(input("Enter the radius (cm): ")) #Converts input into a float.
            area_circle(radius, formula) #Calls the function.
        
        elif choice == '2': #Area of Square.
            side = float(input("Enter the side length (cm): ")) #Converts input into a float.
            area_square(side, formula) #Calls the function.
        
        elif choice == '3': #Area of Triangle.
            base = float(input("Enter the base (cm): ")) #Converts input into a float.
            height = float(input("Enter the height (cm): ")) #Converts input into a float.
            area_triangle(base, height, formula) #Calls the function.
        
        elif choice == '4': #Volume of Rectagular Prism.
            length = float(input("Enter the length (cm): ")) #Converts input into a float.
            width = float(input("Enter the width (cm): ")) #Converts input into a float.
            height = float(input("Enter the height (cm): ")) #Converts input into a float.
            vol_rect_prism(length, width, height, formula) #Calls the function.
        
        elif choice == '5': #Volume of Cube.
            sides = float(input("Enter the side length (cm): ")) #Converts input into a float.
            vol_cube(sides, formula) #Calls the function.
        
        else:
            print("Invalid option. Please try again.") #Prompts the user to input the correct choices listed.

#Main function
def main():
    print("Welcome to the Geometric Calculator...") #Introduction
    while True: #Loops until user exits.
        
        '''Main Menu option'''
        print("\nMain Menu:")
        print("Enter Q/q to quit.")
        print("Enter V/v (with equations).")
        print("Enter D/d (with calculations).")
        
        user_input = input("Please select an option: ").lower() #Prompts the user to select one of the three options, converts any uppercase letters into lowercase.
        
        '''Exits the loop ending the program gracefully'''
        if user_input == 'q':
            print("Exiting the program... Goodbye!✋")
            break
        
        '''Indicates the user wants the formula along with the calculation and result'''
        elif user_input == 'v':
            print("V was chosen.")
            perform_calculation(formula=True) #Calls the function and passes it as True.
        
        '''Indicates the user does not want the formula along with the calculation and result'''
        elif user_input == 'd':
            print("D was chosen.")
            perform_calculation(formula=False)#Calls the function and passes it as False.
        
        else:
            print("Invalid input. Please try again.") #Prompts the user to input the correct choices listed.

if __name__ == "__main__": #Checks if the script runs directly.
    main() #Calls the main funtion if the script runs directly.



