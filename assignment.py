""" PYTHON CODE """

# Step 1 : initialize code 
total = 0
count = 0

while True:
    number = float(input("Enter a number (-1 to stop): " ))
    if number == -1:
        break 
    total += number 
    count += 1

if count > 0:
    average = total/count 
    print("Average is",average)
else:
    print("No numbers were entered. ")   
