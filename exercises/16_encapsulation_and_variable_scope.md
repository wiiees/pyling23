# Python for Linguists 2023

## 16. Encapsulation and variable scope

Effort profile: `▁▁▁▂▁▁▁▂▁▁▁▁▂▁▁▁▁▁▁▁▁▂▂▁▁▂▁█` 



<br>**_Order of execution_**

**16.1.** Earlier we saw what happens if you call a function _before_ defining it. Try this again.

**16.2.** The foregoing exercise should have resulted in an error. A Python program will terminate when an error is encountered (or more accurately: when an exception is _raised_ and not _caught_ somewhere higher up). Nevertheless, you may occasionally have seen noticed printed output appearing _after_ (i.e., below) an error message. Try to reproduce this oddity: Write some code that prints a bunch of stuff and then, at the end, does something illegal (e.g., reference a function before it is defined). Run it to verify that the error message can (at least sometimes) appear in the output before (i.e., above) the printed message. (If this never happens, perhaps your system is configured in a way that prevents this.)

- - - - - -
**Something to keep in mind:** The command `print` sends content to the **standard output stream**, while error messages go through a separate **error stream**. Each stream is 'buffered', meaning messages are first stored in a 'buffer' that is then, periodically, 'flushed' onto the Run output window on your screen -- only _then_ do you see the output. It can happen that the error buffer is flushed _before_ the standard output buffer, and thereby cause an error message to appear _before_ certain printed messages, even if the error was in fact encountered a few nanoseconds _after_ the last `print` command. This is a technicality, but knowing about this can prevent confusion about the (apparent) source of an error.
- - - - -

**16.3.** If in the previous exercise you were able to let an error message appear before the printed messages, now add `flush=True` as an extra argument to your `print` statements (or at least the last one before the error) and try again. The error message should now consistently appear last (i.e., at the bottom of your output). This is because `flush=True` tells Python to flush the standard output buffer immediately, i.e., as soon as the `print` command is given. Although you won't normally need to use `flush=True`, you can use it in the following exercises if you find the order of print and error messages in your output confusing.

**16.4.** ⭐ Define a function `invert` that takes a string and returns the inverted string, and then define a function `print_inverted` that takes a string and (inside its definition) calls the `invert` function to invert it, and finally prints the result (with `flush=True` for clarity). The point here is that we have one function (`print_inverted`) that, in its definition body, references another (`invert`). Does the order in which the two functions are defined matter? Formulate a prediction, then test it. Try to form a hypothesis about why this might be.

**16.5.** Test and (if needed) refine your hypothesis about the order of function definitions and function calls, by comparing two versions of the following program (uncomment either line A or line B).

```python
def print_sum(a, b):
    print(add_numbers(a, b), flush=True)

# print_sum(1, 3)    # Line A
    
def add_numbers(a, b):
    return a + b

# print_sum(1, 3)    # Line B
```


- - - - - -
**Something to keep in mind:** A Python script is interpreted **top-to-bottom**. However, recall from the previous section that _functions are not pieces of code_, and calling a function does _not_ mean 'sending the interpreter to the line where the function is defined'. Rather, functions are objects, that are created and stored in working memory when the interpreter (going top-to-bottom) encounters a `def`-clause. Calling a function means invoking the `__call__` method of that (previously created) function object that is already in working memory. At no point does the interpreter 'go back' to the line where the function is defined.
- - - - -

**16.6.** The foregoing also means that the interpreter has to read and process the function definition's body somehow, but without yet executing it (as the latter should happen only when the function object is called, after all). Can you reconcile this with the fact that, in the body of one function definition A, you can call some other function B even if function B is _defined_ later in the file than function A (as long as A isn't _called_ before function B is _defined_). Also review your understanding of the preceding two exercises.

**16.7.** Write a function `time_to_secs` that takes three arguments -- hours, minutes, seconds -- and converts the time these jointly represent to a total number of seconds, which it returns as output. If necessary extend `time_to_secs` so that it can cope with real (i.e., non-integer, or floating point) values as inputs. It should always return an integer number of seconds ('truncated', or rounded down). <!-- tp3 -->

