def bubble_sort(data):
    if len(data) <= 0: return []
    for i, _ in enumerate(data):
        for j in range(1 + i, len(data)):
            if(data[i] > data[j]):
                data[j], data[i] = data[i], data[j]
    return data

def selection_sort(data):
    if len(data) <= 0: return []
    for i, _ in enumerate(data):
        min = i
        for j in range(1 + i, len(data)):
            if(data[j] < data[min]):
                min = j
        data[i], data[min] = data[min], data[i] 
    return data

def insertion_sort(data):
    if len(data) <= 0: return []
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key
    return data

def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2

        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(right_half) 
        merge_sort(left_half) 

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1

            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

    return data

