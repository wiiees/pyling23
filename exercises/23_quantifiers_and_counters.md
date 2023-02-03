# Python for Linguists 2023

## 23. Quantifiers and counters (`any`, `all`, `Counter`)

Effort profile: `▁▁▁▁▂▁▁▁▁▂▂▂▁▁▄▅▁▁▂▁▂▁▁▁▁▁▁▁▄▅` 




<br>**_Quantifiers and basic couting (`any`, `all`, `list.count`)_**


**23.1.** The built-in functions `all` and `any` take an iterable (such as a list) and return a boolean value, representing if all/any of the iterable's elements evaluate to `True`. What do you think the following expressions evaluate to? Test your predictions.
 - `all([True, True, True])` 
 - `any([True, True, True])` 
 - `all([True, False, True])` 
 - `any([True, False, True])` 
 - `all([False, False, False])` 
 - `any([False, False, False])` 
 - `any([])` 
 - `all([])`

**23.2.** Assuming `booleans = [True, False, True]`, predict what the following two equivalences evaluate to, then test your predictions:  
 - `not any(booleans) == all(not b for b in booleans)` 
 - `any(booleans) == (not all(not b for b in booleans))`

**23.3.** In the previous exercise, note that the argument passed to `all` was not a list, as there were no square brackets around it: `all(not b for b in booleans)`. Do you remember what this kind of expression is called? What is its relation to lists, list comprehension and iteration? (And if you did the optional Section 21: what is its relation to generators and `yield`?)



**23.4.** If you took the course Semantics 1, or encountered _predicate logic_ elsewhere, do Python's `any` and `all` correspond exactly to predicate logic's existential and universal quantifier, respectively? If you are unsure, explore some additional test cases to reach a conclusion.

**23.5.** ⭐ Assuming we have a list of strings assigned to `words`, what does `any(len(word) >= 3 for word in words)` check for? Write a similar one-liner that checks whether _all_ words are less than 10 characters long, and another that checks whether _any_ words start with a vowel.

**23.6.** Write three more one-liners, that check (respectively) whether none, some, and all of the words contain the letter 't'.


**23.7.** Sometimes the coarse-grained quantifiers don't suffice; we may need a precise amount. In an earlier section we encountered the `count` method of lists (and strings, and some other datastructures (explore!)). To refresh your memory, use it to count the number of times `3` occurs in a list of numbers, and the number of times `the` occurs in a sentence like `the quick brown fox jumped over the lazy dog`.

**23.8.** Just like we combined the quantifiers with list comprehension earlier, we can combine `count` with list comprehension to count the number of elements that meet a certain boolean condition. What does the following do?
```python
[w[0] in 'aeiou' for w in words].count(True)
```

**23.9.** Using the previous construction, write a single-line expression that counts the number of words that have a length of at least 3, and write another one that tests whether there are at least 3 words that end with a vowel.

**23.10.** ⭐ An alternative way to count how many elements meet a certain condition relies on `len`: first use list comprehension with `if` to keep only the elements that meet the condition (we learned about such 'filtering' before), and then apply `len` to the result. Use this to provide alternative solutions to the previous exercise.

**23.11.** ⭐ Lastly, instead of using `.count(True)`, we can also use `sum` on a list of booleans to likewise count the number of `True` values (since `True` evaluates numerically to 1). Try to solve exercise 23.9 with this variant.

**23.12.** ⭐ We have now seen three ways of counting how many elements meet a certain condition: using `count`, using `len` and using `sum`. Describe each approach at an intuitive level. How does each work? Which do you find more readable? How do you reconcile this with the following aphorism from the Zen of Python (`import this`)? _There should be one-- and preferably only one --obvious way to do it._

**23.13.** A technical detail: Whereas `sum` (and `any` and `all`) can take any iterable, including a 'generator' object that produces elements on the fly (as produced by comprehension syntax _without_ the brackets around it), `len` does require the square brackets (or `list(...)`, `set(...)`, etc.), and likewise for `count` (though for a different reason). Create an example to show this if you haven't already, try to find this difference in the documentation, and try to understand why Python was built this way.

**23.14.** Could the foregoing be a reason for preferring `sum` over `count` and `len`, as a counting method? If so, in which circumstances especially?

