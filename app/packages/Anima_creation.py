import pandas as pd

class Animal():
    
    def __init__(self, type, name, age, owner) -> None:
        self.type = type
        self.name = name
        self.age = age
        self.owner = owner
 
    def action(self):
        if self.type == 'dog':
            return 'I follow my tail in circles'
        else:
            return "I don't know what to do"


    def fram_creation(self):
        details = [[self.type, self.name, self.age, self.owner]]
        df = pd.DataFrame(data=details, columns=['type', 'name', 'age', 'owner'])
        return df