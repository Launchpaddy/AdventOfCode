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

def main():
    data = read_data()
    data = remove_new_line(data)
    list_of_right_answers = count_answers(data)
    total_right_answers = sum_right_answers(list_of_right_answers)
    print(total_right_answers)


if __name__ == "__main__":
    main()