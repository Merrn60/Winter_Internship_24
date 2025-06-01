class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        seen={}
        MOD=10**9+7 #prevent overflow
        count=0
        li_2=[2**i for i in range(22)] #list power of2
        for i in deliciousness: #i=1
            for target in li_2:#1
                complement=target-i #c=0
                if complement in seen:
                    count+=seen[complement]
                    count%=MOD
            seen[i]=seen.get(i,0)+1 #{0,1} and so on
        return count


