class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if (len(nums1) + len(nums2)) % 2 == 1:
            return sorted(nums1 + nums2)[(len(nums1) + len(nums2)) // 2]
        
        return sum(sorted(nums1 + nums2)[(len(nums1) + len(nums2)) // 2 - 1:(len(nums1) + len(nums2)) // 2 + 1]) / 2
    
print(Solution().findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))