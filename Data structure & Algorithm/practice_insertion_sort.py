n = int(input())
a = []
def insertion_sort():
    for i in range(n):
        a.append(int(input()))

    for i in range(1, len(a)):
        key = i
        j = i - 1
        while j >=0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key

    return a

print(insertion_sort())