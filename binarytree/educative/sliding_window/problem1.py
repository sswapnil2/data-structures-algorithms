# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

# Naive solution using two for loop one from 0 to k-1 and inner for loop from sliding i, i + k
# complexity O(N*K) N elements in array and k is size of subarray


def solution(arr, k):

    windowSum = 0.0
    windowStart = 0
    result = []
    for index, ele in enumerate(arr):
        windowSum += ele

        if index >= k -1:
            result.append((windowSum/k))
            windowSum -= arr[windowStart]
            windowStart +=1
        
    return result


arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5

print("Solution:", solution(arr, k  ))
