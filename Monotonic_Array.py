# Given an array of integers, determine whether the array is monotonic or not.
# An array is monotonic if and only if it is monotone increasing, or monotone decreasing.

A = [6, 5, 4, 4] 
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]

def solution(s):
    return (all(s[i] <= s[i+1] for i in range(len(s)-1)) or 
            all(s[i] >= s[i+1] for i in range(len(s)-1)))


# The algorithm above takes advantage of the all() function that returns True 
# If all items in an iterable are true, otherwise it returns False. 
# If the iterable object is empty, the all() function also returns True.


print(solution(A))
print(solution(B))
print(solution(C))

#True
#False
#True