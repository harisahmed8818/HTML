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
    print(f"\nDetails of {user_input}:")
    print(f"Age: {people[user_input]['Age']}")
    print(f"Gender: {people[user_input]['Gender']}")
elif user_input.isdigit():
    names = [name for name in people if people[name]["Age"] == int(user_input)]
    print("\nNames with this age:")
    for name in names:
        print(name)  # Show each name on a new line
elif len(user_input) == 1:
    count = sum(1 for name in people if name.startswith(user_input))
    print(f"\nNumber of names starting with '{user_input}': {count}")
elif user_input in ["Male", "Female"]:
    filtered_people = {name: info for name, info in people.items() if info["Gender"] == user_input}
    
    print(f"\n{user_input}s:\n{'-' * 20}")
    print(f"{'Name':<10} {'Age':<5}")  # Table headers
    print("-" * 20)
    
    for name, info in filtered_people.items():
        print(f"{name:<10} {info['Age']:<5}")  # Tabular format
else:
    print("Invalid input")
