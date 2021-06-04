""" Tìm kiếm nhị phân """

import random

def binary_search(array, k):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if k == array[mid]:
            return True
        elif k > array[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return False

if __name__=="__main__":
    # array = random.sample(range(1, 20), 8)
    array = [1, 5, 15, 19, 25, 27, 29, 31, 33, 45, 55, 88, 100]
    array.sort()
    k = int(input("Enter k: "))
    print("array = {}".format(array))
    print("k = {}".format(k))
    if binary_search(array, k):
        print("k in array")
    else:
        print("k not in array")

