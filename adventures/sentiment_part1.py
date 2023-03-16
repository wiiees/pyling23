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