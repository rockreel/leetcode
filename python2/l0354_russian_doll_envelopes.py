# O(nlogn) solution, based on longest increasing sequence.
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        import bisect
        # Find the longest increasing sequence in height list. Note that
        # inverese sort height for same width is to avoid same width envelope
        # russian doll each other.
        heights = [h for w, h in sorted(envelopes, key=lambda x: (x[0], -x[1]))]
        
        seq = []
        for h in heights:
            idx = bisect.bisect_left(seq, h)
            if idx == len(seq):
                if not seq or seq[-1] < h:
                    seq.append(h)
            else:
                seq[idx] = h
        return len(seq)

# O(n^2) solution.
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        import bisect
        envelopes = sorted(envelopes)
        dp = [1] * len(envelopes)
        for i in range(1, len(dp)):
            env = (envelopes[i][0]-1, envelopes[i][1]-1)
            idx = bisect.bisect_right(envelopes, env)
            for j in range(0, idx):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0

