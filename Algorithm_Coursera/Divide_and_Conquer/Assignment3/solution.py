
import random

class Solution(object):

    def __init__(self, pivot):
        self.pivot = pivot # left, right, random
        self.count = 0

    def ChoosePivot(self, arr, left, right):
        
        if (right - left) == 1:
            return right
         
        middle = left + (right-left)//2

        r = 0
        l = 0
        m = 0
        if arr[right] < arr[left]:
            l = l + 1
        else:
            r = r + 1
        if arr[middle] < arr[left]:
            l = l + 1
        else:
            m = m + 1
        if arr[middle] < arr[right]:
            r = r + 1
        else:
            m = m + 1
        
        if r == 1:
            return right
        elif l == 1:
            return left
        elif m == 1:
            return middle



    def Partition(self, arr, left, right):

        i = left + 1
        
        for j in range(left + 1, right + 1):
            if arr[j] < arr[left] :
                arr[j], arr[i] = arr[i], arr[j]
                i = i + 1
        
        arr[left], arr[i-1] = arr[i-1], arr[left]

        return i - 1

    def QuickSort(self, arr, left, right):
    
        if left >= right:
            return 0

        self.count = self.count + right - left
        
        if self.pivot == "random":
            pivot = random.randint(left, right)
        elif self.pivot == "left":
            pivot = left
        elif self.pivot == "right":
            pivot = right
        elif self.pivot == "median":
            pivot = self.ChoosePivot(arr, left, right)

        arr[pivot], arr[left] = arr[left], arr[pivot] 
            # move pivot to the left since Partition function expects to do so

        divide = self.Partition(arr, left, right)

        self.QuickSort(arr, left, divide-1)

        self.QuickSort(arr, divide+1, right)


if __name__ == "__main__":

    arr = []
    with open('QuickSort.txt', 'r') as f:
        for str in f:
            arr.append(int(str.rstrip()))
    print(arr[:10])
    # arr = [1,2,3,4,5,6]
    # arr = [6,5,4,3,2,1]
    s = Solution("median") # left, right, random, median
    s.QuickSort(arr, 0, len(arr)-1)
    print(arr[:10])
    print(arr[-10:])
    print(s.count) # right: 164123 # left 162085 # random 155076 # median 138382

