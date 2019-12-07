# Advent of Code 2019 Day 5 Part 1

def main():
    input_file = "input_5.txt"
    program = read_input_file_to_int_list(input_file)
    test_program = [103,4,3,4,33]
    answer_list = run_program(program)

def run_program(program):
    inst_pointer = 0
    inst = program[inst_pointer]
    opcode, param_modes = decode_instruction(inst)
    while (opcode != 99):
        if (opcode == 1):
            # OpCode = 1: (param_a + param_b => param_c)
            if (param_modes[0] == ParameterMode.POSITION):
                param_a_loc = program[inst_pointer + 1]
                param_a = program[param_a_loc]
            elif (param_modes[0] == ParameterMode.IMMEDIATE):
                param_a = program[inst_pointer + 1]

            if (param_modes[1] == ParameterMode.POSITION):
                param_b_loc = program[inst_pointer + 2]
                param_b = program[param_b_loc]
            elif (param_modes[1] == ParameterMode.IMMEDIATE):
                param_b = program[inst_pointer + 2]

            if (param_modes[2] == ParameterMode.POSITION):
                param_c = program[inst_pointer + 3]
            elif (param_modes[2] == ParameterMode.IMMEDIATE):
                param_c = inst_pointer + 3
            
            program[param_c] = param_a + param_b
            inst_pointer += 4

        elif (opcode == 2):
            # OpCode = 2: (param_a * param_b => param_c)
            if (param_modes[0] == ParameterMode.POSITION):
                param_a_loc = program[inst_pointer + 1]
                param_a = program[param_a_loc]
            elif (param_modes[0] == ParameterMode.IMMEDIATE):
                param_a = program[inst_pointer + 1]

            if (param_modes[1] == ParameterMode.POSITION):
                param_b_loc = program[inst_pointer + 2]
                param_b = program[param_b_loc]
            elif (param_modes[1] == ParameterMode.IMMEDIATE):
                param_b = program[inst_pointer + 2]

            if (param_modes[2] == ParameterMode.POSITION):
                param_c = program[inst_pointer + 3]
            elif (param_modes[2] == ParameterMode.IMMEDIATE):
                param_c = inst_pointer + 3

            program[param_c] = param_a * param_b
            inst_pointer += 4
            
        elif (opcode == 3):
            # OpCode = 3: save param_a to input_location
            if (param_modes[0] == ParameterMode.POSITION):
                param_a = program[inst_pointer + 1]
            elif (param_modes[0] == ParameterMode.IMMEDIATE):
                param_a = inst_pointer + 1
            else:
                print("Bad parameter for opcode == 3")
            input_param = input("Please provide input:")
            input_int = int(input_param)

            program[param_a] = input_int

            inst_pointer += 2

        elif (opcode == 4):
            # OpCode = 4: output param_a
            if (param_modes[0] == ParameterMode.POSITION):
                param_a_loc = program[inst_pointer + 1]
                param_a = program[param_a_loc]
            elif (param_modes[0] == ParameterMode.IMMEDIATE):
                param_a = program[inst_pointer + 1]
            else:
                print("Bad first param for opcode == 4")

            print("DIAGNOSTIC PRINT MESSAGE  .... CURRENTLY THIS MANY AWAY FROM CORRECT =====", param_a)
            inst_pointer += 2

        else:
            # Bad opcode, do something
            print("Probably bad opcode:", opcode)

        inst = program[inst_pointer]
        opcode, param_modes = decode_instruction(inst)

    return program

def decode_instruction(inst):
    opcode = int(str(inst)[-2:])

    # For now we'll just assume we always have at least 3 parameter modes
    reversed_instr = str(inst)[-3::-1] + "000" # could be missing leading 0's
    param_modes = []
    for char in reversed_instr:
        if char == '0':
            param_modes.append(ParameterMode.POSITION)
        elif char == '1':
            param_modes.append(ParameterMode.IMMEDIATE)
        else:
            print("Something wrong with reversed_inst:", reversed_instr)

    return opcode, param_modes

def read_input_file_to_int_list(input):
    input_list = []
    with open(input) as file:
        input_list = list(map(int, file.readline().split(',')))
    return input_list

class ParameterMode:
    POSITION = 0
    IMMEDIATE = 1

if __name__ == '__main__':
    main()