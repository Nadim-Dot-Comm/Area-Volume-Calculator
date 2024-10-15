#TPRG-2131-01
#Assignment 1
#pytest file template.
#Due: Oct 16, 2024
#Nadim Gutto - 100665657

#This was solely my work with the help of previous lab contents.
'''
This file is to be the test_A_V_calc.py file used with your A_V_calc.py and pytest.
This must test each of your Area/Volume functions, with a least 3 examples for each of the
5 functions your chose to use.
'''

from A_V_calc import area_circle, area_square, area_triangle, vol_rect_prism, vol_cube #Imports these functions from the file A_V_Calc. 

'''Tests the function area_circle which claculates the area of a circle based on the radius given'''
def test_area_circle():
    assert area_circle(2) == 12.6 #Test by calling the function area_circle with a radius of 2 returning the value 12.6
    assert area_circle(5) == 78.5
    assert area_circle(10) == 314.2

'''Tests the function area_square which claculates the area of a square based on the side length given'''    
def test_area_square():
    assert area_square(11) == 121 #Test by calling the function area_square with a side length of 11 returning the value 121
    assert area_square(50) == 2500
    assert area_square(100) == 10000
    
'''Tests the function area_triangle which claculates the area of a triangle based on the base and height given'''    
def test_area_triangle():
    assert area_triangle(13, 16) == 104 #Test by calling the function area_triangle with a base of 13 and height of 16 returning the value 104
    assert area_triangle(20, 25) == 250
    assert area_triangle(3.5, 5.5) == 9.6
    
'''Tests the function vol_rect_prism which claculates the volume of a rectangular prism based on (length,width,height) given'''    
def test_vol_rect_prism():
    assert vol_rect_prism(14, 14, 14) == 2744 #Test by calling the function vol_rect_prism with (lwh) of 14 returning the value 2744
    assert vol_rect_prism(19, 10, 21) == 3990
    assert vol_rect_prism(15.5, 6.7, 11.4) == 1183.9
    
'''Tests the function vol_cube which claculates the volume of a cube based on the sides given'''    
def test_vol_cube():
    assert vol_cube(12) == 1728 #Test by calling the function vol_cube with sides of 12 returning the value 1728
    assert vol_cube(4) == 64
    assert vol_cube(0) == 0
    