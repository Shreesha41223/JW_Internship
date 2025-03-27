# 2) Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid. 

class Parentheses:
    def __init__(self):
        self.opening = ['(', '{', '[']
        self.closing = [')', '}', ']']
        self.parentheses = {
            ')': '(',
            '}': '{',
            ']': '['
        }

    def is_valid(self, string):
        stack = []  
        for char in string:
            if char in self.opening:
                stack.append(char)
            elif char in self.closing:
                if not stack or stack[-1] != self.parentheses[char]:
                    return False
                stack.pop()
        return not stack
    
#Test
p = Parentheses()
print(p.is_valid("()"))
print(p.is_valid("()[]{}"))
print(p.is_valid("[)"))
print(p.is_valid("({[)]"))