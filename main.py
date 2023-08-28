# write your code here

#part 1
favorite_animals = ['dog', 'cat', 'monkey', 'rabbit']
print(favorite_animals)
print(favorite_animals[1])
favorite_animals.remove('monkey')
print(favorite_animals)

#part 2
favorite_animals.append('parrot')
print(favorite_animals)
for animal in favorite_animals:
    print(f"I love {animal}")

#part3
numbers = [1, 2, 3, 4, 5]

numbers_sum = 0
for number in numbers:
    numbers_sum +=number
print(f"The total is {numbers_sum}")