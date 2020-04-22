class Reader:

    pos = 0
    input = ''

    @classmethod
    def read4(cls, buf):
        bytes_read = min(len(cls.input) - cls.pos, 4)
        buf[:bytes_read] = cls.input[cls.pos:cls.pos+bytes_read]
        cls.pos += bytes_read
        return bytes_read


class Solution:

    def __init__(self):
        # For read function.
        self._buffer = ['', '', '', '']  # 4 char buffer.
        # Internal buffer to read from self._buffer[self._start:self._end]
        self._start = 0
        self._end = 0 

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        # Write your code here
        bytes_read = 0
        while bytes_read < n:
            if self._start == self._end:
                self._end = Reader.read4(self._buffer)
                self._start = 0
                if self._end == 0:
                    # Can not read from read4, exit
                    break
            bytes_to_copy = min(self._end - self._start, n - bytes_read)
            buf[bytes_read:bytes_read+bytes_to_copy] = self._buffer[self._start:self._start+bytes_to_copy]
            self._start += bytes_to_copy
            bytes_read += bytes_to_copy
                
        return bytes_read
