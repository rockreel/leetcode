class ValidWordAbbr:
    """
    @param: dictionary: a list of words
    """
    def __init__(self, dictionary):
        # do intialization if necessary
        self._abbr_set = set([self._abbr(w) for w in dictionary])

    """
    @param: word: a string
    @return: true if its abbreviation is unique or false
    """
    def isUnique(self, word):
        # write your code here
        return self._abbr(word) not in self._abbr_set

    def _abbr(self, word):
        if len(word) < 3:
            return word
        return word[0] + str(len(word) - 2) + word[-1]

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param = obj.isUnique(word)