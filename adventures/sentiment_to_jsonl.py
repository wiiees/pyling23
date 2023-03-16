import os
import json

"""
Reads the text files from the original sentiment dataset, and stores everything in a single .jsonl (json-lines) file.

If you want to try this yourself, you need to download the dataset here:

http://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz

Unpack the file, place the pos and neg folders it contains in a folder data/sentiment, and run 
the preprocessing script sentiment_to_jsonl.py . After that, you can run the current script.  
"""

pos_dir = 'data/sentiment/pos'
neg_dir = 'data/sentiment/neg'

def main():

    reviews = []

    for filename in os.listdir(pos_dir):
        with open(f'{pos_dir}/{filename}', 'r') as textreader:
            reviews.append({
                'text': textreader.read(),
                'sentiment': 'pos'
            })

    for filename in os.listdir(neg_dir):
        with open(f'{neg_dir}/{filename}', 'r') as textreader:
            reviews.append({
                'text': textreader.read(),
                'sentiment': 'neg'
            })

    with open('data/sentiment.jsonl', 'w') as outfile:
        for review in reviews:
            json.dump(review, outfile)
            outfile.write('\n')


if __name__ == '__main__':
    main()