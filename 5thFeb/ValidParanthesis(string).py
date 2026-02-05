class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_pairs = {'()', '[]', '{}'}
        
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack or stack.pop() + char not in valid_pairs:
                    return False
        
        return not stack
