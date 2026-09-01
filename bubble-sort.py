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
            
    return arr


# Exempel på användning
min_lista = [64, 34, 25, 12, 22, 11, 90]
sorterad_lista = bubble_sort(min_lista)

print("Sorterad lista:", sorterad_lista)