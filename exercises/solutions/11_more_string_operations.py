# Solutions for 11_more_string_operations.md



# 11.1
print('~ ~ ~ ~ ~ ~ ~ 11.1 ~ ~ ~ ~ ~ ~')

print(dir(str))
print('testtest strip:', 'testtest'.strip('ts'))
print('TeStthisThing swapcase:', 'TeStthisThing'.swapcase()),
print('isalnum:')
print('  ABC:', 'ABC'.isalnum())
print('  1234:', '1234'.isalnum())
print('  ABC1234:', 'ABC1234'.isalnum())
print('  12.14:', '12.14'.isalnum())
print('  Haha!:', 'Haha!'.isalnum())
print('  1234'.center(30))


# 11.2
print('~ ~ ~ ~ ~ ~ ~ 11.2 ~ ~ ~ ~ ~ ~')

print('abc abc abc abc abc abc abc'.split())
print('abc abc abc abc abc abc abc'.rsplit())   # no difference??
print('abc abc abc abc abc abc abc'.split(maxsplit=2))
print('abc abc abc abc abc abc abc'.rsplit(maxsplit=2)) # ah, splits from the right


# 11.3
print('~ ~ ~ ~ ~ ~ ~ 11.3 ~ ~ ~ ~ ~ ~')

test_string = 'abcblablablaabc'
print(test_string.strip('abc'))
print(test_string.strip('cba'))
print(test_string.strip('a').strip('b').strip('c'))
print(test_string.strip('c').strip('b').strip('a'))
print(test_string.strip('bla'))


# 11.4
print('~ ~ ~ ~ ~ ~ ~ 11.4 ~ ~ ~ ~ ~ ~')

print('11.4')
list_of_strings = ['Alf', 'Beth', 'Gemma']
help(str.join)
print('-'.join(list_of_strings))


# 11.5
print('~ ~ ~ ~ ~ ~ ~ 11.5 ~ ~ ~ ~ ~ ~')

s = """A multiline string
does the job, or one containing tabs: [	] <-- tab  (equivalently: \t <-- tab)
because split splits on those things too, not just spaces.
"""
print('before:', s)
print('after:', ' '.join(s.split()))


# 11.6
print('~ ~ ~ ~ ~ ~ ~ 11.6 ~ ~ ~ ~ ~ ~')

print(' '.join(['a', 'b', 'c']))    # fine, for comparison
# print(' '.join(['a', 'b', 1, 2, 3]))    # nope
# print(' '.join([1, 2, 3]))    # nope


# 11.7
print('~ ~ ~ ~ ~ ~ ~ 11.7 ~ ~ ~ ~ ~ ~')

names = ['john', 'sue', 'bob']
# names_joined = names.join('-')	# Doesn't work!
names_joined = '-'.join(names)   # fixed!
names_unjoined_again = names_joined.split('-')
print(names == names_unjoined_again)


# 11.8
print('~ ~ ~ ~ ~ ~ ~ 11.8 ~ ~ ~ ~ ~ ~')

# Suggestion: always read `x.join(y)` as "use _x_ to join _y_", and read `x.split(y)` as "split _x_ on _y_".
# The reason for this apparent asymmetry is quite simple (though ultimately just a design decision that could
#    have been made otherwise): joining is intended only for a list (or other type of collection) of strings
#    (not ints or other types of objects), but there is no designated class for 'collection of strings' in which
#    a join function could live; it fits more naturally in the string class, but that means it must be called on the
#    joiner (which is a string), not on the list (which isn't).


# 11.9
print('~ ~ ~ ~ ~ ~ ~ 11.9 ~ ~ ~ ~ ~ ~')

# See 11.10


# 11.10
print('~ ~ ~ ~ ~ ~ ~ 11.10 ~ ~ ~ ~ ~ ~')

names = '''#*John#*
#*Mary# *,
*#*Suzy#*,
#*Bob#\t*;
#* Chris#\t*'''

def cleanup_from_pdf(string):
    corrections = {
        '0': 'O',
        '4': 'A',
        '5': 'S',
    }
    for key, target in corrections.items():
        string = string.replace(key, target)
    cleaned = [s.strip('#* \t,;') for s in string.split()]
    cleaned = [s for s in cleaned if not s == '']
    # Capitalize while respecting the dash (and two capitals) in Ann-Mary:
    cleaned = ['-'.join([s.capitalize() for s in n.split('-')]) for n in cleaned]   # this is arguably too complex for a single line...
    return cleaned

print(cleanup_from_pdf(names))

worse_names = '''#*T0DD#*
#*0NA# *,
*#*SUE#*,
#*ANN-M4RY#\t*;
#* R0S5#\t*'''

print(cleanup_from_pdf(worse_names))


# 11.11
print('~ ~ ~ ~ ~ ~ ~ 11.11 ~ ~ ~ ~ ~ ~')

print('abcdefabcdef'.replace('abc', '123'))
print('abcdefabcdef'.replace('qrs', '123'))
print('abcdefabcdef'.replace('abc', ''))    # Delete all occurrences of a certain substring
print('abc'.replace('', ' '))
print('abc!haha!no!'.replace('!', '! '))


# 11.12
print('~ ~ ~ ~ ~ ~ ~ 11.12 ~ ~ ~ ~ ~ ~')

text = 'Is it raining? Well, we\'ll go the beach anyway. It\'s fun, right?' 
text_for_splitting = text.replace('?', '<<<SPLIT>>>').replace('.', '<<<SPLIT>>>').replace('!', '<<<SPLIT>>>')
print(text_for_splitting.split('<<<SPLIT>>>'))


# 11.13
print('~ ~ ~ ~ ~ ~ ~ 11.13 ~ ~ ~ ~ ~ ~')

strings_to_split_on = ['.', '?', '!']
text_for_splitting = text
for splitter in strings_to_split_on:
    text_for_splitting = text_for_splitting.replace(splitter, '<<<SPLIT>>>')
print(text_for_splitting.split('<<<SPLIT>>>'))
