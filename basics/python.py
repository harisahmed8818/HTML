# a = 'haris Ahmed!'

# print(a)

# print(len(a)) #find lenght of characters in a word include spaces.

# print(a.upper()) # coverts into upper case.

# print(a.lower()) # converts into lower case.

# print(a.rstrip('!')) # rstrip removes trailing characters.

# print(a.replace('Haris','Saba')) # replace the word with the given word.

# print(a.split(" ")) # it split the given string at the whitespace"  ".

# print(a.capitalize()) # turns the 1st letter capital, And rest upper case into lower case in string.

# print(a.center(120,".")) # align the string spaces given + fill the spaces with given character.

# print(a.count("h")) # count the numbers of specific word repeating in a string.

# print(a.endswith("!", 0 ,12)) # checks if the given string ends with given value. True/False.

# print(a.find('i')) # give the 1st occurrence of a given word in number. if not return-1.

# print(a.index('i')) # similar to find(), but raise error if the word isn't found!.

# print(a.isalnum()) # alphanumeric return true if entire string contains of A-Z, a-z, 0-9. 
#                    # if any other characters or punctuations are present it return false.

# print(a.isalpha()) # alphabets return true if only A-Z, a-z are present otherwise false.     

# print(a.islower()) # return true if all characters in the string are in lower case, else false.
 
# print(a.isupper()) # return true if all characters in the string are in upper case, else false.     

# print(a.isprintable()) # return true if all characters in the string are printable, else false.                      

# print(a.isspace()) # return true only and only if the string is a whitespace string, else false.

# print(a.istitle()) # return true if the 1st letter of each word is capital, else false.

# print(a.startswith('h')) 

# print(a.swapcase())

# print(a.title())

a = int(input("Enter Your Age :"))
print (f'You are {a} years old.So,' )

if (a>=18): 
    print ('You can drive')
else:
    print("You cannot drive, License banwa Bharway kahin ky")    
