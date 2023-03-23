from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import linear_model
from sklearn.metrics import precision_score, recall_score, f1_score
import pandas

import wordcloud
import matplotlib.pyplot as plt

"""
The result of part 2 of our slightly rushed bag-of-words adventure; next class will start with a recap and some
refactoring.

If you want to try this yourself, you need to download the dataset here:

http://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz

Unpack the file, place the pos and neg folders it contains in a folder data/sentiment, and run 
the preprocessing script sentiment_to_jsonl.py . After that, you can run the current script.  
"""

negative_words = ['awful', 'disgusting', 'shit', 'horrible', 'terrible']
positive_words = ['wonderful', 'amazing', 'beautiful', 'great', 'lovely']

def handcrafted_model(text):

    tokenized_text = text.split()

    neg_count = sum([tokenized_text.count(neg_word) for neg_word in negative_words])
    pos_count = sum([tokenized_text.count(pos_word) for pos_word in positive_words])

    if neg_count > pos_count:
        sentiment = 'neg'
    else:
        sentiment = 'pos'

    return sentiment


def count_words_from_list(text, target_words):
    tokenized_text = text.split()
    return sum([tokenized_text.count(target_word) for target_word in target_words])


def train_model(X, y):
    """
    Returns a logistic regression model using the features n_pos and n_neg.
    """
    model = linear_model.LogisticRegression()
    model.fit(X, y)

    return model


def evaluate(y_pred, target_y):
    return {
        'prec': precision_score(target_y, y_pred, pos_label='pos'),
        'rec': recall_score(target_y, y_pred, pos_label='pos'),
        'f1': f1_score(target_y, y_pred, pos_label='pos'),
    }


word_features = []

def add_features(reviews):
    reviews['n_pos'] = [count_words_from_list(text, positive_words) for text in reviews['text']]
    reviews['n_neg'] = [count_words_from_list(text, negative_words) for text in reviews['text']]
    for word in positive_words + negative_words:
        reviews[f'n_{word}'] = [text.count(word) for text in reviews['text']]
        word_features.append(f'n_{word}')


def main():

    reviews = pandas.read_json('data/sentiment.jsonl', lines=True)
    add_features(reviews)
    train, test = train_test_split(reviews)

    logreg_posneg = train_model(train[['n_pos', 'n_neg']], train['sentiment'])
    logreg_wordlists = train_model(train[word_features], train['sentiment'])

    test['handcrafted_prediction'] = [handcrafted_model(text) for text in test['text']]
    test['posneg_prediction'] = logreg_posneg.predict(test[['n_pos', 'n_neg']])
    test['wordlists_prediction'] = logreg_wordlists.predict(test[[f'n_{word}' for word in positive_words + negative_words]])

    print(test.head(5).to_string())

    basic_model_scores = evaluate(test['handcrafted_prediction'], test['sentiment'])
    sma_model_scores = evaluate(test['posneg_prediction'], test['sentiment'])
    ema_model_scores = evaluate(test['wordlists_prediction'], test['sentiment'])

    print(basic_model_scores)
    print(sma_model_scores)
    print(ema_model_scores)

    for word, coefficient in zip(positive_words + negative_words, logreg_wordlists.coef_.squeeze()):
        print(word, coefficient)



if __name__ == '__main__':
    main()