class Solution:
    def merge (self, list1, list2):
        i,j = 0,0
        list3 = []
        while (i<len(list1) and j<len(list2)):
            if(list1[i]<list2[j]):
                list3.append(list1[i])
                i+=1
            else:
                list3.append(list2[j])
                j+=1
        if (i==len(list1)):
            for x in range (j,len(list2)):
                list3.append(list2[x])
        else:
            for x in range(i,len(list1)):
                list3.append(list1[x])
        return list3

    def sortArray(self, nums: List[int]) -> List[int]:
        if (len(nums)<2):
            return nums
        else :
            list3 = self.merge(self.sortArray(nums[0:(len(nums))//2]),self.sortArray(nums[len(nums)//2:len(nums)]))
        return list3       