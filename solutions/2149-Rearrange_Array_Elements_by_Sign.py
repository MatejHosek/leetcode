class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positives, negatives = [], []

        for num in nums:
            if num >= 0:
                positives.append(num)
                continue
            negatives.append(num)

        toReturn = []
        for i in range(len(positives)):
            toReturn.append(positives[i])
            toReturn.append(negatives[i])

        return toReturn
