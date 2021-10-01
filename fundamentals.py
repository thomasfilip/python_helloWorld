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
    # print(f"'foo' is None => {'foo' is None}")     # False
    # print(f"'None' is None => {None is None}")     # True
    # https://adamj.eu/tech/2020/01/21/why-does-python-3-8-syntaxwarning-for-is-literal/ (version 2021-08-29)
    # Adam says, since python 3.8 we should use identity check only when realy needed.
    print(f"'foo' == None => {'foo' == None}")      # False
    print(f"'None' == None => {None == None}")      # True


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
    elif random.randint(0, 10) == 2:
        print(f"two")
    else:
        print(f"between 3 and 10")

    # If can be used as an expression Equivalent of C's '?:' ternary operator (or Java).
    print(f"{'zero' if random.randint(0, 1) == 0 else 'one'}")


def loops():
    # For loops iterate over lists.
    for e in ["one", "two", "three"]:
        print(f"{e}")

    # range(int, int) returns a sequence and is iterable as well; range(start included, end excluded)
    for e in range(-4, 5):
        print(f"bool({e}) = {bool(e)}")             # -4 .. 4

    # range(int) returns sequence starting with 0, ending with end excluded.
    for e in range(5):
        print(f"bool({e}) = {bool(e)}")             # 0 .. 4

    # range(start, end, sep)
    for i in range(0, 8, 2):
        print(f"{i}")                               # 0, 2, 4, 6 (excluding 8)

    # To loop over a list, and retrieve both the index and the value of each item in the list.
    animals = ["dog", "cat", "mouse"]
    for i, value in enumerate(animals):
        print(i, value)

    #
    i = 0
    while i < 4:
        print(f"{i}")
        i += 1


def try_except():
    try:
        if random.randint(0, 3) == 0:
            raise IndexError("This is an IndexError")
        elif random.randint(0, 3) == 1:
            raise TypeError("This is an TypeError")
        elif random.randint(0, 3) == 2:
            raise NameError("This is an NameError")
        else:
            pass
    except IndexError as err:
        print(err)
        pass
    except (TypeError, NameError) as err:
        print(err)
        pass
    else:
        print("else is optional in a try block")
    finally:
        print("Execution guaranteed")


def data_structure_list():
    # Lists store sequences.
    list = []
    # You can start with a prefilled list
    other_list = [4, 5, 6]

    # Add stuff to the end.
    list.append(0)
    list.append(1)
    list.append(42)
    list.append("3")
    print(f"{list}")                                # [0, 1, 42, '3']

    # Indexing like Java.
    print(f"{list[0]}")                             # => 0
    print(f"{list[3]}")                             # => "3"

    # Reverse Indexing, not like Java.
    print(f"{list[-1]}")                            # => "3"

    # But IndexError like IndexOutOfBound in Java.
    # print(f"{list[-5]}")                          # IndexError
    # print(f"{list[5]}")                           # IndexError

    list.pop()                                      # Remove and return item at index (default last).
                                                    # Raises IndexError if list is empty or index is out of range
    print(f"{list}")                                # [0, 1, 42]
    list.pop(0)
    print(f"{list}")                                # [1, 42]
    list.pop(-1)
    print(f"{list}")                                # [1]

    # Inserts on index.
    list.insert(0, 0)
    list.insert(2, 42)
    list.insert(20, "3")                            # no IndexError, object will be appendend to the end.
    print(f"{list}")                                # [0, 1, 42, '3']

    # Using slice syntax to look at ranges: list[start:end(excluded):step]
    print(f"{list[1:3]}")                           # [   1, 42     ]
    print(f"{list[1:]}")                            # [   1, 42, '3']
    print(f"{list[:3]}")                            # [0, 1, 42     ]
    print(f"{list[::2]}")                           # [0,    42,    ]
    print(f"{list[::-1]}")                          # ['3', 42, 1, 0] reverse order.

    # list2 = list is creating a variable with the same reference (shallow copy).
    # To create a 1 layer deep copy use
    list2 = list[:]

    # Remove arbitrary elements from a list with keyword del.
    del list2[2]
    print(f"{list2}")                               # [0, 1, '3']

    # Remove first occurrence of a value (and also object?)
    list2.remove("3")
    print(f"{list2}")                               # [0, 1]
    # list2.remove("3")                             # ValueError: list.remove(x): x not in list

    # Get index of first occurence item (and object as well?)
    print(f"{list.index('3')}")                     # => index 3
    # print(f"{list.index('foo')}")                 # ValueError: 'foo' is not in list

    # Lists can be added with + operator, but the origin lists are not affected by this.
    l1 = [0, 1]
    l2 = [10, 11]
    print(f"{l1 + l2}")
    l3 = l1 + l2                                    # l3 ==[0, 1, 10, 11]
    print(f"{'l1: ', l1, 'l2: ', l2, 'l3: ', l3}")

    # You can extend a given list. I will stay the same object.
    l1 = [0, 1]
    l2 = [10, 11]
    l1.extend([1337, 42])
    l1.extend(l2)
    print(f"{l1}")                                  # l1 == [0, 1, 1337, 42, 10, 11]

    # Get lenght of list.
    print(f"{len(l1)}")                             # => 6

    # Check for existence in a list with "in".
    print(f"[0, 1] in l1: {[0, 1] in l1}")          # => False
    print(f"(0 in l1) and (1 in l1): {(0 in l1) and (1 in l1)}")  # => True
    print(f"l2 in l1: {l2 in l1}")                  # => False
    print(f"{42}")


