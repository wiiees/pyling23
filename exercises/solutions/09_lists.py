# Solutions for 09_lists.md



# 9.1
print('~ ~ ~ ~ ~ ~ ~ 9.1 ~ ~ ~ ~ ~ ~')

names = ['Alf', 'Beth', 'Chris', 'Dave', 'Esra']
print(type(names))


# 9.2
print('~ ~ ~ ~ ~ ~ ~ 9.2 ~ ~ ~ ~ ~ ~')

list_of_numbers = [1, 2, 3, 4, 5, 6]
list_of_strings = ['abc', 'def', 'ghi']
list_of_both = [1, 'def', 3, 'ghi', 5]
empty_list = []

print(type(list_of_numbers), type(list_of_strings), type(list_of_both), type(empty_list))


# 9.3
print('~ ~ ~ ~ ~ ~ ~ 9.3 ~ ~ ~ ~ ~ ~')

# Try these yourself.


# 9.4
print('~ ~ ~ ~ ~ ~ ~ 9.4 ~ ~ ~ ~ ~ ~')

nested_list = [[1, 2, 3], [4, 5, 6]]
deeper_nested_list = [[[9, 8], [7, 6]], [[5, 4], [3, 2]]] 


# 9.5
print('~ ~ ~ ~ ~ ~ ~ 9.5 ~ ~ ~ ~ ~ ~')

print(names[1])
print(names[2])
# print(names[8])   # error
print(names[-1])
print(names[-2])
print(names[1:3])
print(names[2:2])
print(names[-2:])
print(names[2:])
print(names[:2])
print(names[0])
print(names[2-4])
print(names[3-2])
print(names[1+1])


# 9.6
print('~ ~ ~ ~ ~ ~ ~ 9.6 ~ ~ ~ ~ ~ ~')

print(len(names))
print(len(empty_list))


# 9.7
print('~ ~ ~ ~ ~ ~ ~ 9.7 ~ ~ ~ ~ ~ ~')

# len(names) is always one greater than the last index of the list: 
# because indices start at 0 , not 1, the last index is len(names)-1.


# 9.8
print('~ ~ ~ ~ ~ ~ ~ 9.8 ~ ~ ~ ~ ~ ~')

print(names[::2])
print(names[1::2])
print(names[::-1])


# 9.9
print('~ ~ ~ ~ ~ ~ ~ 9.9 ~ ~ ~ ~ ~ ~')

print(names)


# 9.10
print('~ ~ ~ ~ ~ ~ ~ 9.10 ~ ~ ~ ~ ~ ~')

print(max(list_of_numbers))
print(max(list_of_strings))
# print(max(list_of_both))  # error, cannot compare int to str!


# 9.11
print('~ ~ ~ ~ ~ ~ ~ 9.11 ~ ~ ~ ~ ~ ~')

print('Alf' in names)
print('Alwyn' in names)
print('Alwyn' not in names)
print('alf' in names)   # yep, it is
print('A' in names) # nope, it doesn't


# 9.12
print('~ ~ ~ ~ ~ ~ ~ 9.12 ~ ~ ~ ~ ~ ~')

print('bcd' in 'abcdef')    # indeed
print([2, 3, 4] in [1, 2, 3, 4, 5, 6])  # nope, only checks for single elements


# 9.13
print('~ ~ ~ ~ ~ ~ ~ 9.13 ~ ~ ~ ~ ~ ~')

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[2][1])


# 9.14
print('~ ~ ~ ~ ~ ~ ~ 9.14 ~ ~ ~ ~ ~ ~')

print(nested_list[-1][-1])
print(nested_list[1:3][1])  # hmmm...


# 9.15
print('~ ~ ~ ~ ~ ~ ~ 9.15 ~ ~ ~ ~ ~ ~')

print([0, 1, 2, 3][[3, 2, 1, 0][2]])
print([0, 1, 2, 3][1:][2])


