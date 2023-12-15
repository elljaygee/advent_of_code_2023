# Reddit user HotAd3651's tips: 
# Initialize a dictionary num_dict that stores the amount of each card with 1 for each card. 
# Then I iterated through each cardnumber (line) and added the value num_dict[cardnumber] to each value from cardnumber+1 to cardnumber+1+len(winningsnumbers).
# # that is, add the card_id KEY to the next card's VALUE for as many times as the count (eg card1:4 means add 1 to each of the next 4 card VALUES, which is card_id+1 to card_id+1+count in this case 2, 3, 4, 5)

# Then I summed up the values of each key and it completed in less than 2 seconds.
# note that eg if you have 3 cards that get four winning numbers, then you have to add 3 (not 1!) to each of the next four

# No more points; you win copies of the scratchcards below the winning card equal to the number of matches. 
# So, if card 10 were to have 5 matching numbers, you would win one copy each of cards 11, 12, 13, 14, and 15.

# Copies of scratchcards are scored like normal scratchcards and have the same card number as the card they copied. 
# So, if you win a copy of card 10 and it has 5 matching numbers, it would then win a copy of the same cards that the original card 10 won: 
# cards 11, 12, 13, 14, and 15. This process repeats until none of the copies cause you to win any more cards. (Cards will never make you copy a card past the end of the table.)

# For example:

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53 : this has four matching numbers, & wins one copy each of the next four cards: cards 2, 3, 4, and 5.
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19 : your two instances of card 2 (one original & one copy) have two matching numbers, & wins one copy each of cards 3 and 4. 
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1 : your four instances of card 3 (one original & three copies) have two matching numbers, & wins four copies each of cards 4 and 5.
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83 : your eight instances of card 4 (one original and seven copies) have one matching number, & wins eight copies of card 5.
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36 : your fourteen instances of card 5 (one original and thirteen copies) have no matching numbers & win no more cards.
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11 : your one instance of card 6 (one original) has no matching numbers & wins no more cards.
# In total, this example pile of scratchcards causes you to ultimately have 30 scratchcards!

# code from Github user gamerplant3 that covers parts 1 & 2

import re

# import the txt file and reads each line into a list of strings
file = open('day_4_file.txt', 'r')
lines = file.read().splitlines()

# my functions
def get_lists(your_string):
    # given input string, split at delimiter, separate the numbers, and convert the str lists to int lists
    a, b, c = re.split(r': | \|', your_string)

    int_card = re.findall(r'\d+', a)
    card_num = [int(digit) for digit in int_card]
    int_win = re.findall(r'\d+', b)
    winning_num = [int(digit) for digit in int_win]
    int_my = re.findall(r'\d+', c)
    my_num = [int(digit) for digit in int_my]

    return card_num, winning_num, my_num

    lines = file.read().splitlines()

# PART 1 AND 2
cards_worth = []  # for PART 1
card_count = [1] * len(lines)  # for PART 2: list of every card's number of wins > initalize as 1

for index, line in enumerate(lines):
    card_number, winning_numbers, my_numbers = get_lists(line)
# PART 1: find how many points each card gets
    matches = []
    for x, y in enumerate(winning_numbers):
        for j in range(len(my_numbers)):
            if y == my_numbers[j]: matches.append(x)
    cards_worth.append(2 ** (len(matches) - 1)) if len(matches) > 0 else cards_worth.append(0)  # worth = 1 x 2^n-1

# PART 2:
    for n in range(len(matches)):
    # update the count of the card at spot "index + n + 1" with the count of the card at "index"
    # why does this work? je ne sais pas...c'est le voodoo magic
        card_count[index + n + 1] += card_count[index]

print((sum(cards_worth)))
print((sum(card_count)))



# my attempt, which worked well for the short example file but couldn't get it to work for the large text file
# for some reason i'm getting an "index out of range" error for the final element when using the large text file
# even though it works for the small example file

# num_dict = {}
# file_path = "day_4_file.txt"
# # opens input file in read mode
# with open(file_path, 'r') as file:

#         # loops through each line in the file
#     for line in file:
#         # remove extra whitespace from cards 1-9
#         while line.replace("   ", "  ") != line:
#             line = line.replace("   ", "  ")
#         # splits game id from game data using : as the delimiter
#         card, card_data = line.split(':')
#         # splits the word Card from the card number using the blank space as the delimiter
#         name, card_number = card.split() 
#         card_id = int(card_number)
#         # assigns the remaining values to variable card_nums
#         card_nums = card_data
#         # splits winning numbers from numbers on card useing | as the delimeter
#         win_nums, my_nums = card_nums.split('|')
#         # splits the string of numbers into a list of numnbers for both winning numbers & my numbers
#         win_nums_list = win_nums.split()
#         my_nums_list = my_nums.split()
        
#         #count = 0
#         count_nums = []
#         # first for loop iterates through the winning numbers one at a time       
#         for num1 in win_nums_list:
#             # second for loop compares each of my numbers to the above winning number
#             for num2 in my_nums_list: 
#                 # if they match the counter increments by 1
#                 if num1 == num2:
#                     count_nums.append(num1)
#             num_dict[card_id] = count_nums
        
#     # had to get help from Reddit user spacemicrowave on the math for this part!  
#     # i'd figured out most of the loops but couldn't get my head round what needed to be added to what

#     card_count = [1] * len(num_dict)
#     for key in num_dict:
#         matches = (num_dict[key])
#         for n in range(len(matches)):
#             card_count[key + n + 1] += card_count[key]
    
#     total_cards = sum(card_count)

# print(card_count)
# print(num_dict)
# print(total_cards)           
