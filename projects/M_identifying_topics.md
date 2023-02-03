# Python for Linguists 2023

## Mini-project M: Identifying topics

**_Finish [Section 23](../exercises/23_quantifiers_and_counters.md) before attempting this project._**


**M.1.** Do you think the most frequent words in a book are a good indicator of the _topics_ of that book? Test this if you like.

**M.2.** A plausible topic for a specific book is a word that is significantly _more frequent in that book than one would expect based on a larger set of books_. 'Expect' is a probabilistic notion. If you haven't already, write a function that turns a `Counter` object into a dictionary of (estimated) _probabilities_. Remember that probabilities should sum to 1.

**M.3.** ⭐⭐⭐ Implement the aforementioned idea in Python. The key function of your program should take two arguments -- one Counter constructed from a specific book, and one Counter constructed from a larger set of books -- and return dictionary mapping each word to a float that represents the degree of 'topicality' of the word in the specific book.

**M.4.** ⭐ Apply your program to a number of specific books (each time comparing them against a larger set of books). For easier inspection, consider creating a Counter object from the 'topicality' measures dictionary as before, so that you can use its method `most_common` (this is a slight abuse of the Counter class (why?); the next section introduces better ways to sort items). Does you program identify meaningful topics for each book? Can you think of ways to improve it, e.g., by additionally filtering the set of words or adjusting the counts before computing the topicality measure?


