# Solutions for 13_dictionary_basics.md



# 13.1
print('~ ~ ~ ~ ~ ~ ~ 13.1 ~ ~ ~ ~ ~ ~')

name_to_id = {'Alf': '136124', 'Beth': '008623', 'Chris': '014212', 'Dave': '9123785', 'Esra': '978123'}
print(name_to_id)
print(type(name_to_id))


# 13.2
print('~ ~ ~ ~ ~ ~ ~ 13.2 ~ ~ ~ ~ ~ ~')

print(name_to_id['Alf'])
print(name_to_id['Chris'])


# 13.3
print('~ ~ ~ ~ ~ ~ ~ 13.3 ~ ~ ~ ~ ~ ~')

# name_to_id['Bobby']    # KeyError: 'Bobby'
# name_to_id[Alf]         # NameError: Name 'Alf' is not defined
#   Explanation: without the quotation marks it's looking for a variable with that name, instead
#   of treating it as a string. This is not specific to dictionaries of course.


# 13.4
print('~ ~ ~ ~ ~ ~ ~ 13.4 ~ ~ ~ ~ ~ ~')

print(len(name_to_id))
empty_dict = {}
print('Double check:', type(empty_dict))     # yes :)


# 13.5
print('~ ~ ~ ~ ~ ~ ~ 13.5 ~ ~ ~ ~ ~ ~')

print('Value in dict?', '136124' in name_to_id)   # nope, not values.
print('Key in dict?', 'Alf' in name_to_id)   # yes, checks keys.


# 13.6
print('~ ~ ~ ~ ~ ~ ~ 13.6 ~ ~ ~ ~ ~ ~')

# name_to_id[2]    # KeyError: 2, so nope!


# 13.7
print('~ ~ ~ ~ ~ ~ ~ 13.7 ~ ~ ~ ~ ~ ~')

dict_with_integers = {1: 'hi', 2: 'hello', 3: 'bye', 4: 'tata'}
print(dict_with_integers[2])    # this works now, but better say 'key', not 'index', to avoid confusion; lists items are accessed by index, dictionaries values by key.


# 13.8
print('~ ~ ~ ~ ~ ~ ~ 13.8 ~ ~ ~ ~ ~ ~')

# my_dict = {'Alf' = '36124', 'Beth' = '008623'}  # Invalid syntax.
# This typo is easy to make, because associating values with keys is quite similar to assigning values to variables.


# 13.9
print('~ ~ ~ ~ ~ ~ ~ 13.9 ~ ~ ~ ~ ~ ~')

age_to_count = {20: 4, 21: 6, 22: 8, 23: 5, 26: 3}
word_counts = {'the': 100, 'student': 13, 'studies': 3, 'laughs': 5} # completely imaginary counts; it's a weird corpus
course_to_students = {'syntax': ['Alf', 'Beth', 'Gemma'], 'semantics': ['Dale', 'Ebba']}
# list_to_average = {[1, 2, 3]: 2, [3, 4, 5]: 4}  # TypeError: list is an unhashable type; because it is mutable.
#   Dictionary keys need to be hashable.


# 13.10
print('~ ~ ~ ~ ~ ~ ~ 13.10 ~ ~ ~ ~ ~ ~')

test_dict = {1: 'a', 'b': 3.6, 'c': [1, 2, 3], 123: 125}    # yes, all fine!


# 13.11
print('~ ~ ~ ~ ~ ~ ~ 13.11 ~ ~ ~ ~ ~ ~')

# Nope, dictionaries don't support slicing.
# print(name_to_id['Alf':'Dave']) # TypeError: unhashable type: 'slice'
# print(dict_with_integers[2:4]) # TypeError: unhashable type: 'slice'

# What the above error shows, indirectly, is that Python isn't attempting to retrieve individual keys from the slice
# (because those would be hashable). Rather, it attempts look up the entire slice object as a key (which it cannot,
# because it is not 'hashable'). The short answer is: dictionaries don't support slicing.


# 13.12
print('~ ~ ~ ~ ~ ~ ~ 13.12 ~ ~ ~ ~ ~ ~')

# name_to_id['alf']   # KeyError, because dictionary is case-sensitive, as are most/all operations in Python.


# 13.13
print('~ ~ ~ ~ ~ ~ ~ 13.13 ~ ~ ~ ~ ~ ~')

name_to_id['Suzy'] = '124987'       # adds Suzy with her ID to the dictionary
name_to_id['Alf'] = '999999'        # replaces the ID of Alf that was already there
print(name_to_id)

some_dict = {1: 3, 3: 5, 1: 5}
print(some_dict)
# apparently later occurrences of a key in a dictionary definition override earlier occurrences.
# Note that PyCharm (in the editor) gives a warning about the duplicate keys, but Python runs fine.


# 13.14
print('~ ~ ~ ~ ~ ~ ~ 13.14 ~ ~ ~ ~ ~ ~')

del name_to_id['Esra']  # deletes the key-value pair with key 'Esra'.
print(name_to_id)

names = ['Alf', 'Beth', 'Gemma']
del names[1]
print(names)    # yes, works on lists too!

name = 'Alf'
# del name[1]     # doesn't work on strings, because it is immutable.


# 13.15
print('~ ~ ~ ~ ~ ~ ~ 13.15 ~ ~ ~ ~ ~ ~')

name_to_id['Chris'] = '5987162'
del name_to_id['Suzy']
print(name_to_id)


# 13.17
print('~ ~ ~ ~ ~ ~ ~ 13.17 ~ ~ ~ ~ ~ ~')

globals()['y'] = 10
print(y)
# Yes! It shows that plain variable assignment is a shortcut for assigning a value to a key in the globals dictionary
# or (if you're inside a function) the locals dictionary.


# 13.18
print('~ ~ ~ ~ ~ ~ ~ 13.18 ~ ~ ~ ~ ~ ~')

# PyCharm relies on a more shallow parsing for the warnings it shows, auto-completion, and various other helpful
# programming tools. The reason for this shallow parsing is that it would be very inefficient if while you're coding,
# PyCharm is constantly, in the background, telling Python to interpret your code. (More so with larger programs,
# of course, that may do a lot more than merely assign and print some variables.)


# 13.19
print('~ ~ ~ ~ ~ ~ ~ 13.19 ~ ~ ~ ~ ~ ~')

# One should probably use a list instead, of which the constraint 'range of 
# consecutive integers starting at 0' is part of its essence. The datastructure
# you choose should communicate its intended use.


# 13.20
print('~ ~ ~ ~ ~ ~ ~ 13.20 ~ ~ ~ ~ ~ ~')

def count(l):   
    """
    Counts how many times each element occurs in the list, returning a counts dictionary.
    """
    counts = {}
    for element in l:
        if element not in counts:
            counts[element] = 1
        else:
            counts[element] += 1
    return counts

print(count([1, 2, 3, 8, 7, 6, 1, 2, 8, 7, 4]))
print(count('asdhgjbqweoihasdjhvbdaskjasdkujyqwedsa')) # yes!
