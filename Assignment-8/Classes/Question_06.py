# 6) Write a Python class to implement pow(x, n) 

class Power:
    def __init__(self):
        pass

    def power(self, x, n):
        return x * Power().power(x, n - 1) if n > 0 else 1
    

#Test
p = Power()
print(p.power(2, 3))