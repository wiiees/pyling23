# Python for Linguists 2023

## 8. Defining and calling functions (`def`, `return`)

Effort profile: `▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▄▅▁▁▂▂▂▁▁▁▁▁▁▁▂▁▂▂▁█▁▁▁▁▂▂▂▁▁▁` 



**8.1.** In a python script, enter the following code to define a function with the name `print_spam` and subsequently _call_ it (do you remember why the string literals have a backslash at `I\'m`?):

```python
print('I\'m going to define a function.')

def print_spam():
    print('spam')


print('Now I\'m going to call the function, pay attention:')
print_spam()
```


**8.2.** A function definition is a _clause_, just like an if-clause (and others about which we will learn later). What is its head and what is its suite/body?

**8.3.** What would happen if, in the above example, there was only one empty line after the function definition clause (i.e., after the head plus body)? What if there is no empty line? Predict, on the basis of your familiarity with if-clauses, what will happen if either or both of the last two print statements in the above example are indented too, like the function definition's body?

**8.4.** Can a function contain multiple statements in its body? Can you call the same function multiple times?

**8.5.** What happens if you _define_ a function but don't _call_ it? What happens if, in the function _call_, you forget the parentheses, i.e., `print_spam` instead of `print_spam()`?

**8.6.** What do you think will happen if your script calls a function _before_ defining it (i.e., in the .py file, the definition comes after the call)? Test your expectation.

**8.7.** Can a function, within it's definition body, call _itself_? Write code to test this. This is called **recursion**. Do you remember some relation between recursion and natural language? 

**8.8.** What happens if you change the name of the function in the definition, but forget to update the function call?

**8.9.** Try to predict the output shown when running the following program, then test your prediction:

```python
def print_ab():
    print('A', end='-')
    print_ab()
    print('B', end='-')

print_ab()
```

**8.10.** When defining a function, you can give it **parameters**, enabling it to be called with **arguments**. Make sure you understand the following:

```python
def print_twice(word):
    print(word)
    print(word)


print_twice('bla')
```


**8.11.** What happens if you accidentally call the original `print_spam` from further above, which has no parameters, with an argument, e.g., `print_spam('bla')`? Conversely, what if you call `print_twice`, which does have a parameter, without an argument?

**8.12.** ⭐ Define and call a function `print_inverted` that is given a word, and prints the word back-to-front (e.g., _apple_ is printed as _elppa_). (Hint: String slicing can be helpful here.)

**8.13.** Does a function definition (a `def`-clause) follow the same indentation rules as an `if`-clause? Create some lines of code to test it.

**8.14.** Instead of directly printing something to the user, a function can also `return` a value to the program, i.e., back to where the function was called, for subsequent processing. Run this example and try to understand what it does:

```python
def give_me_spam():
    return 'spam'


some_spam = give_me_spam()
even_more_spam = some_spam.upper() * 5 + '!!!'
print(even_more_spam)
```

**8.15.** You have already encountered functions that return a value, among the built-ins. Do you remember two? And what is a built-in function that does not return a value?

**8.16.** The following code (when executed from a script, _not_ the console) does not print `aaah!`. Make the program print capitalized `AAAH!` _without_ changing the function definition, by doing something with the result of the function call.

```python
def create_scream():
    return 'aaah!'


create_scream()
```

**8.17.** ⭐⭐ Write a function called `is_even` that takes an integer `n` as an argument and returns (_not_ prints) `True` if the argument is an even number and `False` if it is odd. Test the function by applying it to several numbers, one after the other, and only in the end print all test results at once. <!-- tp3 -->

**8.18.** Now write the function `is_odd` that returns `True` when its integer argument `n` is odd and `False` otherwise. To reduce redundancy in your code, you can define this function in terms of the previous function `is_even`. <!-- tp3 -->

**8.19.** What happens if you try to print the supposed 'output' of a function that in fact has no `return` statement, such as the `print_spam` function from earlier? For instance, try:

```python
result = print_spam()
print('the result is:', result)
```


- - - - - -
**Something to keep in mind:** A function can not only take inputs and 'do' stuff (such as print it out to the user), it can also **return** a value, i.e., give it back to wherever in the program the function was called, a value which can then be used for subsequent processing. A function that has no return statement returns nothing, or rather, it returns the special object `None`.
- - - - -

**8.20.** ⭐ Write a function called `hypotenuse` that returns the length of the hypotenuse (Dutch: 'schuine zijde') of a right triangle, given the lengths of the two legs adjacent to the right angle as parameters. Examples: `hypotenuse(3, 4) == 5.0`, `hypotenuse(24, 7) == 25.0`. For a square root function, you can do `import math` and then use the function `math.sqrt`. <!-- tp3 -->

