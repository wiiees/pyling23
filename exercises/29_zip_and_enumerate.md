# Python for Linguists 2023

## 29. Smarter iteration with `zip` and `enumerate`

Effort profile: `(▁▁▂▁▁▁▁▁▁▁▂▁▂▂▁▁▁▁▁▂▂▂)` 




----

🦉 **_This entire section is OPTIONAL!_**

----

<br>**_Avoiding indices; combining lists with `zip`_**

**29.1.** In general, Python programmers are a bit weary of using unnecessary indices to access list elements. Streamline the following code by getting rid of `range`, `len` and the index `i`:

```python
names = ['John', 'Sue', 'Bob', 'Chris']
for i in range(len(names)):
    print(names[i])
```


**29.2.** Besides the streamlined version of the above code being simpler, another reason for avoiding indices where possible is the following. If what a piece of code should do is iteration, then that code should work for any object that is iterable, not only those that happen to support indexing. Give a code example to illustrate the superiority of your streamlined version in this regard.

**29.3.** ⭐ Can you think of another (possibly subjective) reason to avoid indices where possible?

**29.4.** Suppose we have two lists. Write a program that combines every element from one list, with each corresponding element from another, and print the resulting pairs one after the other. Without peeking at the next exercise (resist!), you will probably have to use an index and `range`.

**29.5.** Do you see the resemblance between your preceding program and a zipper (of the type used in clothes)? That is why an analogous built-in function is called `zip`. Call `help` on this function and find a way to use it to solve the preceding exercise, instead of your custom-made function.

**29.6.** What is the difference between `for a in zip(...):` and `for a, b in zip(...):`?

**29.7.** What do you think will happen if `zip` is provided with two lists of unequal length? Test your expectation.

**29.8.** What type of object does a `zip` call on its own (i.e., outside of a for-loop context) return?

- - - - - -
**Something to keep in mind:** Use `zip` to combine elements, each from a different iterable (e.g., list), into tuples. As with several functions we encountered earlier (e.g., a dictionary's `.keys`, `.values` and `.items`; spaCy's `.sents`), the `zip` function does not return its tuples in a list, but rather returns a type of object that will only generate such tuples 'on the fly' as you iterate over it.
- - - - -

**29.9.** As usual with iterator-type objects, you can also directly collect the generated tuples into a list, with `list(zip(...))`. Try this. What do you expect will happen if you wrap a `zip`-call inside a `dict(...)`? Test your expectation.

**29.10.** Can `zip` also be applied to three or more lists? (Non-serious: can you think of an application for this type of zipper in a piece of clothing?)

**29.11.** ⭐ Suppose we have a list of place names and a list of their respective inhabitant counts. Write code to create a dictionary from place names to inhabitant counts.

**29.12.** Predict what happens if `zip` is given the same list twice, e.g., `zip(names, names)`? What if it is given the same list twice, but once without the first element: `zip(names, names[1:])`?

**29.13.** ⭐ Predict the outcomes of the following, given some string `s = 'abcdef'`, and then test your predictions:
 - `list(zip(s, s[:-1]))` 
 - `list(zip(s[1:], s))` 
 - `list(zip(s[:-1], s))` 
 - `list(zip(s, s[::-1]))` 
 - `list(zip(s, s[1:], s[2:]))`

**29.14.** ⭐ With a single `zip`-command like the foregoing examples, and given the same string `s = 'abcdef'`, construct the following list: `[('a', 'b'), ('c', 'd'), ('e', 'f')]`.

**29.15.** Suppose we have two equal-length lists, `l1` and `l2`. Does `result = list(zip(l1, l2))` achieve the same as the following code? As usual, make a prediction before trying it out.

```python
result = []
for e1 in l1:
    for e2 in l2:
        result.append((l1, l2))
```


<br>**_Enumerating elements (`enumerate`)_**

**29.16.** While Python progammers are weary of indexing (remember the reasons why?), sometimes it's simply necessary. Fortunately, there is often a way to get indices without the pesky `range(len(...))`. The built-in function `enumerate` iterates over elements while counting them, returning the count-element pairs. Assuming you still have a list `names` defined, try the following:

```python
for i, name in enumerate(names):
    print(i, name)
```


**29.17.** What happens if, in the above code, you forget the `i` and do `for name in enumerate(names): ...` instead (if relevant: adapt the `print` statement to avoid it causing a NameError)? And what happens if, conversely, you do include the `i` but forget the `enumerate`, that is, `for i, name in names: ...`?

**29.18.** The count-element pairs you get from `enumerate` may superficially resemble the key-value pairs you get from `dict.items()`, but there is a crucial difference between keys and the indices you get from `enumerate`, in how they relate to the datastructure iterated over. Explain how the following illustrates such a difference:

```python
for i, char in enumerate({'a', 'b', 'c', 'd', 'e'}):
    print(i, char)
```


- - - - - -
**Something to keep in mind:** Use the built-in function `enumerate` to iterate over elements while counting them, returning count-element pairs. When applied directly to a list, the counts returned by `enumerate` correspond to the list's indices, and this way of accessing indices (_if_ you need indices at all) is often preferable to `range(len(...))`.
- - - - -

**29.19.** Try to predict the outcome of the following (forgive the uninformative variable names), and then test your predictions:

```python
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for x, y in enumerate(my_dict):
    print(x, y)
for x, y in enumerate(my_dict.items()):
    print(x, y)
```


**29.20.** ⭐ Do you expect any of the following yield an error? Why? Test your expectations. 
 - `list(range(10))` 
 - `list(10)` 
 - `enumerate(10)` 
 - `enumerate(range(10))` 
 - `range(enumerate(10))` 
 - `enumerate(list(range(10))`

**29.21.** ⭐ Predict, and then test and make sure you understand, the outcomes of the following statements:
 - `list(enumerate('abcd'))` 
 - `list(zip(range(4), 'abcd'))` 
 - `list(enumerate(range(5)))` 
 - `list(zip(range(5), range(10)))`  
 - `list(zip(range(10), range(5)))` 
 - `list(enumerate(enumerate(enumerate(range(5)))))`  
 - `list(zip(range(5)))`

**29.22.** ⭐ Previously we collected n-grams from a text with the help of indexing and range (Section 13). Now, try the same with `zip` instead. In particular, zip a tokenized text with itself (one of which offset by one). Next, try to generalize this to tri-grams. How might one generalize this to _n_-grams for higher _n_ work? Do you find this approach more readable, or the original one using `range`?






-------

**_Homework exercises for week 15 end here, now do at least one of the Mini-projects [Q](../projects/Q_gender_bias.md), [R](../projects/R_similarity.md), [S](../projects/S_question_extraction_and_classification.md) (and don't forget to submit! ✉️)._**

-------

