import random


def selection_sort(numbers):
    min = 0
    for i in range(len(numbers)-1):
        min = i
        for j in range(i + 1, len(numbers)):
            if numbers[min] > numbers[j]:
                min = j
        if min != i:
            numbers[min], numbers[i] = numbers[i], numbers[min]
        print(numbers)
    return numbers

if __name__=="__main__":
    numbers = random.sample(range(1, 10), 5)
    print(numbers)
    print(selection_sort(numbers))
