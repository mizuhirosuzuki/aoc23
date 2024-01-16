import numpy as np
import pandas as pd
import re

# load data
with open('input.txt', 'r') as f:
    data = f.read().split('\n')

data = data[:-1]

ans = 0

for i in range(len(data)):

    digits_list = [(m.start(0), m.end(0)) for m in re.finditer('\d+', data[i])]

    for j in range(len(digits_list)):

        tmp = (
            data[max(i - 1, 0)][max(digits_list[j][0] - 1, 0):min(digits_list[j][1] + 1, len(data[i]))] 
            + data[i][max(digits_list[j][0] - 1, 0):min(digits_list[j][1] + 1, len(data[i]))] 
            + data[min(i + 1, len(data) - 1)][max(digits_list[j][0] - 1, 0):min(digits_list[j][1] + 1, len(data[i]))]
        )

        if len(re.sub('\d|\.', '', tmp)) > 0:
            ans += int(data[i][digits_list[j][0]:digits_list[j][1]])
                 
print(ans)

ans = 0

for i in range(len(data) - 1):

    star_list = [(m.start(0), m.end(0)) for m in re.finditer('\*', data[i])]

    if (i > 0):
        digits_list_0 = [(m.start(0), m.end(0)) for m in re.finditer('\d+', data[i - 1])]
    digits_list_1 = [(m.start(0), m.end(0)) for m in re.finditer('\d+', data[i])]
    if (i < len(data)):
        digits_list_2 = [(m.start(0), m.end(0)) for m in re.finditer('\d+', data[i + 1])]

    for k in range(len(star_list)):
        star_pos = star_list[k][0]
        tmp_0 = [x for x in digits_list_0 if ((star_pos - 1) in range(*x)) | ((star_pos) in range(*x)) | ((star_pos + 1) in range(*x))]
        tmp_1 = [x for x in digits_list_1 if ((star_pos - 1) in range(*x)) | ((star_pos) in range(*x)) | ((star_pos + 1) in range(*x))]
        tmp_2 = [x for x in digits_list_2 if ((star_pos - 1) in range(*x)) | ((star_pos) in range(*x)) | ((star_pos + 1) in range(*x))]

        ans_list = []

        if len(tmp_0 + tmp_1 + tmp_2) == 2:
            if (i > 0):
                for l in tmp_0:
                    ans_list.append(int(data[i - 1][l[0]:l[1]]))
            for l in tmp_1:
                ans_list.append(int(data[i][l[0]:l[1]]))
            if (i < len(data)):
                for l in tmp_2:
                    ans_list.append(int(data[i + 1][l[0]:l[1]]))

            ans += ans_list[0] * ans_list[1]

print(ans)
