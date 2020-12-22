# Given an array containing None values fill in the None values with most recent 
# non None value in the array 


array = [1,2,None,4,5,None,None,3,None]

def solution(num):
    valid=0
    out=[]
    for i in num:
        if i is not None:
            out.append(i)
            valid=i
        else:
            out.append(valid)
    return out

print(solution(array))


#output
#[1,2,2,4,5,5,5,3,3]