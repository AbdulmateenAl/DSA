arr = [5, 1, 4, 2, 3, 10, 7, 9, 6, 1, 2]

for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print(arr)