# If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

# The engine schematic (your puzzle input) consists of a visual representation of the engine. 
# There are lots of numbers and symbols you don't really understand, but apparently 
# any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. 
# (Periods (.) do not count as a symbol.)

# # solution from Reddit user errop_ using regex (which is new to me): 
# "Used re.Match objects to get numbers endpoints on the horizontal axis. 
# Everything then boils down to find which symbols are in a rectangular neighborhood of each number.""
# 
# 

import re
from collections import defaultdict
from math import prod

with open("day_3_file.txt") as f:
    lines = f.read().split("\n")

# building symbols grid as {xy_position: symbol}
symbols = dict()
# initial value of y = 0, this will increment by 1 each time it loops
# this tracks the line number
for y, line in enumerate(lines):
    # initial value of x = 0, this will also increment by 1 with each loop
    # this tracks the index number of each item on the line
    for x, c in enumerate(line):
        if c not in "1234567890.":
            # stores the index location (x) & line number (y) of any symbols that are not a digit or a . 
            # in a dictionary with the pair of numbers as the key and the symbol as the value
            symbols[(x, y)] = c

# checking if a number has a rectangular neighborhood containing a symbol by using 
# defaultdict(list) object to store a gear grid as {gear_position(index location, line number): [part numbers list]}
gears = defaultdict(list)
part_numbers_sum = 0
for y, line in enumerate(lines):
    # regex function finditer is a findall function that returns an iterator to loop over each object that it matches
    # \d is a special regex sequence that signifies digits from 0-9, this will find any match to a digit in this range 
    for match in re.finditer(r"\d+", line):
        # the s_x and s_y variables refer to the index location & line number of the symbols
        # and c is the symbol at this location
        # this loops through the items in the symbols dictionary created above 
        for (s_x, s_y), c in symbols.items():
            # match.start() and match.end() are regex expressions that find the start & end index of the matched object
            # in this case the loop is finding the start and end index of any items that match \d, that is any digits
            # if the start index of a number minus 1 is less than or equal to the index location of a * symbol and less than or equal to the end index
            # and if the line number minus 1 is less than or equal to the line number location of a 8 symbol and less than or equal to the line number plus 1
            if (match.start() - 1 <= s_x <= match.end()) and (y - 1 <= s_y <= y + 1):
                # match.group returns the number digits and stores it in the variable num
                num = int(match.group())
                # the num value is added to the total part_numbers_sum value
                part_numbers_sum += num
                # if the sybol at this location is a *
                if c == "*":
                    # the index location, line number, and part number are added to the gears dictionary
                    gears[(s_x, s_y)].append(num)
                break

# ========= PART 1 =========
print(part_numbers_sum)

# ========= PART 2 =========
total = 0
for part_nums in gears.values():
    if len(part_nums) == 2:
        part_prod = (prod(part_nums))
        total += part_prod
    
print(total)


# one-line solution for part 2 from Reddit user errop_'s original code, broken down above in a way that makes sense for me:

# print(sum(prod(part_nums) for part_nums in gears.values() if len(part_nums) == 2))