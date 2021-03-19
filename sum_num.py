import random

last_numbers = 4
first_numbers = 4
iterations = 5
start = 1
finish = 100
number_list = []

for i in range(iterations):
    number_list.append(random.randint(start, finish))

number_list = sorted(number_list)
print(number_list)
max_sum = sum(number_list[-last_numbers:])  # sum the last n numbers of the sorted list
min_sum = sum(number_list[:first_numbers])  # sum the first n numbers of the sorted list

print(max_sum)
print(min_sum)
