import os
import json

"""
Reads the text files from the original sentiment dataset, and stores everything in a single .jsonl (json-lines) file.
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