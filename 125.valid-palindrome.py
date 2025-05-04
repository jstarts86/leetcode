# @leet start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        j = len(s) - 1
        i = 0
        while i < len(s):
            first_ptr = s[i]
            second_ptr = s[j]
            if not first_ptr.isalnum():
                i += 1
            if not second_ptr.isalnum():
                j -= 1
            if first_ptr.isalnum() and second_ptr.isalnum():
                if first_ptr == second_ptr:
                    if i == j:
                        return True
                    i += 1
                    j -= 1
                else:
                    return False
        return True


        
# @leet end
solution_instance = Solution()

test_string = "A man, a plan, a canal: Panama"
test_string1 = "race a car"

result = solution_instance.isPalindrome(test_string1)

print(result)
