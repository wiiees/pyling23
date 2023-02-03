# Python for Linguists 2023

## Mini-project I: Translation

**_Finish [Section 18](../exercises/18_dictionaries_advanced.md) before attempting this project._**


**I.1.** Create a dictionary `en_to_nl` that maps some English words to Dutch words. (You can also use another language pair of choice for these exercises.)

**I.2.** ⭐ Write a function `invert_dict` that takes a dictionary and returns a new, inverse dictionary, mapping the original values back to the original keys. Use this to construct a dictionary `nl_to_en` from the original `en_to_nl` you defined in the previous exercsie. Can you now use the two dictionaries to translate back and forth? For instance, assuming your original dictionary contained the word _tree_, what is the outcome of `nl_to_en[en_to_nl[nl_to_en[en_to_nl['tree']]]]`?

**I.3.** To `en_to_nl`, add the English word _feather_ mapping to Dutch _veer_, as well as the English word _spring_, which also happens to translate into Dutch _veer_. Feed it into your function `invert_dict`. What is the problem, technically and conceptually? Illustrate this in code by inverting your dictionary `en_to_nl` once, and then inverting the result again, comparing the outcome to the original. (You can use your function `print_dict` from above to print the dictionaries in a more readable way.)

**I.4.** ⭐⭐ In general, a single word can have multiple adequate translations, for instance if the word is ambiguous or if the target language has multiple synonyms. To account for this, define a different type of dictionary, `en_to_nl_multi` that maps each English word to a _list_ of Dutch words, e.g., `{'bat': ['vleermuis', 'knuppel'], 'tree': ['boom'], ...}`. Your previous function `invert_dict` does not work on this type of mapping (explain what the problem is), so write a new function `invert_dict_multi` that does work. Note that just switching keys and values won't be adequate; the inverted dictionary `nl_to_en_multi` should again be a mapping from single strings to lists, just like the original. Your new inversion function should handle the _bat_ (_vleermuis_/_knuppel_) example correctly, and also solve the _feather_/_spring_ (_veer_) problem from the previous exercise.

**I.5.** ⭐ Write a function that takes a text and a dictionary as parameters, and returns a word-by-word translation of the text. You can of course use `text_utils.tokenize` to get the individual words for translation. If multiple translations for a given word are possible, choose a random one (e.g., using `random.choice(...)`). Add enough words to your dictionary to enable the translation of some simple sentences. For instance, feeding your translation function the sentence _The feather was very light_ (together with the `en_to_nl` dictionary) should result in _De veer was heel licht_.

**I.6.** ⭐ What if your text contains a word that is not in the dictionary? Give your translation function a third parameter `mask_unknown` that is a boolean with a default value True. If it is set to True, unknown words should appear as `<UNKOWN>` in the resulting translation. If it is set to False, unknown words should simply be left untranslated (e.g., resulting in a mostly-Dutch sentence with some untranslated English words). (Hint: You can of course use `in` to check if a word is included in the dictionary or not, but doing so will often lead to two dictionary lookups where one should suffice (consider why). The `get` method of dictionary objects is better here; enter `help({}.get)` in the Python console to see how you can use it.)

**I.7.** Naturally, a shortcoming of word-by-word translation is that any word order differences between languages are not accounted for. Illustrate this with a sentence of choice. Without programming, can you think of a reason why (or a way in which) n-grams could be used to improve the accuracy of automatic translation?

