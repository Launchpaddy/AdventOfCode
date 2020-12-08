""" OPEN 
    Open our text file and save it into a list of strings
"""
def open_file() :
    my_file = open('data.txt', 'r')
    data = my_file.read().split("\n")
    # print(data)
    my_file.close()
    return data

""" RETURN PRODUCT OF 2 NUMBERS THAT EQUAL OUR SUM
    loop through our list over each instance untill we 
    find our numbers that equal our sum and then return the 
    product
"""
def product_of_two_sum(data, sum):
    product = -1
    for num_1 in data:
        for num_2 in data:
            if int(num_1) + int(num_2) == sum:
                product = int(num_1) * int(num_2)

    return product

""" RETURN PRODUCT OF 3 NUMBERS THAT EQUAL OUR SUM
"""
def product_of_three_sum(data, sum):
    product = -1
    for num_1 in data:
        for num_2 in data:
            for num_3 in data:
                if int(num_1) + int(num_2) + int(num_3) == sum:
                    product = int(num_1) * int(num_2) * int(num_3)

    return product

""" MAIN 
    get the data from our file day01Data.txt
    call our function with the data and the goal sum
"""
def main():
    data = open_file()
    print("product of 2 sums:", product_of_two_sum(data, 2020))
    print("product of 3 sums:", product_of_three_sum(data, 2020))


if __name__ == "__main__":
    main()