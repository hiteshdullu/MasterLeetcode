class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['(', '{', '[']
        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
            
            elif s[i] == ')' and stack:
                if stack[-1] != '(':
                    return False
                stack.pop()
            
            elif s[i] == '}' and stack:
                if stack[-1] != '{':
                    return False
                stack.pop()
            
            elif s[i] == ']' and stack:
                if stack[-1] != '[':
                    return False
                stack.pop()
            
            else:
                return False
              
        if not len(stack):
            return True
        return False