**16.8.** ⭐ Write three functions that are the partial _inverses_ of `time_to_secs`: 
 1. `hours_in` returns the whole integer number of hours represented by a total number of seconds; 
 2. `leftover_minutes_in` returns the whole integer number of _left over_ minutes in a given total number of seconds, once the hours have been taken out; 
 3. `leftover_seconds_in` returns the left over seconds in a given total number of seconds, once the hours and minutes have been taken out. 

 You may assume that the total number of seconds passed to these functions is an integer. <!-- tp3 -->

**16.9.** Write a single function that is the inverse of `time_to_secs`. It takes a total time in seconds as argument, and it should use the preceding three auxiliary functions to obtain hours, minutes and seconds in that total time, and return these values together in a 3-element list. Does the order matter in which the various function definitions (main and auxiliaries) appear in your file? What about the position of the function calls?



<br>**_Encapsulation and variable scope_**

**16.10.** What are some reasons for subdividing your code into functions? 


**16.11.** An important reason for subdividing (or 'chunking') your code into functions is **encapsulation**: variables assigned inside a function, are not accessible outside it. This keeps the number of accessible variables at a given place in your code smaller, which helps prevent certain types of programming errors. Explain how the following code illustrates encapsulation. (Remember `flush=True` lets a print statement flush the print buffer directly, in order for printed output and error messages to appear in order of execution.)

```python
def some_function():
    b = 123
    print('inside the function, b =', b, flush=True)

some_function()
print('outside the function, after calling the function, b =', b)
```


**16.12.** In the previous example, what happens if you assign something to `b` also in the global scope, before the function definition? For instance, add `b = 789` (a different value) above the definition of `some_function`.

**16.13.** ⭐ And what happens if you now remove the line `b = 123` from the function (while keeping `b = 789` above the function definition)? What gets printed? This and the foregoing exercises show that there is some kind of asymmetry between local scope and global scope with regard to variable accessibility. Try to formulate in your own words what this asymmetry is (further below it will be stated in more precise terms).

**16.14.** Unlike `def`-clauses (function definitions), `if`-clauses do not create a local scope, i.e., do not encapsulate the variables assigned within it. Explain how the following example demonstrates this:

```python
if 1 + 1 == 2:
    x = 'test'
    print('inside the if:', x)

print('outside the if:', x)
```


**16.15.** Does the following example demonstrate that `for`-clauses likewise do not encapsulate their variables?

```python
for x in [1, 2, 3]:
    print('inside the for:', x)

print('outside the for:', x)
```


**16.16.** Does the following code show that `if`-clauses do create a local scope after all, contrary to the claim above? Or does it show something else?

```python
if 1 + 1 == 3:
    x = 'test'
    print('inside:', x)

print('outside:', x)
```


**16.17.** What about an `if`-`elif`-`else` compound clause? Are variables assigned in the initial `if`-clause accessible in subsequent `elif` and `else` clauses? (Does the question even make sense?)

**16.18.** The built-in functions `locals` and `globals` give you a _dictionary_ containing all local/global variables and their values. When running the code below, note that among the global variables are many 'dunder' (double underscore) variables like `__name__` that Python relies upon for bookkeeping (this particular one will be explained later). This means that you may need to scroll to the right to see the non-built-in variables you yourself assigned.

```python
a = 3
b = 4

def my_function(c):
    d = 6
    e = 7
    print('inside my_function, locals = ', locals())
    print('inside my_function, globals =', globals())

my_function(5)
```


**16.19.** In the above example, the local scope also contains a variable `c`. Where does it come from, i.e., where is it assigned its value?

**16.20.** Modify the above example to print `globals()` and `locals()` also from _outside_ the function definition, e.g., put the print statements below the function call. What does this demonstrate?

