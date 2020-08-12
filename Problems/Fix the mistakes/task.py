text = input()
words = text.split()
new_list = []
for word in words:
    if "www." in word.lower():
        new_list.append(word)
    elif "https://" in word.lower():
        new_list.append(word)
    elif "http://" in word.lower():
        new_list.append(word)
for element in new_list:
    print(element)
