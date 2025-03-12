# Lists to store values
in_values = []
out_values = []

print("Enter numbers (Enter 0 to stop):")
while True:
    try:
        num = float(input("Enter a number: ")) 
        
        if num == 0:
            break
        elif num < 0:
            in_values.append(num)
        else:
            out_values.append(num)

    except ValueError:
        print("Invalid input! Please enter a numeric value.")

max_length = max(len(in_values), len(out_values))

in_values += [''] * (max_length - len(in_values))
out_values += [''] * (max_length - len(out_values))
#sunny bh
print("\n+-----------+-----------+")
print("| In | Out |")
print("+-----------+-----------+")
for i in range(max_length):
    print(f"| {str(in_values[i]).ljust(9)} | {str(out_values[i]).ljust(9)} |")
print("+-----------+-----------+")
