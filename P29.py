# Python program to print all the items in a dictionary.

# Create a sample dictionary
my_dict = {
    'name': 'Prashant',
    'age': 22,
    'email': 'prashant@gmail.com',
    'city': 'Goa'
}

# Iterate through the dictionary and print key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")
