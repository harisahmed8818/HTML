# This is a comment. Anything following the '#' is ignored by Python
# Comments are used to explain your code to others or for own yourself.

# #Simple output
print("hello world") #The print() funtion outputs text to the screen


#Concatening values
print('hello''world') #without space 
print('hello','world') #with space 

#Inserting spaces (Seperator,sep)
print('hello'   ,  'world', sep='v') #remove spaces,or add custom seperators (anything inside'')

#Ending with a newline (Default)
print('hello')
print('world')

#Ending without a newline (End Character,end)
print('hello', end='') #it prints output in single line and 
print('world')         #add (anything inside'' at the end of line)

#You can force the output to be flushed (print output immediately)
print('hello world!', flush=True)

#Format Specifier (f) use tot the output format
name = "Haris Ahmed" #string 
age = 19 #float (that's why we dont use "")

print(f"My name is {name}. I'm {age} years old.") # with f
print("My name is", name, ".I'm", age, "years old") # without f (Hard to write)

#File output
with open('output.txt','w')as file:
    print('hello world', file)

#Multi-line 
print("""
       * 
      ***
     *****
    *******
   *********
""")    




