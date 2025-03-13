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

