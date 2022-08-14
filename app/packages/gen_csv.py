import pandas as pd

def create_data(di):
    ## generating random datasets from dictionary
    data = pd.DataFrame(data=dictionary)
    ## save the datasets
    data.to_csv('../app/data/team_heart.csv')
    pass


## generating random datasets to test
dictionary = {'Name': ['Gladys', 'Jose', 'jG'], 
                'Age': [23, 28, 1],
                'Hobby': ['Sleeping', 'Complaining', 'slpcomp']}

create_data(di=dictionary)