# Python for Linguists 2023

## 25. Sorting (`sort`, `sorted`, `lambda`)

Effort profile: `▁▁▅▁▁▂▂▁▁▁▁▂▁▅▂▁▁▁▁▁▂▁▁` 



**25.1.** By printing the result, as well as `help` where needed, what are some differences between these two ways of sorting a list?

```python
my_list1 = [1, 3, 5, 6, 4, 2]
my_list1.sort()

my_list2 = [1, 3, 5, 6, 4, 2]
my_list2 = sorted(my_list2)
```


**25.2.** What goes wrong in the following two snippets?

```python
my_list3 = [1, 3, 5, 6, 4, 2]
sorted(my_list3)
print(my_list3)

my_list4 = [1, 3, 5, 6, 4, 2]
my_list4 = my_list4.sort()
print(my_list4)
```


**25.3.** ⭐⭐ Do you expect that the `sort` method exists on a set, dictionary, string or tuple? And do you think you can apply the `sorted` function to these types of objects? Why (not)? Test your expectations. Then try to explain why, given other things you know about Python, the difference in availability/behavior of `sort` vs. `sorted` makes sense.

**25.4.** Does sorting a list keep its duplicate elements (if any)?

**25.5.** The `key` parameter of both sorting functions tells Python what aspect of the elements to sort on. If no `key` is provided, sorting will be based on whatever the comparison operators `<` and `>` are also based on (e.g., string comparison is alphabetical, integer comparison is numerical, tuple comparison is defined in terms of comparison of the tuple elements from left to right). Verify this by sorting a list of strings, a list of integers, and a list of tuples. What happens if you try to sort a list containing objects of different types, e.g., both strings and integers?

**25.6.** ⭐ If you do provide a `key`, then it needs to be a _function_ from the to-be-sorted elements to something sortable (i.e., a type of object for which `<` and `>` are defined). Would the built-in `len` be such a function, i.e., could you use `len` directly as a key? Try to sort a list of strings with `key=len` (why not `key=len()`?).

**25.7.** ⭐ Define a function that counts the number of vowels in a string, and use this as a key to sort a list of strings.


**25.8.** Although a previous exercise said that strings are sorted alphabetically, this is not exactly true. How does string comparison handle capitalization? What about non-alphabetic characters such as numbers or punctuation marks?



**25.9.** What does  `sorted(['DEF', 'abc', 'ABC', 'def'], key=str.lower)` achieve? First formulate a prediction, then test it. Why wouldn't `sorted(['DEF', 'abc', 'ABC', 'def'], key=lower)` work?

**25.10.** Explain the difference in outcome, of `sorted(['DEF', 'abc', 'ABC', 'def'], key=str.lower)` vs. `sorted(['def', 'abc', 'ABC', 'DEF'], key=str.lower)`.

**25.11.** Instead of passing `str.lower` as a `key` function, couldn't we do `sorted([x.lower() for x in ['DEF', 'abc', 'ABC', 'def']])`? Predict the outcome of this variant before testing it.

**25.12.** ⭐ Earlier you found that sorting a list containing both strings and integers results in an error, as the two cannot be directly compared. Can you resolve this by providing a key that turns integers into something that can be compared to strings?

**25.13.** If the function you need as a sorting key will be used _only_ for that purpose, defining a whole function in the usual way with `def` can feel a bit cumbersome. For this reason sorting keys are often defined using so-called **anonymous functions** in a single line, using Python's `lambda` syntax. For instance, `lambda x: x[2]` takes a value `x` and returns its first character (index 2), `lambda x: x % 3` takes a value and returns its modulo 3, and `lambda x: len(x)` takes a value and returns its length (equivalent to simply `len` itself, of course). Before seeing them in action, verify that these expressions indeed construct functions: assign each lambda-expression to a variable and then call it with an argument as you would an ordinary function.

