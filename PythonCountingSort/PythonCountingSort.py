import sys
import random

def counting_sort(array1, max_val):
    m = max_val + 1
    count = [0] * m
    
    for a in array1:
        count[a] = count[a] + 1

    i = 0
    for a in range(m):
        for c in range(count[a]):
            array1[i] = a
            i = i + 1

    return array1


def bogosort(nums):
    def isSorted(nums):
        if(len(nums) < 2):
            return True
        for i in range(len(nums) - 1):
            if(nums[i] > nums[i + 1]):
                return False
        return True
    while(not isSorted(nums)):
        random.shuffle(nums)
    return nums

num1 = input('Comma Separated Entries... \n').strip()
nums = [int(i) for i in num1.split(',')]

print(bogosort(nums))
print(counting_sort([1,2,3,7,7,7,4,3,2,1],7))



