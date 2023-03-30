# Creating and opening a file for the purpose of re-writing
file_out = open("file.txt", "w")
file_out.write("This is the first line.\n")
file_out.write("This is the second line.\n")
file_out.close()

# Create and open a file for the purpose of appending (adding to existing content)
file_out_a = open("file_append.txt", "a")
file_out_a.write("This is a newly added (appended) line.\n")
file_out_a.close()

# Open an existing file for the purpose of reading
file_in = open("file.txt", "r")
print(file_in.read())
file_in.close()

phonebook_file_in = open("phonebook.txt", "r")
phonebook_dictionary = {}

for line in phonebook_file_in:
    name, phone = line.split(" ")

    # add and associate a name with a phone number in the dictionary
    # use .rstrip() to clean up the new line after each phone number
    phonebook_dictionary[name] = phone.rstrip()

phonebook_file_in.close()
print(phonebook_dictionary)

# Get the phone number by providing a name
print("Max's phone number is:", phonebook_dictionary["Max"])

# print("Name       Phone\n---------------------")
print(f"{'Name':10s} Phone\n{'':-<21s}")  # Same as the line above
for name, phone in phonebook_dictionary.items():
    # print("Name:", name, "Phone:", phone)
    # print(f"Name: {name:10s} Phone: {phone}")
    print(f"{name:10s} {phone}")

