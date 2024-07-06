# LEETCODE EASY PROBLEM -> https://leetcode.com/problems/palindrome-number/

# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
# Therefore it is not a palindrome.

# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1
 

# Follow up: Could you solve it without converting the integer to a string?

class Solution:
    # First solution found
    # Runtime: 62ms     | Beats 24.24%
    # Memory:  16.72 MB | Beats 7.97%
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        test_list = []
        count = 0

        for i in range(0, len(num_str)):
            test_list.append(num_str[i])
        if len(test_list) == 2:
            if test_list[0] == test_list[1]:
                return True
            else:
                return False            

        half_len = int(len(test_list) / 2)
        for i in range(0, half_len+1):
            count -= 1
            if test_list[i] == test_list[count]:
                if half_len == i:
                    return True
            else:
                return False
    
    # Second solution found
    # Runtime: 48ms     | Beats 79.91%
    # Memory:  16.52 MB | Beats 37.64%
    def isPalindrome2(self, x: int) -> bool:
        num_str = str(x)
        count = 0       
        half_len = int(len(num_str) / 2)

        for i in range(0, half_len+1):
            count -= 1
            if num_str[i] == num_str[count]:
                if half_len == i:
                    return True
            else:
                return False
    
# s = Solution()
# print(s.isPalindrome(121))


 
