# This is currently in n^2 ish 


length = int(input())
array = input().split()
array = list(map(int, array))
results = 0

for i in range(length):
    j = i
    while j < length:
        if array[i] > array[j]:
            print(array[i], ' ', array[j])
            results += 1
        j += 1
print(results)



