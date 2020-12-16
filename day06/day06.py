# author Trevik Peterson
# The second part of this program really threw me for a ringer
# check out my code at my github /Launchpaddy/AdventOfCode/day06
def read_data(): 
    my_file = open('data.txt', 'r')
    data = my_file.read().split("\n\n")
    my_file.close()
    return data

def remove_new_line(data):
    new_data = []
    for string in data:
        new_string = string.replace("\n", "")
        new_data.append(new_string)

    return new_data


def count_unique_chars(data):
    letter_set = set(())
    for i in range(len(data)):
        letter_set.add(data[i])
        # print(data[i])

    return len(letter_set)


def count_answers(data):
    list_of_right_answers = []

    for string in data: 
        list_of_right_answers.append(count_unique_chars(string))
    return list_of_right_answers

def sum_right_answers(data):
    answer = 0
    for number in data:
        answer += int(number)
    return answer



def only_duplicates(line_one, line_two):
    duplicates = ""
    for i in range(len(line_one)):
        for j in range(len(line_two)):
            if line_one[i] == line_two[j]:
                duplicates += line_one[i]
    return duplicates



def list_of_repeats_in_groups(group_data):
    line_one = ""
    line_two = ""
    repeats = ""
    list_of_right_answers = []
    
   
    for group in group_data:
            
        if len(group) > 1:
            for i in range(len(group) - 1) :
                if i == 0:
                    line_one = group[i]
                    line_two = group[i + 1]
                else:
                    line_one = only_duplicates(line_one, line_two)
                    line_two = group[i + 1]

                if i == (len(group) - 2): #last line in our group 
                    repeats = only_duplicates(line_one, line_two)
                    list_of_right_answers.append(repeats)
                        # print(repeats)

        else:
            repeats = group[0]
            list_of_right_answers.append(repeats)

    

    return list_of_right_answers

def main():
    data = read_data()
    group_data = []
    for group in data:
        group_data.append(group.split("\n"))
    

    list_of_matches = list_of_repeats_in_groups(group_data)

    # print(group_data)

    data = remove_new_line(data)
    list_of_right_answers_part_one = count_answers(data)
    list_of_right_answers_part_two = count_answers(list_of_matches)

    total_right_answers_part_one = sum_right_answers(list_of_right_answers_part_one)
    total_right_answers_part_two = sum_right_answers(list_of_right_answers_part_two)

    print(f"Right answers part one: {total_right_answers_part_one}")
    print(f"Right answers part two: {total_right_answers_part_two}") #3350 is to low


if __name__ == "__main__":
    main()