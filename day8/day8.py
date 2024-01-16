import numpy as np
import pandas as pd
from math import lcm

# load data
with open('input.txt', 'r') as f:
    data = f.read().split('\n')

data = data[:-1]

#data = '''RL
#
#AAA = (BBB, CCC)
#BBB = (DDD, EEE)
#CCC = (ZZZ, GGG)
#DDD = (DDD, DDD)
#EEE = (EEE, EEE)
#GGG = (GGG, GGG)
#ZZZ = (ZZZ, ZZZ)'''.split('\n')
#
#data = '''LLR
#
#AAA = (BBB, BBB)
#BBB = (AAA, ZZZ)
#ZZZ = (ZZZ, ZZZ)'''.split('\n')

#data = '''LR
#
#11A = (11B, XXX)
#11B = (XXX, 11Z)
#11Z = (11B, XXX)
#22A = (22B, XXX)
#22B = (22C, 22C)
#22C = (22Z, 22Z)
#22Z = (22B, 22B)
#XXX = (XXX, XXX)'''.split('\n')

move_order = data[0]
node_list = data[2:]

node_df = pd.DataFrame(node_list)[0].str.split(' = ', expand=True)
node_df[1] = node_df[1].str.replace(r'\(|\)', '', regex=True)
node_df = pd.concat([node_df[0], node_df[1].str.split(', ', expand=True)], axis=1)
node_df.columns = ['node', 'L', 'R']

#i = 0
#current_node = 'AAA'
#while True:
#
#    current_node = node_df.query('node == @current_node')[move_order[i % len(move_order)]].iloc[0]
#    i += 1
#    if current_node == "ZZZ":
#        break
#
#print(i)

current_node_list = node_df[(node_df.node.str[2] == 'A')].node.tolist()
count_list = []
for j in range(len(current_node_list)):
    i = 0
    print(j)
    current_node = current_node_list[j]
    while True:
        current_node = node_df.query('node == @current_node')[move_order[i % len(move_order)]].iloc[0]
        i += 1
        if current_node[2] == 'Z':
            count_list.append(i)
            break

print(i)


