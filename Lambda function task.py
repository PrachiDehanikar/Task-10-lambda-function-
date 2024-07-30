def add(x, y):
    return x + y

# Lambda function
add_lambda = lambda x, y: x + y

print('add_lambda(5,6):', add_lambda(5, 6))



def maximum(a, b):
    return a if a > b else b

# Lambda function
max_lambda = lambda a, b: a if a > b else b

print('max_lambda(2,4):', max_lambda(2,4))



def square(x):
    return x * x

# Lambda function
square_lambda = lambda x: x * x

print('square_lambda(2,1):', max_lambda(2,1))


def modulus(x, y):
    return x % y

#lambda function
modulus_lambda = lambda x, y: x % y

print('modulus_lambda(10,3) : ', modulus_lambda(10,3))


def subtract(x, y):
    return x - y

#lambda function
subtract_lambda = lambda x, y: x - y
print('subtract_lambda (10,4): ', subtract_lambda(10, 4))



def divide(x, y):
    return x / y

#lambda function
divide_lambda = lambda x, y: x / y
print('divide_lambda', divide_lambda(8, 2))


def cube(x):
    return x * x * x

#lambda function
cube_lambda = lambda x: x * x * x
print('cube_lambda:', cube_lambda(4))
