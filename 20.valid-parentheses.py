# @leet start
class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        for i in range(len(s)):
            if s[i] in ('(' , '{' , '['):
                my_stack.append(s[i])
            elif s[i] in (')' , '}' , ']') and len(my_stack) > 0:
                if s[i] == ')':
                    if my_stack[-1] == '(':
                        my_stack.pop()
                    else:
                        return False
                if s[i] == '}':
                    if my_stack[-1] == '{':
                        my_stack.pop()
                    else:
                        return False
                if s[i] == ']':
                    if my_stack[-1] == '[':
                        my_stack.pop()
                    else:
                        return False
            else:
                return False
        if len(my_stack) == 0:
            return True
        else:
            return False
# @leet end

my_solution = Solution()

test1 = "]"

result = my_solution.isValid(test1)
print(result)
