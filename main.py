# selection sort implementation

def selection_sort(arr):
    for i in range(len(arr)):
        index_min = i
        for j in range(i+1, len(arr)):
            if arr[index_min] > arr[j]:
                index_min = j
        arr[i], arr[index_min] = arr[index_min], arr[i]
    return arr


if __name__ == '__main__':
    val = selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92])
    print(val)
