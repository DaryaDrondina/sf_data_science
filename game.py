"""Game guess a number"""

import numpy as np

number = np.random.randint(1,100) #загадываем число 

#количество попыток 
count = 0 

while True:
    count +=1
    predict_number = int(input("Guess a number from 1 to 100 "))
    
    if predict_number > number:
        print ("Less")
    elif predict_number < number:
        print ("More")
    else:
        print(f"Yes! It's {number} for {count} attemps")
        break 
    