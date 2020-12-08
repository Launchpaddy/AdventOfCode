def read_data() :
    my_file = open('data.txt', 'r')
    data = my_file.read().split("\n")
    my_file.close()
    return data

def check_length(password):
    return int(password[1]) <= len(password[3])

def split_data(data):
    clean_data = []
    for line in data:
        min, left_overs = line.split("-")
        max, letter, string = left_overs.split(" ")
        letter = letter.strip(":")
        clean_data.append([min, max, letter, string]) 
    return clean_data

""" RULES 
    min    = [0]
    max    = [1]
    letter = [2]
    string = [3]
    letter must apear in string at least min but not excede max in string
    """
def count_correct_passwords_first(clean_data):
    correct_passwords = 0
    for password in clean_data:
        count = password[3].count(password[2])
        # print(count)
        if count >= int(password[0]) and count <= int(password[1]):
            correct_passwords += 1
    return correct_passwords


""" RULES
    first   = [0]
    seccond = [1]
    letter  = [2]
    string  = [3]
    letter must appear in string at index (first) xor (second)
    Note: index starts at 1 and not 0
    """
def count_correct_passwords_second(clean_data):
    correct_passwords = 0
    for password in clean_data:
        letter = password[2]
        first  = int(password[0]) - 1
        second = int(password[1]) - 1
        if check_length(password):
            if (password[3][first] == letter) ^  (password[3][second] == letter):
                correct_passwords += 1
        else:
            continue

    return correct_passwords



def main():
    data = read_data()
    clean_data = split_data(data)
    print("part one: ",count_correct_passwords_first(clean_data))
    print("part two: ",count_correct_passwords_second(clean_data))


if __name__ == "__main__":
    main()