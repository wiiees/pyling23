# Python for Linguists 2023

## 3. Strings (`'...'`, `+`, `len`, `[]`)

Effort profile: `▁▁▁▁▁▁▁▁▁▁▁▁▂▁▂▁▂▂▁▁▁▁▁▁▁▁▁▁▂▁▁▁▄▅▁▁▁▁▁▁▁▁▁▁▁▁▂▂` 



**3.1.** In Python, text can be represented by strings, i.e., sequences of characters. You can create a string by surrounding characters by quotation marks: `'apple'`. Can you assign a string to a variable?

**3.2.** You know that Python can add and multiply numbers with `+` and `*`. Do these operations also work on strings? Try `'apple' + 'pear'`, `'apple' * 'pear'`, `'apple' * 5`, `'pear' + 5` and others. Which mathematical operations work on strings, and which ones don't? Which types of errors do you get?

**3.3.** How do you create an empty string? And a string containing only a space?

**3.4.** How do you connect two strings together with a dash "-" in between? And with a space in between? And with five spaces in between?

**3.5.** For the sentence _All work and no play makes Jack a dull boy_, first store each word in a separate variable, and, using these, create a sentence by 'adding' those variables together.  <!-- TP3 -->

**3.6.** Can you also create a string by surrounding characters by _double_ quotation marks `"..."`?

**3.7.** What happens if you use two single quotation marks at the start and end of a string literal, e.g., `''cheese''`? What if you use three `'''`? Or four?

**3.8.** Can you create a string that _contains_ a quotation mark, such as the string `She said: "Hello!"` or the string `She said: 'Hello!'`?

**3.9.** What happens if you try to create a string, but the string contains a 'newline' in the middle, as below? What might `EOL` mean?

```python
sentence = 'apples do not fall
far from the tree'
```

**3.10.** Newlines in your string are no longer a problem if you use triple quotation marks (`'''` or `"""`) instead of single ones (`'` or `"`). Fix the previous code so it runs correctly. If you subsequently retrieve the string (i.e., enter the variable name `sentence` in the Console to display its contents), does the newline survive or is it ignored in the Console's output?

- - - - - -
**Something to keep in mind:** There is a distinction between a **string** (a sequence of characters), and the Python expression used for defining it: a **string literal**. In the simplest case, a string literal is simply the string you want to define, surrounded by quotation marks. 
- - - - -

**3.11.** Instead of using triple quotation marks, you can also add newlines to your string by typing `\n` as part of the string literal, e.g., `'apples do not fall\nfar from the tree'`. Here backslash `\ ` is used as an _escape operator_; it is used for various other special characters as well, e.g., `\t` for a tab. Very handy! But what should you do if you want to create a string that contains an actual backslash `\`, such as the string `You can create a newline by typing \n`? (Try to guess, and experiment! If that fails, search the web.)

**3.12.** Can you guess what including `\N{tomato}` in your string literal might do? Test your prediction. Have a look at the list of possible **escape characters** (only some of which will be understandable at this point): https://python-reference.readthedocs.io/en/latest/docs/str/escapes.html .

**3.13.** ⭐ Try to explain what escape characters are used for, in terms of the distinction between strings and string literals.

**3.14.** Previously you constructed a string containing a quotation mark. Can you also construct a string that contains both single and double quotation marks?

**3.15.** ⭐ Try to predict which one of these is legal Python syntax, what the result is, and why: 
1. `fruit = 'apple'` 
2. `fruit = apple` 
3. `'fruit' = 'apple'` 
4. `fruit == apple` 
5. `'fruit' == 'apple'` 
6. `'fruit' == apple`

**3.16.** Do the comparison operators `>` and `<` work on strings, e.g., `'apple' < 'pear'`? What do they mean in this context (experiment with other strings to find out)? Can you explain `'300' > '4'`? What about `'300' > 4`?

**3.17.** ⭐ For each of the following, try to predict whether it's true or false (or neither...), verify, and explain why: 
- `'hat' == "hat"` 
- `hat == 'hat'` 
- `1/3 == .33` 
- `'three' > 'two'` 
- `2 + 2 = 4`  <!-- P4L -->

**3.18.** ⭐ Strings themselves (like numbers, and many other objects) can also be evaluated to `True` or `False` when placed in a boolean context. By testing expressions like `not 'abc'`, can you figure out which strings are 'Truthy' and which strings are 'Falsy'? After experimenting yourself, check the documentation on this aspect of Python: https://docs.python.org/3/library/stdtypes.html#truth-value-testing (the three bullet points; which one covers strings?).

**3.19.** What happens if you feed the built-in functions `max` and `min` a string as argument (e.g., `max('apple')`, `min('bonanza')`)? And what about multiple strings, `max('apple', 'aardvark', 'banana', 'zebra')`? Can you explain the result of `max('250')`? And `min('-852')`? And `max('123abc')`?

**3.20.** What does `len('apple')` do? Come up with a hypothesis and apply `len` to different strings to test it.

**3.21.** Can you also get the `len` of a number, e.g., `len(3)`? What about a boolean? What about the empty string?

**3.22.** What happens if you type `length` instead of `len`? What happens if you forget the quotation marks of the string (like `len(apple)`), or forget a parenthesis?

**3.23.** Try `'p' in 'apple'`, and `'q' in 'apple'`, to figure out what `in` does. Can you use `in` to check for larger substrings (e.g., `app`), or only single characters? According to `in`, does a string contain itself?

**3.24.** Is `in` a keyword or a built-in function? 

**3.25.** Do you expect the following to be equivalent: `not 'p' in 'apple'` and `'p' not in 'apple`? Which one do you find more readable? Chances are that your editor gives you a friendly warning when you use the first one.