**8.21.** ⭐ Define and call a function `invert` that takes a word, and returns a new string representing that word back-to-front (that is, like `print_inverted`, but instead of printing the inverted word, it returns it to the program for subsequent processing). In your program (outside the function definition), apply the function to some word and then print that word and its mirror image next to each other.

**8.22.** ⭐ Do you remember how to use _format strings_ to align a string left, center or right? Try this again. Now write your own function named `right_justify`, _without_ using format strings (for the sake of practice), that takes a string named `s` as a parameter and returns the string with enough leading spaces so that (when printing it) the last letter of the string would be in column 40 of the display. <!-- tp2 -->

**8.23.** Still without using format strings in the function definition, add a parameter to the previous function, such that you can also choose a column other than 40 (i.e., a maximum line width).

**8.24.** Remember `type` from before? What do you expect `type(create_scream())` and `type(invert('abc'))` to be (assuming you still have `create_screen` and `invert` defined from above)? Test your expectations. And what is the type of (the result of) calling a function that does not return anything, e.g., `print_spam()` from above?

**8.25.** Explain the difference between `type(create_scream())` and `type(create_scream)`; and between `type(print_spam())` and `type(print_spam)`.

**8.26.** Define and call a function that both prints a string and returns a string (against recommended practice).

- - - - - -
**Something to keep in mind:** As a rule of thumb, every function should either _return_ stuff (e.g., compute and return some value) or _do_ stuff (e.g., print stuff, modify an existing object), not both. Functions that return stuff are sometimes called fruitful functions; functions that only do stuff are sometimes called procedures. A function that does both is said to have **side effects**, which is considered an 'anti-pattern' (i.e., to be avoided) in programming.
- - - - -

**8.27.** Functions can also have multiple parameters (hence be called with multiple arguments). Write a function that takes three numbers and returns their sum, and a function that takes three numbers and returns their average.

**8.28.** What happens if you define a function with one parameter (like `invert` above), but wrongly call the function as if it has two parameters (e.g., `invert('abc', 'def')`)? Conversely, what if you wrongly call a function that has two parameters, as if it has only one?

**8.29.** What happens if a single function contains multiple different `return` statements (e.g., `return 'haha!'` and `return 'hehehe...'`)?

**8.30.** ⭐ Can you also define a function with an if-clause in its body? For instance, define a function that takes two strings `a` and `b` as arguments, and returns the concatenation `a + b` if `a` alphabetically precedes `b`, and `b + a` otherwise. Apply the function to various test cases and print the result.

**8.31.** Write a function `is_palindrome` that takes a word as an argument, and checks if it is a palindrome, returning `True` or `False` accordingly. Can you implement a version that uses your `invert` function from above? (If you used an if-clause in the body of your function, try to do it without!)

**8.32.** ⭐ Write a `compare` function with two parameters `a` and `b`, that returns `1` if `a > b`, `0` if `a == b`, and `-1` if `a < b`. Examples:
- `compare(5, 4) == 1` 
- `compare(7, 7) == 0` 
- `compare(2, 3) == -1` <!-- tp3 -->

**8.33.** ⭐ Improve the readability (and reusability) of the following function by moving some part(s) into a separate function. (This is called _chunking_, one form of _code refactoring_.)

```python

def estimate_product_quality():
    cyps_input = input('Hi Cyp, rate this product on a scale from 1 to 5:')
    if cyps_input not in '12345':
        print('Wrong input!')
        return
    else:
        cyps_rating = int(cyps_input)
    
    malikas_input = input('Hi Malika, rate this product on a scale from 1 to 5:')
    if malikas_input not in '12345':
        print('Wrong input!')
        return
    else:
        malikas_rating = int(malikas_input)
        
    average = (cyps_rating + malikas_rating) / 2
    print("The estimated product quality is:", average)
```

**8.34.** Can you think of some reasons why it is (often) a good idea to try to avoid repeated chunks of code?

- - - - - -
**Something to keep in mind:** Streamlining your code is called **refactoring**, one aspect of which is dividing your code into functions, sometimes called **chunking**. One rule of thumb for refactoring/chunking is **Don't Repeat Yourself** (DRY), i.e., consider defining a function when you find you are repeating chunks of code. Another is the **Single Level of Abstraction Principle** (SLAP): a function should do a single thing at a single level of abstraction. The latter is related to the ideal of **Separation of Concerns** (SoC), e.g., when you're defining an `ngrams` function, you shouldn't need to worry about how to tokenize a text, and vice versa).
- - - - -

