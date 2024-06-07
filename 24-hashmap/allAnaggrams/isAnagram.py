class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # If len of smaller string is smaller than s, immediatley return False
        if len(p)>len(s):
            return []
        hmp = {}
        hms = {}
        ans = []
        count = 0
        # Create a hashmap of characters in p
        for i in range(len(p)):
            hmp[p[i]] = hmp.get(p[i], 0)+1
        # Lets Create our first window
        for i in range(len(p)):
            hms[s[i]] = hms.get(s[i],0)+1
            if hms[s[i]]<= hmp.get(s[i],0):
                count+=1
            if count==len(p):
                ans.append(0)
        # Now, lets start with sliding part.
        sp = 0
        ep = len(p)
        while(ep<len(s)):
            # Acuisition, add the end point.
            hms[s[ep]] = hms.get(s[ep],0)+1
            if hms[s[ep]]<=hmp.get(s[ep],0):
                count+=1
            # Remove the starting point
            hms[s[sp]] = hms[s[sp]]-1
            # Checking if removed character was useful
            if hms[s[sp]]<hmp.get(s[sp],0):
                count-=1
            sp+=1
            ep+=1

            if count==len(p):
                ans.append(sp)
        return ans