class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Append an unpopable infinity to the end of both arrays
        nums1.append(float('inf')); nums2.append(float('inf'))
        i = 0; j = 0

        # Calculate the half point of both arrays
        half = (len(nums1) + len(nums2) - 2) // 2

        if (len(nums1) + len(nums2) - 2) % 2 == 0:
            half -= 1

        # Find the values at the half point
        for x in range(half):
            if nums1[i] <= nums2[j]:
                i += 1
            else: 
                j += 1

        # If the length is odd, return value at half point
        if (len(nums1) + len(nums2)) % 2 == 1:
            if nums1[i] <= nums2[j]:
                return nums1[i]
            else: 
                return nums2[j]
        # If the lenght is even, return the average of walues around half point
        values = []
        for x in range(2):
            if nums1[i] <= nums2[j]:
                values.append(nums1[i])
                i += 1
            else: 
                values.append(nums2[j])
                j += 1

        return (values[0] + values[1]) / 2.0


print(Solution().findMedianSortedArrays([2, 4], [1,3]))