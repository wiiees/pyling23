# Python for Linguists 2023

## 13. Dictionary basics

Effort profile: `▁▁▁▁▁▁▁▁▂▁▁▁▂▁▁▁▁▂▁▄▅` 


**13.1.** Run the code below to construct `name_to_id`, a mapping or _dictionary_ from fictional student names (the _keys_) to student IDs (the _values_). Then inspect the object you created by printing `name_to_id`, as well as `type(name_to_id)`.

```python
name_to_id = {'Alf': '136124', 'Beth': '008623', 'Chris': '014212', 'Dave': '9123785', 'Esra': '978123'}
```


**13.2.** You can look up a particular value in the dictionary by providing it with a key (e.g., a string) in square brackets (like list index notation). Look up the student IDs (values) of Alf and Chris (keys), and print them.

**13.3.** What happens if you try to look up the student ID (value) of a student whose name is not a key in the dictionary? What happens if you forget the quotation marks around the key string you're looking up?

**13.4.** Does a dictionary have a length, just like lists and strings? Can you create an empty dictionary?

**13.5.** Can you use the keyword `in`, just as with lists, to check if an element is contained in a dictionary? If so, does `in` look at the keys or the values, or both?

**13.6.** Does a dictionary support integer indexing just like lists and strings, e.g., can you select the third item (index 2) in the above dictionary by doing `name_to_id[2]`?

**13.7.** What if we have a dictionary with integers as keys instead of strings, like `{1: 'hi', 2: 'hello', 3: 'bye', 4: 'tata'}`? Can we now access an element by its index (or is this a misleading way to put it)?

- - - - - -
**Something to keep in mind:** A **dictionary** is Python's main datastructure for storing a mapping, from _keys_ to _values_. Both keys and values in a dictionary can be various types of objects, e.g., integers, floats, strings, functions, and more complex objects. However, not every type of object can be used as a dictionary key; keys must have a special property of being **hashable**, which is, roughly, that the object provides a `hash` method that generates a string code that (virtually) uniquely represents the object. It is by these hash strings that the items in a dictionary are stored and retrieved.
- - - - -

**13.8.** What happens if you define a dictionary by specifying key-value pairs (like `{'Alf': '36124', 'Beth': '008623'}`) but using equals signs `=` instead of the colons `:` to connect keys and values? Do you see why this is quite an easy-to-make syntax mistake?

**13.9.** ⭐ Try to define an integer-to-integer dictionary, say, from numbers representing an age (in years) to the number of (hypothetical) students that have that age. Define a string-to-integer dictionary that could represent, for instance, a mapping from words to their counts in some (hypothetical) corpus. Also define a string-to-list dictionary that maps the name of a hypothetical course (say, `'semantics'`, `'syntax'`, `'python'`) to a list of students taking that course. Lastly, what happens if you try to define a list-to-integer dictionary that, say, maps a list of numbers to its average? Any clue why (we return to this below)?

**13.10.** Can a single dictionary mix multiple types (e.g., integers, floats, strings) as values, and/or multiple types as keys?

**13.11.** Do you expect dictionaries to support slicing like lists and strings do, to select a range of elements, e.g., `name_to_id['Alf':'Dave']`? Test your expectation. What about dictionaries that have integers as keys, do they support slicing to get a range of elements? Why might this be?

**13.12.** Do you expect the keys in a dictionary to be case-sensitive? Test this.


**13.13.** ⭐ Similar to assigning a value to a particular index in the list (e.g., `names[3] = 'Bert'`), you can assign a value to a particular key in an (already existing) dictionary, for instance by doing `name_to_id['Suzy'] = '124987'`. What happens if the key to which you assign a value already exists in the dictionary? What happens if it does not yet exist in the dictionary? What happens if the dictionary itself does not exist yet? Relatedly, what happens if there are duplicate keys already at the moment you create a dictionary, e.g., `my_dict = {'a': 1, 'b': 2, 'a': 3}`?

**13.14.** What do you think `del name_to_id['Esra']` does? Try it! In fact, does this syntax also work on lists? Construct a list (like `names` from previous sections) and try to delete the item at one of its integer indices. Do you expect it to work on a string as well, i.e., to delete a character from the index in a string? Why (not)?

**13.15.** Oops, the `name_to_id` dictionary contains the wrong ID for Chris! It should be `'5987162'`. Also, Suzy has quit the course, so let's remove her entry from the dictionary altogether.


**13.16.** Interestingly, dictionaries are also used in Python under the hood, for storing variable assignments. Have a look at `globals()` (for variables defined at the top level) and `locals()` (for variables defined inside functions). Consider printing these at various places in your code to see how your variable assignments affect them. (You may need to scroll: `globals` lists various special double-underscore fields (about some of which we will learn later) before showing any variables you assigned.) 

**13.17.** We will learn more about globals and locals in a later section about 'variable scope'. For now, do you expect the following to be possible? Test your expectation.

```python
globals()['y'] = 10
print(y)
```


**13.18.** ⭐ In the above example, PyCharm will likely warn you, with a red squiggle on the last line, that the variable `y` has not been defined. But Python itself doesn't care; the code runs fine! This means that PyCharm's warnings are based on a more shallow parsing of the code (called **linting**), not on actually interpreting it fully like Python does. Why might that be?



**13.19.** If you needed to store a mapping from integers to values, and the integers are always a range of consecutive integers starting at 0, would a dictionary be a suitable datastructure, or would you use something else?


**13.20.** ⭐⭐ Define a function that takes a list as input, and loops through it to count the different types of list elements, by iteratively updating a dictionary. For instance, when it encounters the list element `'apple'`, it should update the count of `'apple'` by incrementing its count in the dictionary: `counts['apple'] += 1`. Your function should return the counts dictionary. (Can your function handle a string as input too, instead of a list? If so, what will it count?)





-----

**_🦭 You are now ready for [Mini-project E](../projects/E_question_classification.md)!_**

-----

**_🐙 You are now ready for [Mini-project F](../projects/F_feature_structures.md)!_**

-------

**_Homework exercises for week 7 end here, now do at least one of the Mini-projects [D](../projects/D_trees.md), [E](../projects/E_question_classification.md), [F](../projects/F_feature_structures.md) (and don't forget to submit! ✉️)._**

-------

