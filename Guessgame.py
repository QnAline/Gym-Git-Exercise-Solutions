# here we use random integer for two specified points
# we will use loop to execute indefinetly

import random
score=10
random_number=random.randint(1,10)
while True:
    entered=int(input('enter a number'))
    if entered == random_number:
        print('congulations your score is:',str(score))
        break # to end the loop execution   
    else:
        print('try another round')
        score-=1


