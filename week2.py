# run in interpreter - examples

import os
dir(os)
# print(os.environ)
# print(os.environ['PATH'])
# os.getenv() - gets env variable
# print(os.system(command="ping 127.0.0.1"))

import sys
print(sys.path)

import re
pattern = re.compile('b')
cats = ['basil', 'billy', 'bobby', 'fluffy', 'moe', 'dobby']
for cat in cats:
    test = pattern.match(cat)
    if test:
        print("%s is a cat whose name starts with 'b'" % cat)

print("Week 2 Homework Exercises")

# 1. lottery num combination, first 5 can't be duplicated
import random

def generateLotto():
    white_balls = random.sample(range(1, 56), 5)
    red_ball = random.randint(1, 42)
    
    return white_balls, red_ball

white_balls, red_ball = generateLotto()
print("White balls:", white_balls)
print("Red ball:", red_ball)

# 2. tuple(sequence #, shot #) - create directory format $TMP/SHOW/##.#/###.##/character_data
def showSetup():
    pass

tuple_list = [(1,2), (1,4), (1,5.6), (2,4), (2,5), (3,1)]