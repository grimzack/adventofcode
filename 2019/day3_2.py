# Advent of Code 2019 Day 3 Part 2

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
        num_steps = 0
        for step in line:
            x_coord, y_coord, num_steps = add_segment(x_coord, 
                                                      y_coord, 
                                                      step, 
                                                      visited_coords, 
                                                      intersections,
                                                      line_num,
                                                      num_steps)
        line_num += 1

    # print("visited coords = ", visited_coords)
    return intersections

def add_segment(x, y, instr, visited_coords, intersections, line_num, num_steps):
    direction = instr[0]
    distance = int(instr[1])

    if (direction == 'U'):
        for cur_y in range(y, (y + distance + 1)):
            mark_visited(x, cur_y, visited_coords, intersections, line_num, num_steps)
            num_steps += 1

        return x, (y + distance), (num_steps - 1)

    elif (direction == 'R'):
        for cur_x in range(x, (x + distance + 1)):
            mark_visited(cur_x, y, visited_coords, intersections, line_num, num_steps)
            num_steps += 1

        return (x + distance), y, (num_steps - 1)

    elif (direction == 'D'):
        cur_y = y
        while cur_y > (y - distance):
            mark_visited(x, cur_y, visited_coords, intersections, line_num, num_steps)      
            cur_y -= 1
            num_steps += 1
        
        return x, cur_y, (num_steps)

    elif (direction == 'L'):
        cur_x = x
        while cur_x > (x - distance):
            mark_visited(cur_x, y, visited_coords, intersections, line_num, num_steps)
            cur_x -= 1
            num_steps += 1

        return cur_x, y, (num_steps)

    else:
        print("go to hell")

def mark_visited(x, y, visited_coords, intersections, line_num, num_steps):
    cur_coord_status = visited_coords.get((x, y))

    if (cur_coord_status == None):
        visited_coords[(x, y)] = ('l' + str(line_num), num_steps)


    elif (cur_coord_status[0] != ('l' + str(line_num))):
        visited_coords[(x, y)] = ("both", (cur_coord_status[1] + num_steps))
        if (abs(x) > 0 or abs(y) > 0):
            intersections.append((((abs(x) + abs(y))), (cur_coord_status[1] + num_steps)))

def find_closest_intersection(intersections):
    closest_distance = float('inf')
    for inter in intersections:
        if (closest_distance > inter[1]):
            closest_distance = inter[1]
    
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
