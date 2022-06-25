# PyTest in Python #
source: [Edureka](https://www.youtube.com/watch?v=byaxg00Gf9I)  


**PyTest** is a framework that allows building simple and scalable
tests easy.

Some advantages of *pytest*:
- Open source
- Ability to skip tests
- Run parallel tests
- Run a specific test or subset of tests
- Simple and easy syntax


### Install PyTest ###
*Install from your terminal:*
```
pip install -U pytest
```
*Run pytest file (multiple tests will run if stored*
```
python -m pytest path/to/name_of_file.py
```

*Run tests in a directory:*
```
python -m pytest folder/
```

*Run tests by keyword expressions*
```
python -m pytest -k "MyClass and not method"
```
This will run tests which contain names that match the given string expression,
which can include Python operators, filenames, class names and function names as
variables.

*Stop the test after the first failure:*
```
python -m pytest -x
python -m pytest --maxfail=2  # stop after 2 failures
```

*Run a specific test within a module:*
```
python -m pytest name_of_file.py::test_func
```

*Specifying a class method:*
```
python -m pytest name_of_file.py::TestClass::test_method
```

More infomation can be found about [usage and invocations in pytests](https://docs.pytest.org/en/6.2.x/usage.html) from the link provided.

### Objectives ###
- Create first test with PyTest
- Multiple tests
- Grouping multiple tests
- Pytest fixtures
- Paramaterized tests
- Testing an API using pytest
