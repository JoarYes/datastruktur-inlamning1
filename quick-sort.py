def partition(arr, low, high):
    pivot = arr[high]  # Välj det sista elementet som pivot
    i = low - 1  # Pekare för det mindre elementet

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Byt plats

    # Placera pivot på rätt position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # pi är divideringsindexet (pivot är nu på rätt plats)
        pi = partition(arr, low, high)

        # Sortera elementen före och efter pivot
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

    return arr


# Exempel på användning:
data = [10, 7, 8, 9, 1, 5]
sorterad_lista = quicksort(data)
print("Sorterad lista:", sorterad_lista)