my_dictionary = {"John": "0415523658", "Sara": "0423597852", "Jonathan": "0426589965"}

# Get the keys of a dictionary using dictionary_name.keys()
print(my_dictionary.keys())

# Get the values of a dictionary using dictionary_name.values()
print(my_dictionary.values())

# Get the items (pairs) of a dictionary using dictionary_name.items()
print(my_dictionary.items())

# Get the value of a specific key in the dictionary
the_one = my_dictionary["John"]
print(the_one)

# Add a new item (pair) to the dictionary
my_dictionary["Joe"] = "0465359965"
print(my_dictionary)

for one_key, one_value in my_dictionary.items():
    print(one_key, one_value)

# Challenge: Get John's phone number
print("John's phone number is:", my_dictionary["John"])
