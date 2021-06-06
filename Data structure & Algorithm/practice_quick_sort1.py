# Python3 implementation of QuickSort

# This Function handles sorting part of quick sort
# start and end points to first and last element of
# an arr respectively
def partition(start, end, arr):
    # Initializing pivot's index to start
    pivot_index = start
    pivot = arr[pivot_index]

    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:

        # Increment the start pointer till it finds an
        # element greater than pivot
        while start < len(arr) and arr[start] <= pivot:
            start += 1

        # Decrement the end pointer till it finds an
        # element less than pivot
        while arr[end] > pivot:
            end -= 1

        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if (start < end):
            arr[start], arr[end] = arr[end], arr[start]

    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]

    # Returning end pointer to divide the arr into 2
    return end


# The main function that implements QuickSort
def quick_sort(start, end, arr):
    if (start < end):
        # p is partitioning index, arr[p]
        # is at right place
        p = partition(start, end, arr)

        # Sort elements before partition
        # and after partition
        quick_sort(start, p - 1, arr)
        quick_sort(p + 1, end, arr)


# Driver code
arr = list(map(int, "-13 68 -43 -71 -39 -10 40 -49 -19 -3 -70 -62 -76 -94 -73 64 72 -5 88 2 -63 92 -40 16 49 47 -86 -51 -9 -14 96 74 -22 -34 38 -12 6 63 19 -69 14 -90 -27 76 54 57 -87 -91 43 -92".split()))

quick_sort(0, len(arr) - 1, arr)

print(f'Sorted arr: {arr}')

# This code is contributed by Adnan Aliakbar
