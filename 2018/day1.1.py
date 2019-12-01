# Advent of Code 2018, Day 1, Part 1

def main():
    frequency = 0

    filename = 'day1_input.txt'

    with open(filename) as f:
        for line in f:
            if line[0] == '+':
                frequency += int(line[1:])
            else:
                frequency -= int(line[1:])
    
    print(frequency)

main()