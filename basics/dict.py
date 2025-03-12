#Dictionary

people = {
    "Zain": {"Age": 50, "Gender": "Male"},
    "Haris": {"Age": 45, "Gender": "Male"},
    "Sami": {"Age": 22, "Gender": "Male"},
    "Laiba": {"Age": 18, "Gender": "Female"},
    "Zainab": {"Age": 28, "Gender": "Female"}
}

print("First name in the list:", list(people.keys())[0])  # Show first name

user_input = input("Enter a name, age, letter, or gender (Male/Female): ").strip().title()

if user_input in people:
    print(people[user_input])  # Show details if name is entered
elif user_input.isdigit():
    print([name for name in people if people[name]["Age"] == int(user_input)])  # Show names for given age
elif len(user_input) == 1:
    print(sum(1 for name in people if name.startswith(user_input)))  # Count names starting with the letter
elif user_input in ["Male", "Female"]:
    print([name for name in people if people[name]["Gender"] == user_input])  # Show names of the entered gender
else:
    print("Invalid input")
