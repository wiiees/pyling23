# Python for Linguists 2023

## 22. Sets and vocabularies (`set`)

Effort profile: `▁▁▁▁▁▁▂▁▁▁▁▄▅▁▂▂▁▂` 



**22.1.** Use the function `read_from_gutenberg` from the previous section to read a text file from Project Gutenberg, and tokenize the text to obtain the list `tokens`.

**22.2.** Extract the text's _vocabulary_ by doing `set(tokens)` and inspect it. Python's _set_ data structure contains every element only once, hence creating a set from a list (or other collection) gives us the unique elements. Depending on your tokenizer, the vocabulary may be quite messy (e.g., spaces, punctuation); consider improving the tokenizer if that is the case. 

**22.3.** Apply `dir` to the vocabulary to get a quick overview of the available methods for the 'set' class (of which it is an instance). In fact, let's use list comprehension to print only the method names that do _not_ start with an underscore.

**22.4.** In maths/set theory, sets are written with curly braces like `{1, 2, 3}`. Does that work in Python, too? What about creating an empty set like this `{}`? (Make a prediction, but also try it and, just to make sure, check the type of the resulting object.) Can you find (by experimenting or searching the web) some (other) way to create an empty set?

**22.5.** Also in maths/set theory, the order of elements in a set does not matter. Find a way to verify that this is how sets also behave in Python (e.g., using `==` to test if two sets count as 'equal'), and use the same kind of test on lists, to show that order does matter for lists.

**22.6.** Can you create a set containing strings? A set containing tuples? A set containing lists? Why (not)?

- - - - - -
**Something to keep in mind:** The **set** data structure contains each element only once. Moreover, sets are significantly faster than lists when it comes to determining if an object is present in the set. (Though lists are much faster if you know the index of the object you are looking for.) The price to pay for this lookup speed is that sets can only contain objects that are **hashable**, just like a dictionary's keys.
- - - - -

**22.7.** ⭐ Do sets have a 'length' (`len`)? Can you check with `in` whether a set contains a certain element? Can you iterate over a set? Can you construct one set from another using comprehension syntax? Do you expect that you can use slicing on a set, as you would with a list? Why (not)? Test your expectation.

**22.8.** After creating a set, one can add elements to it with the method `add`, e.g., `my_set.add(5)`. What happens if you try to add an element that is already in the set? Do sets also have an `append` method like lists? Why might this be? Do lists have a method `add`, like sets? 

**22.9.** Although you can iterate over the elements in a set, the _order_ of iteration must not be relied upon (unlike lists and, in recent Python versions, dictionaries), as it depends on hash-codes which (in most Python implementations, for anything but the most basic types of objects) will vary between runs of the same program. Verify this by iterating over a set like `{'a', 'b', 'c', 'd', 'e', 'f'}` in your script, printing each element. Running the script several times should result in different element orders (though _within_ a run, e.g., if you iterate over the same set multiple times within a script, the order is maintained).

**22.10.** Recall that `+` is a shortcut for addition-like methods provided by classes like integer, string and list. Does `+` also work on sets? 


**22.11.** There are several operators in Python that work on sets. By trying with different sets, figure out what `set1 - set2`, `set1 | set2` and `set1 & set2` represent, and match these operators with some of the set methods you found above by doing `dir`.

**22.12.** ⭐⭐ Part of cleaning up a vocabulary is to standardize capitalization. Simply lower-casing everything is not satisfactory, since in many languages some words _must_ be capitalized (e.g., names in English, nouns in German). Define a function to standardize capitalization in a smarter way, i.e, that respects the fact that some words should not be lower-cased. Define this as a function that takes a tokenized text as input (i.e., prior to constructing the vocabulary from it); can you think of a reason why that is the better place to do it?

**22.13.** Write code to output the vocabulary you obtained from the Gutenberg text to a new file (in a suitable place and with a suitable file name), with one word per line. (Again, if you notice that your vocabulary is still quite 'polluted', e.g., with spaces, newlines, punctuation, consider improving the tokenizer or adding some subsequent cleanup.)

**22.14.** ⭐ Suppose our purpose is to compare the **lexical diversity** of books (as on Gutenberg) vs. some other textual medium (e.g. tweets, or news media). Think of a way to compute the lexical diversity of the text, and implement this. Formulate a hypothesis about the comparative lexical diversity of different media (no need to actually test your hypothesis, though of course feel free to).

**22.15.** ⭐ A conceptual question about lexical diversity: do you think verbal inflection ought to be standardized before computing lexical diversity, e.g., treating _walk_, _walked_ and _walks_ as the same entry? If not, can you think of some other purpose (research or applied) for which verbal inflection should probably be standardized? Can you think (in outline) of an algorithm to achieve this? (In Section 26 we will encounter two common approaches: _stemming_ and _lemmatization_.)

**22.16.** Can you predict what happens if you construct a set not from the tokenized text (`tokens`), but from the original, un-tokenized text directly? Roughly how many elements do you expect the resulting set to have? Only test this after formulating an explicit prediction.


**22.17.** ⭐ Did this section introduce any new keywords? Did it introduce any new builtins? Built-in functions can be found in `__builtins__`, try printing it. Depending on the implementation it is either of type `module` (the type of thing that results from `import`) or a dictionary. In fact, in PyCharm, `__builtins__` in the Python Console is equivalent to `__builtins__.__dict__` in a script. Do `print(dir(__builtins__))` in a script (`dir` lists the contents of a module), or `print(list(__builtins__))` in the Python console (to list the keys of the dictionary). For which of the built-ins do you already know some purpose?
