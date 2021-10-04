print( '3' > '0')


print(ord('3'))

print(ord('0'))

print(int('3'))

# A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

# Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.


class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        
#         since the provided digit can only be a sum of 1s, the digit with the most 1s is the greatest number

#         greatest_digit = max([char for char in n])
    
#         return int(greatest_digit)
    
        temp = '0'
        for digit in n:
#             "3" "2"
            if (digit > temp):
                temp = digit
            # temp = "3"
        return int(temp)
                