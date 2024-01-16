import numpy as np

# load data
with open('input.txt', 'r') as f:
    data = f.read().split('\n')

time_array = [x for x in data[0].split(' ') if x != ''][1:]
time_array = [int(x) for x in time_array]
record_array = [x for x in data[1].split(' ') if x != ''][1:]
record_array = [int(x) for x in record_array]

def test(x, time, record):
    return x * (time - x) - record

tmp_list = []
for i in range(len(time_array)):
    x = 1
    tmp = 0
    while True:
        if test(x, time_array[i], record_array[i]) >= 0:
            tmp += 1
        if (tmp > 0) & (test(x, time_array[i], record_array[i]) < 0):
            break
        x += 1
    tmp_list.append(tmp)

print(np.prod(tmp_list))

x = 1
tmp = 0
while True:
    if test(x, int(''.join([str(x) for x in time_array])), int(''.join([str(x) for x in record_array]))) >= 0:
        tmp += 1
    if (tmp > 0) & (test(x, int(''.join([str(x) for x in time_array])), int(''.join([str(x) for x in record_array]))) < 0):
        break
    x += 1

print(tmp)
