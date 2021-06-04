import random


def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >=0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers

if __name__=="__main__":
    numbers = random.sample(range(1, 20), 5)
    print("array  = {}".format(numbers))
    print("result = {}".format(insertion_sort(numbers)))
