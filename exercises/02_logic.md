# Python for Linguists 2023

## 2. Logic (`and`, `or`, `==`, `=>`, ...)

Effort profile: `▂▁▁▁▁▂▁▁▁▁▁▁▂▂▄▅▁▄▅▂▁▁▂▂▄▅▄▅▁▂▁▁▁▂` 





**2.1.** ⭐ In maths, it is common to compare numbers or variables with _greater than_, _smaller than_, _not equal to_, and so on. Experiment with the operators `>`, `<`, `!=`, `>=`, `<=` to figure out what they do.

**2.2.** Put the `not` operator in front of some of the expressions you tested, like `not (3 >= 4)`. What does it do? Inspired by the meaning of the operator `!=`, could you also use exclamation mark `!` instead of `not`?

**2.3.** When using the `not` operator, can you leave out the parentheses, like `not 3 >= 4`? Compare this how the `max` function behaved above.

**2.4.** If the operator `not` hadn't existed, what expression could you use instead of `not (3 >= 4)`? 

**2.5.** What do you expect `not True` and `not False` to evaluate to? Test your expectation. 

**2.6.** ⭐ Explore how boolean operators `and` and `or` work. Does `or` correspond to inclusive or exclusive _or_?

**2.7.** First do `cloudy = True` and `windy = True`, and `sunny = not cloudy`, and then write a Python expression to test whether it is nice day to go to the beach for flying a kite.

**2.8.** Ooh, the weather changes! Reassign `cloudy = False`. Did the variable `sunny` automatically update as well? Why (not)?

- - - - - -
**Something to keep in mind:** Variables are 're-assigned' independently of one another. Even if two variables are initially made to refer to the same thing, reassigning something to one variable doesn't automatically reassign the other.
- - - - -

**2.9.** Assign `my_variable = 6`. What happens if you subsequently do `my_other_variable = my_variable`? What if you then reassign `my_variable = 20`, can you predict what happens to the value of `my_other_variable`? Test your prediction.

**2.10.** Predict, test and explain the difference between `not sunny or cloudy` and `not (sunny or cloudy)`.

**2.11.** Verify your previous explanation by considering the table of **operator precedence** in Python: https://docs.python.org/3/reference/expressions.html#operator-precedence

