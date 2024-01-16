import numpy as np
import pandas as pd

# load data
with open('input.txt', 'r') as f:
    data = f.read().split('\n')

data = data[:-1]

df = pd.DataFrame(data)[0].str.split(' ', expand=True)
df.columns = ['hand', 'num']

label_list = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

hand_type_list = []
for i in range(df.shape[0]):

    tmp_dict = {x: sum([y == x for y in df.iloc[i]['hand']]) for x in label_list}

    tmp_series = pd.Series(tmp_dict.values()).value_counts()
    for j in range(0, 6):
        if j not in tmp_series.index:
            tmp_series.loc[j] = 0

    if tmp_series.loc[5] == 1:
        hand_type = "five"
    elif tmp_series.loc[4] == 1:
        hand_type = "four"
    elif (tmp_series.loc[3] == 1) & (tmp_series.loc[2] == 1):
        hand_type = "full_house"
    elif (tmp_series.loc[3] == 1) & (tmp_series.loc[2] != 1):
        hand_type = "three"
    elif (tmp_series.loc[2] == 2):
        hand_type = "two_pair"
    elif (tmp_series.loc[2] == 1):
        hand_type = "one_pair"
    elif (tmp_series.loc[1] == 5):
        hand_type = "high"

    hand_type_list.append(hand_type)

df['hand_type'] = pd.Categorical(hand_type_list, ['five', 'four', 'full_house', 'three', 'two_pair', 'one_pair', 'high'])

df['first'] = pd.Categorical(df.hand.str[0], label_list)
df['second'] = pd.Categorical(df.hand.str[1], label_list)
df['third'] = pd.Categorical(df.hand.str[2], label_list)
df['fourth'] = pd.Categorical(df.hand.str[3], label_list)
df['fifth'] = pd.Categorical(df.hand.str[4], label_list)

df = df.sort_values(['hand_type', 'first', 'second', 'third', 'fourth', 'fifth'], ascending=False)
df['rank'] = range(1, df.shape[0] + 1)
df['point'] = df['num'].astype(int) * df['rank']

print(df['point'].sum())


label_list = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

hand_type_list = []

for i in range(df.shape[0]):

    tmp_dict = {x: sum([y == x for y in df.iloc[i]['hand']]) for x in label_list}

    if tmp_dict['J'] < 5:
        tmp = tmp_dict['J']
        tmp_dict['J'] = 0

        for a, b in tmp_dict.items():
            if b == max(tmp_dict.values()):
                tmp_dict[a] += tmp
                break

    tmp_series = pd.Series(tmp_dict.values()).value_counts()
    for j in range(0, 6):
        if j not in tmp_series.index:
            tmp_series.loc[j] = 0

    if tmp_series.loc[5] == 1:
        hand_type = "five"
    elif tmp_series.loc[4] == 1:
        hand_type = "four"
    elif (tmp_series.loc[3] == 1) & (tmp_series.loc[2] == 1):
        hand_type = "full_house"
    elif (tmp_series.loc[3] == 1) & (tmp_series.loc[2] != 1):
        hand_type = "three"
    elif (tmp_series.loc[2] == 2):
        hand_type = "two_pair"
    elif (tmp_series.loc[2] == 1):
        hand_type = "one_pair"
    elif (tmp_series.loc[1] == 5):
        hand_type = "high"

    hand_type_list.append(hand_type)

df['hand_type'] = pd.Categorical(hand_type_list, ['five', 'four', 'full_house', 'three', 'two_pair', 'one_pair', 'high'])

df['first'] = pd.Categorical(df.hand.str[0], label_list)
df['second'] = pd.Categorical(df.hand.str[1], label_list)
df['third'] = pd.Categorical(df.hand.str[2], label_list)
df['fourth'] = pd.Categorical(df.hand.str[3], label_list)
df['fifth'] = pd.Categorical(df.hand.str[4], label_list)

df = df.sort_values(['hand_type', 'first', 'second', 'third', 'fourth', 'fifth'], ascending=False)
df['rank'] = range(1, df.shape[0] + 1)
df['point'] = df['num'].astype(int) * df['rank']

print(df['point'].sum())



