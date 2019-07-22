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
