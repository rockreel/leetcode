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

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        # Write your code here
        bytes_read = 0
        buffer = ['', '', '', '']
        bytes_to_copy = 4
        while bytes_to_copy != 0:
            bytes_read_4 = Reader.read4(buffer)
            bytes_to_copy = min(bytes_read_4, n - bytes_read)
            buf[bytes_read:bytes_read+bytes_to_copy] = buffer[:bytes_to_copy]
            bytes_read += bytes_to_copy
                
        return bytes_read
