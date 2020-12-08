# open the file 
def open_data():
    my_file = open('data.txt', 'r')
    data = my_file.read().split("\n")
    my_file.close()
    return data

# lenght of a row of data ( assuming all the rows are the same length)
def data_width(data):
    return len(data[0])


""" skips a row if we are not on the (n)th iteration """
def skip_row(times_called, down_slope):
    if times_called % down_slope == 0:
        return False
    else: 
        return True
    
""" HASH Counter
    input: 
        List of data
        Len of a data row
        Right slope integer
        Down slope integer

    output:
        the number of occurences of "#" in the data on the path of the slope from top left 
        to bottow 
"""
def hash_count_on_slope(data, repeat_len, right_slope, down_slope):
    count = 0
    times_called_skip_row = -1
    iterator = 0

    for row in data:
        times_called_skip_row += 1
        # skip row if we arn't on the slope we want
        if down_slope > 1 and skip_row(times_called_skip_row, down_slope):
            continue
            
        

        if row[iterator] == "#":
            count += 1
        # move the iterate to the right the distance of the run but loop at the lenght of the row
        iterator = (iterator + right_slope) % repeat_len

    
    return count

""" MAIN 
    open our file, find out how long each line is.

    First challenge with slope down 1 right 3

    Second challenge is a  product of the numbers returned by various slopes 
"""
def main():
    data = open_data()
    repeat_len = data_width(data)
    right_slope = 3
    down_slope = 1

    count = hash_count_on_slope(data, repeat_len, right_slope, down_slope)
    print("Challenge one: ",  count)

    r1d1 = hash_count_on_slope(data, repeat_len, 1, 1)
    r3d1 = hash_count_on_slope(data, repeat_len, 3, 1)
    r5d1 = hash_count_on_slope(data, repeat_len, 5, 1)
    r7d1 = hash_count_on_slope(data, repeat_len, 7, 1)
    r1d2 = hash_count_on_slope(data, repeat_len, 1, 2)
    # print("test", hash_count_on_slope(data, repeat_len, 1, 4))
    print("Challenge two: ", r1d1 * r3d1 * r5d1 * r7d1 * r1d2)


if __name__ == "__main__":
    main()