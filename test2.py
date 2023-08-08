class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        half = (m + n + 1) // 2
        left = 0
        right = m
        while left <= right:
            i = (left + right) // 2
            j = half - i
            if i < m and nums2[j - 1] > nums1[i]:
                left = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                right = i - 1
            else:
                if i == 0:
                    max_left = nums2[j-1]
                elif j == 0:
                    max_left = nums1[i-1]
                else:
                    max_left = max(nums1[i-1],nums2[j-1])
                if (m + n) % 2 == 1:
                    return max_left

                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[0]
                else:
                    min_right = min(nums1[i], nums2[j])
                return (max_left + min_right) / 2



# nums1 = [1,3,5,   7,9], nums2 = [2,4,   6,8,10]
#   12345   67899
#   67899 12345
#   i






