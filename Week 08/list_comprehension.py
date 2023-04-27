cars = ["Mercedes", "Volvo", "Ferrari", "Mazda"]
cars.append("Toyota")
print("Cars:", cars)

# favourite_cars = []
# for car in cars:
#     # if "r" in car:
#     favourite_cars.append(car)
# print("Favourite cars:", favourite_cars)

# List Comprehension
# list = [APPENDING ZONE    LOOPING ZONE]
best_cars1 = ["Car:" + car for car in cars]
print("Best cars 1:", best_cars1)

# list = [APPENDING ZONE    LOOPING ZONE    IF CONDITION]
best_cars2 = [car for car in cars if "r" in car]
print("Best cars 2:", best_cars2)

# list = [APPENDING ZONE    IF CONDITION WITH ELSE  LOOPING ZONE]
best_cars3 = ["good" if "r" in car else "bad" for car in cars]
print("Best cars 3:", best_cars3)

# TODO: Create a list of results Pass/Fail based on grades in a list
# Condition to pass is the grade to be 50 or above
# The output should look ["Fail", "Fail", "Pass", "Fail", "Fail", "Pass"]

grades = [22, 44, 66, 34, 12, 99]
# list = [APPENDING ZONE    IF CONDITION WITH ELSE  LOOPING ZONE]
results = ["Pass" if grade >= 50 else "Fail" for grade in grades]
print("Results:", results)

count = 0
for time in grades:
    count += 1
    print(grades[count], results[count])
