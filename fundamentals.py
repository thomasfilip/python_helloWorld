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
import random
import sys


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
    print(f"9 / 3 = {9 / 3}")               # 3.0

    # Integer division rounds down for both positive and negative numbers.
    print(f"5 // 3 = {5 // 3}")             # 1
    print(f"-5 // 3 = {-5 // 3}")           # -2
    print(f"5.0 // 3.0 = {5.0 // 3.0}")     # 1.0
    print(f"-5.0 // 3.0 = {-5.0 // 3.0}")   # -2.0
    print(f"5.0 // 3 = {5.0 // 3}")         # 1.0
    print(f"5 // 3.0 = {5 // 3.0}")         # 1.0

    # The result of division is always a float
    print(f"10.0 / 3 = {10.0 / 3}")         # 3.3333333333333335

    # Modulo
    print(f"7 % 3 = {7 % 3}")               # 1
    # i % j have the same sign as j, unlike C
    print(f"-7 % 3 = {-7 % 3}")  # 2

    # Exponentiation
    print(f"2**8 = {2**8}")                 # 256

    # More arithmetic comparisons
    print(f"1 < 10 = {1 < 10}")                     # True
    print(f"1 > 10 = {1 > 10}")                     # False
    print(f"2 <= 2 = {2 <= 2}")                     # True
    print(f"2 >= 2 = {2 >= 2}")                     # True

    # consider assosiation
    print(f"1 < 2 and 2 < 3 = {1 < 2 and 2 < 3}")   # True
    print(f"2 < 3 and 3 < 2 = {2 < 3 and 3 < 2}")   # False
    print(f"1 < 2 < 3 = {1 < 2 < 3}")               # True
    print(f"1 < 2 < 2 = {1 < 2 < 2}")               # False


# https://docs.python.org/3.9/reference/expressions.html#operator-precedence
# version 2021-08-23
def operator_precedence():
    print(f"operator_precedence")
    # Operator                                      Description

    # (expressions...),                             Binding or parenthesized expression, list display,
    # [expressions...],                             dictionary display, set display
    # {key: value...},
    # {expressions...}

    # x[index], x[index:index],                     Subscription, slicing, call, attribute reference
    # x(arguments...), x.attribute

    # await x                                       Await expression

    # **                                            Exponentiation

    # +x, -x, ~x                                    Positive, negative, bitwise NOT

    # *, @ , /, //, %                               Multiplication, matrix multiplication, division,
    #                                               floor division, remainder

    # +, -                                          Addition and subtraction

    # <<, >>                                        Shifts

    # &                                             Bitwise AND

    # ^                                             Bitwise XOR

    # |                                             Bitwise OR

    # in, not in, is, is not,                       Comparisons,including membership tests and identity tests
    # <, <=, >, >=, !=, ==

    # not x                                         Boolean NOT

    # and                                           Boolean AND

    # or                                            Boolean OR

    # if – else                                     Conditional expression

    # lambda                                        Lambda expression

    # :=                                            Assignment expression


