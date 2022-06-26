# Unit Testing With PyTest #

Source:  [Pixegami - Youtube](https://www.youtube.com/watch?v=YbpKMIUjvK8)

Learn how to test your Python code by writing unit tests with the Pytest framework.

In this will build a small shopping cart program which allows the user to:
- Add items to a cart
- Warn the user if the cart is full
- Can culate the total number of items in a cart

By building this, we will wuild unit tests around this to test out each functionality
of the program.
We will cover the following:
- How to write and run unit tests with **Pytest**
- Using *assert* to validate your logic
- Using *fixtures* to set up your tests
- How to *mock* external dependencies

#### Quick Notes ####
We can get pytest to reveal our print statements within our tests; by simply using `-s` after
specifying which test function you want to print from (unless you want it applied to all functions).

In the terminal:
```
pytest test_my_file.py::test_my_function -s
```
