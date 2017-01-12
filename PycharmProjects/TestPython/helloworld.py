


#name = input("Hello, what is your name?")
#name = name.strip()
#print("Hello", name)


def addition(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    sum = int(num1) + int(num2)
    return sum

def difference(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    sum = int(num1) - int(num2)
    return sum

def product(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    sum = int(num1) * int(num2)
    return sum

def remainder(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    sum = int(num1) % int(num2)
    return sum

def division(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    sum = int(num1) / int(num2)
    return sum


num1, num2 = input("Input numbers:").split()

print("Addition: {0}".format(addition(num1, num2)))
print("Difference:{0}".format(difference(num1, num2)))
print("Product:{0}".format(product(num1, num2)))
print("Quotient:{0}".format(division(num1, num2)))
print("Remainder:{0}".format(remainder(num1, num2)))