**25.14.** ⭐⭐ Predict the result of the following sorting commands, and then verify your prediction:
1. `sorted([-5, -9, 2, 5, 8, 9, -3], key=lambda x: -x)` 
2. `sorted([-5, -9, 2, 5, 8, 9, -3], key=abs)` 
3. `sorted(['Alf', 'alf', 'beth', 'Sue', 'Beth', 'sue'])`
4. `sorted(['Alf', 'alf', 'beth', 'Sue', 'Beth', 'sue'], key=lambda x: x.upper())`
5. `sorted(['Alf', 'Beth', 'Sue'], key=lambda x: x[::-1])`
6. `sorted([(1, 5), (-2, 6), (2, 4), (2, 5)], key=lambda x: x[1])`
7. `sorted([(1, 5), (-2, 6), (2, 4), (2, 5)], key=lambda x: (x[1], x[0]))`
8. `sorted(['Hello', 'this', 'is', 'a', 'tokenized', 'text'], key=lambda x: len([a for a in x if a not in 'aeiou']))`
9. `sorted(['Hello', 'this', 'is', 'a', 'tokenized', 'text'], key=lambda x: len([a for a in x if a not in 'aeiou'])/len(x))`
10. `sorted([6, 4, 2, 1, 3, 5], key=lambda x: 873)`
11. `sorted([13, 16, 2, 5, 3, 8, 52, 47, 49], key=lambda x: x % 12)` 

 Of course the more complex your sorting key function, the less readable it becomes if you define it all in a single line, and a separately defined function (with `def`) becomes more attractive.

**25.15.** ⭐ Why do you need the parentheses `()` if you use the sort key `lambda x: x.upper()`, but not if you use the (functionally equivalent) sort key `str.upper`?

**25.16.** Why does `sorted(['Alf', 'Beth', 'Sue'], key=lambda x: x[::-1])` _not_ result in `['euS', 'flA', 'hteB']`? And why also not in `['Sue', 'Alf', 'Beth']`, as one might naively and wrongly guess?

**25.17.** Predict and explain in plain English what the following code achieves, then test it. Why does the key have square brackets now, not round parentheses?

```python
scores = {'John': 123, 'Mary': 512, 'Sue': 82, 'Alf': 921}
my_list = sorted(scores, key=lambda x: scores[x])
```


**25.18.** What goes wrong with the code `sorted(['abc', 'cab', 'acb', 'bac'], lambda x: x[1])`, and why? (Note the asterisk in the function's signature as seen in `help(sorted)`, and cf. Section 14.) Do you agree with this design decision?

- - - - - -
**Something to keep in mind:** Among Python's built-ins there are two main functions for **sorting**: The function `sorted` takes an 'iterable' (anything over which you can iterate) and turns it into a sorted list; the list method `sort` (available only for lists) modifies a list in-place. Both functions take an optional argument `key`, that lets you specify a function that tells Python how to compare the to-be-sorted elements. Such functions can be built-ins, or defined using either `def` or (more convenient in a single line) `lambda`.
- - - - -

**25.19.** Assuming you have a list of (potentially large) tuples, choose a sort key to sort on only the _odd_ (i.e., not even) indices of each tuple. For instance, `(99, 1, 5)` should come before `(1, 99, 5)` (since the first index, index 0, is even, hence is ignored). Your solution should work for tuples of any length.


**25.20.** For the cases involving sorting on particular indices, there is also a (sometimes more convenient, and perhaps faster) function in the `operator` module that you can use: if you do `import operator`, using `operator.itemgetter(3, 1)` as your sort key will sort on index 3 and 0 of your elements. Try this, and also use it to sort a list of tuples on element with index 2 and on the last element. Does it work with a list of strings, too?


**25.21.** ⭐ You have learned that a sort key is supposed to be a function, or at least something that can be called like a function. But the `itemgetter` function in the above example is already called, i.e., `itemgetter(3, 1)`. How can this be?


**25.22.** Extract a vocabulary from a text file, such as _Moby Dick_ from Project Gutenberg (see Section 19; you can use `read_from_gutenberg` from `text_utils.py` again). Earlier we represented the vocabulary of such a text as a `set`. Given this, should we use `sort` or `sorted` if we wanted to sort a vocabulary? And does it make sense to then turn the sorted vocabulary back into a `set` datastructure for the sake of consistency?



**25.23.** Sort the vocabulary first by _initial_ character (alphabetically), then by _count_, by providing as the sorting `key` a custom function that takes a word and returns the kind of tuple by which words should be compared. (If your vocabulary contains an empty string, removing it can simplify the current task.) Write this newly sorted vocabulary to a new file, one word per line.




