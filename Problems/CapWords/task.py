initial_string = input()
list_from_string = initial_string.split("_")
formatted_list = []
for elem in list_from_string:
    formatted_list.append(elem.capitalize())
string_from_list = "".join(formatted_list)
print(string_from_list)
