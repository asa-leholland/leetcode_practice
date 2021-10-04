# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
# num = 123

# 1 + 2 + 3
# 6

# num = 999
# 27
# 9

# 9 + 9 = 18
# 9 + 9 = 18
# 9




# num = 912
# 12
# # 3

# 9 + 1 = 10

# # 1 + 2 
# # 3
#         sum = 0
#         for char in str(num):
#             sum += int(char)
#             if sum >= 10:
#                 sum = (sum % 10) + 1
#         return sum

# #     num = 123
#     # 1 -> sum = 1
#     # 2 -> sum = 3 
#     # 3 sum = 6
#     # 9 -> sum =15


        if num == 0:
            return 0
        else:
            return (num-1)%9 + 1
