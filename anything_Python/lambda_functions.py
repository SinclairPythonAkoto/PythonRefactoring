# Lambda Functions #

'''
Lambdas are anonymous functions
They can have multiple arguments but can only return one expression
Lamdas can have multiple paramaters as well as optional (default) paramters.
Use the 'lambda' keyword to create a lambad, then the name of your argument, 
then a semicolon followed by the action of the function.
Lambas are very useful for single use operations, if you want to create a 
mini function or a function within a function.
'''

# creating a normal function
def func(num):
    return num + 5

print(func(2))


# creating a lambda
func2 = lambda num: num + 5
print(func2(2)) 

'''
We can also use lambdas inside a function 
'''
def func(num):
    func2 = lambda num: num + 5
    
    return func2(num) + 85

print(func(2))


# lambdas with multiple parameters
func3 = lambda x,y: x + y
print(func3(5, 5))


# lambdas with optional parameters 
func4 = lambda x,y=5: x + y
print(func4(3))    # should get 8


# Using Lambdas With Map & Filter #

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list1 = list(map(lambda num: num + 5, list1))
print(new_list1)

new_list2 = list(filter(lambda num: num % 2 == 0, list1))
print(new_list2)
