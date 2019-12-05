# Advent of Code 2019 Day 4 Part 1

def main():
    pass_list = create_potential_password_list()
    num_potential_pass = parse_password_list(pass_list)
    print(num_potential_pass)

def parse_password_list(password_list):
    potential_passwords = 0
    for password in password_list:
        if (is_valid(password)):
            potential_passwords += 1
    
    return potential_passwords

def is_valid(password):
    recurring_char = False
    not_decreasing = True

    if (len(password) != 6):
        return False

    prev_char = password[0]
    for i in range(1, len(password)):
        if (prev_char == password[i]):
            recurring_char = True
        if (int(prev_char) > int(password[i])):
            not_decreasing = False
        prev_char = password[i]

    return (recurring_char and not_decreasing)

def create_potential_password_list():
    pass_list = []
    lower_bound = 138241
    upper_bound = 674034

    for i in range(lower_bound, upper_bound + 1):
        pass_list.append(str(i))

    return pass_list

if __name__ == "__main__":
    main()
