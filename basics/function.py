# def double_a_b(s):
#     result = s.replace('a','a,a').replace('b','b,b')
#     print(result)
# double_a_b("ab")

# name = "Haris Ahmed"  


# for char in name:
#  print(char, end="")

# def Average(*numbers):
#     sum = 0 
#     for i in numbers: 
#         sum = sum + 1
#     print("Average is: ", sum / len(numbers))    

def Average(*numbers):
    if len(numbers) == 0:
        print('no numbers provided')
        return
    sum = 0
    for i in numbers:
        sum = sum + i
    print('Average is:', sum)       

Average(6,9,50)


