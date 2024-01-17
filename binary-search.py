


def binary_search (list,item):
    low =0
    high = len(list) -1   
    while low <= high:
        mid =(high+low)//2

        if(list[mid]==item ): 
            return mid
        if(list[mid]>item) : 
           high= mid-1 
           continue
        else : 
            low=mid+1 
            continue
    return None


def binary_search_recursive(arr,low,high,item): 
        mid=(high+low)//2 

        if(item ==arr[mid]):
            return mid 
        
        if(arr[mid]>item): 
             high= mid-1 
             return binary_search_recursive(arr,low,high,item)
        else:
             low =mid+1  
             return binary_search_recursive(arr,low,high,item)           
        

arr=[1,2,3,4,5,6,7,8] 
print (binary_search(list,4))
print ( binary_search_recursive(arr,0,len(arr),12))



    
    

    