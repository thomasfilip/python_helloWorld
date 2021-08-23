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
    for i in range(-100, 100):
        print(f"bool({i}) = {bool(i)}")             # always True, except bool(0) = False


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


def loops():
    for i in range(-100, 100):
        print(f"bool({i}) = {bool(i)}")


if __name__ == '__main__':
    execute_in_pycharm()
    primitive_datatypes_and_operators()
    boolean_operators()
    equality_identity()
    # loops()
    # operator_precedence()
