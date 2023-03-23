numbers = [10, 20, 30, 40, 50]
# print(numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4])

print("The sum of the numbers is", sum(numbers))
print("The average is", sum(numbers) / len(numbers))

numbers.append(22)  # append() adds to the list
numbers.append(22)
numbers.append(22)
numbers.remove(10)  # remove() removes an item from the list
numbers.count(22)   # count() counts an item from the list

print(numbers)
print("There are", numbers.count(22), "22s in the list")
