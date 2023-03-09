"""Force someone to say YES"""
answer = input("Yes or no: ").lower()

while answer != "yes":
    answer = input("Yes or no: ").lower()

print("Thank you!!!")
