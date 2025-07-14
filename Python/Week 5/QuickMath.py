class Caculator:
    def Add(self, x, y):
        return x+y
    
    def Subtract(self, x, y):
        return x-y
    
    def Mulitpy(self, x, y):
        return x * y
    
    def Divide(self, x, y):
        return x/y
    
caculator = Caculator()

sum = caculator.Add(25, 78)
diffrence = caculator.Subtract(10, 5)
product = caculator.Mulitpy(5, 8)
dividend = caculator.Divide(12, 4)
print(sum)
print(diffrence)
print(product)
print(dividend)