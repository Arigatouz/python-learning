import time
# import pandas as pd
import numpy as np

with open('book_last_2_yeas.txt', 'r') as books:
    recent_books = books.read().split('\n')

with open('programming_books.txt', 'r') as programming_books:
    recent_programming_books = programming_books.read().split('\n')
start = time.time()
selected_books = []
intersected = np.intersect1d(recent_books, recent_programming_books, assume_unique=False, return_indices=False)
for book in intersected:
    selected_books.append(book)
print(selected_books)
print(len(selected_books))
print('time to do the job is {}'.format(time.time() - start))

# that's mean sets is even faster than numpy
start2 = time.time()
recent_coding_books = set(recent_books).intersection(recent_programming_books)
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start2))
