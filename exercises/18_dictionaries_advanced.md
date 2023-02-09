# Python for Linguists 2023

## 18. Dictionaries advanced

Effort profile: `▁▁▁▂▁▁▁▂▁▁▂▂▁▄▅▁▁▁▁▂▁▁▁▂▁▁▁▂▁▂▂▁▁` 



**18.1.** Can you loop over a dictionary with `for` by using the same syntax as looping over the elements of a list? Let `name_to_id` again be a dictionary from names to student ids (as in Section 12). Try to loop over this dictionary, printing each element. Which elements get printed, the keys, the values, or both?

**18.2.** There are three other ways of looping over a dictionary: you can loop over elements in `name_to_id.keys()` (e.g., `for key in name_to_id.keys()`), over elements in `name_to_id.values()` and over elements in `name_to_id.items()`. Try the three versions, in each case simply printing the elements in the loop, and see what gets printed.

**18.3.** If you loop with `for item in name_to_id.items():`, note that what gets printed (each `item`) are _pairs_ of a key and a value (try printing `type(item)`). A pair (or more generally _tuple_) can be _unpacked_ by assigning it to two variables separated by a comma, like this: `for key, value in name_to_id.items():`. (Recall that we saw tuple unpacking before, in the Pythonic way of switching two variables, `x, y = y, x`.) Use this to define a function `print_dict` that takes a dictionary, and loops over its items to print pairs of keys with their associated values separated by a dash: `key-value`.

**18.4.** ⭐ Define a function `update_dict` that takes two dictionaries, and loops over it to add all items of the second dictionary to the first (modifying the first dictionary in-place). Make sure to properly test this function. Should you make the function return anything?

**18.5.** In fact, the function you just defined should achieve the same as the built-in dictionary method `update`, i.e., `name_to_id.update(name_to_id2)`. Test this (after first resetting `name_to_id` to what it was before).


**18.6.** What are differences (in functionality) between the `update` method and assigning a value to a key using direct assignment (`=`)?

**18.7.** Do the dictionary methods `keys`, `values` and `items` return an ordinary list (since we could loop over it), or a different type of object? Do these types of objects support indexing and slicing like a list? If not, it might occasionally be convenient to wrap them in `list(...)`. Try this, and ascertain that the resulting lists do support indexing and slicing.

**18.8.** ⭐ The aforementioned methods return a 'view' of the dictionary's keys, values, and key-value pairs respectively. Crucially, since it is only a particular way to 'view' the original dictionary, the view itself changes when values in the original dictionary are changed (though what cannot change, while iterating over it, is the _size_ of the dictionary). Use this fact to predict, then test and explain the output of the following program:

```python
some_dict = {'a': 1, 'b': 2, 'c': 3}

original_values = list(some_dict.values())
actual_values = some_dict.values()

some_dict['b'] = 99
some_dict['d'] = 100

print(original_values)
print(actual_values)
```
 
**18.9.** What sort of object do you get if you wrap the whole dictionary in a list (without going through the `keys`, `values` or `items` methods), like `list(name_to_id)`? Can you reconcile this with the things we looped over when doing `for x in name_to_id:`?


**18.10.** What determines the order in which the keys are iterated over? Form a hypothesis by defining several dictionaries (and also adding some new items to them later) and iterating over their keys, printing them (you can use your own `print_dict` from before).

- - - - - -
**Something to keep in mind:** Until Python 3.6, the **order** of items in a dictionary could depend on the particular implementation of Python, and was _not_ to be relied upon in Python code. Since Python 3.7, however, dictionary order has been promoted from an implementational side-effect to a core feature of dictionaries: when iterating over a dictionary, the elements are now guaranteed to be given in the order in which they were added to the dictionary (whether in the initial dictionary definition (from left to right) or through subsequent assignment).
- - - - -

**18.11.** ⭐ Write code that relies on dictionary order (in Python 3.7 or higher) to get the value whose key was first added to the dictionary, and code to get the value whose key was last added to the dictionary.

**18.12.** ⭐ Write code that gets whatever value belongs to the maximum key in a dictionary. You can either do this with the help of built-in `max`, or without it, for extra looping practice. <!-- w3r -->



<br>**_A bit about tuples_**

**18.13.** We have seen that iterating over `name_to_id.items()` yields tuples. What are some other contexts in which you encountered tuples so far?

**18.14.** ⭐⭐ The standard way to define your own tuple is as a series of comma-separated expressions in parentheses e.g., `my_tuple = (1, 3, 5)`. Experiment with tuples: What types of values can they contain? Can you access their elements by index? What about slicing a range of indices? Are tuples mutable? What happens if you omit the parentheses from your tuple declaration? Can you create an empty tuple? Can you convert a tuple to a list? To a string? Vice versa (like `tuple('abc')` perhaps?)? Does a tuple have a length? Can you concatenate two tuples into a new one using `+`? Can an element of a tuple be itself a tuple? Can tuples be compared with operators like `<` and `>`?

**18.15.** Comma-separated values are commonly used also to let a function return multiple values at once (e.g., `return x, y`), and for _unpacking_ a tuple (as in `for key, value in name_to_id.items()`), and for the Pythonic way of swapping values (e.g., `x, y = y, x`). Do all of these uses also permit surrounding the comma-separated expression lists with parentheses?

- - - - - -
**Something to keep in mind:** Comma-separated expressions in Python form _expression lists_, and an expression list containing at least one comma (and commonly, but _not_ necessarily, surrounded by parentheses) yields a **tuple** (except when part of defining e.g. a list like `[1, 2, 3]`). Note that it is _not_ the parentheses that signal to Python that you are defining a tuple, but rather the comma (_except_ when defining an empty tuple, which is done with `()`).
- - - - -

