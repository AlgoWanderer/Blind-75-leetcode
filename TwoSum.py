#This is the brute force method. Go traverse through the array and if two numbers add up to the target, return the index of the respective numbers

class SolutionBruteForce(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i , j]
#The problem with this method is that its time complexity in worst case will be O(n²) which is not efficient so we use the Hash Map method. 
#The Space Complexity is O(1) since it is only i and j for 1000 or 10k numbers

class SolutionHashMap(object):
    def twoSum(self, nums, target):
        hm = {} #Create a Hash Map
        for i in range(len(nums)): #Traverse through the array
            y = target - nums[i] #y is the complement here i.e the number we need to find.
            if y in hm: #if y is already in the hash map then:
                return [hm[y], i] #return the index of the two numbers that can be added to obtain the target. Earlier index first and then the index of the current element
            hm[nums[i]] = i #if y is not in the hash map, then add the current number into the hash map

#in this hashmap method, the time complexity will be O(n) but since we are creating space, the space complexity will be O(n) since in the worst case it can hold all the numbers in the array
