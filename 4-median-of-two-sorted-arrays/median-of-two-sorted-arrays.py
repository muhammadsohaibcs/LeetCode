class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        merged = []
        j= k = 0
        for i in range(length//2+1):
            if j == len(nums1):
               merged.append(nums2[k])
               k+=1
               continue
            elif k ==len(nums2):
                merged.append(nums1[j])
                j += 1
                continue
             
            elif nums1[j] >nums2[k]:
                merged.append(nums2[k])
                k += 1
            else:
                merged.append(nums1[j])
                j += 1
        if length % 2 ==0:
            return (merged[-1] + merged[-2])/2
        else:
            return merged[-1]