def data_structure_tupel():
    # Tuples are like lists but are immutable.
    t1 = (1, 2, 3)
    print(f"{t1[0]}")                                # => 1
    # t1[0] = 3                                      # TypeError: 'tuple' object does not support item assignment

    # Note that a tuple of length one has to have a comma after the last element but
    # tuples of other lengths, even zero, do not.
    print(f"{type((1))}")                           # => <class 'int'>
    print(f"{type((1,))}")                          # => <class 'tuple'>
    print(f"{type(())}")                            # => <class 'tuple'>

    # You can do most of the list operations on tuples too.
    print(f"{len(t1)}")                             # => 3
    print(f"{t1 + (4, 5, 6)}")                      # => (1, 2, 3, 4, 5, 6)
    print(f"{t1[:2]}")                              # => (1, 2)
    print(f"{2 in t1}")                             # => True
    print(f"{t1[::2]}")                             # => (1, 3)
    print(f"{t1.index(3)}")                         # => 2

    # You can unpack tuples (or lists) into variables
    a, b, c = (1, 2, 3)                             # a is now 1, b is now 2 and c is now 3
    # You can also do extended unpacking
    a, *b, c = (1, 2, 3, 4)                         # a is now 1, b is now [2, 3] and c is now 4
    # Tuples are created by default if you leave out the parentheses
    d, e, f = 4, 5, 6                               # tuple 4, 5, 6 is unpacked into variables d, e and f
    # respectively such that d = 4, e = 5 and f = 6
    # Now look how easy it is to swap two values
    e, d = d, e                                     # d is now 5 and e is now 4


def data_structure_set():
    empty_set = set()
    prefilles_set = {1, 1, 2, 2, 3, 4}
    print(f"{prefilles_set}")                       # {1, 2, 3, 4}

    # Elements of a set have to be immutable.
    # invalid_set = {[42]}                          # TypeError: unhashable type: 'list'
    # a = ['a']
    # invalid_set = {a}                             # TypeError: unhashable type: 'list'
    valid_set = {(1,), 2}

    # Add a new element into the set. Duplicates are not stored.
    s1 = {1, 2, 3}
    s1.add(42)
    s1.add(42)
    print(f"{s1}")                                  # {1, 2, 3, 42}

    # Intersect (Schnitt)
    print(f"{s1 & {2, 3, 98, 99}}")                 # {2, 3}

    # Union (Vereinigung)
    print(f"{s1 | {2, 3, 98, 99} }")                # {1, 2, 3, 99, 98, 42}

    # Difference
    print(f"{s1 - {2, 3, 98, 99} }")                # {1, 42}

    # https://docs.python.org/3/tutorial/datastructures.html (version 2021-08-29)
    # Symmetric difference (exklusives oder; outer join)
    print(f"{s1 ^ {2, 3, 4}}")                      # {1, 4, 42}

    # Check if set on the left is a superset of set on the right
    print(f"{ {1, 2} >= {1, 2, 3}}")                # => False

    # Check if set on the left is a subset of set on the right
    print(f"{ {1, 2} <= {1, 2, 3}}")                # => True

    # Check for existence in a set with in
    print(f"{2 in s1}")                             # => True
    print(f"{10 in s1}")                            # => False

    # Make a 1 layer deep copy (into a new set object)
    filled_set = s1.copy()                          # filled_set == {1, 2, 3, 42}
    print(f"{filled_set is s1}")                    # => False

    # Clear set.
    s1.clear()


