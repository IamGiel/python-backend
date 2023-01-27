import numpy as np
import random
import string

list1 = ['a', 'b', 'c']
list2 = ['apple', 'banana', 'cherry']
list3 = np.random.randint(0, 12, 12)

# method that will output list of random strings
def randomString(string_size, allowed_chars, list_size):
    container = []
    for i in range(list_size):
        print(i)
        container.append(''.join(random.choice('f{allowed_chars}'.capitalize()) for x in range(string_size)))
        
    return container  

        

chars = string.ascii_letters
size = 5

chars

x = randomString(size, chars, 4)
type(x)
len(x)
