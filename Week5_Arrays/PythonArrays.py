
m = 10
n = 3

array = []

counter = 0


for row in range(n):
    subarray = []
    for col in range(m):
        subarray.append(counter)
        counter = counter + 1

    array.append(subarray)
print(array)
