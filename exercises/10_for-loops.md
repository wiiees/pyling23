# Python for Linguists 2023

## 10. For-loops (`for`)

Effort profile: `▁▁▁▁▁▂▁▂▁(▁)▂▂▂▁▂▂▁▂▂▄▅▄▅▂▄▅▁▂▁▂▄▅▁▂▂▂▁(▂)▂▄▅▁▄▅` 



**10.1.** Another keyword that can create clauses is `for`. Try to understand what it does, with the following code. First make sure the variable `names` is assigned a list of names like `['Alf', 'Beth', 'Chris', 'Dave', 'Esra']`.

```python
for name in names:
    print(name)
```


**10.2.** Is indentation meaningful in the case of for-clauses, too? Verify this empirically.

**10.3.** After executing the above code, do you expect that the variable `name` has a value? If so, which value? Test this and make sure you understand what is going on.

**10.4.** Write a program that loops over the list `names` from above and prints each element twice, using a `for`-loop with two `print` statements in its body. How is this different from looping over the same list twice (i.e., two `for`-loops, one after the other), with a single `print` statement in each loop's body?

**10.5.** What happens if the variable `name` already exists before executing the for-loop? (Perhaps this was already the case in the previous exercises.)

**10.6.** ⭐ Write a function `print_multiple` that is given a list, and prints each element of the list, each on a new line.

**10.7.** Can you predict what will happen if you accidentally do `print_multiple(name)` instead of `print_multiple(names)`? Test your prediction.


**10.8.** ⭐ Write a function `print_multiple_oneline` that is given a list, and prints all list elements on a single line, concatenated with dashes in between. You can either first compose a long string and call `print` only once at the end, or use repeated `print` statements and control the layout with the help of its `end` parameter.

**10.9.** Modify the original `print_multiple` to take an additional boolean argument `oneline`, such that `print_multiple([1, 2, 3], True)` prints all numbers on one line with dashes in between, and `print_multiple([1, 2, 3], False)` prints each number on a new line.

**10.10.** _[Optional, feel free to skip]_ Python's asterisk `*` operator lets us unpack a list into a 'sequence expression', basically splitting it into its elements. Since the built-in function `print` can take any number of arguments (remember?), we can use `*` to pass in each list item as a separate argument (e.g., `print(*names)`, equivalent to `print(names[0], names[1], names[2], ...)`). Use this technique, together with the `print` function's optional argument `sep`, to achieve the same as your functions from the previous exercises.

**10.11.** ⭐ You can also initialize a variable outside the for-loop, and then modify or reassign something to it on each iteration within the for-loop. (A variable used this way is sometimes called a _'gatherer'_; see why?) Use this to write a function that takes a list `numbers`, and loops through it to compute the sum of the squares of the numbers, returning it in the end. For example a call with `[2, 3, 4]` as an argument should return the result of 4+9+16 which is `29` <!-- tp3 -->


**10.12.** ⭐ Define a function `length` that takes a list as input and returns its length, _without_ using the built-in function `len`.

**10.13.** ⭐ Write a function that takes a list of words and concatenates them, placing one after the other with dashes `-` in between, and returns (not prints) the resulting string. (In the next Section we will learn a more standard way to achieve this, but implementing it manually for now makes for good practice!)

**10.14.** Generalize the preceding function to allow changing the separator (e.g., dash, space, underscore) by giving the function an extra string parameter `sep`.

- - - - - -
**Something to keep in mind:** After defining a function, make sure to _test_ it thoroughly by calling it with various arguments. After verifying that it works, you can easily comment out (with `#`) the test function calls, while leaving the function definition itself untouched. This lets you conveniently work in a single file for all the exercises, without all the previous functions being called every time you test the latest function. Later we will learn how to separate the test calls from the function definitions.
- - - - -

**10.15.** ⭐ Can you use an if-clause within a for-loop? Write a function to count how many odd numbers are in a list, returning the result. <!-- tp3 -->

**10.16.** ⭐ Define a function that sums up all the even numbers in a list, returning the result. <!-- tp3 -->

**10.17.** Define a function that sums up all the negative numbers in a list, returning the result. As always, try to use a clear, transparent function name. <!-- tp3 -->

**10.18.** ⭐ Write a function that takes a list of numbers, multiplies each element by 3 and appends the results to a new list. Does the new list have the same number of elements as the original list?

**10.19.** ⭐ Write a function that takes a list of words, and an integer, and counts how many words in the list have a length of at least that integer. <!-- tp3 -->

**10.20.** ⭐⭐ One way to escape a loop early, at least inside a function definition, is the `return` statement. Write a function that sums all the elements in a list up to, and including, _the first even number_, and, as soon as this even number has been encountered and added, returns the result right away (skipping the rest of the list). (What if there is no even number in the list?) <!-- tp3 -->

