import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
key_nums = list(map(int, input().split()))

num_cnt = Counter(numbers)

for key_num in key_nums:
    print(num_cnt[key_num], end = ' ')


"""
git commit -m "code: Solve boj 00000 문제 이름 (yeonhee)"
"""