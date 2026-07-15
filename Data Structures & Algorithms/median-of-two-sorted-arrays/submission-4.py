class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tl = len(nums1) + len(nums2)
        m = tl//2 + 1
        p1, p2 = 0, 0
        n1, n2 = 0, 0
        while m>0:
            if  p2 >= len(nums2):
                n1 = n2
                n2 = nums1[p1]
                p1+=1
            elif p1 >= len(nums1):
                n1 = n2
                n2 = nums2[p2]
                p2+=1
            else:
                if nums1[p1] <= nums2[p2]:
                    n1 = n2
                    n2 = nums1[p1]
                    p1+=1
                else:
                    n1 = n2
                    n2 = nums2[p2]
                    p2+=1
            m-=1
        if tl % 2 == 0:
            return (n1+n2)/2
        else:
            return n2