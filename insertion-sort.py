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


# Exempel på användning:
numbers = [12, 11, 13, 5, 6]
sorted_numbers = insertion_sort(numbers)
print("Sorterad lista:", sorted_numbers)