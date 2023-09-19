class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Create a hash table, for each value check if it is contained in the hash table, if not, add it to the table, if yes, return it
        hashTable = {}
        for num in nums:
            if num in hashTable.keys():
                return num
            else:
                hashTable[num] = None
