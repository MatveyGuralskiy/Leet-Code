#--------------LEET CODE---------------
#506. Relative Ranks

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy
"""
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

 

Example 1:

Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
Example 2:

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].
"""
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedScore = sorted(score, reverse = True)
        lengthSortedScore = len(sortedScore)
        winners = {}
        for i in range(lengthSortedScore):
            if i == 0:
                winners[sortedScore[i]] = "Gold Medal"
            elif i == 1:
                winners[sortedScore[i]]= "Silver Medal"
            elif i == 2:
                winners[sortedScore[i]]= "Bronze Medal"
            else:
                winners[sortedScore[i]] = str(i + 1)
        result = []
        for i in score:
            result.append(winners[i])
        return result   