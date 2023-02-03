# Python for Linguists 2023

## 6. Types (`type`, and `int`, `str`, ..., also `help`, `dir`)

Effort profile: `▂▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▂▁▁▁▁▁▂▁▁▁▄▅▂▂▂` 



**6.1.** ⭐ What does the built-in function `type` do? Apply it at least to the following expressions. Each time, try to make a prediction and check it before moving on to the next item.
1. `4`
2. `238`
3. `-6`
4. `6.3`
5. `3 ** 4`
6. `'apple'`
7. `'apple' * 5`
8. `True`
9. `False`
10. `'True'`
11. `'False'`
12. `'987'`
13. `print`
14. `max`.

**6.2.** You can **convert** between types by using `int`, `str`, `float`, `bool`, for instance `int('400')` constructs an integer `400` from the string `400`, and `bool(0)` constructs the boolean `False` from the integer `0`. Try to convert between different types, and use `type` to check the result.

**6.3.** What happens for conversions that don't make sense, e.g., `int('apple')`, `float('')`?

**6.4.** Try `bool('True')` and `bool('False')`. Is the result what you expected? Try to understand why this is. What string do you need to feed to `bool` to get `False`?

**6.5.** Does 'type conversion' actually _change_ the type of an existing object, or does it merely create a new object of a different type on the basis of the old one? Write code to test this.

**6.6.** Suppose the variable `my_variable` contains a number, e.g., we did `my_variable = 5`. What happens if you now try to assign a string to that same variable? In many programming languages this would not be allowed; is it possible in Python?

- - - - - -
**Something to keep in mind:** Python is a _strongly typed, dynamically typed language_. It is **strongly typed** in the sense that all its _objects_ are of a certain type (`int`, `str`, `bool`, etc.), and the type of an object _cannot_ be changed. It is **dynamically typed** in that the same is not true for the _variables_ to which these objects are assigned: the types of objects you can assign to a given variable or feed into a given function are not a priori fixed. Feeding a function the 'wrong' type can result in unexpected behavior during runtime (and possibly even an error), but it does not prevent the code from compiling and running (unlike _statically typed_ languages).
- - - - -

**6.7.** A consequence of dynamic typing is that functions and operators don't really care about the types of the arguments given to them, as long as they have the required properties and methods for the function to be able to 'do its thing'. (For instance, the `+` operator can operate on objects of any type as long as they have an `__add__` method; and accessing elements with `[...]` works on any object that has a `__getitem__()` method.) This is called **duck typing**, named after a famous illustration of commonsense reasoning: _"If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."_ Can you explain how this could be a metaphor for typing in Python (hence explain why the name 'duck typing' fits)? (Though like any metaphor, it likely isn't perfect...)

**6.8.** Does the `print` function care about the type of its argument?

**6.9.** Suppose the variable `num` contains a number. What happens if you try to append this number to a string by doing `'apple' + num`? Can you fix this by using `str`? And by using `int`?

**6.10.** Can you divide an integer number such as `5` directly by a floating point number such as `6.17`, or does this require explicit type conversion?

**6.11.** Does division always result in a float, or only when the result is not a whole number? For instance, what about `6/3` (e.g., compared to `6/4`)?

**6.12.** Does `5.0000` define a float or an int? What do you expect will be the value of `5.0000 == 5`?

**6.13.** Remember that Python does not allow zero prefixes on integers, e.g., it complains when you do `some_number = 000123`. What do you think will happen if you do `int('000123')`? Given this, can you argue that converting strings to numbers is more lenient than the Python interpreter itself?

**6.14.** If you get a user's input using `input`, what is the type of the resulting object? Does this depend on what the user enters?

**6.15.** ⭐ In a Python script, write a program that gets a number from the user, multiplies it times 5, and prints the result.

**6.16.** Given what you have learned, if you add up two floats that together happen to form a round number (like `0.4 + 0.6`), does the outcome automatically become of type `int`?

**6.17.** ⭐ Write a program that gets one number from the user, then another one, and prints the result of dividing the first by the second. Try it out a couple of times. What happens if you run the program, first enter 9 and then 0?

**6.18.** For each of the following expressions, predict the type, and then test your prediction:
1. `'apple'[0]`
2. `'apple'[1:3]`
3. `'apple[17:21]'`
4. `'a' in 'apple'` 

**6.19.** To test if an object is of a certain type, use the build-in function `isinstance`, for instance `isinstance(500, int)` and `isinstance('apple', str)`. What is the type of `isinstance` itself?

**6.20.** Types form a hierarchy. For instance, just like a mammal is also an animal, a string (type `str`) is at the same time also an object (type `object`), which is a more general, super-type. Test this with `isinstance('apple', str)` and `isinstance('apple', object)`. Unlike `isinstance`, `type` looks only at an object's lowest type in the hierarchy. Can you compare and explain the values of `isinstance('apple', object)` and `type('apple') == object`?

**6.21.** What does this code do: `isinstance(bool == bool, bool)`? What is the output and why? <!-- p4l -->

**6.22.** `help` is a built-in function that gives you information about other functions. Try `help(max)`, `help(min)` (pressing `q` lets you quit the help screen).

**6.23.** ⭐ Use the `help` function to find out about the `round` function. Explore how to use it, with one and with two arguments. <!-- p4l -->

**6.24.** Use `type` to test whether `round` changes a float into an int. If so, does it _inevitably_ do this?

**6.25.** Something seems to be wrong with the following code, which was supposed to print the result `2`. Can you spot the mistake and fix it? This mistake is easily made, so it helps if you recognize the error message.
```python
a = 1 + 3,
b = a / 2
print(b)
```
(Later we will learn more about the type of object that is the culprit, i.e., a tuple, and about the syntax that defines such objects.)

**6.26.** Use `help` to learn more about the `print` function. You will likely not understand everything it says, but you can play around with the parameters `sep` and `end`.

**6.27.** ✉️ _(Don't forget to submit!)_ ⭐⭐ In a Python script, write a program that asks for the user's age in years and prints several things: their age in months, their age in weeks, their age in days, their age in hours, their age in minutes, and their age in seconds; you can ignore leap years (and make other simplifying approximations). Is your program making the same (pieces of) computations multiple times? If so, consider storing intermediate results in auxiliary variables.

**6.28.** ✉️ ⭐ Write a program that uses `input` to ask the user for the time now (in hours), and subsequently asks for the number of hours to wait. Your program should store each user response in a variable, and print what the time will be on the clock when the alarm goes off. <!-- tp3 -->


**6.29.** ✉️ ⭐ Suppose we have a variable storing an integer, say `x = 56784921`. Write an expression to count how many _digits_ the number has (for instance, `623` has three, `62712` has five). 

- - - - - -
**Something to keep in mind:** In programming, an important part of the solution to any problem is often: _how should I represent my data?_ For instance, should you represent a number as an int or as a string? If the goal is to do arithmetic, it makes sense to treat it as a number; but if the goal is to count digits, it can be helpful to first represent the number as a string.
- - - - -

**6.30.** ⭐ When doing linguistic research, what kinds of data would you likely represent in the form of strings? What could be some linguistic uses of integers? What about floats?




-------

**_The homework exercises for week 3 end here (don't forget to submit those marked by '✉️'!)._**

-------

