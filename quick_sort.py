array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start,end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end
    while left <= right:
        while left <= end and array[pivot] >= array[left]:
            left +=1
        while right > start and array[pivot] <=array[right]:
            right -=1
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

def quick_sort_short(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    print(pivot)
    left = [i for i in array[1:] if i <= pivot]
    right = [i for i in array[1:] if i > pivot]

    return quick_sort_short(left) + [pivot] + quick_sort_short(right)


array = quick_sort_short(array)

print(array)
             
        