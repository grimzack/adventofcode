# Advent of Code 2019 Day 3 Part 1

def main():
    input_list = read_input_file_to_tuple_list("input_3.txt")
    intersections = get_intersections(input_list)
    closest_distance = find_closest_intersection(intersections)
    
    print("Closest distance = ", closest_distance)

def get_intersections(line_list):
    direction = ''
    visited_coords = {}
    intersections = []
    line_num = 0
    for line in line_list:
        x_coord = 0
        y_coord = 0
        for step in line:
            x_coord, y_coord = add_segment(x_coord, 
                                y_coord, 
                                step, 
                                visited_coords, 
                                intersections,
                                line_num)
        line_num += 1

    return intersections

def add_segment(x, y, instr, visited_coords, intersections, line_num):
    direction = instr[0]
    distance = int(instr[1])

    if (direction == 'U'):
        # print("go up " + str(distance) + " units")
        for cur_y in range(y, (y + distance + 1)):
            mark_visited(x, cur_y, visited_coords, intersections, line_num)

        return x, (y + distance)

    elif (direction == 'R'):
        # print("go right " + str(distance) + " units")
        for cur_x in range(x, (x + distance + 1)):
            mark_visited(cur_x, y, visited_coords, intersections, line_num)

        return (x + distance), y

    elif (direction == 'D'):
        # print("go down " + str(distance) + " units")
        cur_y = y
        while cur_y > (y - distance):
            mark_visited(x, cur_y, visited_coords, intersections, line_num)      
            cur_y -= 1
        
        return x, cur_y

    elif (direction == 'L'):
        # print("go left " + str(distance) + " units")
        cur_x = x
        while cur_x > (x - distance):
            mark_visited(cur_x, y, visited_coords, intersections, line_num)
            cur_x -= 1

        return cur_x, y

    else:
        print("go to hell")

def mark_visited(x, y, visited_coords, intersections, line_num):
    cur_coord_status = visited_coords.get((x, y))
    if (cur_coord_status == None):
        visited_coords[(x, y)] = 'v' + str(line_num)
    elif (cur_coord_status != ('v' + str(line_num))):
        visited_coords[(x, y)] = visited_coords.get((x, y)) + 'v' + str(line_num)
        if (abs(x) > 0 or abs(y) > 0):
            # Store the Manhatten distance of the intersection
            intersections.append((abs(x) + abs(y)))

def find_closest_intersection(intersections):
    closest_distance = float('inf')
    for inter in intersections:
        if (closest_distance > inter):
            closest_distance = inter
    
    return closest_distance

def read_input_file_to_tuple_list(input):
    input_list = []
    with open(input) as file:
        for line in file:
            input_list.append(list(line.strip().split(',')))
    output_list = [[],[]]
    i = 0
    for inst_set in input_list:
        output_list[i] = []
        for inst in inst_set:
            output_list[i].append([inst[0], inst[1:]])
        i += 1
    return output_list

if __name__ == '__main__':
    main()