# key value table.
# Note - for Python versions < 3.7, dictionary key ordering is not guaranteed.
# However, as of Python 3.7, dictionary items maintain the order at which they are inserted into the dictionary.
def data_structure_dictionary():
    empty_dict = {}
    prefilled_dict = {"one": 1, "two": 2, "three": 3}
    d1 = {"one": 1, "two": 2, "three": 3}

    # Note keys for dictionaries have to be immutable types. This is to ensure that
    # the key can be converted to a constant hash value for quick look-ups.
    # Immutable types include ints, floats, strings, tuples.
    valid_dict = {(1, 2, 3): [1, 2, 3]}             # tupels of ints as keys
    valid_dict = {(1,): 1, (2,): 2, (3,): 3}        # tupels of ints as keys; both are equal
    valid_dict2 = {1: 1, 2: 2, 3: 3}
    # invalid_dict = {[1, 2, 3]: "123"}             # TypeError: unhashable type: 'list'

    # get value by key
    print(f"{d1['two']}")                           # 2

    # Create iterable of keys as list.
    print(f"{list(d1.keys())}")                     # ['one', 'two', 'three']

    # Create iterable of values as list.
    print(f"{list(d1.values())}")                   # [1, 2, 3]

    # Check for existence of keys in a dictionary with "in"
    print(f"{'one' in d1}")                         # => True
    print(f"{42 in d1}")                            # => False

    # Looking up a non-existing key is a KeyError.
    # print(f"{d1['four']}")                        # KeyError

    # Use "get()" method to avoid the KeyError.
    print(f"{d1.get('one')}")                       # => 1
    print(f"{d1.get('four')}")                      # => None
    # The get method supports a default argument when the value is missing.
    print(f"{d1.get('one', 4)}")                    # => 1
    print(f"{d1.get('four', 4)}")                   # => 4

    # "setdefault()" inserts into a dictionary only if the given key isn't present.
    d1.setdefault("five", 55)                       # d1["five"] is set to 5
    print(f"{d1.get('five')}")                      # 5, even key "five" is not present.
    d1.setdefault("five", 66)                       # d1["five"] is still 5, cannot be overwritten.
    print(f"{d1.get('five')}")                      # 5, even key "five" is not present.
    d1["five"] = 5
    print(f"{d1.get('five')}")                      # 5, because key is present.

    # Inserting into a dictionary.
    d1["six"] = 6
    d1.update({"six": 6})                           # Does the same.

    # Removing keys.
    del d1["six"]


# https://docs.python.org/3.9/tutorial/inputoutput.html#reading-and-writing-files (version 2021-08-29)
# The first argument is a string containing the filename.
# The second argument is another string containing a few characters describing the way in which the file will be used.
# mode can be 'r' when the file will only be read,
# 'w' for only writing (an existing file with the same name will be erased),
# and 'a' opens the file for appending; any data written to the file is automatically added to the end.
# 'r+' opens the file for both reading and writing.
# The mode argument is optional; 'r' will be assumed if it’s omitted.
def file():
    # Equivalent to 'with ressources' in Java.
    # https://www.tutorialspoint.com/data_structures_algorithms/merge_sort_algorithm.htm (version 2021-08-29)
    with open(file="mergeSort.txt") as f:
        for line in f:
            print(line)

    with open(file="myfile.txt", mode="a") as f:
        f.write("hallo5\n")


