import random


def selection_sort(numbers):
    for i in range(len(numbers)):
        min = i
        for j in range(i + 1, len(numbers)):
            if numbers[min] > numbers[j]:
                min = j
        if min != i:
            numbers[min], numbers[i] = numbers[i], numbers[min]
    return " ".join(list(map(str, numbers)))

if __name__=="__main__":
    numbers = random.sample(range(1, 1000), 10)
    print("array = {}".format(numbers))
    print("result = {}".format(selection_sort(numbers)))
    