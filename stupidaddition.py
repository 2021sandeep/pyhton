def addition(num1,num2):
    if type(num1)==type(num2):
     if type(num1)==int:
        return str(num1)+str(num2)
     else:
        return int(num1)+int(num2)
    else:
        return "None"

print(addition("10",5))
