# FILE NAME - triangle_area.py

# NAME: Marcelo Luciano
# DATE: February 17, 2025
# BRIEF DESCRIPTION: A function that will calculate the area of a triangle given the height and base lengths.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience





########## ENTER YER CODE BELOW THIS LINE ##########
def find_area():
    height = float(input("Enter the height: "))
    base = float(input("Enter the base: "))
    area = height * base / 2
    print("The area of the triangle is " + str(area))
find_area()
########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''

Enter the height: 1
Enter the base: 1

The area of the triangle is 0.5

'''



'''

Enter the height: 8
Enter the base: 4

The area of the triangle is 16.0

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is the flow of the program? Which line of code kicks off the process?

The code that calls the find_area() function is the one that kicks it off

2. What was the hardest part of this lab?

Getting the correct typecasts.
'''
