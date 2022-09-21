word_dict = { 'this': 11, 'at': 9, 'here': 5, 'why': 12, 'is': 2 }
# Sort Dictionary by value in descending order using lambda function
sorted_dict = dict( sorted(word_dict.items(),
                        key=lambda item: item[1],
                        reverse=True))
print(sorted_dict)