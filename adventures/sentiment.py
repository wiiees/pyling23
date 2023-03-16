from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import linear_model
from sklearn.metrics import precision_score, recall_score, f1_score
import pandas


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

def basic_classifier(text):

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


def train_slightly_more_advanced_classifier(train):
    """
    Returns a logistic regression model using the features n_pos and n_neg.
    """
    model = linear_model.LogisticRegression()
    model.fit(train[['n_pos', 'n_neg']], train['sentiment'])

    return model


def train_even_more_advanced_classifier(train):
    """
    Returns a logistic regression model using the features n_pos and n_neg.
    """
    model = linear_model.LogisticRegression()
    model.fit(train[word_features], train['sentiment'])

    return model


def evaluate(predictions, targets):
    return {
        'prec': precision_score(targets, predictions, pos_label='pos'),
        'rec': recall_score(targets, predictions, pos_label='pos'),
        'f1': f1_score(targets, predictions, pos_label='pos'),
    }


reviews = pandas.read_json('data/sentiment.jsonl', lines=True)

reviews['n_pos'] = [count_words_from_list(text, positive_words) for text in reviews['text']]
reviews['n_neg'] = [count_words_from_list(text, negative_words) for text in reviews['text']]

word_features = []
for word in positive_words + negative_words:
    reviews[f'n_{word}'] = [text.count(word) for text in reviews['text']]
    word_features.append(f'n_{word}')


train, test = train_test_split(reviews)

test['basic_model_prediction'] = [basic_classifier(text) for text in test['text']]

sma_model = train_slightly_more_advanced_classifier(train)

test['sma_model_prediction'] = sma_model.predict(test[['n_pos', 'n_neg']])

ema_model = train_even_more_advanced_classifier(train)

test['ema_model_prediction'] = ema_model.predict(test[[f'n_{word}' for word in positive_words + negative_words]])

print(test.head(5).to_string())

basic_model_scores = evaluate(test['basic_model_prediction'], test['sentiment'])
sma_model_scores = evaluate(test['sma_model_prediction'], test['sentiment'])
ema_model_scores = evaluate(test['ema_model_prediction'], test['sentiment'])

print(basic_model_scores)
print(sma_model_scores)
print(ema_model_scores)

for word, coefficient in zip(positive_words + negative_words, ema_model.coef_.squeeze()[1:]):
    print(word, coefficient)
