def sum(arr):
    
    if(len(arr)==0):
        return 0 
    else :
        return arr.pop() + sum(arr)

def count(arr):
        if(len(arr)==0):
            return 0
        else: 
            arr.pop()
            return 1+ count(arr)
        
def max(m,arr): 
        if(len(arr)==0):
            return m 
        current=arr.pop()
        if(current > m ):
             return max(current,arr)
        else:
            return max(m,arr)     


    
# print(sum([1,2,3,4,5]))
# print(count([1,2,3,4,5]))
arr= [1,7,9,10,12]
# print(max(arr.pop(),arr))
