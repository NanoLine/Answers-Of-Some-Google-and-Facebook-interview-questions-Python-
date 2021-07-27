def deleteOdd(a):
    output = ""
    for i in a:
        if i not in output:
            output += i
    return output
def recurredChar(a):
    output = ""
    for i in a:
        if i in output:
            return i
        output += i
def sumOfTwo(a, b, v):
    for i in a:
        for j in b:
            if i + j == v:
                return True
    return False
def findLongestSubarrayBySum(arr, s):
    r = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if sum(arr[i:j]) == s and len(arr[i:j]) > len(r):
                r = [i, j]
    return r
def arrayMaxConsecutiveSum2(inputArray):
    maxSum = 0
    maxSumOfSubarray = []
    for i in range(len(inputArray)):
        for j in range(len(inputArray)):
            if sum(inputArray[i:j]) > maxSum:
                maxSumOfSubarray = inputArray[i:j]
    return inputArray[i:j]

def selectionSort(l):
    for i in range(len(l)-1): 
        minimum = i
        for j in range(i, len(l)):
            if l[j] < l[minimum]:
                minimum = j
        if minimum != i:
            temp = l[i]
            l[i] = l[minimum]
            l[minimum] = temp

    return l

def sortedSquaredArray(arr):
    arr = [i**2 for i in arr]
    arr = selectionSort(arr)
    return arr
def firstDuplicate(arr):
    it_was = []
    for i in arr:
        if i in it_was:
            return i
        it_was.append(i)
    return -1
