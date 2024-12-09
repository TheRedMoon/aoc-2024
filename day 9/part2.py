

x = 0
y = 0

def map_frequency_to_coordinates(lines) -> dict[tuple[int, int], str]:
    coordinates = {}
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != ".":
                coordinates[(j, i)] = lines[i][j]
    return coordinates

def group_frequency_nodes(coord_dict):
    frequency_nodes = {}
    for coord in coord_dict:
        if coord_dict[coord] not in frequency_nodes:
            frequency_nodes[coord_dict[coord]] = []
        frequency_nodes[coord_dict[coord]].append(coord)
    return frequency_nodes

def create_anti_node_coord_from_pair(pair):
    print(pair)
    dist_x = pair[0][0] - pair[1][0]
    dist_y = pair[0][1] - pair[1][1]

    number = 1
    list_coords = []
    while True:
        coord_1 = None
        coord_2 = None
        anti_node_pair_1_coord = (pair[0][0] + dist_x*number, pair[0][1] + dist_y*number)
        anti_node_pair_2_coord = (pair[1][0] - dist_x*number, pair[1][1] - dist_y*number)
        if check_if_valid_coordinate(anti_node_pair_1_coord):
            coord_1 = anti_node_pair_1_coord
            list_coords.append(anti_node_pair_1_coord)
        if check_if_valid_coordinate(anti_node_pair_2_coord):
            coord_2 = anti_node_pair_2_coord
            list_coords.append(anti_node_pair_2_coord)
        if not coord_1 and not coord_2:
            break
        
        number += 1
    #print(anti_node_pair_1_coord, anti_node_pair_2_coord)
    return list_coords
    
    
def create_anti_nodes(coord_dict):
    frequency_coordinates = group_frequency_nodes(coord_dict)
    # create pairs for each entry in the coordinate list
    anti_nodes = {}
    for frequency in frequency_coordinates:
        for i in range(len(frequency_coordinates[frequency])):
            for j in range(i+1, len(frequency_coordinates[frequency])):
                pair = frequency_coordinates[frequency][i], frequency_coordinates[frequency][j]
                anti_node = create_anti_node_coord_from_pair(pair)
                if '#' not in anti_nodes:
                    anti_nodes['#'] = [anti_node]
                else:
                    anti_nodes['#'].append(anti_node)
    return anti_nodes

    
def create_grid_from_coordinates(x, y, coord_dict: dict[tuple[int, int], str]):
    grid = [["." for i in range(x)] for j in range(y)]
    for coord in coord_dict:
        grid[coord[1]][coord[0]] = coord_dict[coord]
    for i in range(y):
        print(grid[i])

def remove_invalid_coordinates(x, y, coord_dict: list[tuple[tuple[int,int], tuple[int,int]]]):
    valid_coordinates = []
    for coordinates in coord_dict:
        for coord in coordinates:
            if check_if_valid_coordinate(coord) == False:
                continue # first i put here coordinates.delete(coord), but this deleted both the coordinates instead of just the invalid one
            valid_coordinates.append(coord)
    return valid_coordinates

def check_if_valid_coordinate(coord):
    if coord[0] < 0 or coord[0] >= y or coord[1] < 0 or coord[1] >= x:
        return False
    return True
    
if __name__ == '__main__':
    with open("day 8/input.txt") as file:
        lines = [line.rstrip('\n') for line in file]
    y = len(lines)
    x = len(lines[0])
    coord_dict = map_frequency_to_coordinates(lines)
    start_grid = create_grid_from_coordinates(x, y, coord_dict)
    print(start_grid)
    anti_nodes = create_anti_nodes(coord_dict)
    valid_anti_nodes = {}
    for frequency in anti_nodes:
        print(frequency)
        valid_coordinates = remove_invalid_coordinates(x, y, anti_nodes[frequency])
        #update value
        for valid_coordinate in valid_coordinates:
            valid_anti_nodes[valid_coordinate] = frequency
            valid_anti_nodes[valid_coordinate] = frequency

    #draw antinode grid

    anti_node_grid = create_grid_from_coordinates(x, y, valid_anti_nodes)
    print(len(valid_anti_nodes))
    print(len(coord_dict))
    
    a = valid_anti_nodes.keys() | coord_dict.keys() # union of keys to remove duplicates between nodes and antinodes
    print(len(a))
    #part 2

