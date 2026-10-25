class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array for optimization
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            # Partition nums1
            cut1 = (low + high) // 2
            # Partition nums2 to ensure left half has (m+n+1)//2 elements
            cut2 = (m + n + 1) // 2 - cut1
            
            # Handle edge cases for partition boundaries
            left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            right1 = float('inf') if cut1 == m else nums1[cut1]
            right2 = float('inf') if cut2 == n else nums2[cut2]
            
            # Check if we found the correct partition
            if left1 <= right2 and left2 <= right1:
                # If total length is odd
                if (m + n) % 2 == 1:
                    return max(left1, left2)
                # If total length is even
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
            
            # Adjust partition: too many elements from nums1
            elif left1 > right2:
                high = cut1 - 1
            # Too few elements from nums1
            else:
                low = cut1 + 1
        
        return -1  # Should never reach here with valid input
