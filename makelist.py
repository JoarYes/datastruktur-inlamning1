import random

def createArray(length):

    array = []

    for i in range(length):
        array += [i]

    for i in range(length):
        swap = random.randint(0, length-1)
        arrayS = array[swap]

        array[swap] = array[i]
        array[i] = arrayS

    return array