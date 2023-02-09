# Python for Linguists 2023

## Coding Quest O: Language generation with an _n_-gram-based language model

**_Finish [Section 23](../exercises/23_quantifiers_and_counters.md) before attempting this quest._**


**O.1.** ⭐ Conceptually (no programming yet): think of a way in which we could automatically generate text by, repeatedly, randomly sampling the next word given previous words, on the basis of _n_-gram probabilities estimated from a text corpus. Even the largest, current deep learning models for language generation can be regarded as generalizations of this simple idea.

**O.2.** If you haven't already, write a function that turns a `Counter` object into a dictionary of (estimated) probabilities.

**O.3.** ⭐⭐⭐ Write a function that takes a starting word `prompt` and a dictionary of single token and bigram probabilities (or two separate dictionaries, if you prefer). It should return a random next word that could reasonably follow the `prompt` in a sentence (e.g., if the `prompt` is a noun like _cat_, the next word could be a verb like _sleeps_). This should be achieved by probabilistically sampling the next word based on the previous word, for instance as follows (or ignore this and figure it out for yourself!): 
 - Find a list of all bi-grams whose first word matches with the `prompt` (e.g., _cat sleeps_, _cat chased_, etc.). 
 - If any such `prompt`-matching bi-grams are found, use `random.choices` to choose a random bi-gram from this list; you should provide `random.choices` with the optional argument `weights`, which should be a list of the probabilities of the bi-grams to sample from. Then, given a randomly selected bigram (e.g., _cat sleeps_), the word-to-be-generated is simply the _second_ word of that bi-gram (e.g., _sleeps_). 
 - If no `prompt`-matching bi-grams are found, just ignore the bi-grams and instead sample a random word based on the _single_ token probabilities (this will be very random, but it's a last resort).

**O.4.** ⭐⭐ Generalize the foregoing to allow also _tri_-grams: it will first check for a matching tri-gram, if that fails it tries the bi-grams, and only if that fails will it sample a single token at random (i.e., the last resort). For this generalization, it will be best to make the `prompt` a list of tokens: when searching tri-grams you can then look at the final _two_ tokens of the `prompt`).

**O.5.** ⭐ You should now have a function that generates the next word given a list of previous words. Now, wrap this up into a larger program that first asks for `input` from the user (the writing prompt) and then enters a potentially infinite loop that continuously samples the next word by using the current prompt + newly generated word as the next prompt. You can make your program run continuously, or wait for user input each iteration, or have it stop after a certain number of words is reached.

**O.6.** ⭐ Inspect the quality of your language generator. For instance, compare the generated sentences if you use 3, 2 and 1-grams vs. only 2 and 1-grams, or even only 1-grams. Do you observe differences in the type of generated language? Which is more grammatical? More human-like? Do you think your generator will improve with _n_-grams of higher _n_, and/or with a larger corpus to extract the probabilities from? (You can of course generalize your code to try this.)

**O.7.** ⭐ Try to generalize the foregoing code to also work at the character-level, i.e., letting it sample one character at a time. It may be that you don't really need to change much! What is your impression of the generated language? Do you think it will improve with character _n_-grams for higher _n_? Can you think of pros/cons of character-level generation vs. word-level generation?

