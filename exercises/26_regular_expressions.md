# Python for Linguists 2023

## 26. Regular expressions (searching for patterns) 

Effort profile: `▁▁▁▂▄▅▂▁▂▁▁▁▂▁▂▁▁▁▁▂▁▂▁▁▁▁▂▁▄▅▂▂▂▁▁▁` 



**26.1.** Earlier we encountered string methods for searching (`index`, see also `find`), replacing (`replace`) and splitting (`split`). But often one wants to search for (or replace by, split on) not a _literal_ substring, but a _pattern_, i.e., characterizing a _class_ of substrings. _Regular expressions_ are a powerful and convenient method for this, available in Python from the standard `re` library. As a first illustration, execute the following code and try to formulate in ordinary English what the regular expression `[aeiou]+` might represent:

```python
import re

example_string = 'The famous Dr. Freud hastily acquired a magenta T-shirt and an old sweater for 26.95EUR. He then very very eagerly left the H&M at 1am... It was, as the doctor said, "a necessity".'
print(re.findall('[aeiou]+', example_string))
```


**26.2.** Enter `help(re)` or visit the (mostly equivalent) official documentation at https://docs.python.org/3/library/re.html for a global first impression; see especially the list of special characters in the section _Regular Expression Syntax_.

**26.3.** Use `re.findall` to test (and try to understand) which substrings of the above `example_string` the following regular expressions match:
 - `[a-z]+` 
 - `[a-zA-Z]+` 
 - `[a-zA-Z ]+` 
 - `[^a-z]` 
 - `[aeiou]` 
 - `[aeiou]*` 
 - `[^aeiou .]+`

**26.4.** ⭐ A useful exercise, and convenient for some of the following exercises, is to define a function `test_regexes` that takes a list of regular expressions ('regexes') and a string in which to search, and first prints the latter string, followed by each regular expression on a separate line alongside the list of matches that `re.findall` returns for it.

**26.5.** ⭐⭐ With the help of the documentation at https://docs.python.org/3/library/re.html#regular-expression-syntax, try to _predict_ which substrings the following regular expressions will match. Test your predictions with the help of the function from the previous exercise (and you can also use the suggested `example_string` from above).
 - `[0-9]` 
 - `[0-9]+` 
 - `\d+` 
 - `[a-z]+` 
 - `[A-Z]+` 
 - `[A-Za-z]+` 
 - `[a-zA-Z]+` 
 - `[A-Z]+[a-z]+` 
 - `[A-Z]+[a-z]*` 
 - `[^A-Za-z]+` 
 - `[A-Za-z0-9]+` 
 - `\w+` 
 - `\w+s` 
 - `\w+ly` 
 - `[^\w]+` 
 - `The|the` 
 - `[Tt]he`

- - - - - -
**Something to keep in mind:** **Regular expressions** are the go-to method for working with string _patterns_. Regular expressions form a special-purpose language, with its own little syntax, independently of (and older than) Python. In Python, the standard `re` module provides functions for searching, splitting on and replacing patterns defined by regular expressions.
- - - - -

**26.6.** ⭐ Explore what happens if your regular expression is not well-formed (but the containing Python code is), e.g., what happens if you use a regular expression with mismatching brackets (`[A-Z`), an incomplete character range (`[A-]`), or two plusses (`[a-z]++`)? Can you define a character range outside square brackets (e.g., `A-Z` on its own)? If the latter is well-formed, can you figure out what it means? Can you construct a string in which it will find a match?

**26.7.** Form your predictions, then test them: In which of the following strings does the regular expression `ab+c*d` match some substring?
 - `abbccd` 
 - `abbbcd` 
 - `accd` 
 - `aabcd` 
 - `abc` 
 - `abbdd`

**26.8.** ⭐ For the following regular expressions, can you find a string on which _all three patterns_ will return the same match (the same substring)? And a string where they all yield different matches? Try to find the smallest possible strings that satisfy these requirements.
 - `[ab]c+` 
 - `a[bc]+` 
 - `[abc]+`

**26.9.** Is the same possible for the following regular expressions? 
 - `a+|b+` 
 - `a+b+` 
 - `[ab]+`

