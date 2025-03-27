# 4) Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number. Note: There will be one solution for each input and do not use the same element twice. Input: numbers= [90, 20,10,40,50,60,70], target=50 Output: 3, 4 

class Pair:
    def __init__(self):
        pass

    def find_pair(self, numbers, target):
        set_numbers = set(numbers)
        for i, num in enumerate(numbers):
            if target - num in set_numbers and i != numbers.index(target - num):
                return i + 1, numbers.index(target - num) + 1
        return 'No pair found'
            
#Test
p = Pair()
print(p.find_pair([90, 20, 10, 40, 50, 60, 70], 50))
print(p.find_pair([90, 20, 10, 40, 50, 70], 100))