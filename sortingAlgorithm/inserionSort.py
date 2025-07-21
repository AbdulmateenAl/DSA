unsorted = [5, 4, 3, 2, 1]
sorted = []

for num in unsorted:
    if len(sorted) >= 1:
        for j in range(len(sorted)):
            if sorted[j] > num:
                sorted.insert(j, num)
                print(sorted)
                break
            sorted.append(num)
            print(sorted)
    # unsorted.pop(i)
    else:
        sorted.append(num)

print(sorted)