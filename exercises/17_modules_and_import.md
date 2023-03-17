# Python for Linguists 2023

## 17. Modules (`import`, `__name__`)

Effort profile: `(▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▂▁▁▁▁▁▁▁▁▁▁▁▁)` 




----

🦉 **_This entire section is OPTIONAL!_**

----


**17.1.** What are some reasons for subdividing your code into functions? Can you also think of a more long-term kind of benefit?

**17.2.** Suppose you have two ongoing, distinct research projects about n-grams. They are quite different, so you use a separate Python script (`.py`-file) for each project. To illustrate, create two such files, say `project_1.py` and `project_2.py`. Suppose both projects require a function `ngrams` for extracting n-grams from a text. Defining the same function in both project files would violate the DRY principle (which exists for good reason: do you remember why repetition in code is bad?). What might be a better solution, in abstract terms?

**17.3.** Create a separate file `text_utils.py` ('text utilities'), and, in it, define a function `extract_ngrams` which takes a text (string) and a number `n` as input and returns its n-grams. Since the `extract_ngrams` function relies on tokenization, it might be good if a `tokenize` function is defined in the same file as well. You can reuse code from previous sections, or treat this is an extra exercise and code them from scratch.

**17.4.** Now, in your file `project_1.py` include the code `import text_utils`. Verify that you can then call its `extract_ngrams` function as follows:

```python
text_utils.extract_ngrams('The quick brown fox jumped over the lazy dog.', 2)
```


**17.5.** Now do the same in the file `project_2.py`. Does this overall approach, in which you place shared code in a separate file to import, match your answer to 17.2, or did you have something else in mind? 

**17.6.** Play around with the foregoing code. What happens if you accidentally include the file extension `.py` in the `import` statement, e.g., `import text_utils.py`? What happens if you mistype the name, e.g., `import textutils`?

**17.7.** After importing `text_utils`, do `print(text_utils)` and `print(type(text_utils))`. This shows that importing a Python file creates a _module_ object. All code in the imported file is executed relative to that object, such that any variables and functions defined have to be called as attributes on that object (e.g., `text_utils.extract_ngrams`). Try `dir(text_utils)` to see all names available in the `text_utils` module. Compare this to plain `dir()` (with no argument), which lists all names available in the global scope of the main file being run, e.g., `project_1.py`.

**17.8.** Does `dir()` when executed inside `project_1.py` also list `text_utils.extract_ngrams`, or only the parent module `text_utils` as a whole?

**17.9.** Do only _functions_ defined in `text_utils.py` become available when you import this module elsewhere (e.g., in `project_1.py`), or also plain variables? Test this.

**17.10.** Try to remember (or look up) some other exercises where we used `import`. There, we used it to access functions from ready-made Python modules, whereas here we are using it to access functions in our own, custom-made module `text_utils`. 

