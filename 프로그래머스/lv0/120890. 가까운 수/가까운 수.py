def solution(array, n):
    answer = 0
    array += [-1,n,1000]
    array.sort()
    index = array.index(n)
    if array[index+1] - array[index] < array[index] - array[index-1]:
        return array[index+1]
    else:
        return array[index-1]