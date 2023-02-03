# Python for Linguists 2023

## Mini-project B: Random sentence generator

**_Finish [Section 9](../exercises/09_lists.md) before attempting this project._**


**B.1.** Write a program (subdivided into functions as you see fit) that generates a random English sentence of the shape "{determiner} {noun} {verb}s" (e.g., "the student walks"). Use separate lists to store a bunch of lexical items of the required syntactic categories. At the top of your program do `import random`, which lets you use the function `random.choice` to randomly select an item from a list. Select random items from the appropriate lists and compose a string from them, printing the final result.

**B.2.** ⭐⭐ Extend your sentence generator to randomly choose between an intransitive and a transitive verb frame, and then, depending on the verb frame, choose the right type of verb and a direct object if necessary.

**B.3.** ⭐ Extend your sentence generator to have it randomly choose between singular and plural nouns, and adjust the inflection of the verb accordingly.

**B.4.** ⭐ Enable the optional insertion of adjectives and adverbs.

**B.5.** ⭐⭐ _[Optional, feel free to skip!]_ Can you extend the sentence generator to allow for multiple adjectives, as in "The funny, tired, smart student walks"? We didn't learn about loops yet, but we did (briefly) encounter recursion in the previous section, so perhaps you can give it a go.

**B.6.** ⭐ Are there ways in which your code can be improved (refactored)? What are the DRY, SLAP and SoC principles again (Section 8)? Try to apply them.


