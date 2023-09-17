class Solution:
    def candy(self, ratings: List[int]) -> int:
            # Loop through children twice, once from each side
            #         #
            #   #   # #
            # # # # # # #
            # 1 2 1 2 3 1
            # On each pass calculate the candy checking only next child in line
            # Then select the max of the two values and add it to the total

            totalCandy = 0
            i = 0
            candy = [0] * len(ratings)

            # First loop from 0 to n
            prevRating = 0
            while i < len(ratings):
                # Skip if previous child doesn't exist
                if (i - 1) == len(ratings) or (i - 1) < 0:
                    candy[i] = 1
                    prevRating = 1
                    i += 1
                    continue

                if ratings[i] > ratings[i - 1]:
                    candy[i] = prevRating + 1
                    prevRating = candy[i]
                else:
                    candy[i] = 1
                    prevRating = 1

                i += 1

            # Second loop from n to 0
            candy2 = [0] * len(ratings)
            i = len(ratings) - 1
            prevRating = 1
            while i >= 0:
                # Skip if previous child doesn't exist
                if (i + 1) == len(ratings) or (i + 1) < 0:
                    candy2[i] = 1
                    prevRating = 1
                    i -= 1
                    continue

                if ratings[i] > ratings[i + 1]:
                    candy2[i] = prevRating + 1
                    prevRating = candy2[i]
                else:
                    candy2[i] = 1
                    prevRating = 1
                i -= 1

            for i in range(len(candy)):
                totalCandy += max(candy[i], candy2[i])

            return totalCandy