# 9.16
print('~ ~ ~ ~ ~ ~ ~ 9.16 ~ ~ ~ ~ ~ ~')

print([1, 2, 3, 4] + [5, 6, 7])
print([1, 2, 3, 4] * 3)


# 9.17
print('~ ~ ~ ~ ~ ~ ~ 9.17 ~ ~ ~ ~ ~ ~')

names[3] = 'Nick'

print(names)    # yep!


# 9.18
print('~ ~ ~ ~ ~ ~ ~ 9.18 ~ ~ ~ ~ ~ ~')

names[-1] = 'Suzy'
names[0] = 'Bob'

# names[len(names)] = 'Test'  # nope!


# 9.19
print('~ ~ ~ ~ ~ ~ ~ 9.19 ~ ~ ~ ~ ~ ~')

names.append('Matt')
names.append('Mary')
print(len(names))


# 9.20
print('~ ~ ~ ~ ~ ~ ~ 9.20 ~ ~ ~ ~ ~ ~')

my_list = []
my_list.append('a')
my_list.append(10)
print(my_list)


# 9.21
print('~ ~ ~ ~ ~ ~ ~ 9.21 ~ ~ ~ ~ ~ ~')

my_list.append('a')
print(my_list)
print([1, 2, 3, 3, 3, 4, 5, 3, 3, 4, 5, 6, 7, 8])
# Nothing spectacular happens; lists can contain duplicates


# 9.24
print('~ ~ ~ ~ ~ ~ ~ 9.24 ~ ~ ~ ~ ~ ~')

my_string = 'abcde'
# my_string[3] = 'x'  # Nope! Strings are immutable.


# 9.25
print('~ ~ ~ ~ ~ ~ ~ 9.25 ~ ~ ~ ~ ~ ~')

# The int and string variables are changed by reassigning something to it; but the variable list1 is never re-assigned; something is appended to the list, changing the list itself.
# Because variables are re-assigned independently (see section 2), only in the latter case does list2 update along with list1, because they reference the same object that is being changed.


# 9.26
print('~ ~ ~ ~ ~ ~ ~ 9.26 ~ ~ ~ ~ ~ ~')

# my_string.append('y') # Nope, and for the same reason.


# 9.27
print('~ ~ ~ ~ ~ ~ ~ 9.27 ~ ~ ~ ~ ~ ~')

# In the code from the exercise, x is being reassigned a new string (created by .upper()), so it does NOT show that strings are mutable (because they aren't).


# 9.28
print('~ ~ ~ ~ ~ ~ ~ 9.28 ~ ~ ~ ~ ~ ~')

a = [1, 2, 3, 4, 5, 6]
a = a.append(7)
print(a)    # this is now None, because the append method modifies a in place, returning nothing, and that 'nothing' is then reassigned to a.


# 9.29
print('~ ~ ~ ~ ~ ~ ~ 9.29 ~ ~ ~ ~ ~ ~')

# basic_list = [1, 2, 3]
# basic_list = basic_list + 4  # error
# print(basic_list)

basic_list = [1, 2, 3]
basic_list.append(4)
print(basic_list)

basic_list = [1, 2, 3]
basic_list += [4]
print(basic_list)

basic_list = [1, 2, 3]
basic_list.append([4])
print(basic_list)   # hmmm



# 9.30
print('~ ~ ~ ~ ~ ~ ~ 9.30 ~ ~ ~ ~ ~ ~')

my_list = ['a', 'b', 'c', 'd']
my_list2 = my_list[:]
my_list2[2] = 'xxxxx'
print(my_list, my_list2)    # this shows that [:] creates a NEW list containing the same old elements.


# 9.31
print('~ ~ ~ ~ ~ ~ ~ 9.31 ~ ~ ~ ~ ~ ~')

row = [''] * 3
board = [row] * 3

def print_board(board):
    """
    Prints a 3x3 board in a more readable way, by printing each row of the board
    on a separate line. Also some horizontal lines.
    """
    print('  -----------')
    print(board[0])
    print(board[1])
    print(board[2])
    print('  -----------')

