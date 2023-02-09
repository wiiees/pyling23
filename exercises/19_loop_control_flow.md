# Python for Linguists 2023

## 19. Loop control flow (`break`, `while`, `continue`)

Effort profile: `▁▂▁▁▄▅▁▂▁▁▁▁▁▄▅▂▂▁▁▁▁█▁▁▂▁▂▁▁▁▁▁▁▁▄▅▁▄▅▂▂` 



**19.1.** We have seen before that `return` can be used (inside a function) to escape a loop when some condition has been met, causing the rest of the elements looped over to be skipped. Escaping a loop early is an important programming pattern to acquire, as it often results in cleaner and more efficient code. As a warming up, review your own solutions to the exercises of Section 10 that involved this pattern.

**19.2.** ⭐ What is wrong with the following function? Can you fix it? **Note:** In this and the following exercises, for the sake of practicing the main topics of this section, stick to the multi-line loop structure, no list comprehension and `sum` (nor `any` and `all`, about which we will learn in a later section).

```python
def has_any_odd(numbers):   # Note: The docstring is a lie.
    """
    Returns True if the list of numbers has any odd number; False otherwise.
    """
    for number in numbers:
        if number % 2 == 1:
            return True
        else:
            return False
```


**19.3.** Write a function `has_any_vowel` that takes a _string_ as argument, and loops over its characters to return `True` if it contains at least one vowel, and `False` if it contains no vowels. Does your function ever inspect more list elements than necessary to reach a conclusion? If so, try to streamline your function.

**19.4.** Write a function `has_only_odd` that takes a list of integers as argument, and returns `True` if all numbers in the list are odd, and `False` otherwise.

**19.5.** ⭐⭐ Write a function `has_three_odd` that takes a list of integers as argument, and returns `True` if, and only if, at _least_ three numbers in the list are odd. In which case can your function return early? In which case will it have to inspect the entire list?


**19.6.** Write a variant of the foregoing functions that checks if there are _exactly_ three odd numbers (not more, not less). Does it always need to iterate through the entire list, or is there again a situation where it can return early?

**19.7.** ⭐ Write a function `has_at_most_n_vowels` that takes a list of strings and a number `n` as argument, and returns `True` if, and only if, there are no more than `n` vowels in the list of strings (also looking inside individual strings).

**19.8.** In the preceding three exercises, try to identify which _roles_ your various variables have (see class notes).



**19.9.** Execute the following code and try to understand the output:

```python
names = ['Alf', 'Beth', 'Chris', 'Dave', 'Esra']

for name in names:
    print('Checking:', name)
    if name[0].lower() not in 'aeiou':
        print('Got one!')       # Beth is the first consonant person, and the only printed name
        break
```


**19.10.** How many names do you expect this loop to print? Test your expectation.

```python
for name in names:
    print(name)
    break
```


**19.11.** And this one?

```python
for name in names:
    break
    print(name)
```


**19.12.** Try to predict the output of the following program, then test your expectation:

```python
for name in names:
    if len(name) > 4:
        break
    print(name)
```


- - - - - -
**Something to keep in mind:** Whereas `return` lets you escape from a function (hence also from any intervening loop), `break` is more specialized: it lets you escape only the immediately enclosing loop, nothing else. This means that `break` is in many cases more suitable than `return`; we will review some cases below.
- - - - -


**19.13.** ⭐⭐ Write a function `print_until_vowel` that takes a list of strings, and prints all strings until one is encountered that begins with a vowel, in which case it should break out of the loop and end by printing `Done!` (the latter makes `break` more suitable than `return` in this case; why?).

**19.14.** ⭐ To practice with 'default arguments' from an earlier section: give your function `print_until_vowel` a boolean parameter `inclusive`, with `True` as a default value. If this parameter is set to True, the string that begins with a vowel should also itself be printed; if it is set to False, only the strings that precede it should be printed.

