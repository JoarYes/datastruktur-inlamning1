import timeit
from makelist import createArray

def bubble_sort(arr):
    n = len(arr)
        
    for i in range(n):
        # Flagg för att hålla koll på om några byten sker
        swapped = False
        
        # Sista i elementen är redan på rätt plats
        for j in range(0, n - i - 1):
            # Jämför två intilliggande element
            if arr[j] > arr[j + 1]:
                # Byt plats på elementen
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # Om inga byten skedde under innerloopen är listan redan sorterad
        if not swapped:
            break
            
    


list = createArray(100)

stmt = f"bubble_sort({list})"
setupcode = "from __main__ import bubble_sort"

function_time = timeit.timeit(stmt=stmt, setup=setupcode, number=1)
print(f"Function time for array of length 100: {function_time:.5f} seconds")


list1000 = createArray(1000)
stmt = f"bubble_sort({list1000})"

function_time = timeit.timeit(stmt=stmt, setup=setupcode, number=1)
print(f"Function time for array of length 1000: {function_time:.5f} seconds")


list10000 = createArray(10000)
stmt = f"bubble_sort({list10000})"

function_time = timeit.timeit(stmt=stmt, setup=setupcode, number=1)
print(f"Function time for array of length 10000: {function_time:.5f} seconds")
