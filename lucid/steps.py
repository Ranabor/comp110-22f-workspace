"""Incorrect"""
num_input = int(input())
entries = []

for i in range(num_input-1):
    entries.append(input())


coord = entries[0][1:(len(entries[0]) - 1)]
location = tuple(map(int, coord.split(',')))
    
def steps(entries1):
    directions = entries1[1:]
    steps = {}
    for i in directions:
        if "north" in i:
            steps["north"] = i[11]
        elif "south" in i:
            steps["south"] = i[11]
        elif "east" in i:
            steps["east"] = i[10]
        elif "west" in i:
            steps["west"] = i[10]
    return steps

steps_given = steps(entries)

def north_south(loc_coord, steps):
    vertical = int(loc_coord[1])
    step_size = 0
    return vertical
    if vertical < 0:
        step_size = vertical/int(steps["south"])
        return int(abs(step_size))
    elif vertical > 0:
        step_size = vertical/int(steps["north"])
        return int(step_size)

def east_west(loc_coord, steps):
    horizontal = int(loc_coord[0])
    step_size = 0
    if horizontal < 0:
        step_size = horizontal/int(steps["west"])
        return int(abs(step_size))
    elif horizontal > 0:
        step_size = horizontal/int(steps["east"])
        return int(step_size)
    else:
        return north_south(loc_coord, steps)


    
print(east_west(location, steps_given))