# Advent of Code 2019 Day 1 Part 1

def main():
    mass_list = read_input_file_to_list('input_1.txt')
    total_fuel = sum_all_fuels(mass_list)
    print(total_fuel)
    
def sum_all_fuels(mass_list):
    total_fuel = 0

    for mass in mass_list:
        total_fuel += calculate_fuel(mass)
    
    return total_fuel

def calculate_fuel(mass):
    fuel_needed = (mass // 3) - 2
    return fuel_needed

def read_input_file_to_list(input):
    input_list = []
    with open(input) as file:
        for line in file:
            input_list.append(int(line))
    return input_list

if __name__ == '__main__':
    main()