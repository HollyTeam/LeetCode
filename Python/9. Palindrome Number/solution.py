class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # return str(x) == str(x)[::-1]
        if (x < 0) or ((x % 10 == 0) and (x is not 0)):
            return False

        reverse_number = 0
        while x > reverse_number:
            reverse_number = reverse_number * 10 + x % 10
            x = x // 10

        return (x == reverse_number) or (x == reverse_number // 10)
