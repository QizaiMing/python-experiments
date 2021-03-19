import random
import sys

# How to use
# python kilobases.py 0.03

length = float(sys.argv[1])
kilobase = ""
GC = 0.5  # Percentage


bases = ["G", "C", "A", "T"]

print(f"Generating ADN of length {length} kilobases and GC pairs = {GC * 100}%")

for i in range(int(length * 1000)):
    base = random.choice(bases)
    kilobase = kilobase + base

print(kilobase)
