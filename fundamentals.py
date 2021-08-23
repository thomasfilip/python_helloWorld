"""
    This file is for fundamentals training.
    Mainly I will use this reference at first: https://learnxinyminutes.com/docs/python/ (version 2021-08-23).
    A good addition is https://docs.python.org/3.9/tutorial/index.html (version 2021-08-23)
    and https://docs.python.org/3.9/reference/index.html (version 2021-08-23).
    author: thomasfilip
    created: 2021-08-23
"""


# https://www.freecodecamp.org/news/if-name-main-python-example/
# version 2021-08-23
# When the interpreter runs a module,
# the __name__ variable will be set as __main__ if the module that is being run is the main program.
# But if the code is importing the module from another module,
# then the __name__  variable will be set to that module’s name.
def execute_in_pycharm():
    print("__name__ variable should contain __main__:")
    print(__name__)


# https://docs.python.org/3.9/tutorial/inputoutput.html#formatted-string-literals
# version 2021-08-23
def primitive_datatypes_and_operators():
    print(42)
    print("42")
    print('42')
    print('a')
    # type conversion necessary.
    print("1 + 1 = " + str(1 + 1))

    # f or F at begining of output enables output formatting.
    # Inside this string, you can write a Python expression between { and } characters
    # that can refer to variables or literal values.
    print(f"1 + 1 = {1 + 1}")
    print(f"8 - 1 = {8 + 1}")
    print(f"5 * 2 = {5 * 2}")
    # implicite type cast
    print(f"9 / 3 = {9 / 3}")       # 3.0

    # Integer division rounds down for both positive and negative numbers.
    print(f"5 // 3 = {5 // 3}")             # 1
    print(f"-5 // 3 = {-5 // 3}")           # -2
    print(f"5.0 // 3.0 = {5.0 // 3.0}")     # 1.0
    print(f"-5.0 // 3.0 = {-5.0 // 3.0}")   # -2.0
    print(f"5.0 // 3 = {5.0 // 3}")         # 1.0
    print(f"5 // 3.0 = {5 // 3.0}")         # 1.0

    # The result of division is always a float
    print(f"10.0 / 3 = {10.0 / 3}")  # 3.3333333333333335

    # Modulo
    print(f"7 % 3 = {7 % 3}")       # 1


if __name__ == '__main__':
    # execute_in_pycharm()
    primitive_datatypes_and_operators()
