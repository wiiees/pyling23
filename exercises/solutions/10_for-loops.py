# Solutions for 10_for-loops.md



# 10.1
print('~ ~ ~ ~ ~ ~ ~ 10.1 ~ ~ ~ ~ ~ ~')

names = ['Alf', 'Beth', 'Chris', 'Dave', 'Esra']
for name in names:
    print(name)


# 10.2
print('~ ~ ~ ~ ~ ~ ~ 10.2 ~ ~ ~ ~ ~ ~')

# Yes, analogous to the initial exercises about if-clauses
# for name in names:
# print(name)       # no indentation = error

for name in names:
    print(name)
    print('test')

for name in names:
    print(name)
print('test')       # un-indentation means end of clause


# 10.3
print('~ ~ ~ ~ ~ ~ ~ 10.3 ~ ~ ~ ~ ~ ~')

print(name)  # it remains assigned to the last value assigned to it during the loop


# 10.4
print('~ ~ ~ ~ ~ ~ ~ 10.4 ~ ~ ~ ~ ~ ~')

print()
for name in names:
    print(name)
    print(name)

# Note how this is different:
print()
for name in names:
    print(name)
for name in names:
    print(name)
print()


# 10.5
print('~ ~ ~ ~ ~ ~ ~ 10.5 ~ ~ ~ ~ ~ ~')

name = 'Johnny'
for name in names:  # still works fine; the for-loop simply re-assigns it, iteratively, elements of the list.
    print(name)


# 10.6
print('~ ~ ~ ~ ~ ~ ~ 10.6 ~ ~ ~ ~ ~ ~')

# See 10.9


# 10.7
print('~ ~ ~ ~ ~ ~ ~ 10.7 ~ ~ ~ ~ ~ ~')

# See 10.9


# 10.8
print('~ ~ ~ ~ ~ ~ ~ 10.8 ~ ~ ~ ~ ~ ~')

def print_multiple_oneline(l):
    """
    Prints all elements of the list l on one line, concatenated by dashes.
    """
    for element in l[:-1]:
        print(element, end='-')
    print(l[-1])


print_multiple_oneline(names)


# 10.9
print('~ ~ ~ ~ ~ ~ ~ 10.9 ~ ~ ~ ~ ~ ~')

def print_multiple(l, oneline):
    """
    Takes a list and a boolean oneline and prints all elements, either on one line or on separate lines.
    """
    if oneline:
        end = '-'
    else:
        end = '\n'
    for element in l:
        print(element, end=end)
        # print(element, end='' if oneline else '\n')  # More pythonic, using 'ternary if' (i.e., if inside an 
        # expression) instead of the above if-clause.
    if oneline:
        print()  # this is probably desirable


print_multiple(names, False)
print_multiple([1, 2, 3], True)
print_multiple([1, 2, 3], False)
print_multiple(name, True)


# 10.10
print('~ ~ ~ ~ ~ ~ ~ 10.10 ~ ~ ~ ~ ~ ~')

print(*names, sep='\n')
print(*names, sep='-')


# 10.11
print('~ ~ ~ ~ ~ ~ ~ 10.11 ~ ~ ~ ~ ~ ~')

def sum_of_squares(numbers):
    """
    Computes and returns the sum of squares of the numbers in the list.
    """
    result = 0
    for number in numbers:
        result += number ** 2
    return result


print(sum_of_squares([2, 3, 4]))


# 10.12
print('~ ~ ~ ~ ~ ~ ~ 10.12 ~ ~ ~ ~ ~ ~')

def length(l):
    """
    'Manually' computes the length of the list l.
    """
    result = 0
    for element in l:  # more pythonic: for _ in l, because the element doesn't matter, so don't give it a name.
        result += 1
    return result


print(length([1, 2, 3, 4, 5, 6]))


# 10.13
print('~ ~ ~ ~ ~ ~ ~ 10.13 ~ ~ ~ ~ ~ ~')

# See 10.14


# 10.14
print('~ ~ ~ ~ ~ ~ ~ 10.14 ~ ~ ~ ~ ~ ~')

def concatenate(words, sep):
    """
    Returns a concatenation of a list of strings with seps in between
    NOTE: This function emulates the built-in string method 'join', e.g.,  '-'.join(words)  (read as: use '-' to join all words)
    """
    result = words[0]
    for word in words[1:]:
        result += sep + word
    return result


