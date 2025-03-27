# 3) Write a Python class to get all possible unique subsets from a set of distinct integers Input : [4, 5, 6] Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]] 

class Subsets:
    def __init__(self):
        pass

    def get_subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [curr + [num] for curr in result]
        return result
#Test
s = Subsets()
print(s.get_subsets([4, 5, 6]))