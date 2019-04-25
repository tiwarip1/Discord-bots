import os
exists = os.path.isfile('bitchlog.txt')

bitches = []

if exists:
    with open('bitchlog.txt','r') as f:
        for i in f:
            bitches.append(i)
            
print(bitches)            
        
