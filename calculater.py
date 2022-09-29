import operator
class calculater:
    def add(self,num1,num2):
        return operator.add(num1,num2)
    def sub(self,num1,num2):
        return operator.sub(num1,num2)
    def mul(self,num1,num2):
        return operator.mul(num1,num2)
    def div(self,num1,num2):
        while num2==0:
            num2=int(input("enter the num2 grater than 0"))
            return operator.truediv(num1,num2)
obj=calculater()
print(obj.add(10,5))
print(obj.sub(10,5))
print(obj.mul(10,5))
print(obj.div(10,5))
