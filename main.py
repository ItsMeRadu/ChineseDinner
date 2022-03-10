from functions import convertArray, readFile, setUpArrays
def main():
  fisier = './input.txt'
  firstLine = []
  sticksArray = []

  arr = setUpArrays(fisier, firstLine, sticksArray)

  if len(arr) == 0:
    print('The file does not contain information')
    return

  peopleNumber = firstLine[0]
  sticksNumber = firstLine[1]

  sticksArray.sort()
  print("Sorted array: ", sticksArray)

  longSticksArray = []
  for i in range(peopleNumber):
    longSticksArray.append(sticksArray[len(sticksArray) - 1 - i])

  print("Long sticks: ", longSticksArray)

  shortSticksArray = []
  for i in range(len(sticksArray) - peopleNumber):
    shortSticksArray.append(sticksArray[i])

  print("Short sticks: ", shortSticksArray)

  UNAVAILABLE_NUMBER = shortSticksArray[len(shortSticksArray)-1] + 1

  shortSticksLength = len(shortSticksArray) - 1
  costArr = []
  for i in range(shortSticksLength):
    cost = shortSticksArray[i+1] - shortSticksArray[i]
    costArr.append(cost)
    
  print("Cost array: ", costArr)

  pairsNumber = 0
  totalCost = 0
  shortSticksArrayLength = len(shortSticksArray) - 1
  costArrayLength = shortSticksArrayLength - 1

  for number in costArr:
    if pairsNumber == peopleNumber:
      break

    if costArr[0] == min(costArr) and min(costArr) != UNAVAILABLE_NUMBER:
      totalCost += costArr[0]
      costArr[0] = UNAVAILABLE_NUMBER
      costArr[1] = UNAVAILABLE_NUMBER
      pairsNumber = pairsNumber + 1

    if costArr[costArrayLength] == min(costArr) and min(costArr) != UNAVAILABLE_NUMBER:
      totalCost += costArr[costArrayLength]
      costArr[costArrayLength] = UNAVAILABLE_NUMBER
      costArr[costArrayLength - 1] = UNAVAILABLE_NUMBER
      pairsNumber = pairsNumber + 1

    if number == min(costArr) and min(costArr) != UNAVAILABLE_NUMBER:
      totalCost += number
      costArr[costArr.index(number) - 1] = UNAVAILABLE_NUMBER
      costArr[costArr.index(number) + 1] = UNAVAILABLE_NUMBER
      costArr[costArr.index(number)] = UNAVAILABLE_NUMBER
      pairsNumber = pairsNumber + 1

  print("\nTotal cost is: ", totalCost)

main()