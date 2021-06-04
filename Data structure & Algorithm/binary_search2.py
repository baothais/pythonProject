import random


def binary_search(numbers, target, left, right):
    while (left <= right):
        mid = (left + right) // 2
        if target == numbers[mid]:
            return True
        elif target > numbers[mid]:
            return binary_search(numbers, target, mid + 1, right)
        else:
            return binary_search(numbers, target, left, mid - 1)
    return False


if __name__=="__main__":
    numbers = random.sample(range(1, 10), 5)
    target = int(input("Enter target: "))
    numbers.sort()
    print("numbers = {}".format(numbers))
    left = 0
    right = len(numbers) - 1
    if binary_search(numbers, target, left, right):
        print("target in numbers")
    else:
        print("target not in numbers")
