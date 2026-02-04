def reverse_sorting(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] < key:
            a[j + 1] = a[j]
            j = j - 1

        a[j + 1] = key

    return a

if __name__ == "__main__":
    a = [5, 2, 4, 6, 1, 3]
    print("Array before reverse sorting: ", a)
    print("Array after reverse sorting: ", reverse_sorting(a))