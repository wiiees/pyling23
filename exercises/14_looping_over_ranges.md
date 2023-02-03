# Python for Linguists 2023

## 14. Looping over ranges (`range`)

Effort profile: `▁▁▂▁▁▁▂▂▁▂▄▅▂▄▅▄▅▄▅▁▁(▄▅)▂▁▁▁▁█` 



**14.1.** It is often convenient to loop over consecutive numbers (0, 1, 2, 3, ...). One way to achieve this is to create a list of numbers and loop over those list elements just as we did before, e.g., `for n in [0, 1, 2, 3]:`. Use this technique to print each number from 0 to 9. To understand a downside of this technique, consider printing the numbers up to 999 in the same way (but don't).

**14.2.** A more convenient way to loop over consecutive numbers is to use the built-in function `range`, e.g., `for i in range(10):` loops over all integers from 0 to 9. Try this, and see how easily it scales up to larger ranges.

- - - - - -
**Something to keep in mind:** To loop over a **range** of consecutive integers from 0 to some integer `n`, use `range(n)`. We will learn more about `range` later, as it is a lot more flexible/powerful than simply 'integers from 0 to _n_'.
- - - - -

**14.3.** ⭐ Assign a list of strings to the variable `words`. What does looping over `range(len(words))` achieve? Use it to print each index (0, 1, 2, ...) next to the corresponding element in the list (so: `0 cat`, `1 dog`, `2 house`, etc.). (Later we will learn a slightly more Pythonic way to achieve this, using `enumerate`, but this is good practice.)

**14.4.** What happens if in the above `range` construction, you forget the `len`, so it reads `for i in range(words)`? This type of mistake is easily made, so it is helpful if you can recognize it. And what happens if you forget the `i` and simply do `for range(len(words)):`?


**14.5.** Write a loop with `range` to again print strings from the list `words` alongside their indices, but now adjust the range to stop at the penultimate word (i.e., print all but the last).


**14.6.** Another mistake that is likely to happen, so good to be able to recognize: What happens if you accidentally do `for i in range(len(words - 1))`? (Before trying, do you see the mistake?)


**14.7.** ⭐ Use `range` to iterate over indices of the list `words`, in a way that lets you print _pairs_ of consecutive words, or **bigrams** (`the dog`, `dog is`, `is in`, etc.). What should be the upper bound of your range?

**14.8.** ⭐ We have thus far used `range` to iterate through consecutive integers, e.g., `for i in range(10):`, but `range` is quite a bit more flexible. Execute `help(range)` in the Python console for more information (and remember to press `q` to quit). As you can see, you can construct a range with up to three arguments. What do the other arguments do? E.g., what happens if you loop over `range(3, 50, 5)`? And what about `range(100, 5, -3)`? Is there a relation between the three arguments of `range`, and the three integers you can specify when _slicing_ a string or list (e.g., `'applesauce'[1:5:2]`)?

**14.9.** Write a function that counts down from 10 to 1, and then prints _Lift off!_. (Consider printing all numbers on the same line, to more easily keep an overview in your printed output.)

**14.10.** ⭐ Generalize the preceding function by providing it a start and a step parameter. Use it to count down from 20 in steps of 2.

**14.11.** ⭐⭐ Define a function that uses nested loops to print all pairs of numbers, each between 0 and 10 (inclusive), where the first is odd and the second is even. Did you use if-clauses inside the loops, or did you solve it with particular `range` objects instead?

**14.12.** ⭐ Define a function that uses nested loops to print all pairs of numbers, each between 0 and 10 (inclusive), where the second is higher than the first -- but, for the sake of practice, _without_ using an `if`-statement (hint: the inner loop can use a range of which the starting point is determined by the outer loop). (Can you reason about how many such pairs there will be?)

- - - - - -
**Something to keep in mind:** When you need to loop over a range of numbers in a particular way, choosing a smart `range` can sometimes result in more readable code than using if-statements inside the loop, especially in list comprehensions.
- - - - -

**14.13.** ⭐⭐ Write a function that takes a list, and returns a new list containing all elements that occurred at even indices (0, 2, 4, ...) in the original list. Write a version that uses a multi-line loop, and a version with only list comprehension.

**14.14.** ⭐⭐ Write a function that takes a list and returns a new list containing all non-overlapping _pairs_ of elements in the original list. So for input `[1, 2, 3, 4, 5, 6]` it would return `[(1, 2), (3, 4), (5, 6)]`. Try two variants: a multi-line loop and list comprehension. Which do you find more readable in this case?

**14.15.** ⭐⭐ Generalize the foregoing function with an integer parameter `n`, returning the list of non-overlapping n-tuples (pairs, triples, quadruples, etc.). This is likely too complex for a single-line list comprehension. Moreover, you will likely need two `range` objects, one for looping through the list, one for constructing each tuple (from index `i` to index `i + n`). Remember from the previous section that constructing a tuple using list comprehension requires an explicit `tuple(...)` expression.

**14.16.** Can you create a `range` with non-integer steps, e.g., 0.1? What about using a float as a starting point or end point, is that allowed? Can you think of a more indirect way to nevertheless achieve such non-integer ranges whilst still using `range`?

**14.17.** What's going wrong in the following code? Why did the programmer make this mistake?
```python
for i in range(2:9:1):
    print(i)
```




**14.18.** ⭐⭐ _[Optional, perhaps return to this later.]_ The following is a well-known programming job interview question, known as 'FizzBuzz'. Write a function that iterates the integers from 1 to 50, printing the numbers. However, for multiples of 3 print `Fizz` instead of the number, and for multiples of 5 print `Buzz` instead of the number. For numbers which are multiples of both three and five print `FizzBuzz`. Try to minimize repetition in your code.

**14.19.** ⭐ Define a function that takes an integer parameter `ndays` and uses a _single_ loop to repeatedly, `ndays` times, print the numbers 0, 1, 2, ..., 23 (as if `ndays` days pass on a 24-hour clock). (Remember what operation to use for such 'cycling' numbers?)

**14.20.** Remember 'type conversion', i.e., turning an object of one type into a (new) object of another? A `range` object can be converted to a `list`, e.g., `list(range(100))`. Try this. Can you also convert a list back to a range? What happens if you try, and why might this be?

**14.21.** In the Python console compare `x = range(9999)` to `x = list(range(9999))` (without printing the result). Keep increasing nines and try again, e.g., `99999`, `999999`, `9999999`, and beyond (take it easy, don't crash your computer). At some point you will notice that the version `x = list(range(999...9)` gets much slower, while the version `x = range(999...9)` remains fast. Why would this be?

**14.22.** If you do `import sys`, you can access various operating-system-related functions in Python. One of these is the function `sys.getsizeof`. First call `help` on this function to read what it does. Then use the function to compare `range(9)` to `range(9999)`, and `list(range(9))` to `list(range(9999))`. Do your findings align with your answer to the previous exercise?

**14.23.** The foregoing notwithstanding, does a range nevertheless support list-like methods such as indexing, slicing, `len` (and if so, is `len(range(99999))` slow?)? How could this be if the list elements aren't really 'there' until the range is iterated over?


**14.24.** ⭐⭐⭐ We have a micro-computer with a tiny display of 8 by 8 pixels, each of which can only be either on or off. We received what appears to be a secret message: `0000000000110110011111110011111000011100000010000000000000000000`. Write a function that takes such strings and prints them to a (simulated) 8 by 8 display, each pixel represented by a single character, rendering a `0` as an empty space ` `, and a `1` as a hashtag `#`. If you like, compose your own reply.







-----

**_🦈 You are now ready for [Mini-project G](../projects/G_n-grams.md)!_**