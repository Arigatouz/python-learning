# // best refactoring code so we can reach the best practice code

import math
import numpy as np


def bad_code():
    '''
    this function present working code but bad practice
    '''
    s = [88, 92, 79, 93, 85]
    print(sum(s) / len(s))

    s1 = []
    for x in s:
        s1.append(x + 5)
        print(sum(s1) / len(s1))

    s2 = []
    for x in s:
        s2.append(x + 10)
        print(sum(s2) / len(s2))

    s3 = []
    for x in s:
        s3.append(x ** 0.5 * 10)
        print(sum(s3) / len(s3))


# bad_code()


def little_better_code():
    '''
    this function present working code but little better in  practice (not the best practice but its good)
    '''

    test_scores = [88, 92, 79, 93, 85]
    print(np.mean(test_scores))

    curved_5 = [score + 5 for score in test_scores]
    print(np.mean(curved_5))

    curved_10 = [score + 10 for score in test_scores]
    print(np.mean(curved_10))

    curved_sqrt = [math.sqrt(score) * 10 for score in test_scores]
    print(np.mean(curved_sqrt))


# little_better_code()


def better_code():
    '''
    this function present working code and best practice when it come to writing code
    '''
    def flat_curved(arr, n):
        return [i + n for i in arr]

    def square_root_curved(arr, n):
        return [math.sqrt(i) * n for i in arr]

    test_scores = [88, 92, 79, 93, 85]
    curved_5 = flat_curved(test_scores, 5)
    curved_10 = flat_curved(test_scores, 10)
    curved_sqrt = square_root_curved(test_scores, 10)

    def gettin_average():
        for score_list in test_scores, curved_5, curved_10, curved_sqrt:
            print(np.mean(score_list))
    gettin_average()


better_code()
