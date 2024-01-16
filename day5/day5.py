import numpy as np
import pandas as pd
import re

# load data
with open('input.txt', 'r') as f:
    data = f.read().split('\n')

#data = '''seeds: 79 14 55 13
#
#seed-to-soil map:
#50 98 2
#52 50 48
#
#soil-to-fertilizer map:
#0 15 37
#37 52 2
#39 0 15
#
#fertilizer-to-water map:
#49 53 8
#0 11 42
#42 0 7
#57 7 4
#
#water-to-light map:
#88 18 7
#18 25 70
#
#light-to-temperature map:
#45 77 23
#81 45 19
#68 64 13
#
#temperature-to-humidity map:
#0 69 1
#1 0 69
#
#humidity-to-location map:
#60 56 37
#56 93 4
#'''.split('\n')

seeds = [int(x) for x in data[0].split(': ')[1].split(' ')]

data_sep = [i for i in range(len(data)) if data[i] == '']

min_val = 1000000000
for seed in seeds:
    new_loc = seed

    i = 0
    for i in range(len(data_sep) - 1):

        tmp = data[(data_sep[i] + 2):data_sep[i + 1]]

        tmp_df = pd.DataFrame(tmp)[0].str.split(' ', expand = True)
        tmp_df.columns = ['destination', 'source', 'range']
        tmp_df = tmp_df.astype({'destination': int, 'source': int, 'range': int})

        for j in range(tmp_df.shape[0]):
            if (tmp_df.iloc[j].source <= new_loc) & (tmp_df.iloc[j].source + tmp_df.iloc[j].range > new_loc):
                new_loc = tmp_df.iloc[j].destination + (new_loc - tmp_df.iloc[j].source)
                break

    min_val = min(min_val, new_loc)

print(min_val)

min_val = 100000000000
for k in range(len(seeds) // 2):
    for seed_range in range(seeds[2 * k + 1]):
        seed = seeds[2 * k] + seed_range
        new_loc = seed

        i = 0
        for i in range(len(data_sep) - 1):

            tmp = data[(data_sep[i] + 2):data_sep[i + 1]]

            tmp_df = pd.DataFrame(tmp)[0].str.split(' ', expand = True)
            tmp_df.columns = ['destination', 'source', 'range']
            tmp_df = tmp_df.astype({'destination': int, 'source': int, 'range': int})

            for j in range(tmp_df.shape[0]):
                if (tmp_df.iloc[j].source <= new_loc) & (tmp_df.iloc[j].source + tmp_df.iloc[j].range > new_loc):
                    new_loc = tmp_df.iloc[j].destination + (new_loc - tmp_df.iloc[j].source)
                    break

        min_val = min(min_val, new_loc)

print(min_val)



