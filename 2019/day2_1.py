# Advent of Code 2019 Day 2 Part 1

def main():
    input_file = "input_2.txt"
    answer = do_the_thing(input_file)
    print(answer)

def do_the_thing(input_file):
    program = read_input_file_to_int_list(input_file)
    loc = 1
    inst = 0
    while (inst != 99):
        inst = program[loc]
        param_a = program[loc + 1]
        param_b = program[loc + 2]
        output_loc = program[loc + 3]
        if (inst == 1):
            # OpCode = 1 is Addition
            program[output_loc] = param_a + param_b
        elif (inst == 2):
            # Opcode = 2 is Multiplication
            program[output_loc] = param_a * param_b
        else:
            # Bad instruction, do something
            print("Got a bad instruction: " + inst)

def read_input_file_to_int_list(input):
    input_list = []
    with open(input) as file:
        input_list = file.readline().split(',')
    return input_list

if __name__ == '__main__':
    main()