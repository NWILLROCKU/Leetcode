class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        def returnCorrect(query):
            if query in wordlist:
                return wordlist[wordlist.index(query)]
            
            query_lower = query.lower()
            if query_lower in wordlist_lower:
                i = wordlist_lower.index(query_lower)
                return wordlist[i]
        def convertVowel(word):
            word2 = ''
            for j in range(len(word)):
                letter = word[j].lower()
                if letter in vowelList:
                    word2 += 'a'
                else:
                    word2 += letter
            return word2
            
            
        vowelList = ['a','e','i','o','u']
        wordlist2 = []
        for word in wordlist:
            word2 = ''
            for j in range(len(word)):
                letter = word[j].lower()
                if letter in vowelList:
                    word2 += 'a'
                else:
                    word2 += letter
            wordlist2.append(word2)
            
        #spellchecked = ['']*len(queries)
        spellchecked = []
        for query in queries:
            if query in wordlist:
                spellchecked.append(query)
            else:
                query_converted = convertVowel(query)
                if query_converted in wordlist2:
                    spellchecked.append(wordlist[ wordlist2.index(query_converted) ])
                else:
                    spellchecked.append('')
        return spellchecked
                    