**26.10.** Suppose we want to find all indefinite articles (_a_, _an_). We can use the question mark `?`, which marks the thing that precedes it as optional (i.e., zero or one): `an?` therefore means `a` followed optionally by an `n`. Test this regular expression on `example_string` from above and explain its main shortcoming. Try to fix it by tweaking the regular expression (though it doesn't need to be perfect, see next exercise).

**26.11.** In the previous exercise, chances are (spoiler alert) that you tried adding spaces to signify **word boundaries** (like `' an? '`), in order to avoid matching on, e.g., the 'an' of 'and'. A shortcoming of using spaces as word boundaries is that there exist word boundaries other than spaces (can you think of some?). Anticipating this, the `re` module provides a special character `\b` to represent a more accurate notion of word boundary, namely as an empty string at the boundary between 'non-wordlike' and 'wordlike' characters. Verify this by looking up the meaning of `\b` in the online Python documentation for `re` (e.g., via `help(re)`, then click the URL).

**26.12.** ⭐ A slight obstacle for using `\b` in a regular expression, is that `\b` is _also_ a special character for Python itself, but with different meaning: it signifies a 'backspace' (≠ 'backslash'). Try `print('abc\bdef\b\bghij')` to see its effect. This means that, if you want create a string (to be used as a regular expression) containing an _actual, literal_ `\b`, you need to escape the backslash _with another backslash_, that is, write `\\b`: this tells Python that you mean literal `\b` instead of the special backspace character. Verify that this works by doing `print('abc\\bdef\\b\\bghij')`. This literal `\b` (defined in a Python string by `\\b`) can then be passed on to the regular expression parser, where it means a word boundary. Use this to improve your regular expression for matching _a(n)_. Does it make a difference on `example_string`?

**26.13.** To avoid having to worry about Python's special characters requiring double backslashes when defining regular expressions, it is customary to define regular expressions using **raw string literals** (recall a _string literal_ is a way of creating a _string_), which are defined with an `r` prefix, like ``r'abc'`` (can you remember another string prefix we used?). Execute the following code to show that raw strings avoid the need for double backslashes. Also try printing each `regex`, and make sure you understand the result.

```python
regex1 = '\ban?\b'
regex2 = '\\ban?\\b'
regex3 = r'\ban?\b'

print(regex1 == regex3, regex2 == regex3)
```


**26.14.** ⭐ Verify using your `text_regexes` function that `regex3` indeed works as intended for matching indefinite articles, and that `regex2` does too (it's just ugly), but `regex1` fails. To solidify your understanding, explain all of the foregoing, e.g., why either double backslashes or a raw string are necessary.

**26.15.** If you haven't done so already, improve the regular expression `regex3` to also match indefinites with an initial capital, i.e., _A(n)_, and apply it to a relevant test string (since no capitalized indefinites occur in `example_string`). If you are a bit stuck, review the various regular expressions in the exercises above.

**26.16.** Define a new regular expression that matches all definite articles (_the_) in `example_string`. Make sure your regular expression matches the capitalized `The` at the start, and correctly ignores the word `then`.

- - - - - -
**Something to keep in mind:** Defining a regular expression involves two steps: first the Python interpreter parses your string literal (turning a piece of your code into a string object), and then the regular expression parser of the `re` module interprets that string object as a regular expression definition. Using **raw string literals** like `r'abc'` makes the first of these two steps as simple as possible (i.e., it tells Python to keep the backslashes in place), which makes the definition of regular expressions more straightforward.
- - - - -

**26.17.** Predict the lengths (according to `len`) of the following strings, keeping in mind that a special character like a tab (defined by `\t`) counts as 1 character. Then test your predictions. (For additional insight also consider printing each of these strings.) 
 - `'ta\ta\ta'` 
 - `'ta\\ta\\ta'` 
 - `r'ta\ta\ta'` 
 - `r'ta\\ta\\ta'`

**26.18.** The regular expressions you define are strings, hence they have the usual string methods. Concatenate the expression for matching indefinites with the expression for matching definites, with the regular expression operator `|` in between. Before testing it, explain in ordinary English what kinds of substrings the resulting composite expression will match.



-------

**_Homework exercises for week 13 end here, now do at least one of the Coding Quests [M](../quests/M_identifying_topics.md), [N](../quests/N_detecting_collocations.md), [O](../quests/O_language_generation_with_an__n_-gram-based_language_model.md) (and don't forget to submit! ✉️)._**

-------


**26.19.** ⭐ Looking back at previous examples, explain whether `findall` truly returns _all_ substrings that match a given regular expression, or only a specific subset. Do you understand why this (default) matching procedure for regular expressions is called **greedy**? (Consider, for instance, the regular expressions `a+` and `aaa`, and how many matches each yields on the string `aaaaaaa`.)

**26.20.** If you are a linguistics student, did you ever come across the _Chomsky hierarchy_? Where do so-called _regular languages_ -- those characterizable by regular expressions -- fit in this hierarchy? Could you characterize the grammar of a natural human language in a regular expression?

**26.21.** ⭐ As we have seen, some characters, escaped by a backslash, have special meaning in a regular expression. Do you remember the meanings of `\b`, `\w` and `\d`? In addition, with the help of the `re` documentation, illustrate the meanings of `\s` and `\A` by matching them on relevant example strings.

**26.22.** `\d \+ \d` will match any simple summation of single-digit numbers, like _3 + 6_. Verify that it works. Why do you think the backslash in front of the `+`-sign is needed? What if you omit it?

**26.23.** Generalize (and test) the foregoing regular expression for summation, to work also with multi-digit integers like `123 + 51221`. Next, expand it further to also handle subtraction, division and multiplication, and make the spaces around the operator optional (e.g., permitting also `123-321`)`.

**26.24.** Take a moment to appreciate the power of regular expressions: what would the plain Python code look like, in outline, for solving the previous exercise? No actual programming required; just a sketch suffices.

**26.25.** It can be convenient to compose a bigger regular expression from smaller ones with 'format string literals' (and a string literal can be both a _raw_ and a _format_ string literal at the same time: `fr'{some_variable}'`). Try this for your maths regular expression from two exercises ago, by defining one expression `number` that matches numbers, another `operator` that matches operators, and combining them with a format string. Verify that it still works as intended.

**26.26.** ⭐ The period `.` is another special character: outside a square brackets context, the `.` matches _any_ character except newline. (What does it match _inside_ square brackets?) Accordingly, to match an _actual_ period, you need to escape it with backslash. Given this, predict what the following regular expressions mean, and verify your prediction by matching them on a relevant example string of your choice:
 - `.+` 
 - `\.+` 
 - `".+"` 
 - `...`

**26.27.** Since the backslash `\` is a special character for the regular expression parser, defining a regular expression that matches an actual backslash requires escaping the backslash, i.e., `\\`. Verify your understanding, by explaining why even in a _raw_ string literal, you need a double backslash to match a literal backslash. And given that `\` is a special character also for the Python interpreter, how many backslashes would you need to enter in a _non-raw_ string literal, in order to define a regular expression that matches a single backslash?

**26.28.** ⭐⭐ Let us combine the power of regular expressions with some of the things we learned before. In a text of your choice (e.g., a book from Project Gutenberg), find all vowel clusters (single vowels or sequences thereof) and sort them by frequency, printing a top-20 of most frequent vowel clusters.


**26.29.** ⭐ Do the same, but now for word-initial _consonant_ clusters, and (separately) for word-final consonant clusters. (Advice: define consonant by simply listing them manually, since defining consonant as 'anything alphabetical except a vowel' within a regular expression is tricky, requiring some `re` constructs that we have not covered yet.)

**26.30.** ⭐ Think of an imperfect-but-good-enough-for-a-first-stab approach of detecting English adverbs with a regular expression. What are the most common adverbs in a text of your choice?

**26.31.** ⭐ The module `re` provides functions `re.sub` (short for 'substitute') and `re.split`, which are analogous to the string methods `replace` and `split`, but take a regular expression to replace or split on (instead of a plain string). Use these functions to, separately: 
 - replace all vowels in a string by `a`; 
 - replace all adverbs in a given string by `badly`; 
 - censor all numbers, replacing them by _`<censored>`_; 
 - split a string into separate words by splitting on anything that is not alphanumeric (and identify some shortcomings); 
 - split a string into sentences by splitting on certain punctuation (and identify some shortcomings).

**26.32.** The `re` documentation (https://docs.python.org/3/library/re.html) explains several useful extensions of the basic regular expression syntax. Let us consider just two quick examples. With the help of the documentation and the examples below, try to understand what the extensions `(?i)` and `(?<!...)` are for:
```python
print(re.findall(r'the', example_string))
print(re.findall(r'(?i)the', example_string))
print(re.split(r'\.', example_string))
print(re.split(r'(?<!Dr)\.', example_string))
```




**26.33.** To find not only the matching substrings but also the _locations_ of these matching substrings in the original string, use the function `re.finditer` (instead of `re.findall` we used so far). For a given regular expression and string it returns an iterator over `Match` objects instead of the matched substrings themselves. Use this to find all definite/indefinite articles in the `example_string` from before (you can reuse your own regular expression from an earlier exercise). (Note: since `finditer` returns an _iterator_, you have to loop over it, or wrap it in `list(...)`, to get the results.)

**26.34.** From a given `Match` object you can retrieve the matched span (`match.span()`) and the substring (`match.group()`). Write a loop to print, instead of the `Match` objects themselves, more readable lines like `3-6: the` (representing a match with span `(3, 6)` and substring `the`).



-----

**_🐞 You are now ready for [Coding Quest P](../quests/P_extracting_dialogues_from_a_book.md)!_**