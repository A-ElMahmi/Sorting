'''
Python Sorting Algorithms: https://tuxar.uk/popular-sorting-algorithms/

Sorting Algorithms Visualisations: https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
'''

import random
randList = [random.randint(1, 10) for i in range(8)]
print(randList)


def bubbleSort(seq):
  changed = True
  while changed:
    changed = False
    for i in range(len(seq)-1):
      if seq[i] > seq[i+1]:
        seq[i], seq[i+1] = seq[i+1], seq[i]
        changed = True
  return seq

# print(bubbleSort(list(randList)))


def insertionSort(seq):
  for i in range(1, len(seq)):
    while seq[i] < seq[i-1] and i > 0:
      seq.insert(i-1, seq[i])
      seq.pop(i+1)
      i -= 1 
  return seq

# print(insertionSort(list(randList)))


def selectionSort(seq):
  for x in range(len(seq)):
    smallest, index = sum(seq), 0
    for i in range(x, len(seq)):
      if seq[i] < smallest:
        smallest, index = seq[i], i
    seq[x], seq[index] = smallest, seq[x]
  return seq
 
# print(selectionSort(list(randList)))


# def mergeSort(seq):
#   temp = []
#   for i in range(len(seq)):
#     for j in range(0, len(seq)-4):
#       pass
    
#     for k in range(5, len(seq)):
#       pass

