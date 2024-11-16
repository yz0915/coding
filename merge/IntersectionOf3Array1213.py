# 1213. Intersection(common elements) of Three Sorted Arrays
# https://leetcode.com/problems/intersection-of-three-sorted-arrays/

def arraysIntersection(self, arr1, arr2, arr3):
    res = []
    i, j, k = 0, 0, 0
    
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            res.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j] or arr1[i] < arr3[k]:
            i += 1
        elif arr2[j] < arr1[i] or arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
    
    return res