**3.26.** Can you predict what is going on here? `1 in '123'` vs. `'1' in '123'` vs. `1 in 123`. Verify and explain.

**3.27.** Can you predict the truth values of the expression `not '1'` and the expression `not 1`? What about the truth value of `not 'False'`? Make sure you understand what's going on.

**3.28.** Suppose we have a single character assigned to the variable `char`. What ordinary English word corresponds to the following Python expression: `char in 'aeiou'`. (Although: can you make it work on capital letters too?)

**3.29.** ⭐ Assign a variable `name = 'Michael'`. Try to predict what each of the following do. If your prediction is wrong, make sure you understand the reason for your wrong expectation, before moving on to the next item in the list. 
- `name[1]` 
- `name[2]` 
- `name[8]` 
- `name[-1]` 
- `name[-2]` 
- `name[1:3]` 
- `name[2:2]` 
- `name[-2:]` 
- `name[2:]` 
- `name[:2]` 
- `name[0]` 
- `name[2-4]` 
- `name[3-2]` 
- `name[1+1]`
- `name[3:12]`
- `name[12]`
- `name[12:15]`
- `name[:99]`

- - - - - -
**Something to keep in mind:** The square brackets operator `[]` lets us select characters, contiguous substrings, and even non-contiguous substrings (see below). This is called _slicing_ the string.
- - - - -

**3.30.** The last couple of items in the previous exercise demonstrate a difference between selecting a single character and selecting a substring, in terms of how indices 'out of bounds' are handled. Can you describe this difference? 

**3.31.** You can also indicate the step size (or 'stride length') when slicing, by adding another colon and a number. Let's see it in action: what does `name[::2]` do? What about `name[::-1]`? And `name[1:5:2]`?

**3.32.** By using _only_ slicing, extract only the odd-position characters from `michael` (assuming the `m` is at position 0, i.e., even). And can you also obtain the string `eh` from the string `michael` by using only slicing? What about the string `ehm`?

**3.33.** ⭐⭐ By using slicing, write a boolean expression that tests if a given word `w` is a _palindrome_. It should work for words of any length.

**3.34.** Perhaps you'd expect to be able to change the string in `name` by replacing a character like this: `name[2] = 'b'`, expecting the result `Mibhael`. But this doesn't work; what does the error message say? This is because strings are not _mutable_: once you create a string, you cannot change it, only create a new one that is different. We return to mutability later.

**3.35.** Can you predict what `'0123456'[3]` does? What about `'1234567'[3]`? And what about `1234567[3]`?

**3.36.** What happens if you use commas (`,`) or semicolons (`;`) instead of colons (`:`) when slicing? If there is an error message, do you find it informative/helpful?

**3.37.** What does `name[len(name)]` do? What about `name[len(name)-1]`? Why? Write a simple expression that is equivalent to the latter, but without using `len(name)` (and it should work for any string in `name`). 

**3.38.** Predict the outcomes of `len('apple' * 5)`, `len('apple') * 5` and `len('apple * 5')`, then test your predictions.

**3.39.** Based on what you know about parentheses and spaces in relation to functions vs. operators (see Section 2), is `len` a function or an operator?

**3.40.** Python's strings come with various methods, including `upper` and `lower`. What would you expect these methods to do? As methods of the string class, you call them 'on' a string object, like this: `'apple'.upper()`.

**3.41.** Do you expect the following to be true for _any_ possible string assigned to `s`? `s == s.upper().lower()`. Test your expectation.

**3.42.** In other programming languages, `len` is sometimes 'attached to' string objects similar to `upper` and `lower`, requiring you to type for example `'apple'.len()` instead of `len('apple')`. What happens if you try the same in Python? Also try the weird-looking `'apple'.__len__()`? 

- - - - - -
**Something to keep in mind:** Some functions (like `len`, `max`, `print`) can be invoked 'stand-alone', while others (more properly called **methods**) 'live on' objects and must be called 'on' that object (like `s.upper()` for some string `s`). Under the hood, however, most 'stand-alone' functions, as well as operators like `+`, are actually mere _shortcuts_ for methods that live on objects. For instance, `len`, when applied to a string, results in a call to that string's `__len__` method; and `+` when applied to an integer number calls that integer's `__add__` method (defined as numerical summation), while applied to a _string_ it calls an `__add__` method that lives on the string (defined as concatenation). These so-called **dunder methods**, named after their double underscores, are not meant to be called directly; use the shortcuts instead.
- - - - -

**3.43.** ✉️ Write an expression that, given a string `s`, creates a new string that is like `s` but lacks the last 4 characters. What happens if `s` has fewer than 4 characters to begin with?

**3.44.** ✉️ (_Don't forget to submit!) Write an expression that, given a string `s`, evaluates to `True` if the first character of the string is a vowel, and `False` otherwise. Is your expression robust to capitalization differences? Can you improve this using `upper` or `lower`?

**3.45.** ✉️ Write an expression that, given a string `s`, evaluates to `True` if the last character of the string is a consonant, and `False` otherwise. Did you use a long string of all consonants, or the boolean operator `not`?

**3.46.** ✉️ ⭐ Create two variables containing different strings, and write (potentially multiple lines of) Python code to swap their values. (Test it thoroughly.)

**3.47.** ✉️ ⭐ After these dry exercises let's zoom out a bit: consider what kinds of linguistic research might require programming to begin with. Try to come up with several, varied examples of research questions that could require, or at least benefit from, programming.

