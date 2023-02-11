# Python for Linguists 2023

## 5. Scripts (`.py`-files, and the functions `print` and `input`)

Effort profile: `▁▁▂▁▁▁▁▁▁▂▁▁▁▂▂▁▂▁▁▁▂▁▁▂▁▁▁▁▁▁▂▁▁▁` 



**5.1.** Create a Python file (e.g., `exercises5.py`), open it in the editor (if not opened automatically), enter `print('Hello, world!')` in the file and run it (cf. Section 0).

**5.2.** If the printed output `Hello, world!` appeared in the **Run** panel at the bottom of the screen, perfect! This is generally how we will be running our scripts. However, if the output appeared instead in the **Console** panel, then you may have hit the wrong hotkey. Fix this by editing the _run configuration_ for this script: in the toolbar (top right), click the drop-down list (currently likely showing `exercises5`) and from the list click `Edit configurations...`. There, in the run configuration for the script `exercises5.py`, make sure the option `Run with Python console` is _disabled_. Then try to run it again (`shift`+`F10`, or the green 'play' button).

**5.3.** ⭐ Recall that the Python Console always displays the last result, e.g., typing `'apple'` and hitting Enter will make the string `apple` be echoed back to you. Similarly, entering `a = 'apple'` and then entering `a` will show `apple` again. Verify that this is _not_ the case when running a script: adding the line `'apple'` to your script and running it will not output `apple`. This is why, when working inside a script, you need an explicit `print` statement to show any output.

**5.4.** Is `print` a built-in function (just like `max` and `len`) or an operator?

**5.5.** Does `print` also work in the Console?

**5.6.** In the print statement in your script, what happens if you leave out both of the parentheses and run the script again? What happens if you leave out only the opening parenthesis? Or only the closing parenthesis? <!-- TP2 -->

- - - - - -
**Something to keep in mind:** Like many IDEs, PyCharm will often auto-complete your parentheses, quotation marks, etc. So if you want to see what happens if you do something wrong _on purpose_, as required for these exercises, pay attention that PyCharm didn't auto-correct you.
- - - - -

**5.7.** If you are trying to print a string, what happens if you leave out one of the quotation marks? (Try both the starting and the ending quotation mark.) What if you leave out both quotation marks? What might the error messages mean? <!-- TP2 -->

**5.8.** Do you expect both single and double quotation marks around the string to work inside a print statement (`print('cheese')` and `print("cheese")`)? What happens if you mix different types of quotation marks? Why?

**5.9.** What happens if you enter `primt('cheese')`? What happens if you enter `print('cheeze')`? Can you explain why?

- - - - - -
**Something to keep in mind:** Whenever you learn something new, stick with it for a while, to explore different variants and find ways to break it. By consciously introducing errors and learning to recognize what happens, you will become good at diagnosing the problem when you make unintentional mistakes later.
- - - - -

**5.10.** ⭐ In the Python Console, is there a difference (in the resulting output) between entering `print('abc')` and entering `'abc'`? What if you enter `abc` (without quotation marks)? Next, can you predict (and then test) whether entering `abc = 'abc'` into the Console followed by `abc` (without quotation marks) will show quotation marks in the output or not? 

**5.11.** What happens if you split a print statement over multiple lines, like below. Experiment with different places of putting the newline; which places are permitted and which give an error?

```python
print(
'Hello, world!')
```

**5.12.** Can you print only strings, or also numbers? And `True` or `False`? And the truth value of a larger logical expression?

**5.13.** Can you assign a print statement to a variable, like `test = print('Hello!')`? What is the content of the resulting variable? Can you compare this to how other built-ins like `len` or `max` behave? Try to relate this to the following idea: some functions _do_ something, while other functions _give_ something back.

**5.14.** ⭐ Explain what happens in the Python Console vs. running a Python script containing the same code, comparing: 
- `print('cheese')` vs. `'cheese'` 
- `print(n)` vs. `n` (assuming `n` still has a value from before)

An adequate explanation should probably invoke the distinction between strings and string literals.

**5.15.** ⭐ While the Python console is useful for trying out a single command, writing longer programs is much more convenient to do in a file in the editor. Can you think of some reasons why?

**5.16.** Create another `.py` file with some code in it, and find out how you can switch between running one file vs. the other.

