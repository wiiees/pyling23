
# Python for Linguists 2023

◄ (2/03) [Functions (1/2)](../classes/04_Functions_1.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;['Bag of words' (2/2)](../classes/06_Bag_of_words_2.md) (16/03) ►

-------

## Week 5: 'Bag of words' (1/2) (9/03)


### Plan
1. Quiz
2. Homework discussion
3. 'Bag of words' (1/2)
4. Practical


-------

### 1. Quiz

The quiz will be handed out during class.

-------

### 2. Homework for today

Exercises:
- [Section 9. Lists (list, append, [...])](../exercises/09_lists.md): all exercises

And the following Coding Quest (✉️!):
- [Quest B. Random sentence generator](../quests/B_random_sentence_generator.md) 

-------

### 3. Class notes

```python

x = 5

# x += 3        # x.__iadd__(3) if it exists, otherwise x.__add__(3)
x = x + 3       # x.__add__(3)

print(x)


a = [1, 2, 3]
c = a
b = [4, 5, 6]

a += b
# a = a + b

print(a)
print(c)
```

tl;dr: a += b   is _not_ shorthand for  a = a + b, although if a is immutable, they both call the same function.

#### 'Bag of words' (1/2)

Bag-of-words adventure!

Part 1: 'feature engineering' to create a sentiment classifier.
Part 2: 'feature extraction' using bag-of-words.

Approaches:
- hand-crafted rule / rule-based system (inc. feature engineering) <-- part 1 
- machine-learning system
  - feature engineering
  - feature extraction <-- e.g., bag of words (part 2)
    - representation learning <-- deep learning

Overfitting: better not test and train your model on the same data.

#### Our adventure code so far 

```python

import os

pos_dir = 'data/sentiment/pos'
neg_dir = 'data/sentiment/neg'

reviews = []

for filename in os.listdir(pos_dir):
    with open(f'{pos_dir}/{filename}', 'r') as textreader:
        reviews.append([textreader.read(), 'pos'])

for filename in os.listdir(neg_dir):
    with open(f'{neg_dir}/{filename}', 'r') as textreader:
        reviews.append([textreader.read(), 'neg'])

print([label == 'pos' for _, label in reviews].count(True), 'positives')
print([label == 'neg' for _, label in reviews].count(True), 'negatives')

print(sum([text.count('!') for text, _ in reviews]), 'exclamation marks')



negative_words = ['awful', 'disgusting', 'shit', 'horrible', 'terrible']
positive_words = ['wonderful', 'amazing', 'beautiful', 'great', 'lovely']


def classify_sentiment(text):

    tokenized_text = text.split()

    neg_count = sum([tokenized_text.count(neg_word) for neg_word in negative_words])
    pos_count = sum([tokenized_text.count(pos_word) for pos_word in positive_words])

    if neg_count > pos_count:
        sentiment = 'neg'
    else:
        sentiment = 'pos'

    return sentiment

result = classify_sentiment(reviews[5][0])

print(result)

```

-------

### 4. Practicum: homework for next time

Exercises:
- [Section 10. For-loops (for)](../exercises/10_for-loops.md): all exercises&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (`▁▁▁▁▁▂▁▂▁(▁)▂▂▂▁▂▂▁▂▂▄▅▄▅▂▄▅▁▂▁▂▄▅▁▂▂▂▁(▂)▂▄▅▁▄▅`)
- [Section 11. More string operations (split/join, strip)](../exercises/11_more_string_operations.md): all exercises&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (`▄▅▂▁▁▂▁▂▄▅▂▄▅▁▂▂`)

And the following Coding Quest (✉️!):
- [Quest C. Tokenization](../quests/C_tokenization.md) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (`▂▄▅▁▁▂`)

