from collections import deque


def nextGreaterElement(nums1, nums2):
    dic = {}
    for i in range(len(nums2)):
        dic[nums2[i]] = i
    ans = []
    for i in range(len(nums1)):
        index = dic[nums1[i]]
        anss = -1
        for j in range(index+1, len(nums2)):
            if nums2[j] > nums2[index]:
                anss = nums2[j]
                break
        ans.append(anss)
    return ans

print(nextGreaterElement([2,4],[1,2,3,4]))