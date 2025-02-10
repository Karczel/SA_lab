"""Data Processing Pipeline"""
import random


def gen_nums(min, max, amount):
    nums = []
    print("generateing numbers 1 to 100...")
    for i in range(amount):
        nums.append(random.randint(min, max))
    return nums


def even_filter(nums):
    print("filtering even numbers...")
    return [num for num in nums if num % 2 == 0]


def square(nums):
    squared_nums = []
    print("square the even numbers...")
    for i in nums:
        squared_nums.append(i ** 2)
    return squared_nums


# output the results
def output(squared_nums):
    print("output the results...")
    for i in squared_nums:
        print(i)


def main():
    nums = gen_nums(1, 100, 100)
    filtered = even_filter(nums)
    squared_nums = square(filtered)
    output(squared_nums)


if __name__ == "__main__":
    main()
