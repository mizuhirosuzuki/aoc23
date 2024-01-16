import numpy as np
import pandas as pd

# load data
with open('input.txt', 'r') as f:
    data = f.read().split('\n')

data = data[:-1]

#data = '''0 3 6 9 12 15
#1 3 6 10 15 21
#10 13 16 21 30 45'''.split('\n')

ans = 0
for i in range(len(data)):

    tmp = data[i].split(' ')

    k = 0

    tmp_array = np.array([int(x) for x in tmp])
    k += tmp_array[-1]
    while True:
        tmp_array = tmp_array[1:] - tmp_array[:-1]
        k += tmp_array[-1]
        if (tmp_array == 0).all():
            break

    ans += k

print(ans)


ans = 0
for i in range(len(data)):
    j = 0

    tmp = data[i].split(' ')
    tmp_array = np.array([int(x) for x in tmp])

    k = tmp_array[0]

    while True:
        tmp_array = tmp_array[1:] - tmp_array[:-1]
        k -= tmp_array[0] * (-1)**(j % 2)
        j += 1
        if (tmp_array == 0).all():
            break

    print(k)
    ans += k

print(ans)
