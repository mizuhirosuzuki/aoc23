import numpy as np
import pandas as pd

# load data
with open('input.txt', 'r') as f:
    data = f.read().split('\n')

game_num_sum = 0

for i in range(len(data) - 1):

    ball_list = data[i].split(': ')[1].split('; ')
    game_num = int(data[i].split(': ')[0].split(' ')[1])

    def get_ball_num_color(j, ball_list):
        df = pd.DataFrame(ball_list[j].split(', '))[0].str.split(' ', expand = True)
        df.columns = ['num', 'color']
        df['num'] = df['num'].astype(int)
        df['ind'] = j
        return df

    tmp = pd.concat([get_ball_num_color(j, ball_list) for j in range(len(ball_list))], axis=0)

    tmp_agg = tmp.groupby('color')['num'].max()

    for x in ['red', 'blue', 'green']:
        if x not in tmp_agg.index:
            tmp_agg[x] = 0

    if (tmp_agg['red'] <= 12) & (tmp_agg['green'] <= 13) & (tmp_agg['blue'] <= 14):
        game_num_sum += game_num

print(game_num_sum)


ans = 0

for i in range(len(data) - 1):

    ball_list = data[i].split(': ')[1].split('; ')

    def get_ball_num_color(j, ball_list):
        df = pd.DataFrame(ball_list[j].split(', '))[0].str.split(' ', expand = True)
        df.columns = ['num', 'color']
        df['num'] = df['num'].astype(int)
        df['ind'] = j
        return df

    tmp = pd.concat([get_ball_num_color(j, ball_list) for j in range(len(ball_list))], axis=0)

    tmp_agg = tmp.groupby('color')['num'].max()

    for x in ['red', 'blue', 'green']:
        if x not in tmp_agg.index:
            tmp_agg[x] = 0

    ans += tmp_agg['red'] * tmp_agg['blue'] * tmp_agg['green']

print(ans)
