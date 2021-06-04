""" Tìm kiếm tuyến tính """

import random

def linear_search(array, k):
    for i in range(len(array)):
        if k == array[i]:
            return True
    return False

if __name__=="__main__":
    array = random.sample(range(1, 10), 5)
    k = int(input("Enter k: "))
    print("array = {}".format(array))
    print("k = {}".format(k))
    if linear_search(array, k):
        print("==> k in array")
    else:
        print("==> k not in array")


