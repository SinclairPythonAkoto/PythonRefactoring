# Optional Parameters #

'''
By setting a default value to the parameter, we can leave the parameters empty and
it use the default value to operate  the function.
'''

# no default parameters #

def pow_num(num):
    ''' Multiply number by power of 2 '''
    return num ** 2

call = pow_num(5)
print(call)


# default value set #

'''
Notice how we have not given a parameter to the function for the call object.  This would 
cause an error but because we have set a default value, we have the option to include an 
argument or not.
'''

def pow_num(num=1):
    return num ** 2

call = pow_num()
print(call)


'''
If you give your function object an argument, then it will override the default value
and the function will still execute.
'''

call = pow_num(5)
print(call)


'''
You can have functions that have both default & non-default values.
'''

def func(word, freq):
    print(word * freq)

call = func('Tim\n', 5)

# set the frequency a default of 1

def func(word, freq=1):
    print(word * freq)

call1 = func('John\n')  # freq uses default unless given arguement
call2 = func('Julie\n', 10) 


# Creating multiple defaults

'''
Lets say we have the same function but with an extra argument that will add to the 
number of the frequency.  By setting your function up with default values you can 
have more control over your functionality and still expect the function to work 
without all the arguements filled.
'''

def func(word, add=5, freq=1):
    print(word * (freq + add))

call1 = func("hello\n")  # this will print 6x times
call2 = func("hello world\n", 0)  # this will only print once because add is set to 1


# More examples #

'''
We will look at this car class below, it has a class method that displays messages if True.
This is without optional paramters; we will look at how we can apply it to this class later.
'''

class car(object):
    def __init__(self, make, model, year, condition, miles):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.miles = miles

    def display(self, show_all):
        ''' If True then show all parameters '''
        if show_all:
            print(f"This car is a {self.make} {self.model} from {self.year}, it is {self.condition} and has {self.miles} miles.")
        else:
            print(f"This car is a {self.make} {self.model} from {self.year}")

whip = car('Ford', 'Fusion', 2012, 'New', 0)
whip.display(True)          # show details of class object


'''
Lets now look at how we can plly optional parameters to this class.  We want to assume all the cars are new 
unless stated otherwise, and the miles should be 0.  We can also set a default value for the display class function.
This will make it diplay all the details of the class object unless the user states False.
'''

class Car(object):
    def __init__(self, make, model, year, condition='New', miles=0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.miles = miles

    def display(self, show_all=True):
        if show_all:
            print(f"This car is a {self.make} {self.model} from {self.year}, it is {self.condition} and has {self.miles} miles.")
        else:
            print(f"This car is a {self.make} {self.model} from {self.year}.")

whip = Car('Jaguar', 'I-Pace', 2022)
whip.display()
whip.display(False)

whip2 = Car('Jaguar', 'XE', 2017, 'Used', 55000)
whip2.display()
whip2.display(False)


'''
From this I hope you can see how useful optional paramters can be and how you can make the functionality of your 
class or function more effective for optimal performance in your code.
'''
