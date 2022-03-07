# Write a code that prints out the first occurrence of a duplicate in a given array of integers
# Sample Input: [1,2,3,2,1]
# Output: 2

# Code>>>

def find_duplicate_occurrence(arr):
    d={}
    for num in arr:
        if num in d.keys():
            print(num)
            break
        else:
            d[num]=0

num=find_duplicate_occurrence([1,2,3,2,1])

