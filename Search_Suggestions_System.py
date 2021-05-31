class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        answer = []
        for numLtrs in range(1, len(searchWord)+1):
            matchingProds = []
            searchTerm = searchWord[0:numLtrs]
            i = 0
            while i < len(products) and len(matchingProds) < 3:
                if len(searchTerm) > len(products[i]):
                    i += 1
                    continue
                ltr_i = 0
                while ltr_i < numLtrs and products[i][ltr_i]==searchTerm[ltr_i]:
                    ltr_i += 1
                if ltr_i==numLtrs:
                    matchingProds.append(products[i])
                i += 1
            answer.append(matchingProds)
        return answer
            
