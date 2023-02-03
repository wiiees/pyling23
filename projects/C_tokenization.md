# Python for Linguists 2023

## Mini-project C: Tokenization

**_Finish [Section 11](../exercises/11_more_string_operations.md) before attempting this project._**


**C.1.** ⭐ Define a simple **word tokenizer** function, that takes a string (text) as input and returns a list containing the individual words (i.e., particular substrings) in the text. You can try to do this either by looping over the string, checking each character one at a time, or by using string methods like `split` (or a combination). It doesn't need to be perfect yet.

**C.2.** ⭐⭐ Although your tokenizer can get rid of spaces from the original text, it should not get rid of punctuation, treating punctuation marks instead as tokens in their own right. For example, tokenizing `Hello, world!` should result in `['Hello', ',', 'world', '!']`. Make sure this works correctly. Consider doing `import string` so you can use `string.punctuation` as your (still limited) inventory of punctuation.

**C.3.** Define a simple **sentence tokenizer** function, that takes a string (text) as input and returns a list of strings, each string a sentence from the original text. As before, punctuation is meaningful and should not be discarded in the process. 

**C.4.** Write a function that combines the foregoing: it takes a text as input, separates it into sentences, and then separates each sentence into words. Altogether, the result should be a _list of lists of strings_, each inner list representing a sentence split into words. 

**C.5.** ⭐ Apply your tokenizer to a reasonable large text, e.g., copied from a website or e-book. For now, you can simply copy this text into your Python script and assign it to a variable (recall you can use triple quotation marks to define multi-line strings); we will learn better ways to read files into Python later. Manually inspect the outcome of your word and sentence tokenizer to identify any shortcomings, and try to fix (some of) them.

