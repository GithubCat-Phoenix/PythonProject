
list_1 = []
first = "a"
second = "a"
third = "a"
forth = "a"

first_num = ord("a")
second_num = ord("a")
third_num = ord("a")
forth_num = ord("a")

string_list = first
if len(string_list) == 1:
    string_list = first
if len(string_list) == 2:
    string_list = first + second
if len(string_list) == 3:
    string_list = first + second + third
if len(string_list) == 4:
    string_list = first + second + third + forth


list_1.append(string_list)



find_type = input("")
find_num = list_1.index(find_type)
print(find_num)