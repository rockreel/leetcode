class Solution:
    """
    @param word: the given word
    @return: the generalized abbreviations of a word
    """
    def generateAbbreviations(self, word):
        # Write your code here
        queue = [(word, 0)]
        visited = set([word])
        result = []
        while queue:
            w, start = queue.pop(0)
            result.append(w)
            for k in range(1, len(w)+1):
                for i in range(start, len(w)-k+1):
                    # Replace w[i:i+k] with k.
                    num = str(k)
                    new_w = w[:i] + num + w[i+k:]
                    if new_w not in visited:
                        queue.append((new_w, i + len(num) + 1))
                        visited.add(new_w)
        return result     
