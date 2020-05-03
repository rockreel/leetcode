from collections import defaultdict

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        letter_after_graph = defaultdict(list)  # Letter to letters after it.
        letter_before_count = defaultdict(int)  # Count of letters before than it.
        for i in range(len(words)): 
            for k in range(len(words[i])):
                if words[i][k] not in letter_before_count:
                    letter_before_count[words[i][k]] = 0
            if i == len(words) - 1:
                continue
            j = 0
            while (
                j < len(words[i]) and
                j < len(words[i+1]) and
                words[i][j] == words[i+1][j]):
                    j += 1
            if j < len(words[i]) and j < len(words[i+1]):
                letter_after_graph[words[i][j]] = words[i+1][j]
                letter_before_count[words[i+1][j]] += 1
        # Construct letter order based on letter graph.
        orders = []
        # Stores (letter, letter before)
        queue = [(l, None) for l, c in letter_before_count.items() if c == 0]
        while queue:
            l, l_before = queue.pop(0)
            # Insert into orders also need to consider human alphabetical order.:
            if l_before:
                idx = orders.index(l_before) + 1
            else:
                idx = 0
            while idx < len(orders) and orders[idx] < l:
                idx += 1
            orders.insert(idx, l)
            # Find next set of letters to visit.
            for l_after in letter_after_graph[l]:
                letter_before_count[l_after] -= 1
                if letter_before_count[l_after] == 0 and l_after not in orders:
                    queue.append((l_after, l))

        if sum(letter_before_count.values()) == 0: 
            return ''.join(orders)
        else:
            return ''