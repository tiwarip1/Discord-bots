import pandas as pd
import random
import time

nouns = pd.read_csv('nouns.txt')
adjectives = pd.read_csv('adjectives.txt')
curses = pd.read_csv('curses.txt')

nouns_len = len(nouns.columns)
adjectives_len = len(adjectives.columns)
curses_len = len(curses.columns)

used_noun = nouns.sample().values[0][0]

print(used_noun)