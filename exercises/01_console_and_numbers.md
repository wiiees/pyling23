# Python for Linguists 2023

## 1. The Python Console, numbers and variables (`=`, `+`, `%`, ...)

Effort profile: `▂▁▁▁▁▁▁▁▂▁▁▁▁▁▁▂▁▁▁▁▁▅▁▂▂▁▂▁▅▁▁▂` 




**1.1.** ⭐ Try using the Python Console (remember where to find it?) as a calculator, using numbers and operators like + and -. Which operators does Python recognize? What does `**` do?

**1.2.** What happens if you put a minus sign before a number? What happens if you put a plus sign before a number? What do `2+-2` and `2++2` do? (Spoiler: For readability, you would normally write these as `2 + -2`, or simply `2 - 2`, and `2 + 2`, respectively.) <!-- TP2 -->

**1.3.** In math notation, leading zeros are ok, as in `09`. What happens if you try this in Python? <!-- TP2 -->

**1.4.** What happens if you enter two numbers with no operator between them? <!-- TP2 -->

**1.5.** Add parentheses to the expression `6 * 1 - 2` to change its value from `4` to `-6`. <!-- TP2 -->

**1.6.** Write something in the Console again, but instead of executing it (with Enter), cancel it by hitting the hotkey `ctrl+c` or `cmd+c`. This will be useful to remember.

**1.7.** What if instead of hitting the hotkey, you accidentally pressed the Console's 'stop' button (red square; give it a try)? Then you need to restart the Python interpreter in the console (green loopy arrow on the left, or `ctrl+F5`/`cmd+F5`) before you can continue the exercises.

**1.8.** In the Python Console, compute how many seconds there are in 42 minutes and 42 seconds. <!-- TP2 -->

**1.9.** ⭐ How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile. <!-- TP2 -->


**1.10.** What does entering `blabla = 5` in the console do? Subsequently, what does entering `blabla` do?

- - - - - -
**Something to keep in mind:** The equals sign `=` is used for **assigning** a value (on the right of the `=`) to a variable (on the left). When you subsequently need the same value, you can refer to it using the variable.
- - - - -

**1.11.** Can a variable name contain a number? Can it start with a number? Can it contain a space? A quotation mark? An underscore? Explore what other special characters can be used in your variable names. Try some legal and some illegal variable names.

**1.12.** Assignment like `n = 42` is legal. What about `42 = n`? And how about `x = y = 1`? If it is legal, what is the result (try printing the variables)? <!-- TP2 -->

**1.13.** In math notation you can multiply variables _x_ and _y_ like this: _xy_. What happens if you try that in Python? Why? <!-- TP2 -->

**1.14.** Can you reuse variables, i.e., assign a new value to an existing variable? (Does that make sense, given the term 'variable'?)

**1.15.** Create a variable with the value 37; then create another variable with the value 4; and finally compute the result of multiplying those variables together. <!-- P4L -->

**1.16.** ⭐ First enter `n = 42`. Then try each of the following to figure out what they do (make a prediction first if you can); inspect `n` in between to make sure you understand what is happening: 
- `n = n + 3`
- `n = 100` 
- `n = n`
- `n += 3` 
- `3 = n` 
- `n -= 3` 
- `n = n * n`
- `n += n + 3`
- `n = n / n + 2`
- `n = n**2`

**1.17.** What happens in the Console if, instead of entering a new command, you press the up-arrow key on your keyboard, followed by enter? (In which cases might this be convenient?) 

**1.18.** First enter `n = 0`, and then enter `n += 1`. Can you predict what the value of `n` will be if you repeatedly do up-arrow and enter, five times in a row?

**1.19.** In the Python console enter `abcdefg + 4`. What happens and why? Next, assign a value to `abcdefg` so that, subsequently, `abcdefg + 4` evaluates to `10`. <!-- TP3 -->

**1.20.** In some languages every statement ends with a semi-colon, `;`. What happens if you put a semi-colon at the end of a Python statement? Or a colon `:`? (Remember the hotkey for canceling your input?) <!-- TP2 -->

**1.21.** Take some correct Python statement (e.g., `x = 'apple'`), add one or more spaces in front of it and try to run it again. What happens? Do the Console vs. running a script behave the same in this regard?

- - - - - -
**Something to keep in mind:** Unlike in many other programming languages, in Python **indentation is meaningful**. Later we will see cases where you _must_ indent.
- - - - -

**1.22.** ⭐⭐ If you run a 10 kilometer race in 42 minutes and 42 seconds, what is your average speed in kilometers per hour? <!-- TP2 -->

**1.23.** What is the area of a circle with radius 3? <!-- TP2 -->

**1.24.** ⭐ Suppose the cover price of a book is €24.95, but bookstores get a 40% discount. Shipping costs €3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?  <!-- TP2 -->

**1.25.** ⭐ `%` is the modulo operator, look up 'modulo' if you need to. Evaluate each of the following numerical expressions in your head, then use the Python console to check your results. What happens in each case? Why? 
- `5 % 2` 
- `9 % 5` 
- `15 % 12` 
- `12 % 15` 
- `238 % 24` 
- `6 % 6` 
- `0 % 7` 
- `7 % 0`  <!-- TP3 -->

**1.26.** `//` is the 'integer division' operator. What does it do?

**1.27.** ⭐ Compute in your head (or on paper) the result of `3 * (10 // 3) + 10 % 3`, and verify your own answer by subsequently trying it in Python.

**1.28.** What might be some benefits, in this early stage of learning to program, of doing these almost purely 'mathematical' exercises in Python?

**1.29.** ⭐⭐ If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per kilometer in minutes and seconds)? It can be useful to first compute the time per kilometer in seconds and store this in a variable, before processing it further to separate minutes from seconds. (What are some disadvantages if you _don't_ store this intermediate result?) <!-- TP2 -->

**1.30.** What do the built-in functions `max` and `min` do? For example, try `max(3, 4, 5)`, `min(5, -11, -2, 99)`, and `max(10)`; can you guess what the error means?

**1.31.** What happens if you accidentally put a space between the function name and the parentheses (against Python style): `max (3, 4, 5)`? What if you forget the parentheses altogether?

**1.32.** ⭐ You look at the clock, and it is exactly 2pm. You set an alarm to go off in 51 hours. At what time does the alarm go off? (Whenever a value increases and then goes back to zero, again and again, like hours on the clock, modulo can be useful.) <!-- TP3 -->

