# Solutions for 12_more_lists_and_loops.md



# 12.1
print('~ ~ ~ ~ ~ ~ ~ 12.1 ~ ~ ~ ~ ~ ~')

def custom_sum(numbers):
    """
    Returns the sum of all numbers. NOTE: This emulates the built-in function 'sum'.
    """
    result = 0
    for num in numbers:
        result += num
    return result


def average(numbers):
    """
    Returns the average of the list of numbers.
    """
    return sum(numbers) / len(numbers)


import math  # this would normally be at the top of the file


def std(numbers):
    """
    Returns the unbiased sample standard deviation.
    NOTE: the exercise wasn't explicit about which notion of standard deviation to compute; see e.g. Wikipedia.
    Below is not the most efficient possible calculation, for the sake of exposition.
    """
    avg = average(numbers)
    squared_diffs = [(num - avg) ** 2 for num in numbers]  # you can also use a multi-line for-loop of course.
    uncorrected_variance = average(squared_diffs)
    # The uncorrected sample variance is a biased estimate of the true (population) variance; it's a little bit
    # too low: For N items in your sample, it is expected to be a factor 1 / N too low.
    # So we divide it by N-1, and multiply by N, to effectively increase it by a factor 1 / N.
    # This is called Bessel's Correction. See https://en.wikipedia.org/wiki/Bessel's_correction#Source_of_bias
    corrected_variance = uncorrected_variance * len(numbers) / (len(numbers) - 1)
    return math.sqrt(corrected_variance)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(average(numbers), std(numbers))


# 12.2
print('~ ~ ~ ~ ~ ~ ~ 12.2 ~ ~ ~ ~ ~ ~')

# Comparison up to you!


# 12.3
print('~ ~ ~ ~ ~ ~ ~ 12.3 ~ ~ ~ ~ ~ ~')

print(sum([1, 2, 3, 4, 5]))
# print(sum(['a', 'b', 'c'))  # nope, strange hmmm? We're not the only ones to 
#    have noticed: https://stackoverflow.com/questions/3525359/python-sum-why-not-strings
# Use this instead for strings:
print(''.join(['a', 'b', 'c']))

print(sum([True, True, False])) # yep!


# 12.4
print('~ ~ ~ ~ ~ ~ ~ 12.4 ~ ~ ~ ~ ~ ~')

words = ['the', 'dog', 'is', 'in', 'the', 'garden']


def total_word_length(words):
    """
    Returns the total length of all words combined.
    """
    # Let's use the sum builtin with list comprehension.
    # You can also use an explicit for-loop to compute the sum, of course.
    return sum([len(word) for word in words])


print(total_word_length(words))
print(len('the dog is in the garden'))  # this also counts the spaces, hence the difference


# 12.5
print('~ ~ ~ ~ ~ ~ ~ 12.5 ~ ~ ~ ~ ~ ~')

def index_in_string(string, character):
    """
    Returns the first index in the string at which the character occurs.
    Note: this emulates the built-in string method index.
    """
    index = 0
    for char in string:
        if char == character:
            return index
        index += 1
    # note that it returns None if the character does not appear in the string


print(index_in_string('david', 'v'))

# It is the inverse of accessing a character by index, so we can go back and forth:

print('david'[index_in_string('david', 'v')] == 'v')

# going back and forth more slowly:
# index_of_v = index_in_string('david', 'v')
# character_at_index_of_v = 'david'[index_of_v]
# index_of_character_at_index_of_v = index_in_string('david', character_at_index_of_v)
# print(index_of_character_at_index_of_v)


# 12.6
print('~ ~ ~ ~ ~ ~ ~ 12.6 ~ ~ ~ ~ ~ ~')

def index_in_list(l, element):
    """
    Returns the first index in the list at which the element occurs.
    Note: this emulates the built-in list method index.
    """
    return index_in_string(l, element)  # being extremely lazy, it just works already :)


print(index_in_list([1, 2, 3, 4, 5], 3))


# 12.7
print('~ ~ ~ ~ ~ ~ ~ 12.7 ~ ~ ~ ~ ~ ~')

