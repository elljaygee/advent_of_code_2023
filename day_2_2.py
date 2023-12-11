# i didn't even know where to start with this one!!
# solution from zach1502 on reddit, added comments for my own learning

file_path = 'day_2_file.txt'

def count_cubes(game_data):
    # splits the list of game data into sub-sets using ; as the delimeter
    checks = game_data.split(';')
    # sets initial max_cubes value to zero for each colour
    max_cubes = {'red': 0, 'green': 0, 'blue': 0}

    for check in checks:
        # sets initial value of red/green/blue keys to zero
        # this resets with every loop as each sub-set has to be counted individually 
        cubes = {'red': 0, 'green': 0, 'blue': 0}
        # splits the sub-sets into their colour/number pairs using , as the delimeter and runs a for loop
        for data in check.split(','):
            # removes the whitespace from each colour/number pair
            data = data.strip()
            if data:
                # splits the number value from the colour key using a blank space as the delimeter
                num, col = data.split()
                # adds the number value to the corresponding colour key in the cube variable
                cubes[col] += int(num)

        for col in max_cubes:
            # saves the maximum value for each colour by comparing the current subset cubes value with the value saved in max_cubes
            max_cubes[col] = max(max_cubes[col], cubes[col])

    # after all data subsets have been read this returns the final maxiumum value for each cube colour
    return max_cubes

def analyse_input():
    # sets initial total value at zero
    total = 0
    with open(file_path, 'r') as file:
        # loops through each line in the file
        for line in file:
            # splits game id from game data using : as the delimiter
            _, game_data = line.split(':')
            # runs the above count_cubes function and saves the result as the max_cubes value
            max_cubes = count_cubes(game_data)
            # adds the sum of multiplying the max_cubes of each colour to the running total
            total += max_cubes['red'] * max_cubes['green'] * max_cubes['blue']

    return total

print(analyse_input())

