class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        mysum = sum(cardPoints[-k:])
        maxSum = mysum
        for i in range(k):
            mysum = mysum + cardPoints[i] - cardPoints[-k+i]
            maxSum = max(maxSum, mysum)
        return maxSum
