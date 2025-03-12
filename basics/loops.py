# Name = "Haris Ahmed"   

# for i in range(5000):
#   print(i)

# a = int(input('Enter a number :'))
# while (a > 8):
#     print(a) 
#     a = a - 1

# else:
#     print('Below to zero') 

# Do - while loop in python ()

# i = 1
# while True:
#     print(i)
#     i = i + 1
#     if (i%100 == 0):
#       

def Average(*numbers):
    sum = 0 
    for i in numbers: 
        sum = sum + 1
    print("Average is: ", sum / len(numbers))    
Average ( 9, 2, 45)