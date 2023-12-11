# solution from zach1502 on reddit, added comments for my own learning!

file_path = 'day_2_file.txt'

def count_cubes(game_data, red, green, blue):
    # splits the list of game data into sub-sets using ; as the delimeter
    checks = game_data.split(';')

    for check in checks:
        # sets initial value of red/green/blue keys to zero
        # this resets with every loop as each sub-set has to be counted individually 
        cubes = {'red': 0, 'green': 0, 'blue': 0}
        # splits the sub-sets into their colour/number pairs using , as the delimeter and runs a for loop
        for data in check.split(','):
            # removes the whitespace from each colour/number pair
            data = data.strip()
            # if the dat contains a value
            if data:
                # splits the number value from the colour key using a blank space as the delimeter
                num, col = data.split()
                # adds the number value to the corresponding colour key in the cub variable
                cubes[col] += int(num)
        # checks the value of each colour cube against the values specified below
        # and returns either True or False
        if cubes['red'] > red or cubes['green'] > green or cubes['blue'] > blue:
            return False

    return True

def analyse_input():
    # sets initial total value at zero
    total = 0
    # opens input file in read mode
    with open(file_path, 'r') as file:
        # loops through each line in the file
        for line in file:
            # splits game id from game data using : as the delimiter
            game_id, game_data = line.split(':')
            # removes text from gameID to just leave the number in integer format
            game_id = int(game_id.split()[1])
            # uses the function defined above to check if True or False
            if count_cubes(game_data, 12, 13, 14):
                # adds the gameID number to the sum
                total += game_id

    return total

print(analyse_input())



# my initial attempt to use a dictionary, which didn't get me very far!

# with open('day_2_file.txt', 'r') as f: 
#   #read the text file into a list of lines 
#   lines = f.readlines() 


# #create an empty dictionary 
# file_dict = {} 
 
# # #loop through the lines in the text file  
# for line in lines: 
#   #split the line on ':' 
#   key, value = line.split(':') 
#   #strip the whitespace 
#   key = key.strip() 
#   value = value.strip() 
#   #add the key, value pair to the dictionary 
#   file_dict[key] = value 

# print(file_dict)

# list_of_values = []

# for key in file_dict:
   
#    y = tuple(value.split("; ")) # got stuck here, why is this only ever pulling the first set of values it pulls and not moving on to the next key-values?
#    for item in y:
#         list_of_values.append(item)

# print(key, list_of_values)



