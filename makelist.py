import random

def createArray(length):

    array = []

    for i in range(length):
        array += [i]

    for i in range(length):
        swap = random.randint(0, length-1)

        array[swap] = array[i]

    return array
