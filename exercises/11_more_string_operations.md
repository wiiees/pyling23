# Python for Linguists 2023

## 11. More string operations (`split`/`join`, `strip`)

Effort profile: `▄▅▂▁▁▂▁▂▄▅▂▄▅▁▂▂` 



**11.1.** ⭐⭐ Look at `dir(str)`, or equivalently `dir('some_random_string')`, for a list of methods available on the string class itself. Explore at least the string methods `strip`, `swapcase`, `isalnum` and `center`; use `help` if needed (e.g., `help(str.strip)`) and illustrate how each of these work with your own examples.

**11.2.** ⭐ What is the difference between the string methods `split` and `rsplit`? Illustrate with your own example.

**11.3.** Assume that we have assigned `test_string = 'abcblablablaabc'`. For each of the following invocations of `strip`, form an expectation about what it does (based on the `help` you obtained) and then test it (e.g., by printing the result), refining your understanding of `strip`:
 - `test_string.strip('abc')` 
 - `test_string.strip('cba')` 
 - `test_string.strip('a').strip('b').strip('c')` 
 - `test_string.strip('c').strip('b').strip('a')` 
 - `test_string.strip('bla')`

**11.4.** Call `help` on the `str.join` method, look at the example it provides, and try to join your own list of strings with a dash `-` in between.

**11.5.** ⭐ With the help of the documentation (`help`), figure out how to define a string `s` for which the following is _not_ true: `' '.join(s.split())`. <!-- p4l -->

**11.6.** What happens if you try to join a list that contains objects other than strings, e.g., integers?

**11.7.** ⭐ There may be something counterintuitive about `join` and `split`: `split` is called as a method of the string-to-be-split (with 'joiner' as an argument of the function call), while `join` is _not_ called on the strings to be joined, but rather, on the string used for joining them. For instance, when splitting/joining on `'-'`, the dash is the argument of `split`, but not of `join` (for which it is, instead, the object on which the method lives). The following variant would be more 'symmetrical' in this regard, as the connecting character `'-'` would be the argument in both cases. However, test this to see what type of error you get (and then fix it):

```python
names = ['john', 'sue', 'bob']
names_joined = names.join('-')	# Doesn't work!
names_unjoined_again = names_joined.split('-')
print(names == names_unjoined_again)
```


**11.8.** ⭐⭐ Try to think of a natural way in which to read `join` and `split` commands out loud, that will help you memorize the aforementioned apparent asymmetry. In addition, try to think of a reason _why_ Python may have been designed this way, i.e., why `join` is _not_ called as a method _of the list to be joined_, but as a method of the string to join by.

**11.9.** ⭐ Oh no! I copied a list of student names from a low-quality PDF and now all names are surrounded by weird symbols! See below -- imagine the list is much longer (so manual cleaning is not an option) but the type of 'noise' remains the same. Define a function that uses `split` and `strip` that, when applied to the messy string below, return a list of separated, cleaned-up names:

```python
names = '''#*John#*
#*Mary# *,
*#*Suzy#*,
#*Bob#\t*;
#* Chris#\t*'''
```


**11.10.** ⭐⭐ Oops, copying from a different PDF resulted in even more mess, where all names are in uppercase and some characters were misread as similarly-shaped numbers. Can you tweak your previous cleanup function to handle this? Hint: there is a string method called `replace`.

```python
worse_names = '''#*T0DD#*
#*0NA# *,
*#*SUE#*,
#*ANN-M4RY#\t*;
#* R0S5#\t*'''
```


**11.11.** How does the string method `replace` work, exactly? What if the thing-to-be-replaced isn't there? What if it occurs multiple times? How can you use `replace` in order to _delete_ all occurrences of a certain substring? What do you expect the result of `'abc'.replace('', ' ')` to be (form an expectation first, then test it)? How can you use replace to _insert_ things at certain places in a substring, e.g., insert a space after each exclamation mark?

**11.12.** ⭐ The method `split` lets us split only on a particular string, so what if we want to split on multiple? For instance, we may want to split on both spaces and tabs, or on different types of punctuation. One possible solution is to first apply `replace` multiple times to insert a recognizable marker like `<<<SPLIT>>>` in the right places, and then call `split('<<<SPLIT>>>'')` just once. (A more general, powerful technique are _regular expressions_, about which we will learn in a later section.) Use this technique to split a text on all periods, exclamation marks and question marks.


**11.13.** ⭐ If you manually called the `replace` method multiple times in the previous exercise, try to use a loop instead: store all 'characters to split on' in a list or string, and loop over them to carry out the required replacements, before splitting in the end. 



-----

**_🐥 You are now ready for [Coding Quest C](../quests/C_tokenization.md)!_**

-------

**_Homework exercises for week 6 end here, now do Coding Quest [C](../quests/C_tokenization.md) (and don't forget to submit! ✉️)._**

-------

