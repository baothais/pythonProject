import random


def quick_sort(numbers, left, right):
    if left >= right:
        return
    i = left
    j = right
    pivot = numbers[(left + right) // 2]
    while i < j:
        while i < j and numbers[i] < pivot:
            i += 1
        while j > left and numbers[j] > pivot:
            j -= 1
        if i <= j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i += 1
            j -= 1
    quick_sort(numbers, left, j)
    quick_sort(numbers, i, right)


if __name__=="__main__":
    # numbers = random.sample(range(1, 10), 5)
    numbers = list(map(int, "-13 68 -43 -71 -39 -10 40 -49 -19 -3 -70 -62 -76 -94 -73 64 72 -5 88 2 -63 92 -40 16 49 47 -86 -51 -9 -14 96 74 -22 -34 38 -12 6 63 19 -69 14 -90 -27 76 54 57 -87 -91 43 -92".split()))

    quick_sort(numbers, left=0, right=len(numbers) - 1)
    print(numbers)
