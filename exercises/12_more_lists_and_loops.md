# Python for Linguists 2023

## 12. More practice with lists and loops (also `index`)

Effort profile: `▄▅▁▁▂▄▅▁▁▂▂▂▂▁▁▁▂▁▁▁▁▁▁▂▄▅▁▁▄▅▁▁▂▂▂` 



**12.1.** ⭐⭐ Define three functions, each of which takes a list of numbers (e.g., the outcomes of an experiment) and returns a number. The first returns the sum of all elements. The second uses the summation function to compute and returns the list's average. The third uses the averaging function to compute and return the list's standard deviation. For the latter, you can do `import math` to use the `math.sqrt` function.

**12.2.** If you called the first of the above functions `sum`, then PyCharm likely gave you a warning (squiggle underneath the function name in the editor): 'it shadows the name of an existing function'. Indeed, `sum` is also a built-in function. Does it work the same way as your summation function above? (If you named it `sum`, consider changing the name to avoid confusion in what follows.)


**12.3.** Does your own summation function also work on a list of strings (after all, `'abc' + 'def'` is fine, too)? Does it work on a list of booleans? What about the built-in function `sum`? (For a list of strings, what would you expect the result to be, and how might you achieve this _without_ `sum`?)


**12.4.** ⭐ Write a function that takes a list of words like `words = ['the', 'dog', 'is', 'in', 'the', 'garden']`, takes the length of each word, and prints the total sum of word lengths. Do you get the same number as `len('the dog is in the garden')`? Why (not)? What about `len(words)`?

**12.5.** ⭐⭐ Write a function `index_in_string` that takes a string and a character, and returns the index of the first occurrence of that character in the string. For instance, `index_in_string('david', 'v')` returns `2`. Explain why `index_in_string` can be seen as the inverse of the square brackets slicing notation for retrieving a character by index.

**12.6.** Write a function `index_in_list` that does the same, but for a list instead of a string. Could you reuse any of the previous code?

**12.7.** While the previous exercise was excellent practice, lists and strings in fact come with a built-in method `index`, which is called like this: `'david'.index('v')` or `[6, 4, 8, 6].index(8)`. Does this method behave the same as your own implementation from the foregoing exercises? What happens if the string or list does not contain the element you request the index for? Which index is returned if it contains the requested element multiple times? After testing this empirically, call for `help` on the `index` method to confirm your findings.

- - - - - -
**Something to keep in mind:** Lists and strings have a method, `index`, which you can use to find the (first) index of an element in the list, provided it exists.
- - - - -

**12.8.** ⭐ Remember your function `day_number_to_name` from earlier, that converts an integer number 1 to 7 to the name of a day? Now use the list method `index` to write the inverse function `day_name_to_number` which is given a day name, and returns its integer representation. <!-- tp3 -->

**12.9.** ⭐ Write a function `month_to_ndays` which takes the name of a month, and returns the number of days in the month. Ignore leap years. It can be helpful to define two lists, one with the month names and one with the corresponding numbers of days. (Later we will learn about _dictionaries_, which would streamline this a bit further.) <!-- tp3 -->

**12.10.** ⭐ Write a function `find_index_of_largest` that finds and returns the _index_ of the largest element in a list (in mathematical terms this would be an _argmax_ function). You can do this without any explicit looping, namely by using the built-in functions `max` and the list method `index`. (Optional: Consider why this is not the most _computationally efficient_ way, e.g., imagine you had a list of millions of numbers.) What if you give your function a list of strings? What if you give it not a list, but a single string?

**12.11.** ⭐ Define a function that takes a list and two additional arguments `old` and `new`, and returns a copy of the list in which each occurrence of `old` (if any) is replaced by `new`. Note that it resembles the built-in string method `replace`, but for lists instead of strings. By checking `help(str.replace)` to refresh your memory, you may notice that it has a parameter `count`; try to equip your list-level replacement function an analogous parameter.


**12.12.** Could you change your preceding function to modify the original list _in-place_, instead of returning a changed copy? What about the built-in string method `replace`, do you think it (or some variant) could be defined to enable such usage for strings?


**12.13.** In the following example, how come the list `cities` doesn't change?

```python
cities = ['amsterdam', 'rotterdam', 'leiden', 'gouda', 'eindhoven']
for city in cities:
    city.capitalize()

print(cities)
```


**12.14.** What about now? (First formulate your prediction, then test it.)

```python
cities = ['amsterdam', 'rotterdam', 'leiden', 'gouda', 'eindhoven']
for city in cities:
    city = city.capitalize()

print(cities)
```