**23.15.** ⭐⭐ Assuming we have a list of strings assigned to `words`, try to describe in plain English what the following lines compute. First make a prediction, then test and verify your understanding. (You can of course change `words` to include a variety of relevant strings!) Are there expressions among the following that are equivalent? 
 - `any(w[0].lower() in 'aeiou' for w in words)` 
 - `all(w[0].lower() in 'aeiou' for w in words)` 
 - `not any(w[0].lower() in 'aeiou' for w in words)` 
 - `all(w[0].lower() not in 'aeiou' for w in words)`
 - `[w[0].lower() in 'aeiou' for w in words].count(False) >= 2`
 - `sum(w[0].lower() in 'aeiou' for w in words) >= 2`
 - `[len(w) for w in words].count(4)`
 - `len([w for w in words if w[0].lower() in 'aeiou']) >= 2`
 - `not any(w[0].lower() not in 'aeiou' for w in words)`
 - `sum(len(w) for w in words) >= 10`
 - `[len(word) % 2 == 0 for word in words].count(True)`

 Of course, the more involved the comprehension syntax and the boolean condition, the less readable these one-liners become -- but in general, knowing these techniques can greatly improve the readability of your code.


**23.16.** With the help of the built-ins and techniques introduced above, reimplement some functions from Section 18 (there, recall, used to practice `break` and `continue`), in particular `has_any_odd`, `has_only_odd`, `has_three_odd` and `has_at_most_n_vowels`.

**23.17.** How many times does the word `Moby` occur in the text of _Moby Dick_ (or look for another word in a book of your choice)? (You should be able to reuse your function `read_from_gutenberg` from earlier.)

**23.18.** ⭐ Which punctuation marks are the most common in a book of your choice?

**23.19.** If in the previous exercise you used `sum`, `len` and/or `count` for counting the different types of punctuation mark, how often did your program need to iterate through the entire text? Can you think of a way to do this in a different, smarter, more efficient way?

<br>**_Counters (`Counter`)_**

**23.20.** ⭐ Perhaps the previous exercise made you think of a function you defined in Section 13, which counted list elements while iterating through the collection only once, with the help of a dictionary. Do you remember how it worked? Implement such a function again (or copy your previous version), to find out which punctuation marks are the most common in _Moby Dick_ (or a book of your choice).



**23.21.** Which vowels are the most common in a book of your choice? Which consonants?


**23.22.** The `Counter` class from the `collections` module is a type of dictionary that is specifically designed for counting (as in the previous exercises), as well as for retrieving the most common or least common types (exercises further below). First, execute the following code and demonstrate with additional code that the `Counter` object behaves in many ways like a dictionary (e.g., in terms of accessing elements, iterating of it, updating it).

```python
import collections
counter = collections.Counter(['a', 'a', 'b', 'c', 'a', 'a', 'b', 'c', 'c', 'c', 'd'])
```



**23.23.** In the above code, what is the difference (in value, in use) between `Counter` and (lowercase) `counter`?

**23.24.** Do you expect that a `Counter` object can also be constructed from a set, from a dictionary, or from a string? Test this.


**23.25.** Whenever you create a Counter object from, say, a list or a string, the counts will only be integer numbers (why?). But if you construct a Counter object from a dictionary directly (as above), no genuine 'counting' happens, so perhaps there is no inherent restriction to integers... Test this: can you construct a Counter from a dictionary whose values are floats? Reflect on whether such extended usage of Counter objects would be desirable.


**23.26.** Since `Counter` is a subclass of `dict`, it supports all methods a dictionary has, and potentially some in addition. One such additional method is `most_common`, e.g., `counter.most_common(3)` returns the top 3 most common elements. The integer is an optional argument; what is this function's default behavior (i.e., if you omit it the integer)?

**23.27.** Construct a `Counter` object from a tokenized Gutenberg text like _Moby Dick_ and print the 50 most common words. Also look up some specific word counts.

- - - - - -
**Something to keep in mind:** The logical quantifiers `any` and `all`, as well as `sum` and `len`, let us quantify and count how many elements meet a certain condition, but they are less suitable for collecting counts of multiple types of things in parallel. For that, use Python's **Counter** class (a type of dictionary).
- - - - -

**23.28.** ⭐⭐ Construct a counter for all _bigrams_ in a book of your choice, and another for all _trigrams_. Before looking at the results, do you expect bigrams to be generally more or less frequent than trigrams? (You may be able to reuse your own n-grams function from earlier, but to store their counts in a dictionary you need to represent n-grams in a way that is _hashable_.) Which bigrams and trigrams are the most common?






-------

**_Homework exercises for week 12 end here, now do at least one of the Mini-projects [K](../projects/K_processing_some_books.md), [L](../projects/L_scraping_the_web.md) (and don't forget to submit! ✉️)._**

-------




-----

**_🦋 You are now ready for [Mini-project M](../projects/M_identifying_topics.md)!_**

-----

**_🐝 You are now ready for [Mini-project N](../projects/N_detecting_collocations.md)!_**

-----

**_🦂 You are now ready for [Mini-project O](../projects/O_language_generation_with_an__n_-gram-based_language_model.md)!_**