def boolean_operators():
    # Boolean values are also primitive types.
    print(f"True = {True}")
    print(f"False = {False}")
    # print(f"false = {false}")     throws an error

    # Boolean values are also primitive types.
    print(f"not True = {not True}")
    print(f"not False = {not False}")

    # Note "and" and "or" are case-sensitive.
    print(f"True and False = {True and False}")
    print(f"True or False = {True or False}")
    print(f"(True or False) and (True or False) = {(True or False) and (True or False)}")

    # https://docs.python.org/3.9/reference/expressions.html#boolean-operations (version 2021-08-23)
    # The expression  x and y  first evaluates x;
    # if x is false, its value is returned; otherwise, y is evaluated and the resulting value is returned.
    # The expression  x or y  first evaluates x;
    # if x is true, its value is returned; otherwise, y is evaluated and the resulting value is returned.
    # Note that neither  and  nor  or  restrict the value and type they return to False and True,
    # but rather return the last evaluated argument.
    print(f"'' and foo = { '' or 'foo'}")           # 'foo'
    # Because  not  has to create a new value, it returns a boolean value regardless of the type of its argument.
    print(f"not 'foo' = {not 'foo'}")               # False rather then ''

    # True and False are actually 1 and 0 but with different keywords.
    print(f"True + True = {True + True}")           # 1 + 1 = 2
    print(f"True * 42 = {True * 42}")               # 1 * 42 = 42
    print(f"False - 5 = {False - 5}")               # 0 -5 = -5

    # Comparison operators look at the numerical value of True and False
    print(f"True == 1 = {True == 1}")               # 1 == 1 = True
    print(f"False == 0 = {False == 0}")             # 0 == 0 = True
    print(f"False != -5 = {False != -5}")           # 0 != -5 = True
    print(f"False <= True = {False <= True}")       # 0 <= 1 = True

    # Using boolean logical operators on ints casts them to booleans for evaluation,
    # but their non-cast value is returned.
    # Don't mix up with bool(ints) and bitwise and/or (&,|)
    print(f"0 and 0 = {0 and 0}")                   # 0
    print(f"0 and 2 = {0 and 2}")                   # 0
    print(f"0 and -5 = {0 and -5}")                 # 0
    print(f"42 and 42 = {42 and 42}")               # 42

    # note short circuit evaluation: x and y -> if x == False, return x; x or y -> if x False, return y.
    print(f"0 and 2 = {0 and 2}")                   # 0, because left operand is False and is returned before cast.
    print(f"-5 or 0 = {-5 or 0}")                   # -5, because left operand is False and is returned before cast.


# https://docs.python.org/3.9/library/stdtypes.html#truth (version 2021-08-23)
# truth Value Testing: always returns True, unless
# - defined to be False or None
# - zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
# - empty sequences and collections: '', (), [], {}, set(), range(0)
def truth_value_testing():
    for i in range(-100, 100):
        print(f"bool({i}) = {bool(i)}")             # always True, except bool(0) = False

    # The sole value of the type NoneType.
    # None is frequently used to represent the absence of a value,
    # as when default arguments are not passed to a function.
    # Assignments to None are illegal and raise a SyntaxError.
    print(f"None == None => {None == None}")        # == compares value. => True

    print(f"None == False => {None == False}")      # == compares value. None has not the same value as False. => False

    print(f"False == False => {False == False}")    # has same Value (integer 0). => True

    print(f"None == 0 => {None == 0}")              # has not the same Value. => False

    # Because of this confusion better use bool().
    print(f"bool(None) => {bool(None)}")            # False
    print(f"bool(False) => {bool(False)}")          # False
    print(f"bool(0) => {bool(0)}")                  # False
    print(f"bool(0.0) => {bool(0.0)}")              # False
    print(f"bool(0j) => {bool(0j)}")                # False

    # As mentioned: empty sequences and collections: '', (), [], {}, set(), range(0)
    print(f"bool('') => {bool('')}")                # False
    print(f'bool("") => {bool("")}')                # False
    print(f"bool(()) => {bool(())}")                # False
    print(f"bool([]) => {bool([])}")                # False
    print("bool({}) => " f"{bool({})}")             # False
    print(f"bool(set()) => {bool(set())}")          # False
    print(f"bool(range(0)) => {bool(range(0))}")    # False


def equality_identity():
    # Equality
    print(f"1 == 1 = {1 == 1}")                     # True
    print(f"42 == 2 = {42 == 2}")                   # False

    # Inequaility
    print(f"1 != 1 = {1 != 1}")                     # False
    print(f"42 != 2 = {42 != 2}")                   # True

    # in opposite to Java syntax, keyword  is  compares object reference, == compares value equality.
    a = [1, 2, 3, 4]                                # Point a at a new list, [1, 2, 3, 4]
    print(f"a = {a}")
    b = a                                           # Point b at what a is pointing to
    print(f"b is a = {b is a}")                     # True, a and b refer to the same object
    print(f"b == a = {b == a}")                     # True, a's and b's objects are equal
    b = [1, 2, 3, 4]                                # Point b at a new list, [1, 2, 3, 4]
    print(f"b = {b}")
    print(f"b is a = {b is a}")                     # False, a and b do not refer to the same object
    print(f"b == a = {b == a}")                     # True, a's and b's objects are equal

    # https://docs.python.org/3.9/library/constants.html?highlight=none#None (version 2021-08-28)
    # Don't use the equality "==" symbol to compare objects to None.
    # Use "is" instead. This checks for equality of object identity.
    print(f"'foo' is None => {'foo' is None}")      # False
    print(f"'None' is None => {None is None}")      # True


