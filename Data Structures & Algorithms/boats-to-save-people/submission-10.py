class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        left = 0 
        right = len(people)-1
        sum = 0
        count = 0
        pcount = 1
        while (left <= right):
            while sum + people[right] <= limit and pcount < 3:
                sum += people[right]
                right -= 1
                pcount += 1
            while sum + people[left] <= limit and pcount < 3:
                sum += people[left]
                left += 1
                pcount += 1
            count+=1
            sum = 0
            pcount = 1
        return count

        