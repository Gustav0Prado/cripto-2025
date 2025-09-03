#!/usr/bin/python3

import string, random, sys

input = sys.argv[1]
key = sys.argv[2]

random.seed(key)

DISK1_IN  = list(string.ascii_uppercase) # ['A', 'B', 'C'..., 'Z']
DISK1_OUT = random.shuffle(DISK1_IN)

print(DISK1_IN, DISK1_OUT)