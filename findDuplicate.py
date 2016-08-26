

import random

def findDuplicate(arr):
    pos = 0
    val_prev = None
    while True:
        val = arr[pos]
        pos = arr[val]

    return arr


A B C D  

if __name__ == "__main__":
    arr = [random.randint(0,10) for x in range(0,11)]
    print arr
    print findDuplicate(arr)