**19.15.** ⭐ Write code with nested loops to illustrate one of the differences between `return` and `break` mentioned above: that `return` escapes all enclosing loops, whereas `break` escapes only the directly enclosing loop.

**19.16.** What happens if you use `break` in some other place in your code, not inside a loop?

**19.17.** What is wrong with the following code (analogous to the example with `return` above)? Can you fix it? (Maintaining the printout of 'Zero odd numbers here!' in the negative case can be a bit tricky.)

```python
def print_whether_has_any_odd(numbers): # Warning: the docstring is a lie
    """
    Prints whether or not the list contains an odd number, and 'Done!' afterwards.
    """
    for number in numbers:
        if number % 2 == 1:
            print('It has an odd number!')
            break
        else:
            print('Zero odd numbers here!')
            break
    print('   ...really!')    # this final command is here to have a reason for using break to escape the loop, not return
```


**19.18.** Fixing the preceding code is easier if you know that `for` clauses can actually be combined with an `else` clause, just like `if` can. Consider the following fix, and notice the indentation ensuring that the `else` belongs with the `for`, not with the `if`. Does it work correctly?

```python
def print_whether_has_any_odd_2(numbers):
    for number in numbers:
        if number % 2 == 1:
            print('It has an odd number!')
            break
    else:
        print('Zero odd numbers here!')
    print('   ...really!')
```


- - - - - -
**Something to keep in mind:** Similar to if-clauses, for-loops can have an `else`-clause too. The else-clause of a for-loop is executed only if the for-loop finishes _without_ any `break`. Typically (but not always) `break` represents that some target element, that meets some criterion, has been found (e.g., the first odd number, the third name that begins with a vowel...). Therefore, you can often read the `else`-clause of a for-loop as "if no such element was found...". (If you pronounce it simply as 'else', it can be confusing.)
- - - - -

**19.19.** Can a single loop contain multiple `break` statements, e.g., in different if-clauses? Can you think of an (imaginary) use-case where one might need this?



**19.20.** ⭐⭐⭐ _(You can do this and the next two exercises all at once, or one at a time.)_ A rich client needs four functions, that each take a nested _list of lists_ of numbers as parameter and return a boolean. One checks if _some_ (any) inner list contains an odd number (return True if so, False otherwise). The second checks if some inner list contains _only_ odd numbers. The third checks if _each_ inner list contains an (any) odd number. The fourth checks if _each_ inner list contains _only_ odd numbers. Implement a first version of these functions, where each function is self-contained and does _not_ rely on auxiliary functions (e.g., `has_any_odd` from before). Each function will, therefore, contain nested loops.

**19.21.** Our client cares a lot of about efficiency (but insists on using Python). Do all of your loops escape early where possible?

**19.22.** Our client also cares a lot about readability, and hates repetition. Improve the four functions such that each contains only a single (non-nested) loop, within which some auxiliary function is called that does the rest (e.g., `has_any_odd` from before, and you may need to define another).


**19.23.** ⭐ We have seen that both `return` and `break` can both be used for escaping a loop. As an interim symmary, try to list the differences between the two. When would you rather use one rather than the other? When would you _have to_ use one rather than the other?



**19.24.** Besides `break` (and to some extent `return`), another keyword that helps you control your loops is `continue`. It lets you skip an element. Can you predict what the following code prints? Test your prediction and verify your understanding.

```python
for i in range(10):
    if i % 2 == 0 or i % 5 == 0:
        continue
    print(i)
```


**19.25.** ⭐ What `continue` achieves can also be done with an if-clause alone, without `continue`. Show this by re-implementing the above `for i in range(10)` example _without_ using `continue`.

**19.26.** Sometimes `continue` is preferable to a plain if-clause. A typical use case is to filter out cases that don't need to be processed, right at the start of the body of a for-loop (especially if the body of your loop is substantial). Compare program 1 and 2 in the code below (verify that the result is the same). In program 1 the body is more deeply nested (under the if-clause), which means more stuff to keep in mind as you try to understand the code. In Program 2, the body is less deeply nested, and `continue` transparently signals that certain cases can simply be ignored.

