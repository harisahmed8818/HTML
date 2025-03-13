# Taking user input
number = input("Enter an integer (up to millions): ")
digit = input("Enter the digit to find its place value: ")

# Place value names
places = ["Units", "Tens", "Hundreds", "Thousands", "Ten Thousands", "Hundred Thousands", "Millions"]

# Check if digit is in the number
if digit in number:
    index = len(number) - number.index(digit) - 1
    print(f"The digit {digit} is in the '{places[index]}' place.")
else:
    print(f"The digit {digit} is not present in the number.")
