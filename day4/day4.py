import numpy as np
import pandas as pd
import re

# load data
with open('input.txt', 'r') as f:
    data = f.read().split('\n')

data = data[:-1]

ans = 0

for i in range(len(data)):
    game_num = int(data[i].split(': ')[0].split(' ')[-1])
    winning_card_list = [int(x) for x in re.split('\s+', re.split('\s+\|\s+', re.split(':\s+', data[i])[1])[0])]
    owning_card_list = [int(x) for x in re.split('\s+', re.split('\s+\|\s+', re.split(':\s+', data[i])[1])[1])]

    tmp = set(winning_card_list).intersection(set(owning_card_list))
    if len(tmp) > 0:
        ans += 2**(len(tmp) - 1)

print(ans)

card_dict = {i: 1 for i in range(len(data))}

for i in range(len(data)):
    game_num = int(data[i].split(': ')[0].split(' ')[-1])
    winning_card_list = [int(x) for x in re.split('\s+', re.split('\s+\|\s+', re.split(':\s+', data[i])[1])[0])]
    owning_card_list = [int(x) for x in re.split('\s+', re.split('\s+\|\s+', re.split(':\s+', data[i])[1])[1])]

    tmp = set(winning_card_list).intersection(set(owning_card_list))
    for j in range(len(tmp)):
        card_dict[i + j + 1] += card_dict[i]

print(sum(card_dict.values()))


