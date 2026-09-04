import timeit
from makelist import createArray

def merge_sort(arr):
    # Basfall: En lista med 0 eller 1 element är redan sorterad
    if len(arr) <= 1:
        return arr

    # 1. DIVIDE: Hitta mitten och dela listan i två halvor
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 2. CONQUER: Sortera båda halvorna rekursivt
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # 3. COMBINE: Slå ihop de två sorterade halvorna
    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    i = j = 0

    # Jämför element från båda listorna och lägg till det minsta i resultatet
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Lägg till eventuella kvarvarande element
    result.extend(left[i:])
    result.extend(right[j:])

    return result


list = createArray(100)

stmt = f"merge_sort({list})"
setupcode = "from __main__ import merge_sort"

function_time = timeit.timeit(stmt=stmt, setup=setupcode, number=1)
print(f"Function time for array of length 100: {function_time:.5f} seconds")


list1000 = createArray(1000)
stmt = f"merge_sort({list1000})"

function_time = timeit.timeit(stmt=stmt, setup=setupcode, number=1)
print(f"Function time for array of length 1000: {function_time:.5f} seconds")


list10000 = createArray(10000)
stmt = f"merge_sort({list10000})"

function_time = timeit.timeit(stmt=stmt, setup=setupcode, number=1)
print(f"Function time for array of length 10000: {function_time:.5f} seconds")