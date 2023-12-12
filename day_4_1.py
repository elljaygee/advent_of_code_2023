# Given dozens of already scratched scratchcards; each card has two lists of numbers separated by a vertical bar (|)
# one is a list of winning numbers and the other a list of numbers you have. You organize the information into a table (your puzzle input).

# you have to figure out which of the numbers you have appear in the list of winning numbers. 
# The first match makes the card worth one point and each match after the first doubles the point value of that card.

# For example:
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53 : 8 points (4 matches)
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19 : 2 points (2 matches)
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1 : 2 points (2 matches)
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83 : 1 point (1 match)
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36 : 0 points
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11 :0 points
# So, in this example, the Elf's pile of scratchcards is worth 13 points.

# Using the given input, how many points are the cards worth in total?

# probably not the cleanest solution but really happy i figured this one out by myself!!

card_count  = []
file_path = "day_4_file.txt"
# opens input file in read mode
with open(file_path, 'r') as file:
    # loops through each line in the file
    for line in file:
        # splits game id from game data using : as the delimiter
        card_id, card_data = line.split(':')
        # assigns the remaining values to variable card_nums
        card_nums = card_data
        # splits winning numbers from numbers on card useing | as the delimeter
        win_nums, my_nums = card_nums.split('|')
        # splits the string of numbers into a list of numnbers for both winning numbers & my numbers
        win_nums_list = win_nums.split()
        my_nums_list = my_nums.split()

        count = 0
        # first for loop iterates through the winning numbers one at a time       
        for num1 in win_nums_list:
            # second for loop compares each of my numbers to the above winning number
            for num2 in my_nums_list: 
                # if they match the counter increments by 1
                if num1 == num2:
                    count += 1
        # the total in the count variable is appended to a list of pairs in format (card ID, total count)
        final_count = (card_id, count)
        card_count.append(final_count)
    
    doubled_list = []

    for (card_id, value) in card_count:
        # takes the count value from the list above and makes it an integer
        num = int(value)
        if num > 2 :
            doubled = 1 * 2**(num-1) # 1 point for the first match, then doubled for each subsequent match
        elif num == 2:
            doubled = 2    
        elif num == 1:
            doubled = 1
        else:
            doubled = 0
        # appends the doubled value created above to a list
        doubled_list.append(doubled)
        # sums the list of doubled values and saves it to a variable
        points = sum(doubled_list)
    
    print(points)
