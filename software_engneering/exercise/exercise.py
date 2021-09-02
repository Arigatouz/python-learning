from IPython.display import Math
import pandas as pd
df = pd.read_csv('winequality-red.csv', sep=';')
df.head()
# Renaming Columns

df.columns = [label.replace(' ', '_') for label in df.columns]
df.head()

print(df)
# Analyzing Features
'''
"### Analyzing Features\n",
"Now that your columns are ready, you want to see how different features of this dataset relate to the quality rating of the wine. A very simple way you could do this is by observing the mean quality rating for the top and bottom half of each feature. The code below does this for four features. It looks pretty repetitive right now. Can you make this more concise? \n",
"\n",
"You might challenge yourself to figure out how to make this code more efficient! But you don't need to worry too much about efficiency right now - we will cover that more in the next section."'''


def calculate_quality_rating(column_name):
    median = df[column_name].median()
    for i, value in enumerate(df[column_name]):
        if value >= median:
            df.loc[i, column_name] = 'high'
        else:
            df.loc[i, column_name] = 'low'


for lables in df.columns[:-1]:
    calculate_quality_rating(lables)
    group = '{} {}'.format(df.groupby(lables).quality.mean(), "\n")
    print(group)
