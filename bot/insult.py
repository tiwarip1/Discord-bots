import random 
import os
import yaml
import json

def make_insult():
    print('DO SOMETHING')
    config = yaml.load(open(os.getcwd() + 'insults.yml'))
    
    pref = 'Thou'
    
    # algorithm simply makes a random choice from three different columns and concatenates them. 
    
    col1 = random.choice(config['column1'])
    
    col2 = random.choice(config['column2'])
    
    col3 = random.choice(config['column3'])

    # print generated insult for the 'user' 
    return [col1,col2,col3]
    #print( pref + ' ' + col1 + ' ' + col2 + ' ' + col3 + '.' )

