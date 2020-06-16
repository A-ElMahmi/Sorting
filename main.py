import random

randList = [random.randint(1, 10) for i in range(10)]
print(randList)


def bubbleSort(seq):
  while True:
    for i in range(len(seq)-1):
      if seq[i] > seq[i+1]:
        seq[i], seq[i+1] = seq[i+1], seq[i]
        continue
    break
  return seq


def insertionSort(seq):
  for i in range(1, len(seq)):
    while seq[i] < seq[i-1] and i > 0:
      seq.insert(i-1, seq[i])
      seq.pop(i+1)
      i -= 1 
  return seq


print(bubbleSort(randList.copy()))
print(insertionSort(randList.copy()))