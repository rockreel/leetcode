class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        def is_valid_serial(serial_iter):
            node = next(serial_iter, None)
            if node is None:
                return False
            if node != '#':
                return is_valid_serial(serial_iter) and is_valid_serial(serial_iter)
            return True
        
        serial_iter = iter(preorder.split(','))
        # Serialization should construct a tree and no more data left.
        return is_valid_serial(serial_iter) and next(serial_iter, None) is None

