# Counting Inversions in O(nlogn) Time

class Solution(object):
    def Merge_and_count(self, left, right):
        i = 0
        j = 0
        split_inv = 0
        sorted = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted.append(left[i])
                i = i + 1
            else:
                sorted.append(right[j])
                j = j + 1
                split_inv = split_inv + len(left) - i # means all remaining items in left > the item in right

        while i < len(left): 
            sorted.append(left[i]) 
            i+=1
          
        while j < len(right): 
            sorted.append(right[j]) 
            j+=1
    
        return sorted, split_inv

    def Sort_and_count(self, arr):
        if len(arr) == 0 or len(arr) == 1:
            return arr, 0
        else:
            half = len(arr)//2
            left = arr[:half]
            right = arr[half:]
            # print(left, right)
            sorted_left, left_inv = self.Sort_and_count(left)
            sorted_right, right_inv = self.Sort_and_count(right)
            sorted, split_inv = self.Merge_and_count(sorted_left, sorted_right)
            # print(sorted)
            return sorted, left_inv + right_inv + split_inv


if __name__ == "__main__":

    arr = []
    with open('IntegerArray.txt', 'r') as f:
        for str in f:
            arr.append(int(str.rstrip()))
    print(arr[:10])
    #arr = [1,3,2,4,6,5]
    #arr = [6,5,4,3,2,1]
    _, inv = Solution().Sort_and_count(arr)
    print(inv)