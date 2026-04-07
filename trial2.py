a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print ("The sum of", a, "and", b, "is:", a + b)
print ("The difference of", a, "and", b, "is:", a - b)
print ("The product of", a, "and", b, "is:", a * b)
if b != 0:
    print ("The quotient of", a, "and", b, "is:", a / b)

def calculate(a, b):
    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    quotient_result = a / b if b != 0 else "Undefined (division by zero)"
    
    return sum_result, difference_result, product_result, quotient_result