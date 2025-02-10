"""Data Processing Pipeline"""
import random


nums = []

print("generateing numbers 1 to 100...")
# generates numbers 1 to 100
for i in range(100):
    nums.append(random.randint(1, 100))

print("filtering even numbers...")
# filters even numbers
for i in nums:
    if i//2 != 0:
        nums.remove(i)

squared_nums = []
# square the even numbers
print("square the even numbers...")
for i in nums:
    squared_nums.append(i**2)

# output the results
print("output the results...")
for i in squared_nums:
    print(i)
    