**8.35.** ⭐⭐⭐ Let's practice refactoring a bit more. Define a function `filter_by_twos` that takes a string, and returns a new string containing every second element (so given the string `abcdef` it will return the string `bdf`). Define another function `filter_by_threes` that does the same but for every _third_ element (for the same example, it will return the string `cf`). There is likely some code repetition (or a lot, depending on how concise your code is). Define a generalized function `filter_by_n` that takes an additional integer argument `n` and returns a string with every `n`th element. Then redefine your original functions (`filter_by_twos`, `filter_by_threes`) in terms of this, as shortcuts.


**8.36.** It is easy to misunderstand or forget what a function is supposed to be doing, even if you yourself wrote it. To avoid this you should _document_ your code. Adding informative `#`-comments is one way (caveat: `#`-comments can often be replaced by making your code more 'self-documenting', about which we will learn later). Another way to document your code is with so-called _docstrings_ (documentation strings): a string object that occurs in the first line(s) of a function definition. Try this:

```python
def sum_three_numbers(a, b, c):
	"""Takes three integers or floats and returns their sum."""
	return a + b + c
```


**8.37.** Python internally handles docstrings by storing them as properties of the function, in a special field `___doc__`. Try `print(sum_three_numbers.__doc__)`. Docstrings are accessed, for instance, by the `help` function; try `help(sum_three_numbers)` (remember you can press `q` to quit the help).

**8.38.** Why does `print(sum_three_numbers().__doc__)` give an error? 

**8.39.** Docstrings are customarily defined using three double-quotation marks (`"""..."""`). Do you remember how these handle newlines? Can you also define docstrings using single double-quotation marks (`"..."`), i.e., does the `help` function still pick it up? What about using three single-quotation marks (`'''...'''`) or a single single-quotation mark (`'...'`)?

- - - - - -
**Something to keep in mind:** Always start your function definition with a **docstring**, explaining at least what arguments the function takes and what it does or returns. When programming, you can even write the docstring prior to writing the body of the function definition, to guide the actual implementation.
- - - - -

**8.40.** ⭐ Add docstrings to all the functions you defined so far. (This is not just a chore; re-reading your own code from previous exercises, and remembering/reconstructing what it is supposed to do, is a useful exercise in its own right.) Your docstrings can also mention the exercise number for which the function was written.



**8.41.** ⭐ Write a function `is_factor` with integer parameters `f`, `n` that makes each of the following statements evaluate to `True`: 
- `is_factor(3, 12)` 
- `not is_factor(5, 12)` 
- `is_factor(7, 14)` 
- `not is_factor(7, 15)` 
- `is_factor(1, 15)` 
- `is_factor(15, 15)` 
- `not is_factor(25, 15)`. <!-- tp3 -->

**8.42.** ⭐ Write a function `is_multiple` to satisfy these statements: 
- `is_multiple(12, 3)` 
- `is_multiple(12, 4)` 
- `not is_multiple(12, 5)` 
- `is_multiple(12, 6)` 
- `not is_multiple(12, 7)`. <!-- tp3 -->

- - - - - -
**Something to keep in mind:** Sets of statements like the foregoing are useful for **testing** that your function works correctly. Indeed, although most of these exercises do not explicitly tell you, you should always _test_ your function thoroughly, to ascertain it works correctly. Testing your function on one example is never sufficient; always consider possible _edge cases_ (e.g., negative numbers, zero, empty strings, something of an unintended type). Python libraries like `unittest` and `doctest` facilitate incorporating tests in your code, but these will not be covered in this course.
- - - - -

**8.43.** Write a function `farenheit_to_celcius`, that returns the integer value of the nearest degree Celsius for a given temperature in Fahrenheit, as well as its inverse function `celcius_to_farenheit`. Extract suitable test cases from a conversion table on the web. <!-- tp3 -->

**8.44.** Write a function `is_determiner` that checks if a given word is an English determiner, returning True or False accordingly.

**8.45.** In PyCharm and many other IDEs you can ctrl+click (or cmd+click) on a function call, to jump to the place in the code where the function is defined. Clicking on a variable in this way brings you to the place where it is first assigned. This applies also to built-in functions (and functions imported from other modules such as `math.sqrt`), in which case PyCharm takes you to the corresponding source files as well. Try ctrl+click a bunch of times on different functions and variables.




-------

**_Homework exercises for week 4 end here, now do Mini-project [A](../projects/A_a_word-guessing_game.md) (and don't forget to submit! ✉️)._**

-------

