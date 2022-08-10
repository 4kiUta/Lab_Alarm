import pandas as pd

## generating random datasets to test
dictionary = {'Name': ['Gladys', 'Jose'], 
                'Age': [23, 28],
                'Hobby': ['Sleeping', 'Complaining']}

data = pd.DataFrame(data=dictionary)

## save the datasets
data.to_csv('data_gen/team_heart.csv')