```python
# Program 1, not using continue:
for i in range(1000):
    if i % 3 == 0:
        ... # imagine a substantial program here
        bla = 3 
        blo = 5
        ble = bla * blo
        print(i, ble)


# Program 2, using continue:
for i in range(1000):
    if i % 3 != 0:
        continue        # exceptional status of this case immediately clear

    # main program is now not as deeply nested, which is also nice:
    ... # imagine a substantial program here
    bla = 3 
    blo = 5
    ble = bla * blo
    print(i, ble)
```


- - - - - -
**Something to keep in mind:** The previous exercise shows a common refactoring pattern, thought to increase readability: instead of having an if-clause that checks for the 'positive' case (and then does something), write an if-clause that checks for the 'negative' case and then merely skips ahead. The latter type of if-clause is called a **guard clause**.
- - - - -

**19.27.** Try to explain why 'guard' is a suitable metaphor for the smaller if-clause with `continue` in its body. Then check if your explanation actually applies to the original, larger if-clause as well -- if so, that means you haven't quite grasped the core of it.


<br>**_Looping with `while`_**

**19.28.** The `while` keyword lets you loop in a way that is different from for-loops. Run the following and make sure you understand what's happening. As before, try to break it in various ways.

```python
counter = 0
while counter < 10:
    print(counter)
    counter += 1
```


**19.29.** Write a program that does the same, but using a `for`-loop instead of the `while`-loop above (this is not just a matter of replacing the keyword; more things have to change).

- - - - - -
**Something to keep in mind:** For the above use-case, where you know in advance how often to repeat something, for-loops are normally the way to go. But **while-loops** can be convenient if you don't quite know how long to loop, e.g., until some unpredictable condition is met, such as a particular user input. We will see some examples of this.
- - - - -

**19.30.** If a program keeps on running, do you remember how to intervene to stop it? In the Python Console this is often the keyboard shortcut `ctrl`+`c` or `cmd`+`c`; when executing a script it may be `ctrl`+`F2`, but the PyCharm IDE also has a visual stop button for this (red square).

**19.31.** In the above while-loop, replace the condition (`counter < 10`) simply by `True`. What do you expect will happen?


**19.32.** Try to predict and explain what the following variant will print, and verify your understanding:

```python
counter = 0
while counter:
    print(counter)
    counter += 1
```


**19.33.** ⭐⭐ Write a function that repeatedly gets numbers from the user (using the `input` function), until the user enters _done_. Once _done_ is entered, print out the total, count, and average of the numbers. You can assume the user will only enter either `done` or a valid number. <!-- p4e -->


**19.34.** In your solution to the preceding exercise, try to identify which _roles_ your various variables have (see class notes).


**19.35.** ⭐⭐ Write a number guessing game. Start your program with `import random`. Write a function that contains `number = random.randint(100)` (what does it do?), followed by a loop asking the user to guess that number. Upon each guess (you can assume the user enters only valid numbers), the program prints whether it is too high or too low, or, if the guess is exactly right, exit the loop and print _Congratulations! You won in [n] guesses!_ where _n_ is the number of guesses. <!-- tp3 -->

**19.36.** ⭐ Use `continue` to make your number guessing game, from the exercise above, more user-friendly: if the user enters anything other than a number, skip ahead (with the effect of asking for new input right away). You can use the string method `is_numeric`, which returns True if the string contains only numeric digits.

**19.37.** ⭐ This section introduced several new keywords. In the Python console enter `import keyword` to access `keyword.kwlist`. For which of these keywords do you already know some purpose? Try to summarize your understanding, especially of the keywords central to this section (`break`, `continue`, `return`, `for`, `while`): what is the purpose of each of these keywords?





-----

**_🦎 You are now ready for [Coding Quest J](../quests/J_implement_the_game_'semantle'.md)!_**