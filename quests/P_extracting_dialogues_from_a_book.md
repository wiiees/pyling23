# Python for Linguists 2023

## Coding Quest P: Extracting dialogues from a book

**_Finish [Section 26](../exercises/26_regular_expressions.md) before attempting this quest._**


**P.1.** ⭐⭐ Download a text from the Gutenberg project that, incorporated in the story, contains plenty reported speech surrounded by quotation marks (e.g., _The Adventures of Sherlock Holmes_, https://www.gutenberg.org/ebooks/1661). Extract such quotations with the help of a regular expression. You need to look for any passage contained in quotation marks, where the passage does not itself contain a quotation mark (why is the latter restriction necessary?). Be aware of the many types of quotation marks that can in principle be used (https://unicode-table.com/en/sets/quotation-marks/), and make sure your regular expression works at least for your specific text.

**P.2.** ⭐⭐⭐ Building on the foregoing, write a function that extracts all 'dialogues' from a text, where a dialogue is a series of sufficiently close, consecutive quotations. Use the `span` method of the retrieved `Match` objects to decide whether two quotations are close enough to belong to 'the same dialogue', or whether they are better understood as constituting separate dialogues.

**P.3.** ⭐⭐ Write your corpus of extracted dialogues to a file, using a sensible format (so that, say, a dialogue researcher could easily read in the data with Python again). 

**P.4.** With a big enough corpus of literature, do you think the resulting corpus could be used as a window on actual human dialogue? Why (not), or in which way(s)? Do you think the dialogues corpus could be used for probabilistic language generation (whether based on n-grams (cf. an earlier Coding Quest) or something more advanced)? What might be a suitable application? 

