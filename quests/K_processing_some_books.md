# Python for Linguists 2023

## Coding Quest K: Processing some books

**_Finish [Section 20](../exercises/20_reading_and_writing_files.md) before attempting this quest._**


**K.1.** Above you created the function `read_from_gutenberg`. However, as you may have noticed, text files from the Gutenberg project contain some meta-information (title, author, licence, etc.) that must be distinguished from the actual, original text. For instance, in Moby Dick look for lines beginning with `*** START` and `*** END`. Enhance your `read_from_gutenberg` function so that only the original text (between the `*** START` and `*** END` lines) is returned.

**K.2.** ⭐⭐ Modify your `read_from_gutenberg` function further so that instead of ignoring the meta-information, it parses the file-initial portion (with, e.g., title and author information) to store the meta-information in a dictionary. More precisely, any line above `*** START` that contains a colon, should be added to the dictionary as a key-value pair. The extracted text itself should be added to this dictionary too, under the key `'text'`, such that the function can simply return this whole dictionary containing both the meta-information and the plain text.

**K.3.** ⭐ One further enhancement: text files from the Gutenberg project are 'hard word-wrapped', i.e., a newline character was inserted whenever a line exceeded a certain number of characters. Since these single newlines (`\n`) were not meaningful parts of the original text, we want to get rid of them (e.g., replace them by a space). However, make sure we don't lose the information carried by _double_ newlines (`\n\n`), which _do_ represent a meaningful aspect of the original text, namely paragraph separations.

**K.4.** ⭐ Compute some statistics for one or more texts from Project Gutenberg, such as average word length (in number of characters) and average sentence length (in number of words). (You may be able to reuse some of your earlier code for splitting a text into sentences and words.) Do you expect there to be much variation in these numbers between languages? Between books of the same author? Between different authors? Do you think these kinds of statistics could be used to compute a measure of 'reading difficulty' for people (e.g., kids) at different levels of literacy education? Try to think of some other kinds of statistics that could be used for such a purpose.

**K.5.** With Python having such a large ecosystem, _of course_ someone else has already developed some Python code for processing books from Project Gutenberg. For instance, have a look at this repository: https://github.com/raduangelescu/gutenbergpy. In the file [textget.py](https://github.com/raduangelescu/gutenbergpy/blob/master/gutenbergpy/textget.py) you will find the function `strip_headers`; what do you think it does? And how does it do it? Try to understand as much of this function as possible. You will notice that it relies on a variable `TEXT_START_MARKERS`, defined earlier in the same file, have a look! What does this list show us about the Project Gutenberg dataset? And about our approach above?


