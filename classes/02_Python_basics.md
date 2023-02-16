
# Python for Linguists 2023

◄ (9/02) [Introduction](../classes/01_Introduction.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Chat-GPT](../classes/03_ChatGPT.md) (23/02) ►

-------

## Week 2: Python basics  (16/02)


### Plan
1. Quiz
2. Homework discussion
3. Python basics 
4. Practical


-------

### 1. Quiz

The quiz will be revealed during class.

-------

### 2. Homework for today

Exercises:
- [Section 1. The Python Console, numbers and variables (=, +, %, ...)](../exercises/01_console_and_numbers.md): all exercises
- [Section 2. Logic (and, or, ==, =>, ...)](../exercises/02_logic.md): all exercises
- [Section 3. Strings ('...', +, len, [])](../exercises/03_strings.md): all exercises
- _(Optional)_ [Section 4. Python code and Bytecode](../exercises/04_python_and_bytecode.md): all exercises

-------

### 3. Python basics 


#### Strings, quotation marks, printing

`print('abc')`  this prints   `abc`    (not:  `'abc'`)

Why?


#### Float precision

https://docs.python.org/3/tutorial/floatingpoint.html
https://en.wikipedia.org/wiki/Double-precision_floating-point_format

A float is exactly representable if it is equal to a/b where a and b are integers (max 52-bit) and b is a power of 2.

#### Console vs. scripts (Homework sec. 5.) 


#### Duck typing (Homework 6.)

Python is a strongly types, dynamically typed language.

_Type hints_ are possible in Python, but these are _comments for the human programmer_ and not actually enforced when the code is compiled/interpreted:

```python
def say_hi(name: str) -> str:
    return f'Hi {name}'
```

#### A comment about object-oriented programming




-------

### 4. Practicum: homework for next time

Exercises:
- [Section 5. Scripts (.py-files, and the functions print and input)](../exercises/05_scripts.md): all exercises&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (`▁▁▂▁▁▁▁▁▁▂▁▁▁▂▂▁▂▁▁▁▂▁▁▂▁▁▁▁▁▁▂▁▁▁`)
- [Section 6. Types (type, and int, str, ..., also help, dir)](../exercises/06_types.md): all exercises&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (`▂▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▂▁▁▁▁▁▂▁▁▁▄▅▂▂▂`)