**2.12.** First enter `n = 42`, and then `n == 42`. What is the result? What about `n == 43`? What happens if you try to assign a new variable with `==`, e.g., `z == 123` (assuming you haven't used `z` before)?

**2.13.** ⭐ What does this code do: `a = 3 == 3`? What is the result and why? What's the difference between that code snippet and this one: `a == 3 = 3`? Why does the latter produce an error? <!-- P4L -->

- - - - - -
**Something to keep in mind:** While single `=` is used for **assigning** a value to a variable, double `==` tests for **equality**. It matters how you read them, whether mentally or out loud. If you read both simply as _'is'_, you are prone to confuse yourself.
- - - - -

**2.14.** ⭐ Write expressions that are logical opposites of the following (i.e., get opposite truth values):
1. `a == b` 
2. `a > b` 
3. `a >= b` 
4. `a >= 18 and b == 3` 
5. `a >= 18 and b != 3`.  <!-- TP3 -->


**2.15.** ⭐⭐ For each of the following equivalences, determine (first without Python) whether you can make the equivalence come out as `False` by assigning certain truth values to the atomic variables `p` and `q`, and then use Python to verify.
1. `(p or q) == (p and q)`
2. `(not p or not q) == not (p or q)`
3. `(p or q) == (q or p)`
4. `(p or not p) == (q or not q)`
5. `(not p or not q) == not (p and q)`

**2.16.** If in the previous exercise you had to try the same expressions a couple of times (with different truth values assigned to `p` and `q`), then hopefully you remembered to use the up arrow in the Console to cycle through previous commands.

**2.17.** ⭐⭐ Do the same, but now with three variables `p`, `q` and `r` to play with: can you assign truth values to them in a way that makes the following equivalences come out as `False`? (This is tricky! You can either try to reason your way towards the solution, or simply try out different possible variable assignments.)
1. `(p or (q and r)) == ((p or q) and r)`
2. `(p and (q and r)) == ((p and q) and r)`
3. `(p or (q or r)) == ((p or q) or r)`
4. `(p or (q and r)) == ((p or q) and (p or r))`
5. `(p and (q or r)) == ((p and q) or (p and r))`

**2.18.** ⭐ Some of the previous exercises revealed that in some cases the parentheses don't seem to make a difference. Can you safely omit them in those cases? What if you omit them in the cases where it _does_ make a difference? Try to predict the result and then test it with Python. Can you explain what you see with the help of specific operator precedence rules (https://docs.python.org/3/reference/expressions.html#operator-precedence)?


**2.19.** Keywords like `and` and `or` are special, reserved terms that are handled by the syntactic parser _before_ any Python code is interpreted. Because of this, they cannot be used as ordinary variables, e.g., assigned new values. Demonstrate this by trying to assign something to a variable named `and`.

- - - - - -
**Something to keep in mind:** Python has various **built-ins** and **keywords** (or operators). Calling a built-in function (like `max` and `min`) requires parentheses directly following the function name (`max(...)`). By contrast, keywords (such as `not`, `and`, `or`) are followed by a space (e.g., `not 3 >= 4`) and do not require parentheses (though they can increase readability_ (e.g., `not (3 >= 4)`, note there's still a space), and they can also matter for operator precedence, see exercises below).
- - - - -

**2.20.** In contrast to keywords, built-ins (e.g., functions like `max`) _are_ assigned to ordinary variables, hence these can also be reassigned new values. For instance, try `max = 5` or `min = 7`. If you do this, what happens if you subsequently try to get the maximum or minimum of some numbers like you did earlier, e.g., `max(3541, 7312)`? Overriding built-ins like this is not a good idea. (Consider restarting the Console to prevent confusing your future self.)

**2.21.** ⭐ Many types of objects that are not themselves booleans can nevertheless be evaluated to `True` or `False` when placed in a 'boolean context' such as the argument of the `not` operator. This is the case for numbers, for instance, and we will learn about other objects like strings later. Try to understand which numbers are **Truthy** (i.e., get interpreted as `True` when placed in a boolean context) and which are **Falsy**, by predicting and testing the resulting truth values of the following expressions:
1. `not 1`
2. `not 0`
3. `not -1`
4. `not 0.0`
5. `not 6.3`

**2.22.** ⭐ Given the foregoing, can you predict the value of `not (0 + 1)` vs. `not 0 + 1`? Verify your prediction, and compare it with `not (False or True)` vs. `not False or True`. Make sure you understand this potentially puzzling behavior (see again the _operator precedence_ table).

**2.23.** ⭐⭐ Similar to `not`, the boolean operators `and` and `or` create a 'boolean' context, in which numbers end up being interpreted as 'truthy' or 'falsy'. But in Python, `and` and `or` they are not strictly boolean. If `p` as well as `q` evaluate to `False`, then `p and q` evaluates to False; but if `p` as well as `q` evaluate to `True` then `p and q` evaluates to `q` -- which happens to be `True` if `q` was itself a boolean, but we have seen that `q` can also be a number. Illustrate this not-purely-boolean behavior of `and` by comparing `0 and 0`, `0 and 3`, `3 and 0`, `3 and 6` and `6 and 3`.

**2.24.** ⭐⭐ Does `or` display similarly non-purely-boolean behavior? Compare `0 or 0`, `0 or 3`, `3 or 0`, `3 or 6` and `6 or 3`, and try to identify the underlying rule (i.e., fill in "if `p` as well as `q` evaluate to True, then `p or q` evaluates to [...]").

**2.25.** It is easy to mistakenly type `&` instead of `and`. Are they equivalent? Try comparing `True and False` to `True & False`, and other variants. If your answer is 'yes', what about numbers, which previously you learned can be Truthy and Falsy too? For instance, compare `3 and 5` to `3 & 5`, and also try different combinations of numbers. (Unless you know a bit about representating numbers in binary, like `1101` meaning 13, it will be virtually impossible for you to figure out the pattern without looking it up in the documentation.) _In general, for boolean logic dealing with truth values, use only `and`, not `&`._

**2.26.** ⭐ What do you predict these expressions to evaluate to? If you make a mistake, make sure you understand why you had the wrong expectation! (There is something purposefully misleading about some of these...)
1. `3 == 3`
2. `3 != 3`
3. `3 >= 4`
4. `not (3 < 4)`
5. `3 % 4 == 0`
6. `3 % 4 == 3`
7. `3 / 4 == 0`
8. `3 // 4 == 0`
9. `3+4 * 2 == 14`
10. `4 - 2 + 2==0` <!-- TP3 -->

**2.27.** Write a simple expression to check whether a given number `x` is odd or even.

**2.28.** If you have used the Python console for a while, enter `dir()` in the interpreter to show the 'directory', a list of names of all objects currently available (at least those in the _global scope_, about which we will learn later). As you will see, any variables previously created still exist (alongside some automatically created variables like `__name__`, about which we will also learn later). In PyCharm's Python Console, variables and their values are also standardly displayed in a separate panel on the right.

**2.29.** If you mistype e.g. `maxx(1, 2, 3)` instead of `max(1, 2, 3)`, you would normally get the informative error _Name is not defined_ to notify you of this mistake: the name `maxx` does not appear in the `dir()`. But what if you defined a variable `maxx = 5` a while ago and you forgot about it? If you then make the typo `maxx('apple')`, the error you get will seem a bit more mysterious. Try this.

- - - - - -
**Something to keep in mind:** If you keep too many old names hanging around in the interpreter, this can make it more difficult to _detect mistakes_. To reduce this problem, occasionally restart your Python console (especially if you keep getting unexpected results).
- - - - -

**2.30.** ⭐ Given two integer numbers, assigned to variables `x` and `y`, what is the truth value of `x == (y * (x // y) + x % y)`. Can you change the truth value by changing the numbers assigned to `x` and `y`? How / why not?
