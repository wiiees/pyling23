# Python for Linguists 2023

## Coding Quest H: Zipf's law

**_Finish [Section 18](../exercises/18_dictionaries_advanced.md) before attempting this quest._**


**H.1.** ⭐ According to _Zipf's law_, the frequency of any word in a natural language corpus is inversely proportional to its rank in the frequency table (most frequent = 1, second most frequent = 2, etc.). (Consider doing a quick web search to orient yourself around this well-known topic.) Without programming and without peeking at the next exercises, think of a way to test computationally whether a given corpus or text of choice follows Zipf's law: write down a list of concrete programming steps/functions we might need.

**H.2.** Download [this file](../data/alice.txt) containing English text, and place it in a subfolder `data` of your current working directory. You can then read it into Python by doing the following (a later section will teach us more about reading files):
```python
with open('data/alice.txt') as reader:
    text = reader.read()
```
Alternatively, simply copy-paste (some of) the file's contents into your `.py` file and assign it to a variable; you can place the text in between triple quotation marks to create such a large, multi-line string. (Ultimately, mixing code with data in the same file is not ideal; can you think of some reasons why?)

**H.3.** ⭐⭐ Tokenize the text, and then create a dictionary of token counts, i.e., mapping each word to the number of times it occurs in the text, and finally extract just the counts into a list, which you can call `counts`. Finally, sort the counts from high to low with the following command:
```python
counts.sort(reverse=True)
```
Check whether this `sort` method changes the original counts list in-place, or creates a new one (we will learn all about sorting in a later section).

**H.4.** Zipf's law is an observation about the relation between the _rank_ of a word (most frequent, second most frequent, third most frequent, etc.) and its _frequency_ (i.e., count). We already have the sorted frequencies in `counts`; now create a list `ranks` of equal length, simply containing the ranks 1, 2, 3, 4, etc.

**H.5.** One way to inspect the Zipfian-ness of the relation between counts and ranks by creating a line plot, for instance as follows, with the `seaborn` plotting library (here we follow the arguably stupid convention of importing it under a marginally shorter pseudonym `sns`):
```python
import seaborn as sns

plot = sns.lineplot(x=ranks, y=counts)
figure = plot.get_figure()
figure.show()
```
If the plot does not show up, try to solve this with the help of a web search.

**H.6.** ⭐ Whether the plot genuinely shows Zipf's law or some other type of inverse relationship is better seen in a _log-log plot_, where Zipf's law should show up as a straight line. Test whether this is (approximately) the case by computing lists `log_ranks` and `log_counts` (with the help of `import math` and `math.log`) and redoing the plot from these lists. 

**H.7.** ⭐⭐ Does Zipf's law show up only in token frequencies, or also in character frequencies? What about bigram frequencies? And trigram frequencies? And consonant clusters? And just the capital letters? Explore this with code.