print(concatenate(names, '-'))


# 10.15
print('~ ~ ~ ~ ~ ~ ~ 10.15 ~ ~ ~ ~ ~ ~')

def count_odd(numbers):
    """
    Return the number of odd numbers in the list.
    """
    n_odd = 0
    for num in numbers:
        if num % 2 == 1:
            n_odd += 1
    return n_odd


print('number of odd numbers =', count_odd([1, 3, 5, 2, 4, 6, 5, 7, 9]))


# 10.16
print('~ ~ ~ ~ ~ ~ ~ 10.16 ~ ~ ~ ~ ~ ~')

def sum_even(numbers):
    """
    Returns the sum of all even numbers.
    """
    result = 0
    for num in numbers:
        if num % 2 == 0:
            result += num
    return result


print('sum of even numbers =', sum_even([1, 3, 5, 2, 4, 6, 5, 7, 9]))


# 10.17
print('~ ~ ~ ~ ~ ~ ~ 10.17 ~ ~ ~ ~ ~ ~')

def sum_negative(numbers):
    """
    Returns the sum of all negative numberes.
    """
    result = 0
    for num in numbers:
        if num < 0:
            result += num
    return result


print(sum_negative([1, 2, 3, -1, -2, -3, 0, -5]))


# 10.18
print('~ ~ ~ ~ ~ ~ ~ 10.18 ~ ~ ~ ~ ~ ~')

def triple_list_elements(numbers):
    """
    Returns a new list containing each original number times three.
    """
    result = []
    for num in numbers:
        result.append(num * 3)
    return result


print(triple_list_elements([1, 2, 3, 4, 5]))


# 10.19
print('~ ~ ~ ~ ~ ~ ~ 10.19 ~ ~ ~ ~ ~ ~')

def num_of_min_length(words, min_length):
    """
    Returns the number of words in the list that are at least of length min_length.
    """
    count = 0
    for word in words:
        if len(word) >= min_length:
            count += 1
    return count


print(num_of_min_length(['I', 'own', 'a', 'monkey'], 3))


# 10.20
print('~ ~ ~ ~ ~ ~ ~ 10.20 ~ ~ ~ ~ ~ ~')

# See 10.21


# 10.21
print('~ ~ ~ ~ ~ ~ ~ 10.21 ~ ~ ~ ~ ~ ~')

def sum_until_even(numbers, inclusive):
    """
    Sums all numbers until the first even number, inclusive or exclusive.
    """
    result = 0
    for num in numbers:
        if num % 2 == 0:
            if inclusive:
                result += num
            return result  # later we will learn about the 'break' statement, which could also work here.
        result += num
    # this is reached only if there is no even number:
    return result


print(sum_until_even([1, 1, 1, 2, 4, 6, 3, 5, 7], True))
print(sum_until_even([1, 1, 1, 2, 4, 6, 3, 5, 7], False))
print(sum_until_even([1, 1, 1, 3, 5, 7], False))  # this is why the second return statement is needed


# 10.22
print('~ ~ ~ ~ ~ ~ ~ 10.22 ~ ~ ~ ~ ~ ~')

def count_until_the(words):
    """
    Counts number of words occurring before 'the' (or all words if there is no 'the').
    """
    count = 0
    for word in words:
        if word == 'the':
            return count
        count += 1
    return count


print(count_until_the(['I', 'saw', 'the', 'fox']))


# 10.23
print('~ ~ ~ ~ ~ ~ ~ 10.23 ~ ~ ~ ~ ~ ~')

def even_vowel_count(word):
    """
    Returns true if word has even number of vowels, otherwise false.
    """
    vowel_count = 0
    for char in word.lower():
        if char in 'aeoui':
            vowel_count += 1
    return vowel_count % 2 == 0


print(even_vowel_count('monkey'))
print(even_vowel_count('APE'))
print(even_vowel_count('BANANA'))


# 10.25
print('~ ~ ~ ~ ~ ~ ~ 10.25 ~ ~ ~ ~ ~ ~')

def count_even_digits(number):
    """
    Returns the number of even digits in the number.
    """
    count = 0
    for digit in str(number):
        if int(digit) % 2 == 0:
            count += 1
    return count


