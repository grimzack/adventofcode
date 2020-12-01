# Advent of Code 2019 Day 7 Part 2

from collections import deque
import itertools

def main():
    original_program = read_input_file_to_int_list('2019/input_7.txt')

    amp_a = Intcode('A', original_program.copy())
    amp_b = Intcode('B', original_program.copy())
    amp_c = Intcode('C', original_program.copy())
    amp_d = Intcode('D', original_program.copy())
    amp_e = Intcode('E', original_program.copy())

    module_output = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0
    }

    possible_phases = list(itertools.permutations([0,1,2,3,4]))
    output = 0
    max_output = 0

    for permutation in possible_phases:

        amp_a.set_phase_setting(permutation[0])
        amp_a.store_program(original_program.copy())

        amp_b.set_phase_setting(permutation[1])
        amp_b.store_program(original_program.copy())

        amp_c.set_phase_setting(permutation[2])
        amp_c.store_program(original_program.copy())

        amp_d.set_phase_setting(permutation[3])
        amp_d.store_program(original_program.copy())

        amp_e.set_phase_setting(permutation[4])
        amp_e.store_program(original_program.copy())

        # Run each amp and save its output so future amps can retrieve
        amp_a.set_input_param(module_output[amp_e.comp_name])
        # print("using input of output =", amp_a.input_param)
        module_output[amp_a.comp_name] = amp_a.run_program()

        amp_b.set_input_param(module_output[amp_a.comp_name])
        # print("using input of output =", amp_b.input_param)
        module_output[amp_b.comp_name] = amp_b.run_program()

        amp_c.set_input_param(module_output[amp_b.comp_name])
        # print("using input of output =", amp_c.input_param)
        module_output[amp_c.comp_name] = amp_c.run_program()

        amp_d.set_input_param(module_output[amp_c.comp_name])
        # print("using input of output =", amp_d.input_param)
        module_output[amp_d.comp_name] = amp_d.run_program()

        amp_e.set_input_param(module_output[amp_d.comp_name])
        # print("using input of output =", amp_e.input_param)
        module_output[amp_e.comp_name] = amp_e.run_program()

        output = module_output[amp_e.comp_name]
        if (output > max_output):
            max_output = output
        output = 0
        module_output['E'] = 0
    print("Max Output =", max_output)