print_board(board)
board[1][1] = 'x'
print_board(board)  # the outer list refers to the same 'row' list three times, and modifying it
                    # will change all three occurrences.

better_board = [[''] * 3, [''] * 3, [''] * 3]
better_board[1][1] = 'x'
print_board(better_board)   # Now I can no longer cheat


# 9.32
print('~ ~ ~ ~ ~ ~ ~ 9.32 ~ ~ ~ ~ ~ ~')

# See 9.33


# 9.33
print('~ ~ ~ ~ ~ ~ ~ 9.33 ~ ~ ~ ~ ~ ~')

def swap_first_and_last(l, inplace):
    """
    Swaps first and last element of a list (or string), depending on the 'inplace' parameter either in-place (not returning anything)
    or creating (and returning) a new object.
    """
    if not inplace:
        l = l.copy()
        # the following works, but isn't super readable
        # first = l[0]
        # last = l[-1]
        # l[-1] = first
        # l[0] = last
        # more Pythonic, involving creating (on the right of =) and then unpacking (on the left of =) a 'tuple' (later section):
    l[0], l[-1] = l[-1], l[0]
        # the following also works, but isn't super safe, e.g., error if there's only one element.
        # return [l[-1]] + l[1:-1] + [l[0]]
    if not inplace:
        return l

# Note that we can avoid some repetition (= good!) as follows:
def swap_first_and_last2(l, inplace):
    if not inplace:
        l = l[:]
    l[0], l[-1] = l[-1], l[0]
    if not inplace:
        return l


my_list = [1, 2, 3, 4, 5]
print(my_list)

swap_first_and_last(my_list, False)
print(my_list)  # not changed; because it wasn't changed in-place

my_list = [1, 2, 3, 4, 5]
my_list = swap_first_and_last(my_list, False)
print(my_list)  # yep, now it's changed

my_list = [1, 2, 3, 4, 5]
swap_first_and_last(my_list, True)
print(my_list)  # this works too; changed in place (i.e., it's still the same list object, but reordered)

my_list = [1, 2, 3, 4, 5]
my_new_list = swap_first_and_last(my_list, True)
print(my_new_list)  # Nope, nothing was returned.


# 9.34
print('~ ~ ~ ~ ~ ~ ~ 9.34 ~ ~ ~ ~ ~ ~')

# See 9.36


# 9.35
print('~ ~ ~ ~ ~ ~ ~ 9.35 ~ ~ ~ ~ ~ ~')

# See 9.36


# 9.36
print('~ ~ ~ ~ ~ ~ ~ 9.36 ~ ~ ~ ~ ~ ~')

day_names = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
def day_number_to_name(daynumber):
    """
    Translates a number from 1 to 7 into a day name.
    """
    daynumber -= 1  # fix for our annoying client
    return day_names[daynumber % 7]

print(day_number_to_name(0),
      day_number_to_name(1),
      day_number_to_name(3),
      day_number_to_name(7), sep='\n')
# answer to 7.36: while the list approach is more readable, for this particular fix it doesn't matter much;
# the daynumber -= 1 tweak could be made either way.


# 9.37
print('~ ~ ~ ~ ~ ~ ~ 9.37 ~ ~ ~ ~ ~ ~')

def print_return_day_name(start_day_number, duration_n_nights):
    """
    If you leave on start_day_number, and stay for duration_n_nights, on what day (name) wil you return?
    """
    return_day_number = (start_day_number + duration_n_nights) % 7
    return_day_name = day_number_to_name(return_day_number)
    print('Return day:', return_day_name)

print_return_day_name(3, 137)


# 9.38
print('~ ~ ~ ~ ~ ~ ~ 9.38 ~ ~ ~ ~ ~ ~')

print_return_day_name(3, -7)    # yep!