print('david'.index('v'))
print([6, 4, 8, 6].index(8))

print(index_in_string('david', 'x'))  # this returns None


# print('david'.index('x'))   # this gives an error, so they don't quite behave the same.


# 12.10
print('~ ~ ~ ~ ~ ~ ~ 12.10 ~ ~ ~ ~ ~ ~')

def find_index_of_largest(l):
    """
    argmax function; not the most efficient implementation, because it it's (underneath the surface) looping
    through the list twice: once to find the maximum, once to find its index. Better do both at once.
    """
    return l.index(max(l))  # literally, the index of the max :)


print(find_index_of_largest([1, 2, 3, 4, 5, 4, 3, 2]))
print(find_index_of_largest(['a', 'b', 'c', 'b', 'a']))
print(find_index_of_largest('abcba'))


# 12.11
print('~ ~ ~ ~ ~ ~ ~ 12.11 ~ ~ ~ ~ ~ ~')

def list_replace(l, old, new):
    """
    Returns a list that is like l but with all instances of old replaced by new.
    """
    result = []
    for item in l:
        if item == old:
            result.append(new)
        else:
            result.append(item)
    return result

print(list_replace([1, 2, 3, 4, 5, 6], 3, 0))


# 12.12
print('~ ~ ~ ~ ~ ~ ~ 12.12 ~ ~ ~ ~ ~ ~')

# Yes, you could. For strings it wouldn't work though, because strings are not mutable.


# 12.13
print('~ ~ ~ ~ ~ ~ ~ 12.13 ~ ~ ~ ~ ~ ~')

# The string method capitalize returns a new string, it does not change the original string (which is immutable, after
# all).


# 12.14
print('~ ~ ~ ~ ~ ~ ~ 12.14 ~ ~ ~ ~ ~ ~')

# Still doesn't change the list. Recall from section 2 that variables are assigned independently. Thus, assigning
# the new, capitalized string to the variable city DOESN'T automatically assign it to the corresponding
# index in the original list.


# 12.15
print('~ ~ ~ ~ ~ ~ ~ 12.15 ~ ~ ~ ~ ~ ~')

# It's fairly easy to create a new list with the required properties; leaving this up to you. To actually change the 
# list in-place, you need to reassign something to the list index, hence you need to loop over list indices. 
# Later we will learn about using 'range' for this. Without 'range', you might come up with the following:
cities = ['amsterdam', 'rotterdam', 'leiden', 'gouda', 'eindhoven']
index = 0
for city in cities:
    cities[index] = city.capitalize()
    index += 1

print(cities)


# 12.16
print('~ ~ ~ ~ ~ ~ ~ 12.16 ~ ~ ~ ~ ~ ~')

# Firstly, one is a function, the other a list method.
print(sorted(cities))
print(cities)   # It has not been changed, so apparently sorted makes a sorted copy.
print(cities.sort())    # Apparently list.sort doesn't return anything, so it probably...
print(cities)   # ...changes the list in-place!


# 12.17
print('~ ~ ~ ~ ~ ~ ~ 12.17 ~ ~ ~ ~ ~ ~')

# 'kjhasd'.sort()  # nope, because strings are not mutable, hence cannot be 
# modified in place; but sorted makes a modified copy, so sure, why not:
print(sorted('vgjhbkadfsosda'))


# 12.18
print('~ ~ ~ ~ ~ ~ ~ 12.18 ~ ~ ~ ~ ~ ~')

print([1, 2, 3, 4, 5, 6, 1, 2, 3, 1, 2, 4, 5, 6, 1].count(2))
print('abcabc'.count('a'))  # yes!


# 12.19
print('~ ~ ~ ~ ~ ~ ~ 12.19 ~ ~ ~ ~ ~ ~')

# Problem: count only checks for exactly that element, so it counts the number 
# of times the full substring 'aeiou' occurs.
# To fix it one could do text.count('a') + text.count('e') + text.count('i') etc...
# Or with a loop:
def count_vowels(text):
    count = 0
    for char in text:   # Probably .lower() would be desirable here too.
        if char in 'aeiou':
            count += 1
    return count