print(count_even_digits(5671238))


# 10.26
print('~ ~ ~ ~ ~ ~ ~ 10.26 ~ ~ ~ ~ ~ ~')

# Predict the output before trying:
some_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for i in some_numbers:
    if i % 2 == 0:
        some_numbers.append(some_numbers[-1] + 1)
    print(i)


# 10.27
print('~ ~ ~ ~ ~ ~ ~ 10.27 ~ ~ ~ ~ ~ ~')

def custom_max(numbers):
    # greatest = 0  # this was the problem
    greatest = None # you can also use some other non-numerical value, but None is customary; and there's also negative infinity
    for num in numbers:
        if greatest is None or num > greatest:
            greatest = num
    return greatest


# 10.28
print('~ ~ ~ ~ ~ ~ ~ 10.28 ~ ~ ~ ~ ~ ~')

def max_2(numbers):
    greatest1 = numbers[0]
    greatest2 = numbers[1]  # fails when list has only 0 or 1 elements... alternative: use the same None trick as above
    for num in numbers[2:]:
        if greatest1 < greatest2:
            greatest1, greatest2 = greatest2, greatest1
        if num > greatest2:
            greatest2 = num
    return greatest1, greatest2


# 10.29
print('~ ~ ~ ~ ~ ~ ~ 10.29 ~ ~ ~ ~ ~ ~')

# That might be quite tricky and result in long, ugly, repetitive code.
# Having a sorting function would make it trivial: we could simply sort the list, then take the last n elements.


# 10.30
print('~ ~ ~ ~ ~ ~ ~ 10.30 ~ ~ ~ ~ ~ ~')

numbers = [9, 5, 8, 3, 2, 6]
print([n for n in numbers if n > 4])
print([s[0] for s in names])  # initials
print([name[::-1] for name in names])
print([s for s in names if s[0].lower() in 'aeiou'])  # all names that start with a vowel


# 10.31
print('~ ~ ~ ~ ~ ~ ~ 10.31 ~ ~ ~ ~ ~ ~')

print([s.upper() for s in names])
# it demonstrates nothing: neither that strings are mutable (they aren't), nor that lists are mutable (though they are).
# both .upper() and list comprehension create a new object (a new string and a new list, respectively)


# 10.32
print('~ ~ ~ ~ ~ ~ ~ 10.32 ~ ~ ~ ~ ~ ~')

print([num ** 2 for num in numbers if num % 2 == 0])


# 10.35
print('~ ~ ~ ~ ~ ~ ~ 10.35 ~ ~ ~ ~ ~ ~')

print([name for name in names if len(name) >= 3])
print([len(name) for name in names])


# 10.36
print('~ ~ ~ ~ ~ ~ ~ 10.36 ~ ~ ~ ~ ~ ~')

print('----- 8.28 --------')
squared_evens = []
for num in numbers:
    if num % 2 == 0:
        squared_evens.append(num ** 2)
print(squared_evens)

names_3_or_longer = []
for name in names:
    if len(name) >= 3:
        names_3_or_longer.append(name)
print(names_3_or_longer)

name_lengths = []
for name in names:
    name_lengths.append(len(name))
print(name_lengths)


# 10.37
print('~ ~ ~ ~ ~ ~ ~ 10.37 ~ ~ ~ ~ ~ ~')

# Form your own thoughts. A key component of an answer would be to relate
# code clarity to the importance of REPRODUCIBILITY in science.
# Another key component is that code is read far more often than it is
# written, so clarity is simply a time-saver.


# 10.38
print('~ ~ ~ ~ ~ ~ ~ 10.38 ~ ~ ~ ~ ~ ~')

def deduplicate(l):
    result = []
    for a in l:
        if a not in result:
            result.append(a)
    return result


def union(list1, list2):
    result = deduplicate(list1 + list2)
    return result


def intersection(list1, list2):
    result = deduplicate([a for a in list1 if a in list2])  # deduplicate not strictly necessary if list1, list2 are already sets...
    return result


def complement(list1, list2):
    result = deduplicate([a for a in list1 if a not in list2]) # same here
    return result


print(union([1, 2, 3], [3, 4, 5]))
print(intersection([1, 2, 3], [3, 4, 5]))
print(complement([1, 2, 3], [3, 4, 5]))

