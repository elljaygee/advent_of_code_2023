file_list = open('day_1_file.txt').read().splitlines()

# part one

total = 0
for string in file_list:
    digits = "0123456789"
    numbers = ""
    for letter in string:
        if letter in digits:
           numbers += letter
    length = len(numbers)
    if length > 1:
        x = numbers[0]
        y = numbers[-1]
        result = x + y
        sum1 = int(result)
    else:
        x = numbers
        result = x + x
        sum1 = int(result)
    #print(sum1)

    total = total + sum1

print(total)

# part two

cal_list = open('day_1_file.txt').read().split()

alphabet = []

for letters in 'abcdefghijklmnopqrstuvwxyz':
    alphabet.append(letters)

digits = {'one' : 'o1ne', 'two' : 't2wo', 'three' : 'th3ree',
'four' : 'fo4ur', 'five' : 'fi5ve', 'six' : 's6ix',
'seven' : 'se7ven', 'eight' : 'eig8ht', 'nine' : 'ni9ne'}

# loop through each item in the list
for x in range(len(cal_list)):
    # this loops through the item, finds any mention of the word-digit eg "one" and replaces it with o1ne
    for dig in digits:
        cal_list[x] = cal_list[x].replace(dig, digits[dig])
    # this loops through the item, finds each instance of an alphabetical letter, and removes it so that only the numbers are left 
    for char in alphabet:
        cal_list[x] = cal_list[x].replace(char, '')

numerical_list = []

# this loops through the items in the list, which now only consist of numbers, and finds the first and last numbers in the item and appends them to a list
for x in range(len(cal_list)):
    numerical_list.append(int(cal_list[x][0] + cal_list[x][-1]))

# the sum function sums all values in the numbers list
print(sum(numerical_list))