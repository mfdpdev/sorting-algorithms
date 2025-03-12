def bubble_sort(data):
    for i, _ in enumerate(data):
        for j in range(1 + i, len(data)):
            if(data[i] > data[j]):
                data[j], data[i] = data[i], data[j]
    return data

def selection_sort(data):
    for i, _ in enumerate(data):
        min = data[i]
        for j in range(1 + i, len(data)):
            if(data[j] < min):
                min = data[j]
                data[i], data[j] = min, data[i] 
    return data