# Python offers a fundamental abstraction called the Iterable.
# An iterable is an object that can be treated as a sequence.
# The object returned by the range() function, is an iterable.
def iterator():
    filled_dict = {"one": 1, "two": 2, "three": 3}
    iterable1 = filled_dict.keys()
    print(f"{iterable1}")                            # => dict_keys(['one', 'two', 'three'])
                                                    # This is an object that implements our Iterable interface.
    # Let's loop over it.
    for e in iterable1:
        print(f"{e}")                               # => "one" => "two" => "three"

    # Adressing / accessing via index is not possible.
    # print(f"{iterable[0]}")                       # TypeError: 'dict_keys' object is not subscriptable

    # An iterable is an object that knows how to create an iterator.
    iterator1 = iter(iterable1)

    # Our iterator is an object that can remember the state as we traverse through it.
    # We get the next object with "next()".
    print(f"{next(iterator1)}")                     # => "one"

    # It maintains state as we iterate.
    print(f"{next(iterator1)}")                     # => "two"
    print(f"{next(iterator1)}")                     # => "three"

    # After the iterator has returned all of its data, it raises a StopIteration exception.
    # print(f"{next(iterator1)}")                   # Raises StopIteration

    # We can also loop over it, in fact, "for" does this implicitly.
    # But it is neccessary to create new itorator, because the old one is 'used up'.
    iterator2 = iter(iterable1)
    for e in iterator2:
        print(f"{e}")                               # => "one" => "two" => "three"

    # You can grab all the elements of an iterable or iterator by calling list() on it.
    print(f"{list(iterable1)}")                     # => ["one", "two", "three"]
    print(f"{list(iterable1)}")                     # yet no iterator invorlved.
    print(f"{list(iterator1)}")                     # => [] because state is saved


# Use "def" to create new functions.
def functions():
    print(f"{add(5, 37)}")                          # => 42
    print(f"{add(b=37, a=5)}")                      # => 42, keyword arguments can arrive in any order.
    print(f"{varargs1(5, 6, 4)}")                   # => (5, 6, 4) returns a tupel.
    print(f"{varargs1()}")                          # => () returns an empty tupel.
    print(f"{varargs2(5, 6, 4)}")                   # => 15
    print(f"{varargs2()}")                          # => 0 You don't have to call witch variables.
    print(f"{keyword_args(one=1, two=2)}")          # => {'one': 1, 'two': 2} Returns a dictionary.
    all_the_args1(37, 5, x=5, y=9)                  # => (37, 5) {'x': 5, 'y': 9}

    args = (37, 5)
    kwargs = {"x": 5, "y": 9}
    all_the_args1(*args)                            # equivalent to all_the_args1(37, 5)
    all_the_args1(**kwargs)                         # equivalent to all_the_args1(x=5, y=9)
    all_the_args1(*args, **kwargs)                  # equivalent to all_the_args1(37, 5, x=5, y=9)

    # all_the_args2(x=5, y=9, 37, 5)                # => syntx error: * parameter after ** parameter

    print(f"swap(2, 4) => {swap(2, 4)}")            # => tupel (4, 2)


# return keyword returns value.
def add(a, b):
    return a + b


# You can define functions that take a variable number of positional arguments.
def varargs1(*args):
    return args


# Multiple arguments are added to a sum.
def varargs2(*args):
    ans = 0
    for e in args:
        ans = ans + e
    return ans


# You can define functions that take a variable number of keyword arguments, as well.
def keyword_args(**kwargs):
    return kwargs


# You can do both at once, if you like.
def all_the_args1(*args, **kwargs):
    print(f"{args} {kwargs}")
    # return args, kwargs


# You can do both at once, but the order musst be *args first (tupel), then **kwargs (dictionary).
# def all_the_args2(**kwargs, *args):
#     print(f"{args} {kwargs}")
#     # return args, kwargs


# Returning multiple values (with tuple assignments)
# Return multiple values as a tuple without the parenthesis (they are optional here).
def swap(x, y):
    return y, x


x = 42
# See line above: local var x not the same as global variable x
def function_scope_local():
    x = 'python'
    print(f"local variable x is in scope: {x}")     # => 'python'


x = 42
# See line above: to access global variable x, use the keyword 'global'.
def function_scope_global():
    global x
    print(f"global variable x is in scope: {x}")     # => 42


if __name__ == '__main__':
    # execute_in_pycharm()
    # primitive_datatypes_and_operators()
    # boolean_operators()
    # truth_value_testing()
    # equality_identity()
    # strings()
    # operator_precedence()
    # function_print()
    # cli_input()
    # control_flow_if_else()
    # loops()
    # try_except()
    # data_structure_list()
    # data_structure_tupel()
    # data_structure_set()
    # data_structure_dictionary()
    # file()
    # iterator()
    # functions()
    function_scope_local()
    function_scope_global()
