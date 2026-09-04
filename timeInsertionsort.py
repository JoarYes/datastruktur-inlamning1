import timeit
from makelist import createArray

def insertion_sort(arr):
    # Gå igenom listan från det andra elementet (index 1) till det sista
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Flytta element i arr[0..i-1] som är större än key
        # ett steg framåt för att göra plats för key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Sätt in key på rätt plats
        arr[j + 1] = key

    return arr


list = createArray(100)

stmt = f"insertion_sort({list})"
setupcode = "from __main__ import insertion_sort"

function_time = timeit.timeit(stmt=stmt, setup=setupcode, number=1)
print(f"Function time for array of length 100: {function_time:.5f} seconds")


list1000 = createArray(1000)
stmt = f"insertion_sort({list1000})"

function_time = timeit.timeit(stmt=stmt, setup=setupcode, number=1)
print(f"Function time for array of length 1000: {function_time:.5f} seconds")


list10000 = createArray(10000)
stmt = f"insertion_sort({list10000})"

function_time = timeit.timeit(stmt=stmt, setup=setupcode, number=1)
print(f"Function time for array of length 10000: {function_time:.5f} seconds")