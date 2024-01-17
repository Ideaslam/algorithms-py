

def  findSmallest(arr):
    smallest=arr[0]
    index=0
    for  i in  range(1,len(arr)):
        if(arr[i]<smallest):
            smallest=arr[i]
            index=i

    return index



def selectionSort(arr):
    newArr=[] 
    for  i in  range(0,len(arr)):
       index= findSmallest(arr)
       newArr.append(arr.pop(index))
    return  newArr

# def selectionSortRecursive(index,arr):
#     if(index == len(arr)-1):
#         return arr
#     else:
#         if arr[index] > arr[index+1]:
#             temp= arr[index+1]
#             arr[index+1] =arr[index]
#             arr[index] =temp 
#         index+=1
#         return selectionSortRecursive(index,arr)





# print(selectionSort([3,4,2,6,1,5,8,0]))
# print(selectionSortRecursive(0,[3,4,2,6,1,5,8,0]))