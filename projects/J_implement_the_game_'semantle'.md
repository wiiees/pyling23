# Python for Linguists 2023

## Mini-project J: Implement the game 'Semantle'

**_Finish [Section 19](../exercises/19_loop_control_flow.md) before attempting this project._**


**J.1.** ⭐ _Semantle_ is a free online game (https://semantle.com/) based on distributional semantics. Read the description (the question mark button) and give it a try.

**J.2.** This Mini-project will assume you have word vectors in the variable `word_vectors`, which behaves like dictionary mapping each word to its vector, i.e., a list (or Numpy-array) of numbers. For testing your code you can either a. manually define a small set of vectors, or b. use the word vectors we developed in the previous class, or c. use (something like) the following code to import 'real' word vectors using the `gensim` libary:

```python
import gensim.downloader as api

wv = api.load('glove-twitter-25')  
```
The `glove-twitter-25` vectors are only one of many standardly available 'models', see [this overview](https://github.com/RaRe-Technologies/gensim-data#models), which differ in the precise way of obtaining vectors from text and in the text corpus used. For quicker testing during development, consider using a smaller model such as `text8`. For the same vectors used in the real Semantle, use `word2vec-google-news-300` (large file). 

**J.3.** ⭐⭐⭐ Implement the mechanics of the Semantle game in Python. It should start with a random word choice, and then enter a loop where the user can guess words and the program gives feedback. Try to give the same type of feedback Semantle does (mainly: distributional semantic similarity to the target word). A commonly used similarity metric is `cosine similarity`; consider a web search on how to compute this in Python.
