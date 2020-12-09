import re

def make_list_of_dictionaries(data):
    list_of_dictionaries = []
    
    for passport in data:
        attributes = passport.split()
        # print(attributes)
        dictionary = {}
        for att in attributes:
            key, value = att.split(":")
            dictionary[key] = value 
            

        list_of_dictionaries.append(dictionary)
    return list_of_dictionaries
        

def read_file():
    my_file = open('data.txt', 'r')
    data = my_file.read().split("\n\n")
    my_file.close()
    return data


def check_birth_year(birth_year):
    return int(birth_year) >= 1920 and int(birth_year) <= 2002

def check_issue_year(issue_year):
    return int(issue_year) >= 2010 and int(issue_year) <= 2020

def check_expiration_year(expiration_year):
    return int(expiration_year) >= 2020 and int(expiration_year) <= 2030

def check_height(height):
    valid = False
    number = ""
    # Literally everywhere else 
    if re.findall(r"cm\b", height):
        for i in height:
            if i.isdigit():
                number += i
        if int(number) >= 150 and int(number) <= 193:
            return True

    # US measurement 
    if re.findall(r"in\b", height):
        for i in height:
            if i.isdigit():
                number += i
        if int(number) >= 59 and int(number) <= 76:
            return True

    return valid 

def check_hair_color(hair_color):
    return re.findall(r"^\#[0-9a-f]{6}$", hair_color) 

def check_eye_color(eye_color):
    valid = False
    options = ["amb","blu", "brn", "gry", "grn", "hzl", "oth"]
    for  color in options:
        if eye_color == color:
            return True
    return valid 

def check_passport_id(passport_id):
    return re.findall(r"^[0-9]{9}$", passport_id)


def passport_validator(passport):

    valid = 0
    if check_birth_year(passport["byr"]):
        valid += 1
    if check_issue_year(passport["iyr"]):
        valid += 1
    if check_expiration_year(passport["eyr"]):
        valid += 1
    if check_height(passport["hgt"]):
        valid += 1
    if check_hair_color(passport["hcl"]):
        valid += 1
    if check_eye_color(passport["ecl"]):
        valid += 1
    if check_passport_id(passport["pid"]):
        valid += 1

    print(valid)
    return valid == 7 # only true if all are valid 


def count_legit_passports(list_of_dictionaries):
    count = 0
    # print(len(list_of_dictionaries))
    for passport in list_of_dictionaries:
        # print(len(passport))
        # print(passport)
        # print("\n")
        if len(passport) < 7:
            # print("Less 7 credentials")
            continue # we need at least 7 of the credentials 
        elif len(passport) == 7: 
            if "cid" in passport.keys():
                continue
            else:
                # TODO check each credentials validity 
                if passport_validator(passport):
                    count += 1
                              
        else:
            # TODO check each credentials validity 
            if passport_validator(passport):
                    count += 1
                  
    
    return count


def main():
    # print("hello world")
    data = read_file()
    list_of_dictionaries = make_list_of_dictionaries(data)
    count = count_legit_passports(list_of_dictionaries)
    print(f"Number of valid passports part 2: {count}")
    




if __name__ == "__main__":
    main()