def strings():
    print(f"this is a string.")
    print(f'this is also a string.')
    print(f"this is possible {'also'}")
    print(f'this {"as well"}')

    print(f"stings " "can " "be " "concatinated.")
    print(f"stings " + "can " + "be " + "concatinated " + "also " + "this " + "way.")

    # A string can be treated like a list of characters
    print(f"Hello Python"[0])
    for i in range(len("String")):
        print(f"String"[i])

    # Length of a string.
    print(f"{len('Five!')}")                        # 5

    name = "Alice"
    print(f"{name} is {len(name)} characters long.")


# https://docs.python.org/3.9/library/functions.html#print (version 2021-08-28)
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
#
# Print objects to the text stream file, separated by sep and followed by end.
# sep, end, file and flush, if present, must be given as keyword arguments.
#
# All non-keyword arguments are converted to strings like str() does and written to the stream,
# separated by sep and followed by end.
# Both sep and end must be strings; they can also be None, which means to use the default values.
# If no objects are given, print() will just write end.
#
# The file argument must be an object with a write(string) method;
# if it is not present or None, sys.stdout will be used. Since printed arguments are converted to text strings,
# print() cannot be used with binary mode file objects. For these, use file.write(...) instead.
#
# Whether output is buffered is usually determined by file,
# but if the flush keyword argument is true, the stream is forcibly flushed.
#
# Changed in version 3.3: Added the flush keyword argument.
def function_print():
    print("")

    # Print multiple objects at once.
    str1 = "Hello"
    str2 = "Python"
    print(str1, str2)

    # Add a seperator (must be String; default: ' ').
    print(str1, str2, sep=' : ')

    # Add end of line (must be String; default: '\n').
    print(str1, end=' ')
    print(str2, end=' EOL\n')                       # Hello Python EOL

    # Change the output 'file (must have write(string) method; default: 'sys.stdout').
    print(str1, str2, file=sys.stdout)

    # Control flush behaviour of streams (True/False; default: False).
    print(str1, str2, flush=True)


# Simple way to get input data from console.
def cli_input():
    var_input = input("Enter some data: ")
    print(f"{var_input}")


# https://docs.python.org/3.9/tutorial/controlflow.html#if-statements (version 2021-08-28)
# https://docs.python.org/3.9/reference/compound_stmts.html#the-if-statement (version 2021-08-28)
# There can be zero or more elif parts, and the else part is optional.
# The keyword ‘elif’ is short for ‘else if’, and is useful to avoid excessive indentation.
# An if … elif … elif … sequence is a substitute for the switch or case statements found in other languages.
def control_flow_if_else():
    if random.randint(0, 10) == 0:
        print(f"zero")
    elif random.randint(0, 10) == 1:
        print(f"one")
    else:
        print(f"between 2 and 10")

    # If can be used as an expression Equivalent of C's '?:' ternary operator (or Java).
    print(f"{'zero' if random.randint(0, 1) == 0 else 'one'}")


def loops():
    for i in range(-100, 100):
        print(f"bool({i}) = {bool(i)}")


if __name__ == '__main__':
    execute_in_pycharm()
    primitive_datatypes_and_operators()
    boolean_operators()
    truth_value_testing()
    equality_identity()
    strings()
    operator_precedence()
    function_print()
    # cli_input()
    control_flow_if_else()
    # loops()
