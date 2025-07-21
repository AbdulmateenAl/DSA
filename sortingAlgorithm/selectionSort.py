arr = [5, 4, 2, 3, 1]

for i in range(len(arr)):
    smallest, pos = arr[i], i
    for j in range(i, len(arr) - 1):
        if arr[j + 1] < arr[j]:
            smallest, pos = arr[j + 1], j + 1
    temp = arr[i]
    arr[i] = smallest
    arr[pos] = temp

print(arr)