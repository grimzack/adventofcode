# Advent of Code 2019 Day 7 Part 1

from collections import deque
import itertools

def main():
    original_program = read_input_file_to_int_list('2019/input_7.txt')
    usable_program = original_program.copy()
    modules = ['A', 'B', 'C', 'D', 'E']
    possible_signals = list(itertools.permutations([0,1,2,3,4]))
    output = 0
    max_output = 0
    in_val = deque()
    for permutation in possible_signals:
        i = 0
        for module in modules:
            in_val.append(permutation[i])
            in_val.append(output)
            print("using input:", permutation[i], "then output:", output)
            output = run_program(usable_program, in_val)
            usable_program = original_program.copy()
            i += 1
        if (output > max_output):
            max_output = output
        output = 0
    print("Max Output =", max_output)
    print(original_program)

def run_program(program, input_value):
    output = 0
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
    
            # input_param = input("Please provide input:")
            # input_int = int(input_param)
            next_input = input_value.popleft()
            print("using input_value =", next_input)
            program[param_a] = next_input

            inst_pointer += 2

        elif (opcode == 4):
            # OpCode = 4: output param_a
            if (param_modes[0] == ParameterMode.POSITION):
                param_a_loc = program[inst_pointer + 1]
                param_a = program[param_a_loc]
            elif (param_modes[0] == ParameterMode.IMMEDIATE):
                param_a = program[inst_pointer + 1]
            else:
                print("Bad ParameterMode for opcode = 4")

            print("DIAGNOSTIC PRINT MESSAGE 8=============>", param_a)
            output = param_a
            inst_pointer += 2
        
        elif (opcode == 5):
            # OpCode = 5: if param_a != 0 jump inst_pointer to param_b
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

            if (param_a != 0):
                inst_pointer = param_b
            else:
                inst_pointer += 3

        elif (opcode == 6):
            # OpCode = 6: if param_a == 0 jump inst_pointer to param_b
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

            if (param_a == 0):
                inst_pointer = param_b
            else:
                inst_pointer += 3

        elif (opcode == 7):
            # OpCode = 7: if param_a <  0 param_b store 1 in param_c
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

            if (param_a < param_b):
                program[param_c] = 1
            else:
                program[param_c] = 0

            inst_pointer += 4
        
        elif (opcode == 8):
            # OpCode = 7: if param_a <  0 param_b store 1 in param_c
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

            if (param_a == param_b):
                program[param_c] = 1
            else:
                program[param_c] = 0

            inst_pointer += 4

        else:
            # Bad opcode, do something
            print("Probably bad opcode:", opcode)

        inst = program[inst_pointer]
        opcode, param_modes = decode_instruction(inst)

    return output


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


class ParameterMode:
    POSITION = 0
    IMMEDIATE = 1


def read_input_file_to_int_list(input):
    input_list = []
    with open(input) as file:
        input_list = list(map(int, file.readline().split(',')))
    return input_list

if __name__ == "__main__":
    main()