import numpy as np
import re
import regex

# load data
with open('input.txt', 'r') as f:
    data = f.read().split('\n')

ans = 0

for i in range(len(data) - 1):
    tmp = re.sub(r'[a-z]', '', data[i])
    ans += int(tmp[0] + tmp[-1])

print(ans)


word_to_digit = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

ans = 0
for i in range(len(data) - 1):
    tmp = regex.findall('\d|one|two|three|four|five|six|seven|eight|nine|zero', data[i], overlapped=True)
    tmp_list = [word_to_digit[x] if x in word_to_digit.keys() else x for x in tmp]
    ans += int(tmp_list[0] + tmp_list[-1])

print(ans)

