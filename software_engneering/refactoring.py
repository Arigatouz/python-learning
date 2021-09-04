import math
import numpy as np


test_scores = [88, 92, 97, 93, 85]
print(np.mean(test_scores))

curved_test_score = [math.sqrt(score) * 10 for score in test_scores]
print(np.mean(curved_test_score))
