"""This program will detect any capital letter
 in a user's entry and display a message"""

word = input("Enter a word: ")
caps_count = 0

# For loop to count the caps
for letter in word:
    if letter == letter.upper():
        caps_count += 1
    if letter == " ":
        print("space found")

if caps_count > 0:
    print("At least 1 capital letter was found")
    # print("Actually, there are", caps_count, "capital letters")
else:
    print("No capital letter(s) was found")
