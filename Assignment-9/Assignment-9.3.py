# A balanced delimiter starts with an opening character ((, [, {), ends with a matching closing character (), ], } respectively), and has only other matching delimiters in between. A balanced delimiter may contain any number of balanced delimiters.

# Examples
# The following are examples of balanced delimiter strings:

# ()[]{}
# ([{}])
# ([]{})
# The following are examples of invalid strings:
# ([)]
# ([]
# [])
# ([})
# Input is provided as a single string. Your output should be True or False according to whether the string is balanced. For example:

# Input:
# ([{}])
# Output:
# True

def is_balanced(s):
    stack = []
    opening = set("([{")
    matching = {")": "(", "]": "[", "}": "{"}
    
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in matching:
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

string = input("Enter a string ['(',')', '[',']', '{','}']: ")
print(is_balanced(string))