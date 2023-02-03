# Python for Linguists 2023

## Mini-project G: n-grams

**_Finish [Section 14](../exercises/14_looping_over_ranges.md) before attempting this project._**


**G.1.** Define a function `tokenize` that takes a string (and English sentence) and splits it into its individual words (tokens). You may be able to reuse a tokenizer from a previous section or Mini-project (i.e., copy and paste into your current file; later we will learn about `import` to avoid such duplication), or do it anew for extra practice.

**G.2.** ⭐⭐ Define a function to collect all _bigrams_, each bigram represented as a list containing two strings, e.g., `['the', 'apple']` for the bigram _the apple_. The function should return a list of such two-element lists, and it should contain the bigrams _as they occur in the text_ (i.e., including duplicates if the same bigram occurs in multiple places). Pause to consider whether you want this function to: a. take a plain text as input and automatically call tokenize within the function body, or b. take an already-tokenized text as input (in which case you need to tokenize the text separately _before_ you call the bigrams function). Up to you!


**G.3.** ⭐ Create another function to collect not bigrams but _trigrams_, i.e., sequences of three consecutive words.

**G.4.** Suppose we are interested in both bigrams and trigrams. Whether you called the tokenizer from _within_ each n-grams function, or separately beforehand, can affect the efficiency of your program. Do you see how? How often would either approach need to tokenize the same text? What about the approach you took?

**G.5.** ⭐ In case you haven't done so yet, define a more general `ngrams` function that takes an additional integer argument `n` and returns a list of `n`-grams. When this works, consider redefining the `bigrams` and `trigrams` functions as mere shorthands for a function call to `ngrams`. Why might this be a good idea (e.g., in relation to the DRY, SLAP and/or SoC principles)?

**G.6.** ⭐⭐ Write code to find the most frequent bigram, trigram and quadrigram of a given text (you can test it on a made-up example, or on an actual, longer text; see for instance Mini-project E for how to read the contents of a `.txt` file into your program). If you implement your counting with the help of a dictionary, you will notice that your current representation of n-grams (i.e., as lists) does not work, because dictionary keys need to be _hashable_. Find a way to solve this.

**G.7.** Conceptually (no programming requred): can you think of a way to use n-gram counts to automatically identify **collocations**? These are word combinations that occur more frequently than one would expect based on the frequencies of the individual words (e.g., idiomatic expressions such as 'kick the bucket'). (There will be another Mini-project specifically about collocations, later on.)
