# Write a code that checks if two given strings are anagrams
# Sample Input: Mary Army
# Output: Yes

# code>>>

def isAnagram(s1,s2):
    s1=s1.lower()        #changing M, A into lowercase 
    s2=s2.lower()
    if (len(s1)!=len(s2)):
        print('No')
        return 'No'
    if (len(s1)==len(s2)):
        dict1={letter: 1 for letter in s1}      #if letter present in s1, mark it's value as 1. Note: it is not counting occurance of a letter.
        dict2={letter: 1 for letter in s2}        
    if (dict1==dict2):
        print('Yes')
        return 'Yes'
    else:
        print('No')
        return 'No'

given_string=isAnagram('Mary', 'Army')  

