# Advent of Code 2019 Day 2 Part 1

def main():
    input_file = "input_2.txt"
    answer_list = do_the_thing(input_file)
    print(answer_list)

def do_the_thing(input_file):
    program = read_input_file_to_int_list(input_file)
    loc = 0
    inst = program[loc]
    while (inst != 99):
        param_a_loc = program[loc + 1]
        param_b_loc = program[loc + 2]
        output_loc = program[loc + 3]
        if (inst == 1):
            # OpCode = 1 is Addition
            program[output_loc] = program[param_a_loc] + program[param_b_loc]
        elif (inst == 2):
            # Opcode = 2 is Multiplication
            program[output_loc] = program[param_a_loc] * program[param_b_loc]
        else:
            # Bad instruction, do something
            print("Hit instruction: " + str(inst))
        loc += 4
        inst = program[loc]

    return program

def read_input_file_to_int_list(input):
    input_list = []
    with open(input) as file:
        input_list = list(map(int, file.readline().split(',')))
    return input_list

if __name__ == '__main__':
    main()