**17.11.** Can the same Python file import both a custom module (e.g., `text_utils` and existing modules (e.g., `random`)? Demonstrate this by extending the `project_1.py` file with code that prints a random n-gram.

**17.12.** Does importing standard Python modules such as `random` result in a similar 'module' object as importing your own `text_utils.py`?

**17.13.** In PyCharm you can ctrl+click (or cmd+click) on `random` (e.g., its occurrence in `import random`, or in a call to, for instance, `random.randrange`), which brings you to the file `random.py`: this file is part of the standard Python library which lives somewhere in your computer. (Note: This does not work for all modules: if the underlying module is implemented in C rather than Python itself, PyCharm will bring you to an automatically generated 'placeholder' file, which basically shows only the function names and some documentation, but not their actual definitions.)

- - - - - -
**Something to keep in mind:** Some terminology: a _module_ is a Python file that is (meant to be) imported into another, whereas a _script_ is a Python file that is meant to be executed as such. (Relatedly, a _package_ is a collection of related modules that can be imported together, and the term _library_ is sometimes used more loosely for some collection of code designed for a certain coherent set of purposes (in one or multiple modules).)
- - - - -

**17.14.** Do you remember that, ideally, functions should either _do_ stuff (e.g., print something, modify a list in-place) or _return_ stuff (e.g., return a new list), and not both? Can you think of a way to apply this same principle to scripts like `project_1.py` vs. modules like `text_utils.py`?

**17.15.** Place a simple, recognizable command like `print('Hello from text_utils!')` in `text_utils.py`. Verify that running `text_utils.py` itself prints this string. What happens if you now run `project_1.py` again, in which `text_utils.py` is imported?

**17.16.** Modules and other Python objects have a special field called `__name__`. In `project_1.py` add the print statement `print('The name of project_1.py is:', __name__)`. Inside `text_utils.py` add `print('The name of text_utils.py is:', __name__)`. Execute each file separately, and try to understand what gets printed in each case.

**17.17.** Can you also access the `__name__` field of an imported module? For instance, in the `project_1.py`, try to access the `__name__` field of the imported `text_utils`.

- - - - - -
**Something to keep in mind:** The `__name__` attribute of a script or module differs depending on whether a file is run as its own script, or imported by another as a module. If it is run on its own, then `__name__ == '__main__'`; otherwise `__name__` will be derived from the filename of the imported file.
- - - - -

**17.18.** Use the foregoing to change `text_utils.py` as follows: create an `if`-clause that checks if the file is run as the main file. Move all the print-statements in `text_utils.py` to the body of the if-clause: these are executed only if the file is run on its own, and not if it is imported elsewhere. Verify that this is the case.

**17.19.** What happens if, still in `text_utils.py`, you also move the function definition of `extract_ngrams` to the body of the if-clause? Can you then still call that function from within `project_1.py`? Why (not)? (Revert this change for what follows.)

**17.20.** If you are coding in PyCharm, note that the editor puts a little green 'run' arrow in the margin left of the if-clause: from its presence it recognizes that the code can be run as a script, not (just) imported in another.

**17.21.** A bit of an aside: functions have names too, e.g., try printing `max.__name__` for the built-in function `max`, or `text_utils.ngrams.__name__` for your own function `ngrams`. What happens to the `__name__` property if you assign an existing function to a new variable, e.g., `get_maximum = max`? Is the function's name changed along with it? Why (not)?

**17.22.** What if you create a file with the same name as an existing module, e.g., create `random.py` containing just a print statement `print('Greetings from fake random.py!')`, and then in `project_1.py` do `import random`. Does Python give priority to the standard module, or to the user-defined file? (You can test this for instance with `dir(random)`.)

**17.23.** How does Python know where to find the right files to import? Do `import sys` (a standard module with various system tools) and then `print(sys.path)`. This lists all the paths (to memory locations somewhere on your computer) where Python will look, one after the other, to find a standard module or user-created file with a matching name.

**17.24.** ⭐ To solidify your understanding of `import`, create two new files, `file_a.py` and `file_b`, containing the code given below. Try to predict (and subsequently test) what gets printed if you execute `file_a.py`, and also what if you execute `file_b.py`:

```python
# Put the following in file_a.py:
import file_b

print('Hohohoho!')

def laugh():
    print('Hahaha!')

if __name__ == '__main__':
    laugh()
    file_b.cry()

# Put the following in file_b.py:
def cry():
    print('Boohoo...')

if __name__ == '__main__':
    print('I\'m so sad...')

print('Ayayay!')
```


**17.25.** ⭐ Explore the `import` mechanism further. Suggestions: What happens if, in `file_a.py`, you call `laugh` like this: `file_a.laugh()`? What happens if a file tries to import itself? What happens if two files import each other (e.g., in `file_b.py` add `import file_a.py`)? What happens if you place an import statement at the bottom of your file instead of at the top? What happens if you create a file `file_c` _without_ the customary Python extension `.py`, and try to import it?

- - - - - -
**Something to keep in mind:** Python files can both _define_ stuff (e.g., define functions) and _do_ stuff (e.g., call functions). By convention (and for good reason), a file should _do_ stuff only if it is run as the main script, i.e., if `__name__ == '__main__'`. That is why any function _calls_ should be placed under an if-clause that checks this. Put differently, importing a file should not have _side effects_.
- - - - -

**17.26.** Clean up the files `file_a.py` and `file_b.py` to adhere to the foregoing principle.


**17.27.** Recall from earlier that functions enable **encapsulation**: variables created in a local scope, such as a function definition, are not accessible elsewhere. Do you remember one or more reasons why encapsulation is generally good?

**17.28.** Any variables or functions defined in the _global scope_ of a program are not encapsulated, hence accessible elsewhere. Do you remember whether an if-clause creates a local scope or not? In the file `file_a.py`, try whether the body of the main if-clause (under `if __name__ == '__main__':`) belongs to the global scope. For instance, is a variable defined there, accessible within the function definition of `laugh`?

**17.29.** To increase encapsulation, statements in the body of the main if-clause are typically moved into their own separate function `main`. For instance, for the file `file_a.py` this would look as follows. Verify that this indeed improves the encapsulation, namely, that variables defined in the function `main` can not be reached outside of that function.

```python
import file_b

def main():
    laugh()
    file_b.cry()

def laugh():
    print('Hahaha!')

if __name__ == '__main__':
    main()
```

**17.30.** Restructure the file `file_b.py` in a similar way, i.e., replace the main if-clause's body by a call to a designated function `main`. Verify that everything works as before.

- - - - - -
**Something to keep in mind:** From now on, for better encapsulation, you should do this for every file you create: define a `main` function that is called at the bottom of the file only if the file is run as main file, and put all your commands that 'do something' (hence that should _not_ be side-effects when importing the file elsewhere) into the `main` function (or in functions called by the `main` function).
- - - - -

**17.31.** Python interprets files from top to bottom, right? Then how come in the restructured `file_a.py` above, `laugh` can be called within `main`, despite it being defined _after_ (i.e., below) `main`?

**17.32.** Add some docstrings to the functions in files `file_a.py` and `file_b.py`. When importing a file, do you get access to the docstrings of its functions (try calling `help` on the imported function)?

**17.33.** From memory, make a list of Python built-ins (_not_ keywords) as well as Python modules that you have learned about in this course so far. Becoming a better Python programmer is in large part a matter of learning those ways -- and creating new ones, in your own modules, if none yet exists.

**17.34.** For some libraries it is customary to import them under a (typically shorter) alias. For instance, if you did Coding Quest H you might have seen `import seaborn as sns`, which imports the 'Seaborn' library (for plotting) and assigns this imported module to the (somewhat arbitrary, but customary) `sns` variable instead of its original name `seaborn` (hence you then call its functions like `sns.lineplot`, not `seaborn.lineplot`). Can you do the same with custom modules, e.g., like `import file_b as some_new_name` in the above example? How do you then call its methods? What happens if you accidentally use its original name after importing under an alias?

- - - - - -
**Something to keep in mind:** In code examples online you will often see `import ... as ...` to import a module under a shorter alias. (But you may recall that using abbreviations is generally not advised, so do this only with aliases that are really commonplace.) Common ones you may encounter are `import matplotlib.pyplot as plt` (on which seaborn relies under the hood), `import pandas as pd` (for handling tabular data) and `import numpy as np` (for numerical computation).
- - - - -

**17.35.** A final variant that we will briefly cover is `from ... import ...`, which is used to assign a specific submodule, function or field from a given module to a variable in the 'main' namespace (i.e., `globals`). For instance, when you do `from sklearn.metrics import accuracy_score`, you can then use the `accuracy_score` function in your program without prefixing it with the module name (e.g., simply `accuracy_score` instead of `sklearn.metrics.accuracy_score`). This _can_ enhance readability, but it can also result in a lack of clarity about which functions are 'standard' vs. defined by yourself. In general, try to follow common practice (i.e., most online examples) in how you import a certain library. For now, just to try, use `from ... import ...` to import a particular function from `file_b.py` from above.

**17.36.** An earlier exercise related the use of modules to the DRY principle. Can you also relate it to the SLAP and SoC principles?

**17.37.** Executing `import this` (in a script or in the Console) shows some of Python's programming principles in poetic form. This 'easter egg' was introduced into the language with **PEP20** (https://peps.python.org/pep-0020/). Have a look!


