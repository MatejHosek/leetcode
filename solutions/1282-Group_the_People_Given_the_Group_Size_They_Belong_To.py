class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # Generate a placeholder list of groups of (size, [array of people])
        # Append to arrays of correct size for all people in groupSizes
        # If group is filled after append, transfer it to array finalGroups for return
        # Return finalGroups

        # Placeholder array for groups
        placeholderGroups = []

        # Array for finalised groups
        finalGroups = []

        # Loop through all people
        for i in range(len(groupSizes)):
            # Find group of correct size
            found = False
            for j in range(len(placeholderGroups)):
                if placeholderGroups[j][0] == groupSizes[i]:
                    placeholderGroups[j][1].append(i)
                    found = True

                    # Check werther the group was filled up
                    if len(placeholderGroups[j][1]) == placeholderGroups[j][0]:
                        finalGroups.append(placeholderGroups.pop(j)[1])
                    break

            if not found:
                placeholderGroups.append((groupSizes[i], [i]))

                # Check werther the group was filled up
                j = len(placeholderGroups) - 1
                if len(placeholderGroups[j][1]) == placeholderGroups[j][0]:
                    finalGroups.append(placeholderGroups.pop(j)[1])

        return finalGroups