**10.21.** ⭐⭐ Extend the previous function with a boolean parameter `inclusive`: setting it to False should result in summing up to, but _excluding_, the first even number.

**10.22.** ⭐ Write a function that counts how many words occur in a list up to (and including) the first occurrence of the word _the_. <!-- tp3 -->

**10.23.** ⭐⭐ Just as you can loop through a list, you can loop through the characters of a string. Write a function `has_even_vowel_count` that uses a loop to count the number of vowels in a string, and returns a boolean that indicates whether that number is even or not.

**10.24.** Did you remember to add docstrings to your functions?

**10.25.** ⭐ Write a function that counts the number of even digits in a number `n`, e.g., the number `5671238` has 3 even digits (6, 2 and 8). <!-- tp3 -->



**10.26.** Can you predict the output of the following program?

```python
some_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for i in some_numbers:
    if i % 2 == 0:
        some_numbers.append(some_numbers[-1] + 1)
    print(i)
```


**10.27.** ⭐ As we saw, the built-in function `max` can be applied to an entire list, to find the greatest value. But a good exercise is to implement a `max` function yourself (i.e., without using the built-in). Someone else has already tried this, but it doesn't quite work if the list contains only negative numbers. Can you fix it?
```python
def custom_max(numbers):
    greatest = 0
    for num in numbers:
        if num > greatest:
            greatest = num
    return greatest
```

**10.28.** ⭐⭐ Try to define a variant of the above function that finds the _2_ greatest values in a list.

**10.29.** Conceptually (no programming required): Can you think of a way to generalize the above '2 greatest' function to an '`n` greatest' function, i.e., a function that takes a list as well as an additional integer argument `n`, and returns the `n` greatest values in the list? If not, do you think a function to _sort_ a list from low to high could be helpful? (We learn about sorting in later sections.)



<br>**_List comprehension_**


**10.30.** ⭐ The keyword `for` also appears in a powerful and 'Pythonic' pattern called **list comprehension**. With a single line of code, it lets you construct a new list from an old one by changing or filtering the original elements. Try to predict (and test) what the following do:
- Let `numbers = [9, 5, 8, 3, 2, 6]`, and try `[n for n in numbers if n > 4]` 
- Assuming you still have `names` assigned: `[s[0] for s in names]` (if you were to assign the result to a variable, what would be a fitting variable name?) 
- `[name[::-1] for name in names]`
- `[s for s in names if s[0].lower() in 'aeiou']` (try to describe what this means, in plain English)

**10.31.** ⭐ Use list comprehension to take a list of words, and construct a list of the same words but in full capitals. Does your code demonstrate that strings are mutable? Does it demonstrate that lists are mutable?

**10.32.** ⭐ Use list comprehension to take a list of numbers, and return a list of squares of those numbers, but only of those numbers which were even.

**10.33.** List comprehensions were added to the language in the Python Enhancement Proposal **PEP202** (https://peps.python.org/pep-0202/) very early in Python's lifetime (2000). Have a look, and see if you recognize some of the rationale and the examples given.

**10.34.** ⭐ _[Optional, feel free to skip]_ The `... for ... in`-structure of list comprehensions is a so-called _generator expression_ (introduced as a generalization of list comprehension, in [PEP289](https://peps.python.org/pep-0289/). Generator expressions actually define an object in their own right. To see this, run the following code, and inspect the resulting object (e.g., `print`, `type`). (Without a 'container' context like a list `[...]`, generator expressions need to be surrounded by (round) parentheses lest you get a syntax error.)

```python
uppercase_name_generator = (name.upper() for name in names)
```

Can you loop over the created generator object as you would over an ordinary list? Does it have a length (`len`)? Why (not)?

**10.35.** ⭐ Use list comprehension to create a list containing all names in the list `names` that are at least 3 characters long. Also use list comprehension to create a list of integers that indicate, for each name in the original `names`, how many characters it contains.

- - - - - -
**Something to keep in mind:** With great power comes great responsibility: list comprehension lets you do a _lot_ in a single, compact line of code. But compact code is never in itself a goal; code must be _readable_ above all else. Therefore, use list comprehension only if you think this makes the code more readable than e.g. a multi-line `for`-loop. (This is only the case, typically, if the modification or filtering condition you want to apply is sufficiently simple.)
- - - - -

**10.36.** ⭐⭐ Redo the previous two exercises _without_ list comprehension, by using an ordinary multi-line for-loop. Which version do you find more readable?

**10.37.** Why does readability matter, anyway? Isn't _correctness_ of code the thing that primarily matters? Consider this question especially from the perspective of using code for scientific research.


**10.38.** ⭐⭐ Use list comprehension to write three functions that take two lists and compute (and return) their _union_, _intersection and _complement_, respectively (notions from set theory). (Later we will learn about Python's built-in `set` datastructure, which of course provides such operations already. Solving this exercise without those built-ins is excellent practice.)

