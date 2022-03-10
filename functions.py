import os, sys
def convertArray(arrToAppend, arr):
  for element in arr:
    arrToAppend.append(int(element))

def readFile(filepath):
  tempArr = []
  f = open(os.path.join(sys.path[0], filepath), 'r')
  for line in f:
    tempArr.append(line.split())
  f.close()
  return tempArr

def setUpArrays(fisier, lineOne, lineTwo):
  array = readFile(fisier)
  if len(array) == 0:
    return []
  convertArray(lineOne, array[0])
  convertArray(lineTwo, array[1])
  return array