class Intcode:

    def __init__(self, comp_name, program):
        self.comp_name = comp_name
        self.memory = program
        self.phase_setting = 0
        self.input_param = 0
        self.phase_or_input = 'PHASE'

    def set_phase_setting(self, phase_setting):
        self.phase_setting = phase_setting

    def set_input_param(self, input_param):
        self.input_param = input_param

    def store_program(self, program):
        self.memory = program

    def run_program(self):
        output = 0
        inst_pointer = 0
        inst = self.memory[inst_pointer]
        opcode, param_modes = self.decode_instruction(inst)
        while (opcode != 99):
            if (opcode == 1):
                # OpCode = 1: (param_a + param_b => param_c)
                if (param_modes[0] == ParameterMode.POSITION):
                    param_a_loc = self.memory[inst_pointer + 1]
                    param_a = self.memory[param_a_loc]
                elif (param_modes[0] == ParameterMode.IMMEDIATE):
                    param_a = self.memory[inst_pointer + 1]

                if (param_modes[1] == ParameterMode.POSITION):
                    param_b_loc = self.memory[inst_pointer + 2]
                    param_b = self.memory[param_b_loc]
                elif (param_modes[1] == ParameterMode.IMMEDIATE):
                    param_b = self.memory[inst_pointer + 2]

                if (param_modes[2] == ParameterMode.POSITION):
                    param_c = self.memory[inst_pointer + 3]
                elif (param_modes[2] == ParameterMode.IMMEDIATE):
                    param_c = inst_pointer + 3
                
                self.memory[param_c] = param_a + param_b
                inst_pointer += 4

            elif (opcode == 2):
                # OpCode = 2: (param_a * param_b => param_c)
                if (param_modes[0] == ParameterMode.POSITION):
                    param_a_loc = self.memory[inst_pointer + 1]
                    param_a = self.memory[param_a_loc]
                elif (param_modes[0] == ParameterMode.IMMEDIATE):
                    param_a = self.memory[inst_pointer + 1]

                if (param_modes[1] == ParameterMode.POSITION):
                    param_b_loc = self.memory[inst_pointer + 2]
                    param_b = self.memory[param_b_loc]
                elif (param_modes[1] == ParameterMode.IMMEDIATE):
                    param_b = self.memory[inst_pointer + 2]

                if (param_modes[2] == ParameterMode.POSITION):
                    param_c = self.memory[inst_pointer + 3]
                elif (param_modes[2] == ParameterMode.IMMEDIATE):
                    param_c = inst_pointer + 3

                self.memory[param_c] = param_a * param_b
                inst_pointer += 4
                
            elif (opcode == 3):
                # OpCode = 3: save param_a to input_location
                if (param_modes[0] == ParameterMode.POSITION):
                    param_a = self.memory[inst_pointer + 1]
                elif (param_modes[0] == ParameterMode.IMMEDIATE):
                    param_a = inst_pointer + 1
        
                # input_param = input("Please provide input:")
                # input_int = int(input_param)
                if (self.phase_or_input == 'PHASE'):
                    next_input = self.phase_setting
                    self.phase_or_input = 'INPUT'
                else:
                    next_input = self.input_param
                    self.phase_or_input = 'PHASE'
                print("using input value =", next_input)
                self.memory[param_a] = next_input

                inst_pointer += 2

            elif (opcode == 4):
                # OpCode = 4: output param_a
                if (param_modes[0] == ParameterMode.POSITION):
                    param_a_loc = self.memory[inst_pointer + 1]
                    param_a = self.memory[param_a_loc]
                elif (param_modes[0] == ParameterMode.IMMEDIATE):
                    param_a = self.memory[inst_pointer + 1]
                else:
                    print("Bad ParameterMode for opcode = 4")

                print("DIAGNOSTIC PRINT MESSAGE 8=============>", param_a)
                output = param_a
                inst_pointer += 2
            
            elif (opcode == 5):
                # OpCode = 5: if param_a != 0 jump inst_pointer to param_b
                if (param_modes[0] == ParameterMode.POSITION):
                    param_a_loc = self.memory[inst_pointer + 1]
                    param_a = self.memory[param_a_loc]
                elif (param_modes[0] == ParameterMode.IMMEDIATE):
                    param_a = self.memory[inst_pointer + 1]

                if (param_modes[1] == ParameterMode.POSITION):
                    param_b_loc = self.memory[inst_pointer + 2]
                    param_b = self.memory[param_b_loc]
                elif (param_modes[1] == ParameterMode.IMMEDIATE):
                    param_b = self.memory[inst_pointer + 2]

                if (param_a != 0):
                    inst_pointer = param_b
                else:
                    inst_pointer += 3

            elif (opcode == 6):
                # OpCode = 6: if param_a == 0 jump inst_pointer to param_b
                if (param_modes[0] == ParameterMode.POSITION):
                    param_a_loc = self.memory[inst_pointer + 1]
                    param_a = self.memory[param_a_loc]
                elif (param_modes[0] == ParameterMode.IMMEDIATE):
                    param_a = self.memory[inst_pointer + 1]

                if (param_modes[1] == ParameterMode.POSITION):
                    param_b_loc = self.memory[inst_pointer + 2]
                    param_b = self.memory[param_b_loc]
                elif (param_modes[1] == ParameterMode.IMMEDIATE):
                    param_b = self.memory[inst_pointer + 2]

                if (param_a == 0):
                    inst_pointer = param_b
                else:
                    inst_pointer += 3

            elif (opcode == 7):
                # OpCode = 7: if param_a <  0 param_b store 1 in param_c
                if (param_modes[0] == ParameterMode.POSITION):
                    param_a_loc = self.memory[inst_pointer + 1]
                    param_a = self.memory[param_a_loc]
                elif (param_modes[0] == ParameterMode.IMMEDIATE):
                    param_a = self.memory[inst_pointer + 1]

                if (param_modes[1] == ParameterMode.POSITION):
                    param_b_loc = self.memory[inst_pointer + 2]
                    param_b = self.memory[param_b_loc]
                elif (param_modes[1] == ParameterMode.IMMEDIATE):
                    param_b = self.memory[inst_pointer + 2]

                if (param_modes[2] == ParameterMode.POSITION):
                    param_c = self.memory[inst_pointer + 3]
                elif (param_modes[2] == ParameterMode.IMMEDIATE):
                    param_c = inst_pointer + 3

                if (param_a < param_b):
                    self.memory[param_c] = 1
                else:
                    self.memory[param_c] = 0

                inst_pointer += 4
            
            elif (opcode == 8):
                # OpCode = 7: if param_a <  0 param_b store 1 in param_c
                if (param_modes[0] == ParameterMode.POSITION):
                    param_a_loc = self.memory[inst_pointer + 1]
                    param_a = self.memory[param_a_loc]
                elif (param_modes[0] == ParameterMode.IMMEDIATE):
                    param_a = self.memory[inst_pointer + 1]

                if (param_modes[1] == ParameterMode.POSITION):
                    param_b_loc = self.memory[inst_pointer + 2]
                    param_b = self.memory[param_b_loc]
                elif (param_modes[1] == ParameterMode.IMMEDIATE):
                    param_b = self.memory[inst_pointer + 2]

                if (param_modes[2] == ParameterMode.POSITION):
                    param_c = self.memory[inst_pointer + 3]
                elif (param_modes[2] == ParameterMode.IMMEDIATE):
                    param_c = inst_pointer + 3

                if (param_a == param_b):
                    self.memory[param_c] = 1
                else:
                    self.memory[param_c] = 0

                inst_pointer += 4

            else:
                # Bad opcode, do something
                print("Probably bad opcode:", opcode)

            inst = self.memory[inst_pointer]
            opcode, param_modes = self.decode_instruction(inst)

        return output


    def decode_instruction(self, inst):
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