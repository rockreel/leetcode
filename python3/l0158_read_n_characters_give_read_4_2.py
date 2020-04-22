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
        # Internal buffer to read: self._buffer[self._start:self._end]
        self._start = 0
        self._end = 0 

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        # Write your code here
        bytes_read = 0
        if self._start != -1:
            bytes_read_4 = self._end - self._start
            if n < bytes_read_4:
                # All bytes can be read from buffer.
                buf[:n] = self._buffer[self._start:self._start+n]
                self._start += n
                return n
            else:
                buf[:bytes_read_4] = self._buffer[self._start:self._end]
                bytes_read += bytes_read_4
                self._start = -1
                self._end = -1
                if n == bytes_read_4:
                    return n

        while True:
            bytes_read_4 = Reader.read4(self._buffer)
            if bytes_read + bytes_read_4 >= n:
                # All n bytes are read.
                bytes_to_copy = n - bytes_read
                buf[bytes_read:n] = self._buffer[:bytes_to_copy]
                if bytes_to_copy < 4:
                    self._start = bytes_to_copy
                    self._end = bytes_read_4
                return n
            else:
                if bytes_read_4 < 4:
                    # Not enough byte read from input.
                    buf[bytes_read:bytes_read+bytes_read_4] = self._buffer[:bytes_read_4]
                    self._start = -1
                    self._end = -1
                    return bytes_read + bytes_read_4
                else:
                    buf[bytes_read:bytes_read+bytes_read_4] = self._buffer[:bytes_read_4]
                    bytes_read += bytes_read_4
