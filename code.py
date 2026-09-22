class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        d={}
        for wo in words[0]:
            if wo not in d:
                d[wo]=1
            else:
                d[wo]+=1
        for word in words[1:]:
            d1={}
            for wo in word:
                if wo not in d1:
                    d1[wo]=1
                else:
                    d1[wo]+=1
            
            for wr in d:
                if wr not in d1:
                    d1[wr]=0
                d[wr]=min(d[wr],d1[wr])
        print(d)
        ans=[]
        for k,v in d.items():
            
            ans.extend(k*v)
        return ans
        