**18.16.** Suppose we accidentally end our line with a comma, like `a = 1,`. Invent a possible context where this typo could lead to a subsequent error.

**18.17.** Although when creating tuples the parentheses are sometimes optional, sloppiness can lead to (potentially) unexpected results. Explain the difference between `(1, 2, 3) + (4, 5)` and `1, 2, 3 + 4, 5`.

**18.18.** Predict and explain the truth value of the expression `True, True, True == (True, True, True)`, and verify your understanding.

**18.19.** ⭐ Tuples are ideal for storing a (small) number of fixed values with a fixed order, such as a name with a student ID and email address, or the coordinates of a point in 3D-space `(x, y, z)`. If you need to store more data fields (e.g., email address, average grade, place of birth...) then a dictionary usually becomes more convenient than a tuple (why?), and if you need to store an in principle unbounded number of (typically more homogeneous) elements, a list is preferable (why?). Can you identify reasons for these preferences? Reflect on the varying use-cases of these three data structures.

**18.20.** Recall the relation between dictionaries and **hashability**. There is also a relation between hashability and mutability: objects that are intended to be mutated, like lists (and also dictionaries themselves), are typically not hashable (try this). This is because the hash code of a container object is computed based on the hash codes of the objects it contains, such that changing the objects it contains (as mutability allows) would cause the hash code of the container object to change, and the latter would cease to be a suitable, fixed 'anchor' for storing and retrieving objects in a dictionary. Test whether tuples are hashable (e.g., can they be used as keys in a dictionary?). Based on this, do you expect tuples to be mutable? Test this, too.

**18.21.** Is the following statement true? 'The fact the items of a dictionary are tuples, shows that tuples are hashable.'

**18.22.** Tuples are immutable, lists are mutable, but tuples can contain lists... Can a tuple that contains a list as one of its elements, be used as a dictionary key?

**18.23.** ⭐ Recall that **list comprehension** syntax can be used for concisely constructing a list (e.g., from an existing list, a range, or more generally a 'generator expression', see below), like `[i**2 for i in range(10)]`. To construct a tuple in this way, instead of a list, merely surrounding it with round parentheses instead of square brackets doesn't work: `(i**2 for i in range(10))`. Does this match what you learned about defining tuples in Python? Instead, you need to explicitly construct a tuple using `tuple(i**2 for i in range(10))` (note that the same also works with lists: `list(i**2 for i in range(10))`). Try this.

**18.24.** This is an exercise from earlier, but now you are better equipped to understand it: something seems to be wrong with the following code, which was supposed to print the result `2`. What's going on?
```python
a = 1 + 3,
b = a / 2
print(b)
```



<br>**_Comprehension syntax for dictionaries_**

**18.25.** List comprehension-type syntax also works on dictionaries. More correctly, `... for x in y` is a so-called **generator expression**, and the items it 'generates' can be collected not only in a list with square brackets: `[... for x in y]`), but also in a dictionary (among other datastructures), as long as `...` has the right format, namely key-value pairs in case of a dictionary. Given this, what do you think the following does?

```python
new_dict = {key: value for key, value in name_to_id.items() if key[0].lower() in 'aeiou'}
```


**18.26.** Use comprehension to take an existing dictionary with strings as keys (e.g., `name_to_id`), and filter it, constructing a new dictionary that contains only those items whose key has an even length.

**18.27.** ⭐ Explain in ordinary English what the following comprehensions do (before trying): 
 - `{name: len(name) for name in name_to_id}` 
 - `{i: i**2 for i in range(10)}` 
 - `{name: name[::-1] for name in name_to_id.keys()}` 
 - `{key: value for key, value in name_to_id.items() if int(value) % 2 == 0}`

**18.28.** Use comprehension to take an existing dictionary and invert it, swapping the keys with the values.

**18.29.** ⭐ Suppose we have a predefined list of English numerals `numerals = ['zero', 'one', 'two', 'three', 'four', 'five']` (or more). Use comprehension and `range` to create a dictionary from English numerals to numbers (0, 1, 2, 3, ...), and another one for the reverse mapping.

**18.30.** ⭐ Conversion to a dictionary (that is, creating a new dictionary from some existing object of a different type) can be done with `dict`. But which types of objects can be converted to a dictionary? Can you convert an ordinary list to a dictionary? A string? (In each case, try to form an expectation before testing it.) What about a list of pairs (2-tuples)? What about a list of lists, where each inner list has two elements? What if one of the inner lists has only one element, or three? What about a list of two-character strings?

**18.31.** Do you expect that converting a list to a dictionary and back to a list brings you back to where you started (e.g., `list(dict(some_list_of_pairs))`)? Make a careful prediction first, then test it.

**18.32.** In a previous section you defined a function that takes a list and returns item counts in a dictionary, e.g., `{'a': 16, 'b': 12}` would mean that, in the given list, the string `a` occurred 16 times and `b` 12 times. Reuse that function or implement one anew, but add the parameter `percentage` with default value `False`: when set to `True`, the function should use dictionary comprehension to turn the counts dictionary into a _percentages_ dictionary.



-----

**_🐍 You are now ready for [Coding Quest H](../quests/H_zipf's_law.md)!_**

-----

**_🐬 You are now ready for [Coding Quest I](../quests/I_translation.md)!_**

-------

**_Homework exercises for week 10 end here, now do at least one of the Coding Quests [H](../quests/H_zipf's_law.md), [I](../quests/I_translation.md) (and don't forget to submit! ✉️)._**

-------

