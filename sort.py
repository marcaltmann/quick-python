# Custom sort
def compare_num_of_chars(str):
    return len(str)

word_list = ['Python', 'is', 'better', 'than', 'C']

word_list.sort()
print(word_list)

word_list.sort(reverse=True)
print(word_list)

word_list.sort(key=compare_num_of_chars)
print(word_list)

def compare_lists(sublist):
    return sublist[1]

list_list = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]

list_list.sort(key=compare_lists)

print(list_list)
