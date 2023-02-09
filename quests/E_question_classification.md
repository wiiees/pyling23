# Python for Linguists 2023

## Coding Quest E: Question classification

**_Finish [Section 13](../exercises/13_dictionary_basics.md) before attempting this quest._**


**E.1.** Download [this file](../data/questions.txt) containing many English questions, and place it in a subfolder `data` of your current working directory. You can then read it into Python by doing the following (a later section will teach us more about reading files):
```python
with open('data/questions.txt') as questionreader:
    questions = questionreader.read()
```
Alternatively, simply copy-paste the file's contents into your `.py` file and assign it to a variable; you can place the text in between triple quotation marks to create such a large, multi-line string. (Ultimately, mixing code with data in the same file is not ideal; can you think of some reasons why?)

**E.2.** Split the questions text into separate lines and verify that this gives you a list of individual questions. How many questions are there? How long are they on average (number of words)?

**E.3.** ⭐ Define a function that categorizes questions according to their 'wh'-word (e.g., _who_, _what_, _where_, _how_). For instance, "Who was there?" should receive category `who`, and "Do you like icecream?" should receive category `other`.

**E.4.** ⭐⭐ Iterate through the list of questions (or their categories), and use a dictionary to count how often each category occurs. Which type of question is the most frequent in this dataset? Does the 'other' category erroneously include questions that should have been classified otherwise? If so, try to improve your code. For instance, your program should probably detect wh-words also if they appear later in the sentence, not only when they are fronted. Once it does, do you get many 'false positives'? (For instance, wh-words in relative clauses should arguably be ignored: "the student who sneezed apologized".) Try to implement some simple heuristics to reduce the amount of misclassifications -- but of course you are not expected to build a full syntactic parser at this level; we will return to syntactic analysis in a later section.

**E.5.** ⭐ Categorizing questions based on wh-word is arguably too superficial, as the same wh-word can be used to ask very different kinds of questions, and different wh-words can be used to ask the same question. For instance, 'How come' can be an alternative way of asking 'Why', 'Which person' is basically synonymous with 'Who', and 'Who' and 'Whom' should arguably be conflated into a single category. Implement code to achieve this. You can browse through the data itself for examples on which to base a more refined categorization.


