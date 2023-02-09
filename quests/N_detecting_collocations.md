# Python for Linguists 2023

## Coding Quest N: Detecting collocations

**_Finish [Section 23](../exercises/23_quantifiers_and_counters.md) before attempting this quest._**



**N.1.** ⭐ Let's try to automatically detect **collocations**, such as 'fast food', 'richly decorated' and 'regular exercise'. These are word combinations that occur more frequently than one would expect based on the frequencies of the individual words. 'Expect' is a probabilistic notion. If you haven't already, write a function that turns a `Counter` object into a dictionary of (estimated) _probabilities_. Remember that probabilities should sum to 1.

**N.2.** ⭐⭐ Define a function that takes three arguments -- a bigram, a dictionary with single token probabilities and a dictionary with bigram probabilities -- and returns a measure of 'collocationhood' for the specific bigram. A simple approach might be to compute the difference between the 'observed' probability of a bigram (_prob(word1 word2)_) and the 'expected' probability if the two tokens had been independent (_prob(word1) * prob(word2)_).

**N.3.** ⭐ Use the preceding function to obtain a dictionary mapping all bigrams to their degree of 'collocationhood', and inspect the result to see if your collocation detection program yields reasonable results. For easier inspection, consider creating a Counter object from the dictionary as before, so that you can use its method `most_common` (this is a slight abuse of the Counter class (why?); the next section introduces better ways to sort items).

**N.4.** ⭐ Generalize the previous code to find potential three-word collocations, and inspect the outcome.

**N.5.** ⭐ Generalize the foregoing to be able to find not only word-level collocations, but also _character-level_ collocations (e.g., perhaps 'th' is more common than one would expect based on 't' and 'h' alone).