**12.15.** ⭐ If the previous code did not change the list `cities`, modify the code so that it does. Does your modification actually change the original list in-place, or create a new, modified copy (re-assigned to the old variable)?

**12.16.** In a later section we will learn all about _sorting_, but it is already helpful here to briefly introduce the built-in function `sorted`, and the built-in list method `sort`. For instance, given a list like `cities` you can do `sorted(cities)` or `cities.sort()`, Try to figure out what the difference is (from experimenting and/or the documentation).


**12.17.** Based on your understanding of `sort` and `sorted`, would you expect strings to have a `sort` method too, like lists? And do you think `sorted` could be applied to a string? Test your expectation, and make sure you understand your findings. (We will be studying sorting extensively in a later section.)


**12.18.** Another list method, besides `index` and `sort` (and what about `sum`, was that a list method too?), is the method `count`. Try to figure out what it does, by experimenting or by checking the documentation. Does it also work on strings? (Like sorting, we will learn all about counting in a later section.)


**12.19.** Why doesn't the following function work as intended? How else would you implement this?

```python
def count_vowels(text):
    return text.count('aeiou')
```



**12.20.** Earlier we saw that if-clauses can be nested. What about for-clauses? Write a function (and think of an appropriate name) that loops over the `cities` list from earlier (`for city1 in cities:`), and nested within that loop, loops over the same list again (`for city2 in cities:`). In the body of the inner loop, print the two names stored in `city1` and `city2`, concatenated with a dash in between. Can you predict what will be printed? Try it, and make sure you understand what's happening.

**12.21.** (If you make all exercises within a single `.py` file, it may be helpful to print a separator in between exercises (e.g., `print('---------')`), or you'll loose track of where each printed text originates from!) In the previous exercise, why did the inner loop use a different variable from the outer loop, namely `city2` and `city1`, respectively? Do you understand the output of the following variant?

```python
for city in cities:
    for city in cities:
        print(city)
```


**12.22.** ⭐ Use nested loops and if-statements to print all pairs of cities where the first city name starts with a vowel and the second with a consonant. Looking at the city names, can you predict how many lines will be printed?

**12.23.** ⭐⭐ Write a function `chain` that takes a list of lists, and chains all lists into a single list. For example, chaining `[[1, 2], [3, 4, 5], [6, 7]]` will result in `[1, 2, 3, 4, 5, 6, 7]`.

**12.24.** Do `import itertools` (i.e., tools for iteration), and explore `itertools.chain`, comparing it to your custom function above. (What type of object does this function return? Consider wrapping it in `list(...)` to see the elements. We learn more about this in a later section!) 

- - - - - -
**Something to keep in mind:** Learning to program is in large part learning to find and combine pre-existing tools. This involves gauging whether some (part of a) tool you need is likely to have been needed by others before you -- if this is the case, it likely exists. Throughout this course we will rely increasingly on built-ins and existing libraries, but implementing analogous functions yourself remains excellent practice.
- - - - -

**12.25.** Also explore `itertools.product`. For which of the preceding exercises would this have been convenient? What do you think other (likely non-linguistics) people might have needed it for, i.e., why it became part of the `itertools` module? And what about `itertools.combinations`?


**12.26.** ⭐⭐ The four compass points can be abbreviated by single-letter strings as `'N'`, `'E'`, `'S'`, and `'W'`. Write a function `turn_clockwise` that takes one of these four compass point strings as an argument, and returns the next compass point in the clockwise direction. <!-- tp3 -->

**12.27.** A refresher of types and functions: explain the difference between `type(turn_clockwise)` and `type(turn_clockwise('N'))`.

**12.28.** Also define an analogous function `turn_counterclockwise`. Should `turn_counterclockwise(turn_clockwise('N')) == 'N'` evaluate to `True`? Does it? <!-- tp3 -->

**12.29.** ⭐ If you haven't done so already, perhaps you can streamline the functions `turn_clockwise` and `turn_counterclockwise` by storing the four compass points in a list. To simplify the function definitions, both the list method `index` and the modulo operator `%` can be useful here.

**12.30.** ⭐ Extend your clockwise and counterclockwise functions to deal with four diagonal directions (such as North-East `NE` and South-West `SW`). If this is difficult or requires a lot of manual typing, it means your functions could probably have been implemented in a smarter, more concise way...

**12.31.** ⭐ If there is still considerably overlap between the two functions, `turn_clockwise` and `turn_counterclockwise`, try to minimize this (remember DRY? remember why?), for instance by redefining each as a special case of a more general function `turn` that can turn in both directions...




-----

**_🦏 You are now ready for [Coding Quest D](../quests/D_trees.md)!_**