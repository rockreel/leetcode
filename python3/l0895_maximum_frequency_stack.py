class FreqStack:

    def __init__(self):
        self._freq_map = dict()
        self._freq_stack = dict()
        self._max_freq = 0        

    def push(self, x: int) -> None:
        freq = self._freq_map.get(x, 0)
        freq += 1
        self._freq_map[x] = freq
        self._max_freq = max(freq, self._max_freq)
        if freq in self._freq_stack:
            self._freq_stack[freq].append(x)
        else:
            self._freq_stack[freq] = [x]

    def pop(self) -> int:
        x = self._freq_stack[self._max_freq].pop()
        self._freq_map[x] -= 1
        if not self._freq_stack[self._max_freq]:
            self._freq_stack.pop(self._max_freq)
            self._max_freq -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