# 12.20
print('~ ~ ~ ~ ~ ~ ~ 12.20 ~ ~ ~ ~ ~ ~')

for city1 in cities:
    for city2 in cities:
        print(city1 + '-' + city2)


# 12.21
print('~ ~ ~ ~ ~ ~ ~ 12.21 ~ ~ ~ ~ ~ ~')

for city in cities:
    for city in cities:
        print(city)


# 12.22
print('~ ~ ~ ~ ~ ~ ~ 12.22 ~ ~ ~ ~ ~ ~')

for city1 in cities:
    # Note: you can put the first if-condition over here, so that the second loop
    # doesn't even begin if the first city doesn't start with a vowel. That would be more efficient
    # (in case you have many cities), but arguably a bit less readable.
    for city2 in cities:
        if city1[0].lower() in 'aeoui' and city2[0].lower() not in 'aeiou':
            print(city1, city2)


# 12.23
print('~ ~ ~ ~ ~ ~ ~ 12.23 ~ ~ ~ ~ ~ ~')

def chain(list_of_lists):
    """
    Takes a list of lists and chains them together, returning a single 'flattened' list.
    """
    result = []
    for inner_list in list_of_lists:
        for element in inner_list:
            result.append(element)
    return result

print(chain([[1, 2], [3, 4, 5], [6, 7]]))


# 12.26
print('~ ~ ~ ~ ~ ~ ~ 12.26 ~ ~ ~ ~ ~ ~')

directions = ['N', 'E', 'S', 'W']

def turn_clockwise(start_direction):
    """
    Takes a string representation of a direction (NESW) and returns the new direction after
    turning one 'step' clockwise.
    """
    index = directions.index(start_direction)
    turned_index = (index + 1) % len(directions)
    return directions[turned_index]

print(turn_clockwise('W'))
print(turn_clockwise('N'))


# 12.27
print('~ ~ ~ ~ ~ ~ ~ 12.27 ~ ~ ~ ~ ~ ~')

# One is the type of the function itself, the other is the type of the result of calling the function.


# 12.28
print('~ ~ ~ ~ ~ ~ ~ 12.28 ~ ~ ~ ~ ~ ~')

def turn_counterclockwise(start_direction):
    """Takes a string representation of a direction (NESW) and returns the new direction after
    turning one 'step' counterclockwise."""
    index = directions.index(start_direction)
    turned_index = (index - 1) % len(directions)
    return directions[turned_index]

print(turn_counterclockwise('W'))
print(turn_counterclockwise('N'))

print(turn_counterclockwise(turn_clockwise('N')) == 'N')    # yes :)


# 12.29
print('~ ~ ~ ~ ~ ~ ~ 12.29 ~ ~ ~ ~ ~ ~')

# They are already pretty streamlined. However, note that there is still considerable overlap between the
# two functions, so perhaps you can try to streamline the code further... Later there will be an exercise about this.


# 12.30
print('~ ~ ~ ~ ~ ~ ~ 12.30 ~ ~ ~ ~ ~ ~')

# See 12.31.


# 12.31
print('~ ~ ~ ~ ~ ~ ~ 12.31 ~ ~ ~ ~ ~ ~')

directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

def turn_clockwise(start_direction, steps=1):
    """
    Takes a string representation of a direction and returns the new direction after
    turning n_turns 'steps' clockwise. Default is 1 step.
    """
    return turn(start_direction, steps)

def turn_counterclockwise(start_direction, steps=1):
    """Takes a string representation of a direction and returns the new direction after
    turning n_turns 'steps' counterclockwise. Default is 1 step."""
    return turn(start_direction, -steps)

def turn(start_direction, steps):
    """
    Takes a string representation of a direction and returns the new direction after turning the amount
    specified by turns. turns can be positive (clockwise) or negative (counterclockwise).
    """
    index = directions.index(start_direction)
    turned_index = (index + steps) % len(directions)
    return directions[turned_index]

print(turn_clockwise('W'))
print(turn_clockwise('NE', steps=2))
print(turn_counterclockwise('W'))
print(turn_counterclockwise('NW', steps=3))
