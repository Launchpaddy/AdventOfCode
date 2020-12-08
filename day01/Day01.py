""" OPEN 
    Open our text file and save it into a list of strings
"""
def openFile() :
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
def productOfTwoSum(data, sum):
    product = -1
    for num_1 in data:
        for num_2 in data:
            if int(num_1) + int(num_2) == sum:
                product = int(num_1) * int(num_2)

    return product

""" RETURN PRODUCT OF 3 NUMBERS THAT EQUAL OUR SUM
"""
def productOfThreeSum(data, sum):
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
    data = openFile()
    print("product of 2 sums:", productOfTwoSum(data, 2020))
    print("product of 3 sums:", productOfThreeSum(data, 2020))


if __name__ == "__main__":
    main()