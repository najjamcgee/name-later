"""
Name: Najja McGee
Date: June 28th, 2023
Course: CIS 111
Section: 05
Program Name: Print a list in reverse

Algirithm:
1. prompt the user to enter something
2. make this input a string
3. repeat steps 1-2 until user inputs a datatype to quit
4. create a list from the inputed strings
5. display the list in reverse
"""
#try to get a subset of what the user is inputting
my_list= []

while True:
  user_input = str(input("Enter what you have to do today or N/A to quit: "))
  if user_input == "N/A":
    break
  else: 
    my_list.append(user_input)
  
print("Here is your list: ", my_list)
print("Here is the list in reverse order: ", my_list[::-1])
    
  
