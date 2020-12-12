import re
import math


def read_data(): 
    my_file = open('data.txt', 'r')
    data = my_file.read().split("\n")
    my_file.close()
    return data


def find_rows_and_columns(data):
    row_col_list = []
    
    for seat in data:
        
        row_variable = ""
        col_variable = ""
        for i in range(0,len(seat)):
            if i < 7:  # get the first 7 characters: row
                row_variable += seat[i]
            else: # get last 3 characters: column 
                col_variable += seat[i]
        
        row_col_list.append([row_variable, col_variable])
        
    # print(row_col_list)
    return row_col_list


# B upper half F == lower half
def number_finder(code, size):
    
    last_is_B = False
    top = size
    bottom = 0
    for i in range(0, len(code)):
        if code[i] == "B" or code[i] == "R":
            if i == len(code):
                last_is_B = True
            bottom = math.floor((top + bottom) / 2)
        elif code[i] == "F" or code[i] == "L":
            top = math.floor((top + bottom) / 2)
        else:
           next #TODO 

    if last_is_B:
        return top
    else:
        return bottom

    
# returns a list of row col's in base 10
def base_ten_row_col(row_col_bi_list):
    row_col_base_ten_list = []
    for seat in row_col_bi_list:
        row = number_finder(seat[0], 128)
        col = number_finder(seat[1], 8)
        row_col_base_ten_list.append([row, col])
    return row_col_base_ten_list


def create_ordered_list(unordered_list):
    ordered_list = unordered_list.sort()
    # print(ordered_list)
    return ordered_list

def largest_seat_id(row_col_base_ten_list):
    largest_product = 0
    id_list = []
    for seat in row_col_base_ten_list:
        id_list.append((seat[0] * 8) + seat[1])
        if largest_product < (seat[0] * 8) + seat[1]:
            largest_product = (seat[0] * 8) + seat[1]

    id_list.sort()
    print(id_list)
    # print(create_ordered_list(id_list))
    return largest_product



# 128 rows 8 columns (0-127, 0-7)
def main():
    data = read_data()
    row_col_bi_list = find_rows_and_columns(data)
    row_col_base_ten_list = base_ten_row_col(row_col_bi_list)
    print(largest_seat_id(row_col_base_ten_list))
    # number with 128 and 8 == 806 


if __name__ == "__main__":
    main()