**5.17.** ⭐ Do you remember how the Python interpreter in the Console keeps all the old variables around until you restart the interpreter? Verify that running a Python script (at least in the 'normal' way) starts a Python interpreter from scratch. In particular, show that it removes any variables defined in a previous run. (Hint: You can test this by first running a script that creates a certain variable and then prints it, then remove the variable creation and try to run it again.)


**5.18.** In fact, `print` can take multiple arguments, e.g., `print('apple', 'pear', 'banana')`. Show this. Why doesn't `print('Hello', 'world!')` print `Hello, world!`?

**5.19.** Write a `print` statement that, given a string `s` and an integer `cut_at`, prints two substrings: the starting portion until the position indicated by `cut_at`, and the remainder.

**5.20.** In a script, try placing a hash `#` before a line of code that previously worked, and record what happens when you rerun the program.

- - - - - -
**Something to keep in mind:** Any text or code preceded by a hash (`#`) is ignored by Python, as it represents a comment meant for humans.
- - - - -

**5.21.** ⭐ In all of the Python scripts you create, add a _comment_ with the exercise number above the relevant chunk of code, e.g., `# Ex 5.20`, so that you can retrieve your own solutions later. 

**5.22.** Is the above 'something to keep in mind' really true? What if the hash occurs in quotation marks?

**5.23.** What does the built-in function `input` do? Write a script containing `name = input('What is your name?')` and run it. In the Run panel you will see that you can now type your name (and hit Enter when done). What happens? Modify the script to subsequently print the contents of the variable `name`, and re-run the script to verify your understanding.

**5.24.** ⭐ In a Python script write a program that uses `input` to ask for the user's name, and in response let it print `Hi [name], how are you?`, with the name the user entered.

**5.25.** Python's **format strings** can help you easily print stuff in a readable format. You can create a format string in many ways; an easy way is to prefix the string with an `f`, i.e., before the initial quotation mark. Inside a format string, curly braces can contain any Python expression. Make sure `name` contains a string, and try the following:

```python
print(f'Hi, my name is {name}, which starts with "{name[0]}" and is {len(name)} characters long!')
```

**5.26.** What happens if you forget the `f` prefix in the above example?

**5.27.** What happens if you want to print a format string, but somewhere in the curly braces it references a variable that does not exist?

**5.28.** Try printing the same stuff _without_ using a format string. Which version of the print statement do you find more readable?

**5.29.** Format strings have many more options; see what the following do:

```python
my_number = 6.1239871
print(f'{my_number} or {my_number:.6f} or {my_number:.4f} or {my_number:.2f}')

my_string = 'just testing'
print(f'left {my_string:>40} right')
print(f'left {my_string:<40} right')
print(f'left {my_string:^40} right')
```


**5.30.** While programming languages tend to have a strict syntax, programmers still have considerable freedom, for instance in how they name their variables or where to put spaces. For code safety as well as reusability, consistent code style is important. Why, do you reckon?

**5.31.** ⭐ A Python 'style guide' is kept in the eighth _Python Enhancement Proposal_, or **PEP8** (https://www.python.org/dev/peps/pep-0008/). Have a look at it! Highlight some guidelines that you were already familiar with, some that you were perhaps unaware of but kind of understand, and some which you don't understand (yet).


**5.32.** Does the PyCharm editor warn you of violations of Python style? Construct some code examples to test/demonstrate this.

- - - - - -
**Something to keep in mind:** Python is a very open, community-driven programming language. It has come to be the way it is with the help of **Python Enhancement Proposals** or PEPs (https://www.python.org/dev/peps/). **PEP8** contains the Python style guidelines.
- - - - -

**5.33.** To give another example, **PEP285** (https://peps.python.org/pep-0285/) introduced the boolean values `True` and `False` into the language (in 2002; previously one would simply use integers `1` and `0` to represent boolean values). Browsing through this PEP (especially the sections Review and Rationale) can give you an impression of the kinds of considerations that go into designing a programming language (and perhaps an appreciation of the effort).


**5.34.** Earlier we learned that keywords are special reserved terms that are handled by the syntactic parser before any Python code is interpreted. You demonstrated this in the Console by trying to assign something to a variable named `and`. Now, demonstrate the same within a Python script, but this time also show that even code that occurs _before_ the problematic line does not get interpreted.


