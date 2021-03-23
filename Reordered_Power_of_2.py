class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        N_str = str(N)
        n = len(N_str)
        pow2 = 1
        pow_str = str(pow2)
        while len(pow_str) <= n:
            if len(pow_str)==n:
                N_s = list(N_str)
                for powchar in pow_str:
                    try:
                        N_s.remove(powchar)
                    except:
                        break
                if len(N_s)==0:
                    return True
            pow2 *= 2
            pow_str = str(pow2)
        return False
