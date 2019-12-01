# Advent of Code 2018, Day 1, Part 2

def main():
    frequency = 0
    freq_set = set()
    freq_set.add(frequency)

    filename = 'day1_input.txt'

    with open(filename) as f:
        input_lines = f.readlines()
        while True:
            for line in input_lines:
                if line[0] == '+':
                    frequency += int(line[1:])
                else:
                    frequency -= int(line[1:])

                if frequency in freq_set:
                    return frequency
                else:
                    freq_set.add(frequency)

answer = main()
print("Answer =", answer)