# 9.39
print('~ ~ ~ ~ ~ ~ ~ 9.39 ~ ~ ~ ~ ~ ~')

# similar, e.g., slicing, len, concatenation.
# different, e.g., mutability (e.g., assignment to index, append), elements of a string are #
# themselves strings while lists are more flexible.


# 9.40
print('~ ~ ~ ~ ~ ~ ~ 9.40 ~ ~ ~ ~ ~ ~')

# Note that one object is a list, and the other object is a string that merely looks like a list.
print(len([1, 2, 3]) == len('[1, 2, 3]'))


# 9.41
print('~ ~ ~ ~ ~ ~ ~ 9.41 ~ ~ ~ ~ ~ ~')

print(str(list('apple')) == 'apple')

# Converting a string to a list, results in a list of all its single character strings.
# Converting a list back to a string does not revert the aforementioned change; rather the result is a string
# matching what it looks like if you were to print a list. (And this makes sense; while one could in principle
# 'convert' a list of strings back to a string by concatenating all characters, this would only work in case
# list elements were themselves strings. Since converting a list to a string ought to work for any sort of list,
# not just lists of strings, that is not how it is defined.)


# 9.42
print('~ ~ ~ ~ ~ ~ ~ 9.42 ~ ~ ~ ~ ~ ~')

# Python permits this; PyCharm will issue a warning (squiggle underneath the variable name).
# it is dangerous to change the meaning of things that everyone assumes they know the meaning of.


# 9.43
print('~ ~ ~ ~ ~ ~ ~ 9.43 ~ ~ ~ ~ ~ ~')

def swapped_list_by_indices(l, i, j):
    """
    Creates a modified copy (i.e., not in-place) of the list l with elements at indices i and j swapped.
    """
    # With some assumptions, e.g., i < j and both are positive, the following works correctly in many cases:
    # return l[:i] + [l[j]] + l[i+1:j] + [l[i]] + l[j+1:]
    # But the following is a bit safer and more readable:
    copy = l[:] # create a copy, let's not modify in-place; perhaps more explicit: l.copy()
    copy[i], copy[j] = copy[j], copy[i]     # using 'tuple' for easy swapping of elements
    return copy

print(swapped_list_by_indices([1, 2, 3, 4], 1, 2))
print(swapped_list_by_indices([1, 2, 3, 4], 2, 1)) # takes i,j in any order
print(swapped_list_by_indices([1, 2, 3, 4], 1, -1))    # even works on negative indices
print(swapped_list_by_indices([1, 2, 3, 4], 1, 1))    # extreme case, also works
# print(swapped_list_by_indices([], 2, 2))    # I'd expect an error here, which indeed we get.


# 9.44
print('~ ~ ~ ~ ~ ~ ~ 9.44 ~ ~ ~ ~ ~ ~')

# For a string, assigning to indices doesn't work, so you would need the commented-out variant in 9.43 above.
# A preferable variant might be to convert to list and back to string, like a 'wrapper' around the above function:
def swapped_str_by_indices(s, i, j):
    """
    Swaps two characters (by indices) in a string s, returning the new string.
    """
    swapped_list = swapped_list_by_indices(list(s), i, j)
    swapped_str = ''.join(swapped_list) # we learn about the join function later
    return swapped_str

print(swapped_str_by_indices('test', 1, 2))


# 9.45
print('~ ~ ~ ~ ~ ~ ~ 9.45 ~ ~ ~ ~ ~ ~')

# construct these lists outside the function for efficiency, in case the function will be called
# a million times in a big corpus.
determiners = ['the', 'a', 'an', 'many', 'some']
lowercased_determiners = [det.lower() for det in determiners]   # just in case our dictionary is not uniform

def is_determiner(word):
    """
    Checks if the word is a determiner, by comparing against a predefined list. Not case-sensitive.
    """
    return word.lower() in lowercased_determiners

print(is_determiner('the'))
print(is_determiner('there'))
print(is_determiner('the man'))
print(is_determiner('The'))
