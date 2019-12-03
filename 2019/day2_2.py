# Advent of Code 2019 Day 2 Part 2

def main():
    input_file = "input_2.txt"
    answer1, answer2 = do_the_thing(input_file)
    print((answer1 * 100) + answer2)

def do_the_thing(input_file):
    orig_program = read_input_file_to_int_list(input_file)
    program = orig_program.copy()
    target_output = 19690720
    for first_param in range(100):
        for second_param in range(100):
            program[1] = first_param
            program[2] = second_param
            resulting_list = calculate_program_output(program)
            if (resulting_list[0] == target_output):
                return first_param, second_param
            else:
                program = orig_program.copy()

    return -1, -1


def calculate_program_output(program):
    loc = 0
    inst = program[loc]
    while (inst != 99):
        inst = program[loc]
        param_a_loc = program[loc + 1]
        param_b_loc = program[loc + 2]
        output_loc = program[loc + 3]
        if (param_a_loc > len(program) or 
            param_b_loc > len(program) or 
            output_loc > len(program)):
            break;
        if (inst == 1):
            # OpCode = 1 is Addition
            program[output_loc] = program[param_a_loc] + program[param_b_loc]
        elif (inst == 2):
            # Opcode = 2 is Multiplication
            program[output_loc] = program[param_a_loc] * program[param_b_loc]
        # else:
            # Either bad instruction or code 99
        loc += 4

    return program

def read_input_file_to_int_list(input):
    input_list = []
    with open(input) as file:
        input_list = list(map(int, file.readline().split(',')))
    return input_list

if __name__ == '__main__':
    main()