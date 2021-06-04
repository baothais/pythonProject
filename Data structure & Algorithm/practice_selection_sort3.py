import random

def selection_sort(numbers):
    for i in range(len(numbers)):
        min = i
        for j in range(i + 1, len(numbers)):
            if numbers[min] > numbers[j]:
                min = j
        if min != i:
            numbers[i], numbers[min] = numbers[min], numbers[i]
    return " ".join(list(map(str, numbers)))

if __name__=="__main__":
    numbers = [random.randint(1, 1000) for _ in range(random.randint(5, 8))]
    print("array  = {}".format(numbers))
    print("result = {}".format(selection_sort(numbers)))

