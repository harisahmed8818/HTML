
"""  1. FIRST PROGRAM : " HELLO WORLD "!  """

# This is a comment. Anything following the '#' is ignored by Python
# Comments are used to explain your code

print("Hello World") #The print() funtion outputs text to the screen.


"""  2. VARIABLES AND DATA TYPES  """

#Here we create variables and assign values to them 


name = "Haris"   # 'name' is a variable storing a string.
age = 25         # 'age' is a variable storing a integer (a whole number).
weight = 55.2    # 'weight' is a variable storing a float (a decimal number).

# Display the values using the print() function.

print("My name is", name )
print("I am", age, "years old")
print("My weight is", weight, "kg")


"""  3. GETTING USER INPUT  """

#The input() function displays a prompt and waits for the user to type something

user_name = input("Enter your name :")
print("Hello, " + user_name + "!" )  #Concatenates strings to form a greeting.


"""  4. CONVERTING USER INPUT TO NUMBERS AND SIMPLE CALCULATIONS  """

#Ask the user for their age.
user_age = input("Enter your age: ") #Convert the input (which is text) to an integer using int()
user_age = int(user_age)

#Calculate the age next year.
next_year_age = user_age + (1)

#Display the result.
print("One year later , you will be", next_year_age, "years old.")

"""  5. CONDITIONAL STATEMENTS (IF-ELSE)  """

#Ask the user for their age.
age = int(input("Enter your age :"))
#Use an if-else statement to decide what to print.
if age >= 18:
    print("You are an adult")  #This block runs if the condition is True.
else:
    print("You are a minor")   #This block runs if the condition is False.


"""  6. LOOPS : REPEATING CODE  """

" A. FOR LOOP "
 
# The for loop repeats code for each value in a sequence.

for i in  range(1, 6):  #range(1, 6) generates numbers 1 through 5.
    print("Iteration number:", i)

" B. WHILE LOOP "
       
# The while loop repeats as long as a condition remains True.
count = 1  # Iniitialize a counter.
while count <= 5:
    print("Count:", count )
    count = count + 1  # Increment the counter by 1.


"""  7. FUNCTIONS: GROUPING CODE TOGETHER  """

#This function greets a person by name. 
def greet(name):  #The function prints a greeting message.
    print("Hello,", name + "!")  #Call the function with the argument ("Alice")
greet("Alice") 


