import random


def quickSort(arr, left, right):
    # Write your code here
    # i = left
    # j = right
    # pivot = arr[(left + right) // 2]
    # if left >= right:
    #     return
    # while i < j:
    #     while i < j and arr[i] < pivot:
    #         i += 1
    #     while j > i and arr[j] > pivot:
    #         j -= 1
    #     arr[i], arr[j] = arr[j], arr[i]
    #     i += 1
    #     j -= 1
    # quickSort(arr, left, j)
    # quickSort(arr, i, right)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


if __name__=="__main__":
    arr = list(map(int, "-13 68 -43 -71 -39 -10 40 -49 -19 -3 -70 -62 -76 -94 -73 64 72 -5 88 2 -63 92 -40 16 49 47 -86 -51 -9 -14 96 74 -22 -34 38 -12 6 63 19 -69 14 -90 -27 76 54 57 -87 -91 43 -92".split()))
    quickSort(arr, left=0, right=len(arr) - 1)
    print(" ".join(list(map(str, arr))))