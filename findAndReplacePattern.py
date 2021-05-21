class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        n = len(pattern)
        matching = []
        for word in words:
            w = []
            p = []
            ii = 0
            while ii < n:
                if pattern[ii] in p:
                    i = p.index(pattern[ii])
                    if w[i] != word[ii]:
                        break
                elif word[ii] in w:
                    i = w.index(word[ii])
                    if p[i] != pattern[ii]:
                        break
                else:
                    w.append(word[ii])
                    p.append(pattern[ii])
                    #print(w, p)
                ii += 1
            if ii==n:
                matching.append(word)
        return matching
