#Write a program to print all the unique combinations of 1,2,3 and 4
from itertools import permutations

nums = [1, 2, 3, 4]

for p in permutations(nums):
    print(p)