- - - - - -
**Something to keep in mind:** When Python enters a local scope (e.g., function definition), `locals()` is initially empty. If a variable is _assigned_ a value inside a local scope (e.g., inside a function definition), this variable+value will be stored in `locals()`, not `globals()`. When a variable's value is _retrieved_ inside a local scope, Python will first try to find it in the `locals()` dictionary, and only if it does not find the variable there it will look in `globals()`. (Actually there are two other 'namespaces' in which Python will search for a variable: Python indeed first looks in the local scope, but then it checks the immediately 'enclosing scope' (e.g., if the function is itself contained in a function or class), before considering the global scope, and finally it looks among the `__builtins__`, for built-in functions such as `len` and `print`.)
- - - - -

**16.21.** We have seen that variables defined inside functions can have the same name of an existing variable from outside the function, without the latter being affected. Explain exactly how this can be.

**16.22.** ⭐ For every place in the following code where the value of a variable is retrieved, determine the place where its value at that point was assigned. Take into account mutability: mutable objects like lists can be changed _without_ this involving reassigning the variable. While you're at it, a good exercise is to try to predict the exact output of this program.

```python
students = ['ann', 'beth', 'gemma']
more_students = ['dale', 'ebba']
message = 'Hello!'

def print_students(students):
    students = [name.capitalize() for name in students]
    for student in students:
        print(message, student)

students[1] = 'elisabeth'
all_students = students + more_students
all_students.append('philip')
print_students(all_students)

if len(all_students) > 3:
    message += ' Nice crowd!'
    print(message, flush=True)
```


**16.23.** ⭐ The above 'something to keep in mind' left out an important detail: when a variable is assigned a value _anywhere_ in the local scope, then that variable becomes _strictly local_ to that scope, meaning Python will _only_ try to find it in `locals()`, and _never_ look for that variable in`globals()`, _even if the lookup in locals() (kind of) fails_. This can cause surprising behavior. Try to predict what the following code does, test your prediction, and reconcile your findings with the rules for encapsulation explained so far.

```python
a = 5

def erroneous_function():
    print(a)
    a = 8

erroneous_function()
```


**16.24.** What might one naively expect the following function to print? Explain why this expectation is wrong, namely, why the following gives an error:

```python
b = 10

def bad_function():
    b += 3
    print(b)

bad_function()
```
 <!-- amy -->

**16.25.** The foregoing exercises reveal that a variable inside a function is either local or global, _never_ local on some lines (in the function) and global on other lines (in that same function). Can you think of a possible benefit of this all-or-nothing behavior?

**16.26.** ⭐ Try to predict the entire printed output of the following program, and test your prediction:

```python
x = 6

print(x)

def first_function(x):
    print(x)

def second_function():
    print(x)

def third_function(y):
    x = y - 3
    print(x)

print(x)
first_function(3)
print(x)
second_function()
print(x)
third_function(x)
print(x)
```


**16.27.** Does the foregoing mean that there is _no_ way to have a function assign a value to a global variable? Well, you may not ever need this, but there is a way: for a given variable `x`, typing `global x` at the top of the body of a function definition will make sure that `x` in that function serves as a global variable, even if you assign something to `x` in that function later (result: it will assign to a global variable). Play around with this if you like. But the more important take-away of this section is how Python governs variable scope (hence, why something like the `global` keyword would be needed in the first place) -- try to summarize that.

**16.28.** ⭐⭐⭐ Predict what the following code prints out, then carefully go through your calculations once more until you are somewhat confident in your prediction, and finally test your prediction by running the code. In case you do not fully understand but want to, consider watching this explanation: https://www.youtube.com/watch?v=jXugs4B3lwU (the code below is taken from 'level 6' in this video).

```python
# Code from https://www.youtube.com/watch?v=jXugs4B3lwU

x = "global x"

def level_six():
    
    z = "outer z"
    
    def donky():
        def inner(y):
            return x, y, z
    
        z = "donky z"
        return inner
    
    def chonky():
        x = "chonky x"
        f = donky()
        return f("y arg")

    return chonky()

print(level_six())
```



