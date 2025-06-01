class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result=[]
        seen={}
        for i in range(len(s)-10+1):
            sub=s[i:i+10]

            seen[sub] = seen.get(sub, 0) + 1
            if seen[sub] ==2:
                result.append(sub)




        return result
